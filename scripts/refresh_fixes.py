"""Refresh PR states and uptake facts in decisions/fixes.json from GitHub; report generation stays offline.

Editorial fields (client, decisions, partial, depends_on, conflicts_with, verified_cases, note) are kept as
written. `uptake` is rewritten for every merged PR with a client, from these facts:

- merge_commit: the PR's merge commit, and `via`, the PR whose branch it merged into, if any: its changes reach
  the default branch through that PR's merge, which then stands in for its own below.
- releases (library PRs): for each library on the path to the client (see `libraries`), the first version
  tag that carries the change, its commit date and the versions it gives the library's crates. The first
  library's tag is its earliest one containing the merge commit; a downstream library's tag is its earliest
  one whose Cargo.toml requirement admits the upstream release.
- client (library PRs): the client default-branch commit whose Cargo.lock first pins every release, kept
  from earlier refreshes once seen; null while the default branch does not pin them.
- builds: {commit: bool} for the measured builds of the PR's client (the latest build per client captured
  by the runs in reports.lock.json): whether the merge commit is in the build's history or, for a library
  PR, whether the build's Cargo.lock pins every release.
"""
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import time
import tomllib

from trace_interop.presentation import family, library_chain, measured_builds

ROOT = Path(__file__).resolve().parents[1]
VERSION_TAG = re.compile(r'v?\d+(\.\d+)*')


class GitHub:
    """Read-only GitHub queries through the authenticated gh CLI, memoized for one refresh."""

    def __init__(self):
        self.outputs, self.locks = {}, {}

    def gh(self, *args, attempts=3):
        """gh output, retrying the transient failures a long refresh meets."""
        for attempt in range(attempts):
            if args in self.outputs:
                break
            result = subprocess.run(['gh', *args], capture_output=True, text=True, check=False)
            if result.returncode == 0:
                self.outputs[args] = result.stdout
                break
            time.sleep(2 ** attempt)
        else:
            raise RuntimeError(f'gh {" ".join(args)} failed: {result.stderr.strip()}')
        return self.outputs[args]

    def pr(self, url):
        return json.loads(self.gh('pr', 'view', url, '--json', 'title,state,isDraft,mergedAt,mergeCommit,baseRefName,headRefName'))

    def contains(self, repo, commit, ref):
        """Whether `commit` is in the history of `ref`."""
        return self.gh('api', f'repos/{repo}/compare/{commit}...{ref}?per_page=1', '--jq', '.status').strip() in ('ahead', 'identical')

    def tags(self, repo):
        return self.gh('api', '--paginate', f'repos/{repo}/tags?per_page=100', '--jq', '.[].name').split()

    def commit(self, repo, ref):
        """{sha, date} of a commit, tag or branch."""
        return json.loads(self.gh('api', f'repos/{repo}/commits/{ref}', '--jq', '{sha: .sha, date: .commit.committer.date}'))

    def file(self, repo, path, ref):
        return self.gh('api', f'repos/{repo}/contents/{path}?ref={ref}', '-H', 'Accept: application/vnd.github.raw')

    def history(self, repo, path, since):
        """Default-branch commits that touched `path` since a timestamp, oldest first."""
        return self.gh('api', '--paginate', f'repos/{repo}/commits?path={path}&since={since}&per_page=100', '--jq', '.[].sha').split()[::-1]

    def lockfile(self, repo, ref):
        """{crate: [(version, source)]} from the repository's Cargo.lock at `ref`."""
        if (repo, ref) not in self.locks:
            found = self.locks[repo, ref] = {}
            for package in tomllib.loads(self.file(repo, 'Cargo.lock', ref))['package']:
                found.setdefault(package['name'], []).append((package['version'], package.get('source', '')))
        return self.locks[repo, ref]


def version(text):
    """(major, minor, patch) of a tag, version or requirement such as v0.44.0, v120 or ^43."""
    numbers = [int(n) for n in re.match(r'[\^=~v ]*(\d+(?:\.\d+)*)', text)[1].split('.')][:3]
    return tuple(numbers + [0] * (3 - len(numbers)))


def admits(requirement, release):
    """Whether a Cargo default (caret) requirement admits a release version: at least the requirement, with the
    same leftmost nonzero component."""
    base = version(requirement)
    significant = next((i for i, n in enumerate(base) if n), 2) + 1
    return version(release) >= base and version(release)[:significant] == base[:significant]


def version_tags(gh, repo):
    return sorted((tag for tag in gh.tags(repo) if VERSION_TAG.fullmatch(tag)), key=version, reverse=True)


def dependencies(manifest):
    """{crate: requirement} of a root Cargo.toml's dependencies and workspace dependencies."""
    found = {}
    for table in (manifest.get('dependencies', {}), manifest.get('workspace', {}).get('dependencies', {})):
        for key, dep in table.items():
            dep = {'version': dep} if isinstance(dep, str) else dep
            if 'version' in dep:
                found[dep.get('package', key)] = dep['version']
    return found


def crate_versions(manifest, crates):
    """The versions a root Cargo.toml gives the listed crates: the package itself, or path members of the workspace."""
    package = manifest.get('package', {})
    found = {package['name']: package['version']} if isinstance(package.get('version'), str) else {}
    found |= {dep.get('package', key): dep['version'] for key, dep in manifest.get('workspace', {}).get('dependencies', {}).items()
              if isinstance(dep, dict) and 'path' in dep and 'version' in dep}
    return {crate: found[crate] for crate in crates if crate in found}


def first_release(gh, repo, commit):
    """The earliest version tag of `repo` containing `commit`, walking back from the newest; None before a release."""
    found = None
    for tag in version_tags(gh, repo):
        if not gh.contains(repo, commit, tag):
            break
        found = tag
    return found


def first_adopting(gh, repo, upstream):
    """The earliest version tag of downstream library `repo` whose manifest requirements admit the upstream crate releases."""
    found = None
    for tag in version_tags(gh, repo):
        wanted = {crate: req for crate, req in dependencies(tomllib.loads(gh.file(repo, 'Cargo.toml', tag))).items() if crate in upstream['crates']}
        if not wanted or not all(admits(req, upstream['crates'][crate]) for crate, req in wanted.items()):
            break
        found = tag
    return found


def satisfies(gh, repo, commit, needed, locked, source):
    """Whether one locked package carries a hop: a registry version of at least `needed`, or a git checkout of `repo` containing `commit`."""
    if git := re.fullmatch(rf'git\+https://github\.com/{re.escape(repo)}(?:\.git)?[?#].*?([0-9a-f]{{40}})', source, re.IGNORECASE):
        return commit is not None and gh.contains(repo, commit, git[1])
    return needed is not None and version(locked) >= version(needed)


def pins(gh, lock, required):
    """Whether a Cargo.lock carries every hop of `required`, [(repo, commit, {crate: version or None})]: at least one
    of the hop's crates is locked, and each locked one satisfies it."""
    return all(any(crate in lock for crate in crates)
               and all(any(satisfies(gh, repo, commit, needed, *package) for package in lock[crate]) for crate, needed in crates.items() if crate in lock)
               for repo, commit, crates in required)


def first_pinning(gh, repo, since, required):
    """{commit, date} of the earliest default-branch Cargo.lock change since `since` that pins `required`, by bisection;
    the default branch head must pin it."""
    history = gh.history(repo, 'Cargo.lock', since) or [gh.commit(repo, 'HEAD')['sha']]
    low, high = 0, len(history) - 1
    while low < high:
        middle = (low + high) // 2
        if pins(gh, gh.lockfile(repo, history[middle]), required):
            high = middle
        else:
            low = middle + 1
    return {'commit': history[low], 'date': gh.commit(repo, history[low])['date']}


def repository(url):
    return re.fullmatch(r'https://github\.com/([^/]+/[^/]+)/pull/\d+', url)[1]


def uptake(gh, pr, commit, libraries, builds, previous=None):
    """Releases, client and build facts of a merged PR (see the module docstring). `commit` is the commit that carries
    it into its repository's default branch, None while the branch it merged into has not; `previous` is its last uptake."""
    repo = repository(pr['url'])
    own = [ref for client, ref in sorted(builds.items()) if family(client) == pr['client']]
    if commit is None:
        return ({'releases': [], 'client': None} if repo in libraries else {}) | {'builds': {ref['commit']: False for ref in own}}
    if repo not in libraries:
        return {'builds': {ref['commit']: gh.contains(repo, commit, ref['commit']) for ref in own}}
    target, = {ref['repository'].removeprefix('https://github.com/') for ref in own}
    chain = library_chain(libraries, repo, target)[:-1]
    releases = []
    for library in chain:
        tag = first_adopting(gh, library, releases[-1]) if releases else first_release(gh, library, commit)
        if tag is None:
            break
        releases.append({'repo': library, 'tag': tag, 'date': gh.commit(library, tag)['date'],
                         'crates': crate_versions(tomllib.loads(gh.file(library, 'Cargo.toml', tag)), libraries[library]['crates'])})
    required = []
    for i, library in enumerate(chain):
        release = releases[i] if i < len(releases) else None
        required.append((library, commit if i == 0 else release and release['tag'],
                         release['crates'] if release else dict.fromkeys(libraries[library]['crates'])))
    client = None
    if pins(gh, gh.lockfile(target, gh.commit(target, 'HEAD')['sha']), required):
        client = (previous or {}).get('client') or first_pinning(gh, target, pr['merged_at'], required)
    return {'releases': releases, 'client': client,
                    'builds': {ref['commit']: pins(gh, gh.lockfile(target, ref['commit']), required) for ref in own}}


def current_builds(root):
    """The measured builds of the current reports: the latest build per client in the runs of reports.lock.json."""
    selection = json.loads((root/'reports.lock.json').read_text())
    pairs = {(client, v) for run in selection['runs'] for client, v in json.loads((root/run/'summary.json').read_text())['versions'].items()}
    return measured_builds(pairs, json.loads((root/'locks/source-revisions.json').read_text()))


def refresh(path, gh, builds):
    fixes = json.loads(path.read_text())
    infos = {pr['url']: gh.pr(pr['url']) for pr in fixes['prs']}
    branches = {(repository(url), info['headRefName']): url for url, info in infos.items()}
    for pr in fixes['prs']:
        info = infos[pr['url']]
        current = dict(title=info['title'], state=info['state'].lower(), draft=info['isDraft'], merged_at=info['mergedAt'])
        changed = {k: v for k, v in current.items() if pr[k] != v}
        if changed:
            print(pr['url'], ', '.join(f'{k}: {pr[k]} -> {v}' for k, v in changed.items()))
        pr.update(current)
        before = pr.pop('uptake', None)
        if pr['state'] == 'merged' and pr['client']:
            # A PR merged into another PR's branch reaches the default branch through that PR's merge.
            via = branches.get((repository(pr['url']), info['baseRefName']))
            commit = (infos[via]['mergeCommit'] or {}).get('oid') if via else info['mergeCommit']['oid']
            pr['uptake'] = ({'merge_commit': info['mergeCommit']['oid']} | ({'via': via} if via else {})
                            | uptake(gh, pr, commit, fixes.get('libraries', {}), builds, before))
            if pr['uptake'] != before:
                print(pr['url'], 'uptake:', json.dumps(pr['uptake']))
    fixes['checked_at'] = datetime.now(timezone.utc).date().isoformat()
    path.write_text(json.dumps(fixes, indent=2) + '\n')
    return fixes


if __name__ == '__main__':
    fixes = refresh(ROOT/'decisions/fixes.json', GitHub(), current_builds(ROOT))
    print(f'Checked {len(fixes["prs"])} PRs; run scripts/build_reports.py to regenerate the reports.')

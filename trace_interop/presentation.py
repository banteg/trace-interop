"""Maintainer-facing views of the independently evaluated observations."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
import json
import os
import re

from .progress import BUCKETS, pr_counts, svg, tally
from .status import decision_status, LEGEND, NATIVE_CLIENTS, POSITIONS, NO_POSITION, POSITION_LEGEND, check_positions, client_positions


SOURCE_GROUPS = {
    'H01': ['replay'], 'H02': ['lookup'], 'H03': ['filter'],
    'H04': ['filter'], 'H05': ['filter', 'frames'], 'H06': ['lookup', 'replay'],
    'H07': ['replay'], 'H08': ['replay', 'call'], 'H09': ['frames'],
    'H10': ['frames'], 'H11': ['call'], 'H12': ['raw'], 'H13': ['raw'],
    'H14': ['raw', 'call'], 'H15': ['call'], 'H16': ['call', 'state'],
    'H17': ['state'], 'H18': ['state', 'replay'], 'H19': ['vm', 'replay'],
    'H20': ['vm'], 'H21': ['vm'], 'H22': ['frames'], 'H23': ['filter'],
    'H24': ['frames'], 'H25': ['raw', 'replay'], 'H26': ['state'],
    'H27': ['filter'], 'H28': ['call'], 'H29': ['frames'],
    'H30': ['bounds'], 'H31': ['many'], 'H32': ['tags', 'many'],
}
BAD = {'change_needed', 'unsupported'}


def relative(path, parent):
    return os.path.relpath(path, parent).replace(os.sep, '/')


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def table(headers, rows):
    lines = ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join('---' for _ in headers) + ' |']
    lines.extend('| ' + ' | '.join(cell(c) for c in row) + ' |' for row in rows)
    return '\n'.join(lines) + '\n\n'


def save(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(line.rstrip() for line in text.splitlines()).rstrip() + '\n')


def family(client):
    return 'geth' if client == 'go-ethereum_trace' else client.split('_')[0]


def source_revision(client, version, revisions):
    refs = [ref for ref in revisions.get(client, []) if ref['version'] == version]
    if len(refs) > 1:
        raise ValueError(f'ambiguous source revision for {client}: {version}')
    return refs[0] if refs else None


def version_label(version):
    compact = version.removeprefix('Reth Version: ').removeprefix('besu/v').removeprefix('Geth/v').split('/')[0]
    return re.sub(r'[+-][0-9a-f]{7,40}(?:-\d{4}-\d{2}-\d{2})?$', '', compact)


def build_label(client, version, revisions):
    """Show the captured version and exact source identity, not its update channel."""
    ref = source_revision(client, version, revisions)
    return version_label(version) + ' · ' + (ref['commit'][:8] if ref else 'commit not recorded')


def verdict(checks):
    statuses = {c['status'] for c in checks}
    if 'unsupported' in statuses:
        return 'Method unavailable'
    if 'change_needed' in statuses:
        return 'Differs'
    substantive = statuses - {'control','not_applicable'}
    if 'unassessed' in substantive or 'blocked' in substantive:
        if substantive & {'matches','observation'}:
            return 'Partially assessed'
        return 'Not assessed' if 'unassessed' in substantive else 'Blocked'
    if 'observation' in statuses:
        return 'Policy open'
    if 'matches' in statuses:
        return 'Checked cases agree'
    if statuses and not substantive:
        return 'Control / not applicable'
    return 'Not assessed'


def display_verdict(checks, fixes=()):
    """Link submitted (pr, partial) fixes to a difference or partial assessment; only a complete fix replaces it."""
    label = verdict(checks)
    icon = {
        'Checked cases agree': '✅',
        'Differs': '⚠️',
        'Method unavailable': '⛔',
        'Partially assessed': '🟡',
        'Not assessed': '⚪',
        'Policy open': '❔',
        'Blocked': '🚧',
        'Control / not applicable': '🔎',
    }[label]
    if not fixes or label not in ('Differs', 'Partially assessed'):
        return f'{icon} {label}'
    links = ' · '.join(f'[{pr["label"]}]({pr["url"]})' + (' (partial fix)' if partial else '') for pr, partial in fixes)
    return f'{icon} {label} · {links}' if all(partial for _, partial in fixes) else f'🛠️ Fix submitted: {links}'


def timestamp(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00'))


def check_fixes(fixes, decisions, families):
    """Validate related PRs against the decision ledger and client families, and label them."""
    urls = [pr['url'] for pr in fixes['prs']]
    if len(urls) != len(set(urls)):
        raise ValueError('duplicate fix PR')
    for pr in fixes['prs']:
        match = re.fullmatch(r'https://github\.com/([^/]+/[^/]+)/pull/(\d+)', pr['url'])
        if (not match or match[1] not in fixes['repositories'] or pr['client'] not in {*families, None}
                or not set(pr['decisions']) <= set(decisions) or not set(pr.get('partial', [])) <= set(pr['decisions'])
                or pr['state'] not in ('open', 'merged', 'closed') or (pr['state'] == 'merged') != bool(pr['merged_at'])
                or not isinstance(pr.get('awaiting_uptake', False), bool)):
            raise ValueError(f'invalid fix PR: {pr["url"]}')
        pr['label'] = f'{fixes["repositories"][match[1]]} #{match[2]}'
        pr['order'] = (fixes['repositories'][match[1]].lower(), int(match[2]))
    return fixes


def pending_fixes(fixes, client, topic, built):
    """(pr, partial) for this build and decision: open, merged after the build's commit, or merged but awaiting uptake."""
    return [(pr, topic in pr.get('partial', [])) for pr in sorted(fixes['prs'], key=lambda pr: pr['order'])
            if pr['client'] == family(client) and topic in pr['decisions']
            and (pr['state'] == 'open' or pr['state'] == 'merged' and (pr.get('awaiting_uptake')
                 or built is not None and timestamp(pr['merged_at']) > built))]


def merged_fixes(fixes, topic):
    """(client, source) for merged, complete native-client fixes of a decision: agreement by implementation."""
    return [(pr['client'], {'label': pr['label'], 'url': pr['url']}) for pr in sorted(fixes['prs'], key=lambda pr: pr['order'])
            if pr['state'] == 'merged' and pr['client'] in NATIVE_CLIENTS and topic in pr['decisions'] and topic not in pr.get('partial', [])]


def fix_change(pr):
    """The PR title without its conventional-commit scope, plus any tracking note."""
    change = re.sub(r'^[\w./-]+(\([^)]*\))?!?: ', '', pr['title'])
    return change[:1].upper() + change[1:] + (f'; {pr["note"]}' if pr.get('note') else '')


def fixes_page(fixes, root, parent):
    text = ('# Related pull requests\n\n'
            f'Related client, specification and test-suite PRs. Status checked **{fixes["checked_at"]}**.\n\n'
            'Reports show 🛠️ Fix submitted instead of ⚠️ or 🟡 for a build when a PR tagged with its client and decision '
            'is open, was merged after the build’s commit, or awaits uptake of the merged library change. A PR marked partial is linked '
            'but leaves ⚠️ or 🟡 in place, since part of the measured difference has no submitted fix. Generated from [fixes.json](../decisions/fixes.json); '
            'refresh PR states with `uv run python scripts/refresh_fixes.py`.\n\n')
    for state in ['open', 'merged', 'closed']:
        prs = sorted((pr for pr in fixes['prs'] if pr['state'] == state), key=lambda pr: pr['order'])
        merged = ['Merged (UTC)'] if state == 'merged' else []
        rows = [[f'[{pr["label"]}]({pr["url"]})' + (' (draft)' if pr['draft'] else ''), fix_change(pr),
                 ', '.join(f'[{t}]({relative(root/"reports/decisions"/(t + ".md"), parent)})' + (' (partial)' if t in pr.get('partial', []) else '')
                           for t in pr['decisions']) or '—',
                 *([utc_date(pr['merged_at'])] if merged else [])] for pr in prs]
        if rows:
            text += f'## {state.capitalize()}\n\n' + table(['PR', 'Change', 'Decisions', *merged], rows)
    return text


def coverage_summary(checks):
    """Explain gaps and open policy by case, without counting every assertion twice."""
    groups = defaultdict(set)
    for c in checks:
        status = c['status']
        if status not in ['blocked', 'unassessed', 'observation']:
            continue
        detail = c.get('detail', '') if status != 'observation' else ''
        detail = detail.removeprefix('Cannot inspect this property: ').rstrip('.')
        if detail == 'malformed_json':
            detail = 'malformed JSON response'
        groups[status, detail].add((c.get('corpus'), c.get('case')))
    return ' '.join(
        f'{len(cases)} {"policy-open" if status == "observation" else status} '
        f'{"case" if len(cases) == 1 else "cases"}' + (f': {detail}.' if detail else '.')
        for (status, detail), cases in sorted(groups.items()))


def utc_date(timestamp):
    if not timestamp:
        return 'Not recorded'
    return datetime.fromisoformat(timestamp.replace('Z', '+00:00')).astimezone(timezone.utc).date().isoformat()


def build_rows(selected, runs, revisions, parent):
    """Pair exact tested versions with source commits, never infer from a channel label."""
    groups = {}
    for client in selected:
        for run in runs:
            if client not in run['manifest']['clients']:
                continue
            version = run['versions'].get(client, 'unknown')
            dates = groups.setdefault((client, version), {})
            tested = utc_date(run['manifest'].get('started_at'))
            dates.setdefault(tested, run['path'])
    rows = []
    for (client, version), dates in groups.items():
        ref = source_revision(client, version, revisions)
        commit = f'[`{ref["commit"][:8]}`]({ref["repository"]}/commit/{ref["commit"]})' if ref else 'Not recorded'
        committed = utc_date(ref['committed_at']) if ref else 'Not recorded'
        tested = '<br>'.join(f'[{date}]({relative(path, parent)})' for date,path in sorted(dates.items()))
        rows.append([f'`{version_label(version)}`', commit, committed, tested])
    return rows


def source_url(source):
    return f'{source["repository"]}/blob/{source["commit"]}/{source["path"]}#L{source["line"]}'


def source_links(sources, client, topic):
    links = []
    for group in SOURCE_GROUPS[topic]:
        ref = sources.get(family(client), {}).get(group)
        if ref:
            links.append(f'[{ref["label"]}]({source_url(ref)})')
    return ' · '.join(links)


def case_link(output, parent, check, label='Example'):
    path = output/'cases'/check['corpus']/(check['case'] + '.md')
    return f'[{label}]({relative(path, parent)})'


def examples(output, parent, checks, limit=2):
    selected = {}
    priority = {'change_needed':0, 'unsupported':0, 'blocked':1, 'unassessed':1, 'observation':2, 'matches':3}
    for c in sorted(checks, key=lambda x: (priority.get(x['status'],4), x['corpus'], x['case'])):
        selected.setdefault((c['corpus'], c['case']), c)
    return ' · '.join(case_link(output, parent, c, c['case'].replace('-', ' ').capitalize()) for c in list(selected.values())[:limit])


def outcome(entry):
    """Describe the RPC outcome without treating intentional errors as test failures."""
    r = entry['record']; obs = entry['observation']
    if not r['eligible']:
        return 'Setup incomplete; not assessed'
    response = obs.get('response') or {}
    status = r['status']
    if status in ('rpc_error', 'unsupported'):
        error = response.get('error') or {}
        label = 'Method unavailable' if status == 'unsupported' else 'RPC error'
        return f'{label} `{error.get("code", "?")}`'
    if status != 'result':
        return {'malformed_json': 'Incomplete or malformed JSON', 'invalid_envelope': 'Invalid JSON-RPC envelope', 'not_observed': 'No response captured'}.get(status, status.replace('_', ' '))
    value = response.get('result')
    if value is None:
        return '`null`'
    if isinstance(value, list):
        return f'{len(value)} records' if value else '`[]`'
    if isinstance(value, dict):
        if value.get('jsonrpc') == '2.0' and 'error' in value:
            return 'Error envelope nested inside result'
        if 'traceAddress' in value:
            return f'One frame, path `{json.dumps(value["traceAddress"])}`'
        if 'output' in value:
            output = value['output']
            suffix = f'{len(value["trace"])} call frames; ' if isinstance(value.get('trace'), list) else ''
            return suffix + ('output `null`' if output is None else 'output `0x`' if output == '0x' else 'nonempty output')
        return 'Object returned'
    return f'`{str(value)[:80]}`'


def note(editorial, client, topic, checks):
    topic_notes = editorial['topics'].get(topic, {})
    entry = topic_notes.get(family(client))
    if entry:
        requirements = list(dict.fromkeys(c['requirement'] for c in checks if c['status'] in BAD))
        suffix = ' Checked requirements: ' + ' '.join(requirements) if requirements and topic_notes.get('append_checked_requirements', True) else ''
        return entry['observed'], entry['change'] + suffix
    failed = list(dict.fromkeys(c['requirement'] for c in checks if c['status'] in BAD))
    return 'The linked case differs from the proposed behavior.', ' '.join(failed)


def prune_case_pages(output, cases):
    """Keep generated case pages aligned with the active report inventory."""
    expected = {output/'cases'/corpus/(name+'.md') for corpus,name in cases}
    for path in (output/'cases').rglob('*.md'):
        if path not in expected:
            path.unlink()


def changes_page(previous, records, by_client, decisions, editorial, revisions, matrix, output):
    """Captured verdict flips per decision and build between the previous and current matrices."""
    builds = {'previous': defaultdict(set), 'current': defaultdict(set)}
    for side, rows in [('previous', previous['records']), ('current', records)]:
        for r in rows:
            builds[side][r['client']].add(r['version'])
    clients = sorted(set(builds['previous']) | set(builds['current']), key=lambda c: (family(c), c.endswith('_development')))
    name = lambda c: editorial['clients'][family(c)]['name'] + {'release': ' stable', 'development': ' dev'}.get(c.rsplit('_', 1)[1], '')
    labels = {side: {c: '<br>'.join(build_label(c, v, revisions) for v in sorted(versions)) for c, versions in b.items()} for side, b in builds.items()}
    checked = {side: json.loads((m/'preflight.json').read_text())['checked_at'] for side, m in [('previous', previous['matrix']), ('current', matrix)]}
    text = '# Changes since the previous matrix\n\n[All reports](README.md) · [Test status key](technical.md#test-status-key)\n\n'
    text += (f'Captured check verdicts per decision and build: the current matrix (builds checked at **{checked["current"]}**, [preflight]({relative(matrix/"preflight.json", output)})) '
             f'against the previous one (checked at **{checked["previous"]}**, [preflight]({relative(previous["matrix"]/"preflight.json", output)})). '
             'The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. '
             'Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).\n\n')
    status = lambda c: ('New' if c not in labels['previous'] else 'Removed' if c not in labels['current']
                        else 'Updated' if labels['previous'][c] != labels['current'][c] else 'Unchanged')
    text += '## Builds\n\n' + table(['Client', 'Previous', 'Current', 'Change'], [
        [name(c), labels['previous'].get(c, '—'), labels['current'].get(c, '—'), status(c)] for c in clients])
    flips = defaultdict(list)
    for c in clients:
        if c in labels['previous'] and c in labels['current']:
            for topic, d in decisions.items():
                before, after = (display_verdict(checks.get(c, {}).get(topic, [])) for checks in (previous['by_client'], by_client))
                if before != after:
                    flips[family(c)].append([f'[{topic} · {d["title"]}](decisions/{topic}.md)', name(c), before, after])
    text += '## Verdict changes\n\n'
    if not flips:
        return text + 'No captured verdict changed.\n'
    count = sum(map(len, flips.values()))
    text += f'{count} {"verdict" if count == 1 else "verdicts"} changed for {len(flips)} {"client" if len(flips) == 1 else "clients"}.\n\n'
    for f in sorted(flips):
        text += f'### [{editorial["clients"][f]["name"]}](clients/{f}.md)\n\n' + table(['Decision', 'Build', 'Previous', 'Current'], flips[f])
    return text


def render(root, output, records, by_client, case_pages, run_rows, decisions, lock, previous=None):
    prune_case_pages(output, case_pages)
    editorial = json.loads((root/'decisions/impact.json').read_text())
    positions = check_positions(json.loads((root/'decisions/status.json').read_text()), decisions)
    statuses = {topic: decision_status(d, records, positions.get(topic, {})) for topic, d in decisions.items()}
    sources = json.loads((root/'decisions/sources.json').read_text())
    revisions = json.loads((root/'locks/source-revisions.json').read_text())
    clients = sorted({r['client'] for r in records})
    fixes = check_fixes(json.loads((root/'decisions/fixes.json').read_text()), decisions, editorial['clients'])
    stances = {topic: client_positions(positions.get(topic, {}).get('positions', {}), merged_fixes(fixes, topic)) for topic in decisions}
    built = {c: max((timestamp(ref['committed_at']) for v in {r['version'] for r in records if r['client'] == c}
                     if (ref := source_revision(c, v, revisions))), default=None) for c in clients}

    def build_verdict(client, topic):
        return display_verdict(by_client.get(client, {}).get(topic, []), pending_fixes(fixes, client, topic, built.get(client)))
    run_manifests = {row['name']: output/row['manifest'] for row in run_rows}
    build_runs = [{'manifest': json.loads(run_manifests[row['name']].read_text()),
                   'versions': row['versions'], 'path': run_manifests[row['name']]} for row in run_rows]
    captured = defaultdict(set)
    for r in records:
        captured[r['client']].add(r['version'])

    def label(client, version=None):
        versions = [version] if version is not None else sorted(captured[client])
        return '<br>'.join(build_label(client, v, revisions) for v in versions)

    freshness = ''
    selection = json.loads((root/'reports.lock.json').read_text())
    if selection.get('matrix') and {p.parent.resolve() for p in run_manifests.values()} == {(root/name).resolve() for name in selection['runs']}:
        matrix = root/selection['matrix']
        preflight = json.loads((matrix/'preflight.json').read_text())
        freshness = f'Published builds checked at **{preflight["checked_at"]}**. [Freshness preflight]({relative(matrix/"preflight.json", output)}) · [Nine-build lock]({relative(matrix/"clients.lock.json", output)}). All corpora use this snapshot; later upstream changes require a new capture.\n\n'
    availability = defaultdict(lambda: defaultdict(set))
    for entries in case_pages.values():
        for e in entries:
            r = e['record']
            if r['eligible']:
                availability[e['request']['method']][r['client']].add(r['status'])

    def method_status(method, client):
        statuses = availability[method][client]
        if 'unsupported' in statuses:
            return '⛔ Unavailable' if statuses == {'unsupported'} else '🟡 Mixed responses'
        if 'result' in statuses:
            return '📬 Returns results'
        return '↩️ Errors only' if statuses else '⚪ Not observed'

    families = sorted({family(c) for c in clients})
    names = {c: editorial['clients'][family(c)]['name'] for c in clients}

    # Progress is measured on each client's development build (the draft fork for Geth).
    converged = {t for t in decisions if positions.get(t, {}).get('policy') == 'converged'}
    progress_build = lambda f: 'go-ethereum_trace' if f == 'geth' else f + '_development'
    agreed = lambda checks: {t for t in decisions if verdict(checks.get(t, [])) == 'Checked cases agree'}
    progress = {}
    for f in families:
        c = progress_build(f)
        if c not in by_client:
            continue
        stable = f + '_release'
        progress[f] = dict(
            build=c, counts=tally({t: build_verdict(c, t).split(' ', 1)[0] for t in decisions}, converged),
            gained=len(agreed(by_client[c])) - len(agreed(previous['by_client'][c])) if previous and c in previous['by_client'] else None,
            dev_only=len(agreed(by_client[c]) - agreed(by_client[stable])) if stable in by_client else None,
            prs=pr_counts(fixes, f))
    native = [f for f in NATIVE_CLIENTS if f in progress]
    sums = sum((progress[f]['counts'] for f in native), Counter())
    signed = lambda n: f' ({n:+d} since the previous capture)' if n else ''
    gained = sum(progress[f]['gained'] or 0 for f in native)
    headline = (f'Across the {", ".join(editorial["clients"][f]["name"] for f in native[:-1])} and {editorial["clients"][native[-1]]["name"]} '
                f'development builds, **{sums["agree"]} of {len(native) * len(decisions)}** client decisions agree with the draft'
                f'{signed(gained) if previous else ""}. {sums["fix"]} more have a submitted fix, and '
                f'**{sums["converged"] + sums["review"]} differ with no fix yet**: {sums["converged"]} on converged decisions '
                f'and {sums["review"]} on decisions still under review. '
                f'{sum(progress[f]["dev_only"] or 0 for f in native)} agreements are in development builds but not yet in a stable release.') if native else ''

    def progress_line(f):
        p = progress[f]; counts = p['counts']
        pending = counts['converged'] + counts['review']
        parts = [f'✅ {counts["agree"]} agree{signed(p["gained"]) if p["gained"] is not None else ""}']
        parts += [f'🛠️ {counts["fix"]} fix submitted'] * bool(counts['fix'])
        parts += [f'⚠️ {pending} with no fix yet' + (f' ({counts["converged"]} on converged decisions)' if counts['converged'] else '')] * bool(pending)
        parts += [f'❔ {counts["policy"]} policy open'] * bool(counts['policy'])
        parts += [f'⚪ {counts["unmeasured"]} not fully measured'] * bool(counts['unmeasured'])
        text = f'**Progress on {label(p["build"])}** (of {len(decisions)} decisions): ' + ' · '.join(parts) + '.'
        if p['dev_only']:
            text += f' {p["dev_only"]} of these agreements are not yet in {label(f + "_release")}.'
        merged, opened = p['prs']
        if merged or opened:
            text += f' Upstream fix PRs: {merged} merged, {opened} open ([client fixes](../../docs/client-fixes.md)).'
        return text + '\n\n'
    by_family = {f: sorted((c for c in clients if family(c) == f), key=lambda c: c.endswith('_development')) for f in families}

    # Case pages are the drill-down, keeping the overview free of wire dumps.
    for (corpus, name), entries in sorted(case_pages.items()):
        path = output/'cases'/corpus/(name + '.md')
        method = entries[0]['request']['method']
        text = f'# {name.replace("-", " ").capitalize()}\n\n`{method}` · {corpus} · [All reports]({relative(output/"README.md", path.parent)})\n\n'
        requirements = list(dict.fromkeys(c['requirement'] for e in entries for c in e['record']['checks']))
        if requirements:
            text += '**What this checks:** ' + ' '.join(requirements) + '\n\n'
        rows = []
        for e in sorted(entries, key=lambda e: (family(e['record']['client']), e['record']['client'].endswith('_development'), e['record']['run'])):
            r = e['record']; client = r['client']
            assessment = display_verdict(r['checks'] if r['eligible'] else [])
            if r.get('schema', {}).get('status') == 'invalid':
                assessment += '; ⚠️ result shape differs'
            rows.append([f'[{names[client]} · {label(client, r["version"])}]({relative(output/"clients"/(client+".md"), path.parent)})', outcome(e), assessment, f'[Response]({relative(e["raw"], path.parent)}) · [Build/run]({relative(run_manifests[r["run"]], path.parent)})'])
        text += table(['Build', 'Returned', 'Compared with draft', 'Evidence'], rows)
        text += '<details><summary>Request and assertion details</summary>\n\n```json\n' + json.dumps(entries[0]['request'], indent=2) + '\n```\n\n'
        for e in entries:
            r = e['record']; failures = [c for c in r['checks'] if c['status'] in BAD or c['status'] in {'observation','unassessed','blocked','control','not_applicable'}]
            errors = r.get('schema', {}).get('errors', [])
            if not failures and not errors:
                continue
            text += f'**{names[r["client"]]} · {label(r["client"], r["version"])}** (`{r["version"]}`)\n\n'
            for c in failures:
                text += f'- [{c["topic"]}]({relative(output/"decisions"/(c["topic"]+".md"), path.parent)}): {c["requirement"]} {c.get("detail", "")}\n'
            for err in errors:
                text += f'- Result shape at `{err["path"] or "/"}`: {cell(err["message"])}\n'
            text += '\n'
        text += '</details>\n'
        save(path, text)

    # Each family has one review page, with stable per-build entry points as well.
    def client_page(f, selected, path):
        profile = editorial['clients'][f]
        text = f'# {profile["name"]}: changes to review\n\n{profile["summary"]}\n\n[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)\n\n'
        if f in progress and path.name == f + '.md':
            text += progress_line(f)
        text += table(['Tested version', 'Commit', 'Commit date (UTC)', 'Tested (UTC)'], build_rows(selected, build_runs, revisions, path.parent))
        versions = {r['version'] for r in records if r['client'] in selected}
        for build_note in profile.get('build_notes', []):
            if versions and versions <= set(build_note['versions']):
                text += build_note['text'] + '\n\n'
        text += 'Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method. [Test status key](../technical.md#test-status-key).\n\n'
        rows = []; matched = []; untested = []; observations = []; partial = []
        for topic, d in decisions.items():
            checks = [q for c in selected for q in by_client[c].get(topic, [])]
            if verdict(checks) == 'Policy open':
                observations.append(topic)
                continue
            if not any(q['status'] in BAD for q in checks):
                if topic != 'H01':
                    (partial if any(q['status'] in ['unassessed','blocked'] for q in checks) else matched if any(q['status']=='matches' for q in checks) else untested).append(topic)
                continue
            affected = next(c for c in selected if any(q['status'] in BAD for q in by_client[c].get(topic, [])))
            observed, change = note(editorial, affected, topic, checks)
            subject = f'[{d["title"]}](../decisions/{topic}.md)<br>{observed}'
            statuses = []
            for c in selected:
                cchecks = by_client[c].get(topic, [])
                value = build_verdict(c, topic)
                if coverage_summary(cchecks):
                    value += '<br>' + coverage_summary(cchecks)
                if cchecks:
                    value += '<br>' + examples(output, path.parent, cchecks, 1)
                statuses.append(value)
            links = source_links(sources, affected, topic)
            rows.append([subject, *statuses, change + ('<br>' + links if links else '')])
        text += '## Changes to discuss\n\n'
        text += table(['Behavior', *[label(c) for c in selected], 'Proposed change'], rows) if rows else 'No differences were found by the selected semantic assertions.\n\n'
        if observations:
            text += '## Open policy observations\n\nThese results record behavior whose policy is unresolved. Passing a checked part of a topic does not settle the remaining choices.\n\n'
            observation_rows = []
            for topic in observations:
                for c in selected:
                    checks = by_client[c].get(topic, [])
                    if checks:
                        detail = ' '.join(dict.fromkeys(q['detail'] for q in checks if q['status'] == 'observation'))
                        observed = [q for q in checks if q['status'] == 'observation']
                        observation_rows.append([label(c), f'[{decisions[topic]["title"]}](../decisions/{topic}.md)', coverage_summary(checks) + ' ' + detail, examples(output, path.parent, observed)])
            text += table(['Build', 'Decision', 'Observed', 'Example'], observation_rows)
        other_schema = [r for r in records if r['client'] in selected and r.get('schema', {}).get('status') == 'invalid']
        if other_schema:
            text += 'Result-shape differences are recorded on the [case pages](../technical.md#result-shape-checks); schema validity is separate from semantic coverage.\n\n'
        if partial:
            text += '## Assessment gaps\n\n'
            gap_rows = []
            for t in partial:
                for c in selected:
                    checks = by_client[c].get(t, [])
                    gaps = [q for q in checks if q['status'] in ['blocked','unassessed']]
                    if gaps:
                        fix = build_verdict(c, t)
                        gap_rows.append([f'[{decisions[t]["title"]}](../decisions/{t}.md)', label(c),
                                         coverage_summary(checks) + (f'<br>{fix}' if fix != display_verdict(checks) else ''),
                                         examples(output, path.parent, gaps)])
            text += table(['Decision', 'Build', 'Reason', 'Example'], gap_rows)
        if matched:
            text += '<details><summary>✅ Behaviors with no difference in the checked cases</summary>\n\n'
            text += table(['Behavior', 'Examples'], [[f'[{decisions[t]["title"]}](../decisions/{t}.md)', examples(output, path.parent, [q for c in selected for q in by_client[c].get(t, [])])] for t in matched])
            text += '</details>\n\n'
        if untested:
            text += '**⚪ Still needs review:** ' + ', '.join(f'[{decisions[t]["title"]}](../decisions/{t}.md)' for t in untested) + '.\n\n'
        text += '[Method availability](../decisions/H01.md) · [All decisions](../../decisions/README.md)\n\n'
        text += 'For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).\n'
        save(path, text)

    for f, selected in by_family.items():
        client_page(f, selected, output/'clients'/(f + '.md'))
        for c in selected:
            client_page(f, [c], output/'clients'/(c + '.md'))

    for topic, d in decisions.items():
        path = output/'decisions'/(topic + '.md')
        text = f'# {d["title"]}\n\n**Question:** {d["question"]}\n\n{topic} · {d["kind"]} · [All decisions](../../decisions/README.md)\n\n'
        position = positions.get(topic, {})
        text += f'**Status: {statuses[topic]}** · [Status definitions](../../decisions/README.md#status-key)\n\n'
        text += position.get('note', 'No policy conclusion has been recorded. Implementation observations below do not establish client-team agreement.') + '\n\n'
        if position.get('sources'):
            text += 'Policy evidence: ' + ' · '.join(f'[{source["label"]}]({source["url"]})' for source in position['sources']) + '.\n\n'
        key = '[Client positions](../../decisions/README.md#client-positions)'
        text += f'{key}: none recorded.\n\n' if not stances[topic] else f'{key}:\n\n' + table(['Client', 'Position', 'Note', 'Sources'], [
            [editorial['clients'][c]['name'], POSITIONS[s['position']], s['note'], ' · '.join(f'[{source["label"]}]({source["url"]})' for source in s['sources'])]
            if (s := stances[topic].get(c)) else [editorial['clients'][c]['name'], NO_POSITION, '', ''] for c in NATIVE_CLIENTS])
        sections = {'H12': 'explicit-choices-in-this-draft', 'H13': 'open-details-requiring-focused-review', 'H29': 'precompile-frames-h29'}
        if topic in sections:
            text += f'[Rule in the pinned draft]({lock["repository"]}/blob/{lock["commit"]}/docs-api/docs/trace-profile.md#{sections[topic]})\n\n'
        text += f'## Recommendation\n\n{d["recommendation"]}\n\n{d["rationale"]}\n\n'
        if d.get('background'):
            text += '## Background\n\n' + '\n\n'.join(d['background']) + '\n\n'
        if d.get('references'):
            text += 'Supporting controls (not standalone assertions): ' + ' · '.join(
                f'[{ref}](../cases/{ref}.md)' for ref in d['references']) + '.\n\n'
        text += f'## {d.get("comparison_heading", "What changes for clients")}\n\n'
        text += '[Test status key](../technical.md#test-status-key) · Build labels show the captured version and source commit.\n\n'
        rows = []
        for f, selected in by_family.items():
            checks = [q for c in selected for q in by_client[c].get(topic, [])]
            affected = next((c for c in selected if any(q['status'] in BAD for q in by_client[c].get(topic, []))), None)
            if affected:
                observed, change = note(editorial, affected, topic, checks)
                behavior = observed + '<br>**Proposed:** ' + change
            elif any(q['status'] in ['unassessed','blocked'] for q in checks):
                behavior = 'Some cases remain blocked or unassessed; see the per-build reasons. Matching checks do not establish agreement for this topic.'
            elif any(q['status'] == 'observation' for q in checks):
                details = []
                for c in selected:
                    observed = list(dict.fromkeys(q['detail'] for q in by_client[c].get(topic, [])
                                                  if q['status'] == 'observation' and q['detail']))
                    if observed:
                        details.append(f'{label(c)}: ' + ' '.join(observed))
                behavior = ('Evaluated requirements agree in the checked cases. ' if any(q['status']=='matches' for q in checks) else '') + '<br>'.join(details) + ' Policy remains open; these observations alone do not require a baseline change.'
            else:
                behavior = 'No change identified in the checked cases.' if checks else 'No automated assertion yet; review the recommendation.'
            build_cells = '<br>'.join(f'{label(c)}: {build_verdict(c, topic)}' +
                (f'<br>{coverage_summary(by_client[c].get(topic, []))}' if coverage_summary(by_client[c].get(topic, [])) else '') for c in selected)
            links = examples(output, path.parent, checks)
            code = source_links(sources, selected[0], topic)
            evidence_links = '<br>'.join(x for x in (
                '🧪 Tests: ' + links if links else '',
                '💻 Client code: ' + code if code else '',
            ) if x)
            rows.append([f'[{editorial["clients"][f]["name"]}](../clients/{f}.md)', build_cells, behavior, evidence_links])
        if topic == 'H01':
            text += '📬 Returned results establish method availability, not conformance. ⛔ Unavailable means unsupported; 🟡 marks mixed availability, ↩️ errors only, and ⚪ no observation. Errors for malformed input are expected.\n\n'
            method_rows = []
            for method in sorted(m for m in availability if m.startswith('trace_')):
                values = []
                for f, selected in by_family.items():
                    labels = [method_status(method, c) for c in selected]
                    values.append(labels[0] if len(set(labels)) == 1 else '<br>'.join(f'{label(c)}: {value}' for c,value in zip(selected,labels)))
                method_rows.append([f'`{method}`', *values])
            text += table(['Method', *[editorial['clients'][f]['name'] for f in families]], method_rows)
            text += 'Besu needs individual transaction replay or an agreed exclusion from the profile; the [block replay implementation](' + source_url(sources['besu']['replay']) + ') is a starting point.\n\n'
        else:
            text += table(['Client', 'Tested builds', 'Impact', 'Examples and code'], rows)
        text += f'## Decision needed\n\n{d["next_step"]}\n'
        save(path, text)

    text = '# Trace API: what would change?\n\nThe clients already share much of the `trace_*` API. These reports show where adopting the [draft specification](' + lock['repository'] + '/tree/' + lock['commit'] + ') would change their behavior. Start with your client, then use the examples and source links to review a proposed change.\n\n'
    text += freshness
    if previous:
        text += 'For verdicts that changed since the last capture, see [changes since the previous matrix](changes.md).\n\n'
    if native:
        save(output/'progress.svg', svg([(editorial['clients'][f]['name'], progress[f]['counts']) for f in native], len(decisions)))
        text += '## Progress\n\n' + headline + '\n\n![Decision outcomes per client development build](progress.svg)\n\n'
        text += table(['Client', 'Build', *[f'{symbol} {label}' for _, symbol, label, _, _ in BUCKETS], 'In dev, not stable', 'Fix PRs merged / open'], [
            [f'[{editorial["clients"][f]["name"]}](clients/{f}.md)', label(progress[f]['build']),
             *[str(progress[f]['counts'][key]) + (signed(progress[f]['gained']).replace(' since the previous capture', '') if key == 'agree' and progress[f]['gained'] else '')
               for key, *_ in BUCKETS],
             '—' if progress[f]['dev_only'] is None else str(progress[f]['dev_only']), '{} / {}'.format(*progress[f]['prs'])]
            for f in native])
        text += ('Each client has one outcome per decision on its development build. A difference with no submitted fix is the rough measure of pending work; '
                 'one decision can need several changes, and a PR can cover part of a decision or several. “Converged” and “under review” refer to the decision’s policy status. “In dev, not stable” counts agreements that the stable release does not share yet. '
                 'Fix PRs are upstream PRs attributed to the client, including its libraries; closed PRs are excluded. The Geth draft fork implements the proposal and is not counted. '
                 '[Status key](technical.md#test-status-key) · [Policy status](../decisions/README.md#status-key)\n\n')
    else:
        (output/'progress.svg').unlink(missing_ok=True)
    text += '## Start with your client\n\n'
    text += table(['Client', 'Main review areas'], [[f'[{editorial["clients"][f]["name"]}](clients/{f}.md)', editorial['clients'][f]['summary']] for f in families])
    text += '## Decisions to review\n\n'
    text += 'The largest API choices are [tree-path lookup](decisions/H02.md), [address-filter composition](decisions/H03.md), and [failed-frame results](decisions/H09.md). Other rows concern missing information or inconsistent execution/reporting. All recommendations remain proposals for client review.\n\n'
    text += table(['Question', 'Status', 'Proposed behavior'], [
        [f'[{title}](decisions/{topic}.md)', statuses[topic], behavior]
        for topic, title, behavior in [
            ('H02', 'How does trace_get select a frame?', 'Follow one tree path; return one object or null. An empty path selects the root.'),
            ('H03', 'How do address filters combine?', 'OR within each list, AND between sender and recipient lists.'),
            ('H30', 'Where does an unbounded filter start?', 'Default both omitted bounds to latest; historical searches specify fromBlock.'),
            ('H31', 'What block does trace_callMany use by default?', 'Accept an omitted block and use latest, matching trace_call.'),
            ('H32', 'Which tags and pending state can trace methods use?', 'Resolve mined-block tags; agree pending state and localization per method.'),
            ('H09', 'What survives a failed call?', 'Keep the error on that frame and preserve revert bytes and measured gas when available.'),
            ('H29', 'Which precompile frames are visible?', 'Keep root frames and nested frames with nonzero value; omit zero-value nested frames.'),
            ('H13', 'Signed transaction execution validity', 'Validate against the selected state, including nonce, funds and gas. Keep pool policies separate; propose -32003 for validation rejection.'),
        ]])
    text += '[Status definitions](../decisions/README.md#status-key). Policy direction is distinct from verified implementation on the captured builds.\n\n'
    text += '[All decisions](../decisions/README.md) · [Method availability](decisions/H01.md)\n\n'
    text += '[Client fixes](../docs/client-fixes.md) · [Client source guide](sources.md) · [Run a case](../docs/usage.md) · [Builds, coverage and raw results](technical.md) · [Standardization discussion](https://github.com/ethereum/execution-apis/issues/890)\n'
    save(output/'README.md', text)

    if previous:
        save(output/'changes.md', changes_page(previous, records, by_client, decisions, editorial, revisions, root/selection['matrix'], output))
    else:
        (output/'changes.md').unlink(missing_ok=True)

    text = '# Client source guide\n\nEntry points for reviewing the proposed changes. Links are pinned to the tested development revisions (or the experimental Geth fork), so line numbers remain stable. They identify relevant code, not necessarily the full fix.\n\n'
    for f in families:
        text += f'## {editorial["clients"][f]["name"]}\n\n'
        text += table(['Area', 'Source', 'Revision'], [[group.capitalize(), f'[{ref["label"]}]({source_url(ref)})', f'`{ref["commit"][:12]}`'] for group, ref in sources[f].items()])
    text += 'Reth’s inspector links point into its locked `revm-inspectors` 0.43.0 dependency. File hashes and anchor text are retained in [the source catalog](../decisions/sources.json).\n'
    save(output/'sources.md', text)

    text = '# Technical appendix\n\n[Back to the maintainer overview](README.md)\n\n'
    text += freshness
    text += 'The human reports summarize selected assertions against a proposed specification. Agreement is not full conformance, and an RPC error can be the correct result for an invalid-input case. Setup failures are excluded from semantic assessment. Version and commit labels identify captured builds; channel identifiers in raw artifacts describe how updates are discovered.\n\n'
    text += 'The experimental Geth fork implements the draft and is not an independent vote for its decisions. No verified pruning scenario is included for that fork.\n\n'
    text += ('## Test status key\n\n'
             '- ✅ **Checked cases agree:** the evaluated cases match the proposed contract; not full conformance.\n'
             '- ⚠️ **Differs:** at least one checked assertion differs from the proposal.\n'
             '- 🛠️ **Fix submitted:** the build differs or is partially assessed, and linked PRs for its client and decision cover the measured difference. '
             'Each is open, merged after the build’s commit, or merged in a library the build has not yet taken up. The captured checks are unchanged; '
             'retesting a build that contains the fix replaces this marker. A difference with only partial fixes keeps ⚠️ or 🟡 and links them as “partial fix”. '
             '[Related PRs](../docs/client-fixes.md).\n'
             '- ⛔ **Method unavailable:** the tested method is unsupported.\n'
             '- 🟡 **Partially assessed:** some declared cases or topics were not evaluated.\n'
             '- ⚪ **Not assessed:** no evaluated assertion establishes an outcome.\n'
             '- 🚧 **Blocked:** a missing response, failed setup or earlier failure prevents this check.\n'
             '- 🔎 **Control / not applicable:** reference evidence or a property that does not apply; never a semantic pass.\n'
             '- ❔ **Policy open:** observed behavior is recorded without a settled assertion.\n\n'
             'Build labels show versions and source commits. Test outcomes are separate from '
             '[policy agreement and harmonization](../decisions/README.md#status-key).\n\n')
    text += '## Reproduction and machine-readable results\n\nSee [usage](../docs/usage.md) for commands and [stateful scenarios](../docs/scenarios.md) for setup requirements. '
    text += '[checks.json](checks.json) retains every assertion; [comparisons.json](comparisons.json) groups exact responses; [assessment.json](assessment.json) pins the specification and assessment source hashes. Each case links its original response and run manifest.\n\n'
    text += 'To reproduce one case, use its linked manifest and the exact client, corpus and case name:\n\n```sh\nuv run trace-interop run --lock evidence/2026-09-21/RUN/manifest.json \\\n  --clients CLIENT --corpus CORPUS --case "^CASE$" --output runs/reproduce\n```\n\n'
    gaps = sorted({(r['client'],r['run'],r['corpus']) for r in records if not r['eligible']})
    text += '## Assertion coverage\n\nCoverage below counts all selected trace observations, including missing responses and failed setup, separately from schema validation. Partially assessed means at least one declared topic was not checked. A checked assertion is not proof of the rest of the topic.\n\n'
    text += table(['Coverage', 'Observations'], [[{'assessed': '🔎 Assessed', 'partial': '🟡 Partial', 'unassessed': '⚪ Unassessed', 'blocked':'🚧 Blocked', 'control':'🔎 Control'}[status], sum(r.get('assessment')==status for r in records if r['method'].startswith('trace_'))] for status in ['assessed','partial','unassessed','blocked','control']])
    property_gaps = defaultdict(lambda: defaultdict(int))
    for r in records:
        if r['method'].startswith('trace_'):
            for c in r['checks']:
                if c['status'] in ['unassessed','blocked','control','not_applicable']:
                    property_gaps[(c['topic'],c['status'],c.get('detail',''))][r['client']] += 1
    text += '\n### Unevaluated properties\n\nEach row names the reason; controls and inapplicable properties do not count as passes. Counts are topic obligations, so one response may appear more than once.\n\n'
    text += table(['Topic','Disposition','Reason','Observations'], [[topic,kind,detail,sum(counts.values())] for (topic,kind,detail),counts in sorted(property_gaps.items())])
    text += 'Eligibility is recomputed from the frozen head and independent scenario controls. `capture_eligible` in checks.json preserves the original capture decision; original summaries and wire observations are unchanged.\n\n'
    text += '## Setup gaps\n\n'
    text += table(['Build', 'Scenario', 'Run evidence'], [[names[c]+' · '+label(c), corpus, f'[{run}]({relative(run_manifests[run].parent/"summary.json", output)})'] for c,run,corpus in gaps]) if gaps else 'All selected runs passed their scenario eligibility checks.\n\n'
    text += '## Result-shape checks\n\nThese cases returned results that differ from the draft schema. The case pages retain the validation details; an unclassified schema failure is not silently counted as agreement.\n\n'
    shape = defaultdict(list)
    for r in records:
        if r.get('schema', {}).get('status') == 'invalid':
            shape[(r['corpus'],r['case'])].append(r['client'])
    text += table(['Case', 'Affected builds'], [[f'[{corpus}/{case}](cases/{corpus}/{case}.md)', ', '.join(names[c]+' '+label(c) for c in sorted(set(cs)))] for (corpus,case),cs in sorted(shape.items())])
    text += '## Runs\n\nCapture completeness records whether requests finished, not whether their results match the proposal.\n\n'
    text += table(['Run', 'Corpus', 'Capture complete'], [[f'[{row["name"]}]({row["manifest"]})',row['corpus'],'✅ Yes' if row['complete'] else '⚠️ No'] for row in run_rows])
    save(output/'technical.md', text)
    if output == (root/'reports').resolve():
        text = '# Trace API decisions\n\n[Client reports](../reports/README.md) · [Tested builds and coverage](../reports/technical.md) · [Source guide](../reports/sources.md)\n\n'
        index_families = ['besu', 'erigon', 'nethermind', 'reth', 'geth']
        text += ('The target is a useful, precise contract. Historical implementations explain compatibility costs, '
                 'but do not decide the recommendation. Intentional departures need a concrete benefit and an '
                 'explicit migration cost; observed agreement alone does not establish correctness.\n\n')
        if native:
            text += headline + ' [Progress by client](../reports/README.md#progress).\n\n'
        def channel_symbols(topic, channel):
            symbols = []
            for f in index_families:
                client = 'go-ethereum_trace' if f == 'geth' else f'{f}_{channel}'
                symbols.append('—' if f == 'geth' and channel == 'release' else build_verdict(client, topic).split(' ', 1)[0])
            return ''.join(symbols)
        text += table(['Decision', 'Status', 'Positions', 'Question', 'Stable', 'Dev'], [
            [f'[{t}](../reports/decisions/{t}.md)', statuses[t],
             ''.join(POSITIONS[stances[t][c]['position']].split(' ')[0] if c in stances[t] else NO_POSITION.split(' ')[0] for c in NATIVE_CLIENTS),
             f'**{d["title"]}**<br>{d["question"]}', channel_symbols(t, 'release'), channel_symbols(t, 'development')]
            for t,d in decisions.items()])
        text += '## Status key\n\n### Client checks\n\n'
        text += '**Client order:** ' + ' → '.join(f'[{editorial["clients"][f]["name"]}](../reports/clients/{f}.md)' for f in index_families) + '. Geth is the experimental draft fork, dev only; — marks its absent stable build.\n\n'
        text += ('Stable/dev symbols describe captured checks: ✅ agree · ⚠️ differ · 🛠️ fix submitted · ⛔ unavailable · '
                 '🟡 partial · ⚪ unassessed · 🚧 blocked · ❔ policy open · 🔎 control/N/A. '
                 '🛠️ replaces ⚠️ or 🟡 while [related PRs](../docs/client-fixes.md) for that client and decision cover the measured difference '
                 'and are not yet in the build; partial fixes leave ⚠️ or 🟡 in place. The captured checks are unchanged. '
                 '[Outcome details](../reports/technical.md#test-status-key).\n\n')
        text += '### Policy status\n\n' + LEGEND + '\n\n### Client positions\n\n' + POSITION_LEGEND + '\n'
        text += '\nDecision pages link directly relevant upstream issues and PRs as context. A filed issue, proposed patch or merged change does not establish cross-client agreement or change the captured checks for the pinned builds; 🛠️ only marks a difference with a submitted fix, and [client fixes](../docs/client-fixes.md) tracks implementation and retesting.\n'
        save(root/'decisions/README.md', text)
        save(root/'docs/client-fixes.md', fixes_page(fixes, root, root/'docs'))

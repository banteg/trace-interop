"""Build the trace_* tech tree page from site/tech-tree/tree.toml and the tracker.

tree.toml holds the layout and wording; every number and state comes from the tracker:
reports/progress.json (client builds), decisions/fixes.json (PR states) and decisions/status.json (policy).
The page is site/tech-tree/index.html with that data embedded, written to site/dist/index.html.
Standard library only, so Cloudflare's build image runs it without installing the project.
"""
import argparse
import json
from pathlib import Path
import subprocess
import tomllib

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT/'site/tech-tree'
PLACEHOLDER = '{{TREE_DATA}}'
UNSETTLED = ('fix', 'converged', 'review', 'policy')


def plural(count, word):
    return f'{count} {word}' + ('' if count == 1 else 's')


def repository(url):
    return '/'.join(url.split('/')[3:5])


def client_facts(spec, client, decisions):
    """A client build's agreement, version and PR counts; a dev build is done once nothing is unsettled."""
    builds = client['builds']
    build, dev = builds[spec['build']], builds['development']
    version = build['build'][0].split(' · ')[0]
    settled = not any(client['counts'][key] for key in UNSETTLED)
    facts = {'sub': spec['sub'].format(version=version), 'progress': [build['agree'], decisions, 'decisions agree']}
    if spec['build'] == 'development':
        counts, prs = client['counts'], client['prs']
        notes = [f'{counts["fix"]} more covered by submitted fixes' if counts['fix'] else '',
                 f'{plural(counts["converged"], "converged difference")} without a fix' if counts['converged'] else '']
        facts |= {'status': 'done' if settled else 'active', 'prs': {'merged': prs['merged'], 'open': prs['open']},
                  'summary': f'Agrees on {build["agree"]} of {decisions} decisions'
                             + ''.join(f'; {note}' for note in notes if note) + '. '
                             + f'{plural(prs["merged"], "PR")} merged, {prs["open"]} open.'}
    else:
        behind = dev['agree'] - build['agree']
        facts |= {'status': 'done' if settled and not behind else 'active',
                  'summary': f'{version} agrees on {build["agree"]} of {decisions} decisions'
                             + (f'; {behind} more agree in {dev["build"][0].split(" · ")[0]}.' if behind > 0 else ', as the dev build does.')}
    return facts


def library_facts(spec, prs):
    """PR counts over the node's repositories; closed PRs don't count."""
    states = [pr['state'] for pr in prs.values() if repository(pr['url']) in spec['repos']]
    merged, open_ = states.count('merged'), states.count('open')
    return {'status': 'active' if open_ else 'done', 'prs': {'merged': merged, 'open': open_},
            'summary': f'{plural(merged, "PR")} merged, {open_} open.'}


def pr_facts(spec, prs):
    pr = prs[spec['pr']]
    if pr['state'] == 'merged':
        return {'status': 'done', 'label': 'merged'}
    return {'status': 'active', 'label': 'draft PR' if pr['draft'] else 'open PR'}


def build(tree, progress, fixes, status, captured):
    """The page data: tree.toml's nodes with states, labels, progress and PR counts from the tracker."""
    decisions = progress['decisions']
    clients = {client['client']: client for client in progress['clients']}
    prs = {pr['url']: pr for pr in fixes['prs']}
    converged = sum(entry['policy'] == 'converged' for entry in status.values())

    nodes = {}
    for spec in tree['node']:
        col, row = spec['cell']
        node = {'id': spec['id'], 'title': spec['title'], 'sub': spec['sub'], 'icon': spec['icon'], 'col': col, 'row': row,
                'span': spec.get('span', 1), 'category': spec['category'], 'critical': spec.get('critical', False),
                'requires': spec.get('requires', []), 'actor': spec.get('actor'), 'also': spec.get('also'), 'url': spec['url'],
                'text': spec['text'], 'tag': spec.get('tag'), 'label': spec.get('label'), 'status': spec.get('status', 'active'),
                'summary': None, 'progress': None, 'prs': None}
        if 'client' in spec:
            node |= client_facts(spec, clients[spec['client']], decisions)
        elif 'repos' in spec:
            node |= library_facts(spec, prs)
        elif 'pr' in spec:
            node |= pr_facts(spec, prs)
        if spec.get('progress') == 'converged':
            node |= {'progress': [converged, decisions, 'decisions converged'], 'label': f'{converged}/{decisions} converged',
                     'summary': f'{converged} of {decisions} decisions have converged on a policy.'}
        nodes[spec['id']] = node

    # States that depend on other nodes, in file order.
    for spec in tree['node']:
        node = nodes[spec['id']]
        if 'done_with' in spec and nodes[spec['done_with']]['status'] == 'done':
            node['status'] = 'done'
        waiting = [nodes[other] for other in spec.get('locked_until', []) if nodes[other]['status'] != 'done']
        if waiting and node['status'] != 'done':
            node |= {'status': 'locked', 'label': f'waits on {waiting[0]["title"]}'}
    for node in nodes.values():
        node['allows'] = [other['id'] for other in nodes.values() if node['id'] in other['requires']]
    researching = next((node for node in sorted(nodes.values(), key=lambda n: n['col'])
                        if node['critical'] and node['status'] == 'active'), None)
    if researching:
        researching['now'] = True

    counted = [client for client in progress['clients'] if client['counted']]
    return {
        'decisions': decisions,
        'captured': captured,
        'fixes_checked': fixes['checked_at'],
        'researching': researching and researching['id'],
        'totals': {'agree': sum(client['builds']['development']['agree'] for client in counted),
                   'of': len(counted) * decisions,
                   'merged': sum(client['prs']['merged'] for client in counted),
                   'open': sum(client['prs']['open'] for client in counted),
                   'clients': [client['name'] for client in counted]},
        'layout': tree['layout'],
        'eras': tree['era'],
        'advisor': tree['advisor'],
        'nodes': list(nodes.values()),
        'actors': tree['actor'],
        'contributors': tree['contributor'],
        'repos': [repo | {'url': f'https://github.com/{repo["name"]}'} for repo in tree['repo']],
        'steps': tree['step'],
    }


def load(root=ROOT):
    """The tracker files the page reads, as build() arguments."""
    read = lambda path: json.loads((root/path).read_text())
    matrix = read('reports.lock.json')['matrix']
    return {'tree': tomllib.loads((root/'site/tech-tree/tree.toml').read_text()),
            'progress': read('reports/progress.json'),
            'fixes': read('decisions/fixes.json'),
            'status': read('decisions/status.json'),
            'captured': read(f'{matrix}/preflight.json')['checked_at'][:10]}


def render(data, template):
    """Embed the data in the page; `</` is escaped so text can't close the script element."""
    payload = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    return template.replace(PLACEHOLDER, payload)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--out', type=Path, default=ROOT/'site/dist', help='output directory (default: site/dist)')
    args = parser.parse_args()
    data = build(**load())
    data['commit'] = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], cwd=ROOT, check=True,
                                    capture_output=True, text=True).stdout.strip()
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out/'index.html').write_text(render(data, (SITE/'index.html').read_text()))
    print(f'wrote {args.out/"index.html"} ({len(data["nodes"])} nodes, commit {data["commit"]})')


if __name__ == '__main__':
    main()

"""One explicit inventory for report generation and evidence-reference verification."""
import json
from pathlib import Path


def report_runs(root):
    selection = json.loads((root/'reports.lock.json').read_text())
    names = selection['runs']
    if not names or len(names) != len(set(names)):
        raise ValueError('empty or duplicate report runs')
    paths = [(root/name).resolve() for name in names]
    for path in paths:
        if not path.is_relative_to(root.resolve()/'evidence') or not (path/'manifest.json').is_file():
            raise ValueError(f'invalid report run: {path}')
    if selection.get('matrix'):
        matrix = (root/selection['matrix']).resolve()
        if not matrix.is_relative_to(root.resolve()/'evidence'):
            raise ValueError('matrix must be retained evidence')
        pinned = json.loads((matrix/'clients.lock.json').read_text())
        preflight = json.loads((matrix/'preflight.json').read_text())
        builds = {n:v['image_id'] for n,v in pinned['clients'].items()}
        from .versions import NAMES
        from .cli import compatible
        if set(builds) != set(NAMES)|{'go-ethereum_trace'}:
            raise ValueError('current report matrix requires every native build and the Geth fork')
        if preflight.get('status') != 'current' or preflight.get('clients') != builds or not preflight.get('checked_at'):
            raise ValueError('current report matrix lacks a matching freshness preflight')
        # A focused capture outside the matrix directory, with the matrix's builds, adds a corpus the
        # matrix lacks or replaces the matrix's run of a corpus when it resends every request that run sent.
        manifests = {path: json.loads((path/'manifest.json').read_text()) for path in paths}
        corpora = {manifest['corpus']: path for path, manifest in manifests.items()}
        if len(corpora) != len(paths):
            raise ValueError('a focused run repeats a corpus of the current matrix')
        for run in json.loads((matrix/'matrix.json').read_text()):
            own, chosen = (matrix/run['corpus']).resolve(), corpora.get(run['corpus'])
            if chosen is None:
                raise ValueError('report selection must retain the entire current matrix, including incomplete runs')
            if chosen != own:
                sent = {c['name']: c['request'] for c in manifests[chosen]['selected_cases']}
                if any(sent.get(c['name']) != c['request'] for c in json.loads((own/'manifest.json').read_text())['selected_cases']):
                    raise ValueError(f'a focused recapture must resend every request of the matrix run it replaces: {chosen}')
        for path, manifest in manifests.items():
            expected = {n for n in builds if compatible(manifest['corpus'], pinned['clients'][n])}
            if set(manifest['clients']) != expected or any(
                info != pinned['clients'].get(name) for name,info in manifest['clients'].items()
            ):
                raise ValueError(f'mixed or missing builds in current matrix: {path}')
    return paths


def previous_runs(root):
    """Every run of the previous matrix named by reports.lock.json, for the changes page."""
    selection = json.loads((root/'reports.lock.json').read_text())
    previous = (root/selection['previous']).resolve()
    if (not previous.is_relative_to(root.resolve()/'evidence') or previous == (root/selection['matrix']).resolve()
            or not (previous/'matrix.json').is_file()):
        raise ValueError(f'invalid previous matrix: {previous}')
    paths = [previous/r['corpus'] for r in json.loads((previous/'matrix.json').read_text())]
    if not paths or any(not (path/'manifest.json').is_file() for path in paths):
        raise ValueError(f'incomplete previous matrix: {previous}')
    return paths


def verify_inventory(root):
    available = set()
    for path in report_runs(root):
        manifest = json.loads((path/'manifest.json').read_text())
        available.update(manifest['corpus']+'/'+c['name'] for c in manifest['selected_cases'])
    items = json.loads((root/'decisions/ledger.json').read_text())['items']
    status = json.loads((root/'decisions/status.json').read_text())
    for item in items:
        # A decision still under review may precede its cases; a policy conclusion needs evidence.
        if not item['cases'] and status.get(item['id'], {}).get('policy', 'review') != 'review':
            raise ValueError(f'empty evidence references: {item["id"]}')
        if set(item['cases']) & set(item.get('references', [])):
            raise ValueError(f'case is also a reference: {item["id"]}')
        for reference in item['cases'] + item.get('references', []):
            if reference not in available:
                raise ValueError(f'missing report evidence: {item["id"]}/{reference}')
    return len(items)


def cover_topics(checks, expected):
    covered = {c['topic'] for c in checks}
    return checks + [{'topic': topic, 'status': 'unassessed',
                      'requirement': 'Assess this declared topic case.',
                      'detail': 'No semantic assertion evaluated this topic for the captured response.'}
                     for topic in sorted(set(expected)-covered)]

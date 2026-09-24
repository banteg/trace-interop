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
        if set(builds) != set(NAMES)|{'go-ethereum_trace'}:
            raise ValueError('current report matrix requires all nine builds')
        if preflight.get('status') != 'current' or preflight.get('clients') != builds or not preflight.get('checked_at'):
            raise ValueError('current report matrix lacks a matching freshness preflight')
        captured = json.loads((matrix/'matrix.json').read_text())
        if {p.resolve() for p in paths} != {(matrix/r['corpus']).resolve() for r in captured}:
            raise ValueError('report selection must retain the entire current matrix, including incomplete runs')
        for path in paths:
            manifest = json.loads((path/'manifest.json').read_text())
            expected = {'reth_release','reth_development'} if manifest['corpus'] == 'pruned' else set(builds)
            if set(manifest['clients']) != expected or any(
                info != pinned['clients'].get(name) for name,info in manifest['clients'].items()
            ):
                raise ValueError(f'mixed or missing builds in current matrix: {path}')
    return paths


def verify_inventory(root):
    available = set()
    for path in report_runs(root):
        manifest = json.loads((path/'manifest.json').read_text())
        available.update(manifest['corpus']+'/'+c['name'] for c in manifest['selected_cases'])
    items = json.loads((root/'decisions/ledger.json').read_text())['items']
    for item in items:
        if not item['cases']:
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

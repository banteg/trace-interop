"""One explicit inventory for report generation and evidence-reference verification."""
import json
from pathlib import Path


def report_runs(root):
    names = json.loads((root/'reports.lock.json').read_text())['runs']
    if not names or len(names) != len(set(names)):
        raise ValueError('empty or duplicate report runs')
    paths = [(root/name).resolve() for name in names]
    for path in paths:
        if not path.is_relative_to(root.resolve()/'evidence') or not (path/'manifest.json').is_file():
            raise ValueError(f'invalid report run: {path}')
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

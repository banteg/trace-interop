"""Refresh PR titles and states in decisions/fixes.json from GitHub; report generation stays offline.

Editorial fields (client, decisions, partial, awaiting_uptake, note) are kept as written.
"""
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess


def view(url):
    return json.loads(subprocess.run(['gh', 'pr', 'view', url, '--json', 'title,state,isDraft,mergedAt'],
                                     capture_output=True, text=True, check=True).stdout)


def refresh(path, view=view):
    fixes = json.loads(path.read_text())
    for pr in fixes['prs']:
        info = view(pr['url'])
        current = dict(title=info['title'], state=info['state'].lower(), draft=info['isDraft'], merged_at=info['mergedAt'])
        changed = {k: v for k, v in current.items() if pr[k] != v}
        if changed:
            print(pr['url'], ', '.join(f'{k}: {pr[k]} -> {v}' for k, v in changed.items()))
        pr.update(current)
    fixes['checked_at'] = datetime.now(timezone.utc).date().isoformat()
    path.write_text(json.dumps(fixes, indent=2) + '\n')
    return fixes


if __name__ == '__main__':
    fixes = refresh(Path(__file__).resolve().parents[1]/'decisions/fixes.json')
    print(f'Checked {len(fixes["prs"])} PRs; run scripts/build_reports.py to regenerate the reports.')

"""Warn when the pinned draft trails its branch or the fix catalog has not been refreshed recently.

Advisory only: exits 1 when there is a warning (including an unreachable remote), so CI runs it
as a step that may fail without failing the check.
"""
import argparse
from datetime import date, datetime, timezone
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def remote_head(repository, branch):
    output = subprocess.run(['git', 'ls-remote', repository, f'refs/heads/{branch}'],
                            capture_output=True, text=True, timeout=60, check=True).stdout.split()
    return output[0] if output else None


def warnings(lock, head, checked_at, today, max_age):
    found = []
    if head is None:
        found.append(f'{lock["repository"]} has no branch {lock["branch"]}')
    elif head != lock['commit']:
        found.append(f'spec.lock.json pins {lock["commit"][:12]}, but {lock["branch"]} is at {head[:12]}; '
                     'review the branch and run scripts/pin_spec.py if the draft changed')
    age = (today - date.fromisoformat(checked_at)).days
    if age > max_age:
        found.append(f'decisions/fixes.json was last checked {checked_at} ({age} days ago); run scripts/refresh_fixes.py')
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--max-age', type=int, default=7, help='days before the fix catalog counts as stale')
    args = parser.parse_args()
    lock = json.loads((ROOT/'spec.lock.json').read_text())
    try:
        head = remote_head(lock['repository'], lock['branch'])
        found = []
    except (subprocess.SubprocessError, OSError) as error:
        head, found = lock['commit'], [f'could not check {lock["repository"]} {lock["branch"]}: {error}']
    found += warnings(lock, head, json.loads((ROOT/'decisions/fixes.json').read_text())['checked_at'],
                      datetime.now(timezone.utc).date(), args.max_age)
    for message in found:
        print(f'::warning title=Freshness::{message}' if os.environ.get('GITHUB_ACTIONS') else f'warning: {message}')
    if not found:
        print(f'Draft pin matches {lock["branch"]} and the fix catalog is current.')
    return 1 if found else 0


if __name__ == '__main__':
    raise SystemExit(main())

"""Print the Telegram caption announcing the eval matrix that reports.lock.json selects.

The caption gives each client's development and stable scores from reports/progress.json, the
decisions its build agrees on with their change since the previous matrix, and links to the
pages at `--url`. It is Telegram HTML whose visible text stays within the 1024-character photo
caption limit; the progress chart is sent as the photo.
"""
import argparse
from html import escape, unescape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CAPTION_LIMIT = 1024


def delta(gained=0, lost=0):
    return ' '.join(f'{sign}{n}' for sign, n in (('+', gained), ('−', lost)) if n)


def score(agree, gained=0, lost=0, **_):
    change = delta(gained, lost)
    return f'{agree} ({change})' if change else str(agree)


def channel(clients, name):
    return ' · '.join(f'{escape(c["name"])} {score(**c["builds"][name])}' for c in clients if name in c['builds'])


def caption(root, url):
    matrix = Path(json.loads((root/'reports.lock.json').read_text())['matrix'])
    progress = json.loads((root/'reports/progress.json').read_text())
    counted = [c for c in progress['clients'] if c['counted']]
    total = {key: sum(c['builds']['development'].get(key, 0) for c in counted) for key in ('agree', 'gained', 'lost')}
    change = delta(total['gained'], total['lost'])
    omitted = [c['name'] for c in progress['clients'] if not c['counted']]
    links = [('Progress', 'reports/README.md#progress')]
    if (root/'reports/changes.md').exists():
        links.append(('Changes', 'reports/changes.md'))
    links.append(('Eval notes', (matrix/'README.md').as_posix()))
    text = '\n'.join([
        f'<b>Eval {escape(matrix.parent.name)}</b> · {total["agree"]} of {len(counted) * progress["decisions"]} agree' + (f' ({change})' if change else ''),
        '',
        f'Dev: {channel(progress["clients"], "development")}',
        f'Stable: {channel(progress["clients"], "release")}',
        '',
        f'Scores count decisions that agree with the draft, of {progress["decisions"]}' + (f'; the total omits {escape(", ".join(omitted))}.' if omitted else '.'),
        ' · '.join(f'<a href="{escape(f"{url}/{path}")}">{name}</a>' for name, path in links),
    ])
    visible = len(unescape(re.sub(r'<[^>]+>', '', text)))
    if visible > CAPTION_LIMIT:
        raise ValueError(f'caption is {visible} characters; Telegram allows {CAPTION_LIMIT}')
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--url', required=True, help='base URL of the repository files, e.g. a GitHub blob URL at the commit')
    args = parser.parse_args()
    print(caption(ROOT, args.url.rstrip('/')))


if __name__ == '__main__':
    main()

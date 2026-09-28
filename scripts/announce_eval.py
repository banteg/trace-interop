"""Print the Telegram caption announcing the eval matrix that reports.lock.json selects.

The caption reuses the generated reports: the eval notes' title, the progress headline and the
verdict-change summary, with links to the pages at `--url`. It is Telegram HTML whose visible text
stays within the 1024-character photo caption limit; the progress chart is sent as the photo.
"""
import argparse
from html import escape, unescape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CAPTION_LIMIT = 1024


def paragraph(text, heading):
    """The first paragraph under a markdown heading."""
    section = text.split(f'\n{heading}\n', 1)[1]
    return section.strip().split('\n\n', 1)[0]


def inline(markdown):
    """Telegram HTML for a markdown paragraph: bold kept, links reduced to their text."""
    text = escape(re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', markdown), quote=False)
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)


def caption(root, url):
    matrix = json.loads((root/'reports.lock.json').read_text())['matrix']
    notes = root/matrix/'README.md'
    title = notes.read_text().split('\n', 1)[0].removeprefix('# ')
    lines = [f'<b>{escape(title, quote=False)}</b>', inline(paragraph((root/'reports/README.md').read_text(), '## Progress'))]
    links = [('Progress', 'reports/README.md#progress')]
    changes = root/'reports/changes.md'
    if changes.exists():
        lines.append(inline(paragraph(changes.read_text(), '## Verdict changes')))
        links.append(('Changes', 'reports/changes.md'))
    links.append(('Eval notes', notes.relative_to(root).as_posix()))
    lines.append(' · '.join(f'<a href="{escape(f"{url}/{path}")}">{name}</a>' for name, path in links))
    text = '\n\n'.join(lines)
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

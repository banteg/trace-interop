"""List retained evidence that nothing references, as candidates to move out of the repository.

Dry run only: nothing is moved or deleted. A capture unit is `evidence/<date>/<name>`, or the whole
`evidence/<date>` directory when that directory holds a capture's files itself. A unit is referenced
when reports.lock.json selects it (`runs`, `matrix` or `previous`), when a Markdown link anywhere in
the repository points into it (links from inside the unit itself do not count), or when a tracked
text file outside evidence/ names a path inside it. `--tests` also runs the unit tests and counts
evidence they open, which catches paths the tests assemble at run time.
"""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT/'evidence'
TEXT = {'.md', '.py', '.json', '.yml', '.yaml', '.sh', '.toml'}


def units():
    found = set()
    for manifest in EVIDENCE.rglob('manifest.json'):
        date = EVIDENCE/manifest.relative_to(EVIDENCE).parts[0]
        found.add(date if any(p.is_file() for p in date.iterdir()) else date/manifest.relative_to(date).parts[0])
    return sorted(found)


def unit_of(path, all_units):
    return next((u for u in all_units if path == u or path.is_relative_to(u)), None)


def text_references(all_units):
    """Units named by Markdown links or literal evidence paths, ignoring links from inside a unit to itself."""
    files = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split('\0')
    targets = set()
    for name in filter(None, files):
        path = ROOT/name
        inside = path.is_relative_to(EVIDENCE)
        if path.suffix not in TEXT or inside and path.suffix != '.md' or not path.is_file():
            continue
        text = path.read_text(errors='replace')
        source = unit_of(path, all_units) if inside else None
        targets |= {(source, os.path.normpath(path.parent/t.split('#')[0])) for t in set(re.findall(r'\]\(([^)\s#]+)', text))
                    if '://' not in t}
        if not inside:
            targets |= {(None, os.path.normpath(ROOT/t.rstrip('./'))) for t in set(re.findall(r'evidence/[\w./-]+', text))}
    return {unit for source, target in targets if (unit := unit_of(Path(target), all_units)) and unit != source}


def opened_by_tests():
    opened = set()
    sys.addaudithook(lambda event, args: event in ('open', 'os.scandir', 'os.listdir') and isinstance(args[0], (str, Path))
                     and opened.add(Path(os.path.abspath(args[0]))))
    with open(os.devnull, 'w') as quiet:
        unittest.TextTestRunner(stream=quiet).run(unittest.defaultTestLoader.discover(str(ROOT/'tests')))
    return opened


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--tests', action='store_true', help='also count evidence the unit tests open')
    args = parser.parse_args()
    all_units = units()
    selection = json.loads((ROOT/'reports.lock.json').read_text())
    referenced = {unit_of((ROOT/p).resolve(), all_units) for p in [*selection['runs'], selection.get('matrix'), selection.get('previous')] if p}
    referenced |= text_references(all_units)
    if args.tests:
        referenced |= {unit_of(p, all_units) for p in opened_by_tests()}
    candidates = [u for u in all_units if u not in referenced]
    size = lambda folder: sum(p.stat().st_size for p in folder.rglob('*') if p.is_file())
    for unit in candidates:
        print(f'{size(unit)/1e6:8.1f} MB  {unit.relative_to(ROOT)}')
    print(f'{len(candidates)} of {len(all_units)} capture units are unreferenced '
          f'({sum(map(size, candidates))/1e6:.1f} of {sum(map(size, all_units))/1e6:.1f} MB); nothing was moved.')


if __name__ == '__main__':
    main()

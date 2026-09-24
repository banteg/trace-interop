"""Compare captured client responses.

show:   print one case's selected output family for every build.
groups: list cases whose builds disagree on an output family, grouped by identical output.
"""
import argparse
import json
from pathlib import Path

from trace_interop.cli import COMPACT_OBSERVATIONS, OBSERVATIONS, load_observations

FAMILIES = ['trace', 'stateDiff', 'vmTrace', 'output']


def result(observation):
    if 'response' not in observation:
        return {'malformed': observation['raw_response'][:200]}
    response = observation['response']
    return response['result'] if 'result' in response else {'error': response.get('error')}


def select(value, family):
    """Project an envelope (or list of envelopes) onto one output family; other results pass through."""
    if isinstance(value, list) and all(isinstance(e, dict) and family in e for e in value):
        return [e[family] for e in value]
    if isinstance(value, dict) and family in value:
        return value[family]
    return value


def show(args):
    path = Path(args.observations)
    case = load_observations(path if path.is_dir() else path.parent)[args.case]
    for build, observation in case.items():
        if args.builds and not any(b in build for b in args.builds):
            continue
        print('==', build)
        print(json.dumps(select(result(observation), args.family), sort_keys=True, indent=args.indent)[:args.limit])


def groups(args):
    runs = {p.parent for name in [OBSERVATIONS, COMPACT_OBSERVATIONS] for p in Path(args.evidence).glob('*/'+name)}
    for run in sorted(runs):
        for name, case in load_observations(run).items():
            if name.startswith('_control'):
                continue
            outputs = {}
            for build, observation in case.items():
                value = select(result(observation), args.family)
                if value not in (None, [], {}) and not (isinstance(value, list) and all(v is None for v in value)):
                    outputs.setdefault(json.dumps(value, sort_keys=True), []).append(build)
            if len(outputs) > 1:
                ranked = sorted(outputs.values(), key=len, reverse=True)
                print(run.name, name, ' | '.join(','.join(sorted(g)) for g in ranked))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(required=True)
    one = commands.add_parser('show', help="print one case's output for every build")
    one.add_argument('observations', help='a run directory or its observations file (observations.json or observations.json.gz)')
    one.add_argument('case')
    one.add_argument('--family', choices=FAMILIES, default='stateDiff')
    one.add_argument('--builds', nargs='*', help='substrings selecting builds, e.g. besu reth_release')
    one.add_argument('--indent', type=int)
    one.add_argument('--limit', type=int, default=4000, help='truncate each printed output to this many characters')
    one.set_defaults(run=show)
    many = commands.add_parser('groups', help='list cases whose builds disagree')
    many.add_argument('evidence', help='an evidence snapshot directory, e.g. evidence/2026-09-24/h15-call-compat')
    many.add_argument('--family', choices=FAMILIES, default='stateDiff')
    many.set_defaults(run=groups)
    args = parser.parse_args()
    args.run(args)


if __name__ == '__main__':
    main()

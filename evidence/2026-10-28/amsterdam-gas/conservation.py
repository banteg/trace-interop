"""Check the two-dimensional vmTrace law on each client's ops.

Within one frame, for an op that enters no child frame:
  ex.used[i] + stateUsed[i] == ex.used[i-1] + stateUsed[i-1] - cost[i] - stateGasCost[i]
(Erigon's members; a client without them is checked with zeros, which is the one-dimensional law).
The one-dimensional law ex.used[i] == ex.used[i-1] - cost[i] is reported alongside.
Usage: uv run python conservation.py <run dir>
"""
import gzip
import json
import sys
from collections import Counter
from pathlib import Path

ENTERS = {0xf0, 0xf1, 0xf2, 0xf4, 0xf5, 0xfa}


def walk(vm, tally, start):
    code = bytes.fromhex(vm.get('code', '0x')[2:])
    prev = start
    for op in vm.get('ops', []):
        ex = op.get('ex')
        if op.get('sub'):
            walk(op['sub'], tally, None)
        if not ex:
            prev = None
            continue
        used, state = ex['used'], ex.get('stateUsed', 0)
        byte = code[op['pc']] if op['pc'] < len(code) else None
        if prev is not None and byte not in ENTERS:
            tally['2d ok' if prev[0] + prev[1] - op['cost'] - op.get('stateGasCost', 0) == used + state else '2d broken'] += 1
            tally['1d ok' if prev[0] - op['cost'] == used else '1d broken'] += 1
        prev = (used, state)


def main(run):
    observations = json.load(gzip.open(Path(run) / 'observations.json.gz'))
    by_client = {}
    for case, results in observations.items():
        for client, obs in results.items():
            if 'raw_response' not in obs:
                continue
            result = json.loads(obs['raw_response']).get('result')
            vm = result.get('vmTrace') if isinstance(result, dict) else None
            if vm:
                walk(vm, by_client.setdefault(client, Counter()), None)
    for client, tally in sorted(by_client.items()):
        print(client, dict(sorted(tally.items())))


if __name__ == '__main__':
    main(sys.argv[1])

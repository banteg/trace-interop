"""Check the two-dimensional vmTrace law on each client's ops.

Within one frame, each op moves the total ex.used + stateUsed by its charges and what a child returns:
  ex.used[i] + stateUsed[i] == ex.used[i-1] + stateUsed[i-1] - cost[i] - stateGasCost[i] + returned[i]
(Erigon's members; a client without them is checked with zeros, which is the one-dimensional law).
returned is 0 for an op that enters no child frame. A CALL or CREATE whose child ran instructions
lends the child the caller's reservoir after its own state charge, max(stateUsed[i-1] - stateGasCost[i], 0),
and gets back:
  - from a child that stops or returns, the child's total after its last op; a creation pays its code
    deposit out of it, 1530 state gas per byte plus 6 per word of hashing;
  - from a reverted child, that total plus the child's net state gas (its own charges and its
    successful children's), which the rollback refills;
  - from a halted child, only the lent reservoir: its gas_left is consumed.
A CALL or CREATE whose child ran no instruction (an empty-code target, a precompile) or that entered
no frame (a failed balance or depth precheck) gets back the gas it forwarded, which vmTrace does not
report apart from cost, so it is counted as unchecked. The one-dimensional law
ex.used[i] == ex.used[i-1] - cost[i] + returned[i], ignoring the state members, is reported alongside.
Usage: uv run python conservation.py <run dir>
"""
import gzip
import json
import sys
from collections import Counter
from pathlib import Path

from trace_interop.vm_model import returned_size

ENTERS, CREATES = {0xf0, 0xf1, 0xf2, 0xf4, 0xf5, 0xfa}, {0xf0, 0xf5}
STATE_BYTE, HASH_WORD = 1530, 6


def frame(vm, tally, law):
    """Check one frame's ops under the '1d' or '2d' law and return its outcome ('ok', 'revert' or
    'halt'), its total after its last op and its net state gas."""
    code = bytes.fromhex(vm.get('code', '0x')[2:])
    member = (lambda o, k: o.get(k, 0)) if law == '2d' else (lambda o, k: 0)
    prev, net, outcome = None, 0, 'ok'
    for op in vm.get('ops', []):
        ex, sub = op.get('ex'), op.get('sub')
        byte = code[op['pc']] if op['pc'] < len(code) else None
        child = frame(sub, tally, law) if sub and sub.get('ops') else None
        if not ex:
            prev, outcome = None, 'halt'
            continue
        total, charge = ex['used'] + member(ex, 'stateUsed'), member(op, 'stateGasCost')
        kind = 'call/create' if byte in ENTERS else 'other'
        want = prev[0] - op['cost'] - charge if prev else None
        net += charge
        if child:
            ended, end, child_net = child
            if ended == 'ok' and byte in CREATES:
                size = returned_size(sub)
                stored = STATE_BYTE*size*(law == '2d') if size is not None else 0
                end = None if size is None else end - stored - HASH_WORD*((size+31)//32)
                child_net += stored
            if ended == 'ok':
                net += child_net
            if want is not None:
                lent = max(prev[1] - charge, 0)
                back = lent if ended == 'halt' else end + child_net if ended == 'revert' else end
                want = None if back is None else want + back - lent
        elif byte in ENTERS:
            want = None
        if want is None:
            tally[f'{law} {kind} unchecked'] += byte in ENTERS
        else:
            tally[f'{law} {kind} {"ok" if want == total else "broken"}'] += 1
        prev, outcome = (total, member(ex, 'stateUsed')), 'revert' if byte == 0xfd else 'ok'
    return outcome, prev and prev[0], net


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
                for law in ['1d', '2d']:
                    frame(vm, by_client.setdefault(client, Counter()), law)
    for client, tally in sorted(by_client.items()):
        print(client, dict(sorted((k, v) for k, v in tally.items() if v)))


if __name__ == '__main__':
    main(sys.argv[1])

"""Tabulate the gas each client reports in the amsterdam-gas capture.

Usage: uv run python analyze.py <run dir> > tables.md
Frames: traceAddress, type, action.gas, result.gasUsed and any member beyond the Parity set.
vmTrace: every op that charges or refills state gas or enters a frame (SSTORE, CALL family,
CREATE family), with cost, ex.used and extra members, plus the root op count.
"""
import gzip
import json
import sys
from pathlib import Path

ACTION = {'callType', 'from', 'to', 'gas', 'input', 'value', 'init', 'creationMethod', 'address',
          'refundAddress', 'balance', 'author', 'rewardType'}
RESULT = {'gasUsed', 'output', 'address', 'code'}
OP = {'pc', 'op', 'cost', 'ex', 'sub', 'idx'}
EX = {'used', 'push', 'mem', 'store'}
WATCH = {'SSTORE', 'CALL', 'CALLCODE', 'DELEGATECALL', 'STATICCALL', 'CREATE', 'CREATE2'}
BYTES = {0x55: 'SSTORE', 0xf0: 'CREATE', 0xf1: 'CALL', 0xf2: 'CALLCODE', 0xf4: 'DELEGATECALL', 0xf5: 'CREATE2', 0xfa: 'STATICCALL'}


def num(value):
    if isinstance(value, str) and value.startswith(('0x', '-0x')):
        return int(value, 16)
    return value


def extras(obj, known):
    return {k: num(v) for k, v in obj.items() if k not in known}


def frames(trace):
    rows = []
    for frame in trace or []:
        action, result = frame.get('action', {}), frame.get('result')
        row = {'addr': frame.get('traceAddress'), 'type': frame.get('type'), 'gas': num(action.get('gas')),
               'gasUsed': num(result.get('gasUsed')) if result else None, 'error': frame.get('error')}
        row.update({'action.' + k: v for k, v in extras(action, ACTION).items()})
        if result:
            row.update({'result.' + k: v for k, v in extras(result, RESULT).items()})
        rows.append(row)
    return rows


def ops(vm, path=()):
    rows = []
    code = bytes.fromhex((vm or {}).get('code', '0x')[2:])
    for i, op in enumerate((vm or {}).get('ops', [])):
        ex = op.get('ex') or {}
        # Besu omits the mnemonic; name the watched opcodes from the frame's code.
        name = op.get('op') or BYTES.get(code[op['pc']] if op.get('pc', len(code)) < len(code) else None)
        if name in WATCH or extras(op, OP) or extras(ex, EX):
            row = {'path': list(path) + [i], 'op': name, 'cost': op.get('cost'), 'used': ex.get('used') if ex else None,
                   'next': num(vm['ops'][i + 1]['ex']['used']) if i + 1 < len(vm['ops']) and vm['ops'][i + 1].get('ex') else None}
            row.update({'op.' + k: v for k, v in extras(op, OP).items() if k != 'op'})
            row.update({'ex.' + k: v for k, v in extras(ex, EX).items()})
            rows.append(row)
        if op.get('sub'):
            rows += ops(op['sub'], tuple(path) + (i,))
    return rows


def calltree(frame, path=()):
    known = {'type', 'from', 'to', 'gas', 'gasUsed', 'input', 'output', 'value', 'calls', 'error', 'revertReason', 'logs'}
    row = {'path': list(path), 'type': frame.get('type'), 'gas': num(frame.get('gas')), 'gasUsed': num(frame.get('gasUsed')),
           'error': frame.get('error')}
    row.update(extras(frame, known))
    rows = [row]
    for i, child in enumerate(frame.get('calls') or []):
        rows += calltree(child, tuple(path) + (i,))
    return rows


def structlog(result):
    steps = [{'pc': s.get('pc'), 'op': s.get('op'), 'depth': s.get('depth'), 'gas': num(s.get('gas')),
              'gasCost': num(s.get('gasCost')), **extras(s, {'pc', 'op', 'depth', 'gas', 'gasCost', 'stack', 'memory', 'storage', 'refund', 'error'})}
             for s in result.get('structLogs', [])]
    keep = [s for s in steps if s['op'] in WATCH or len(s) > 5]
    top = extras(result, {'structLogs', 'returnValue'})
    return {'top': top, 'steps': keep}


def summarize(response):
    if not isinstance(response, dict):
        return {'error': 'no response'}
    if 'error' in response:
        return {'error': response['error']}
    result = response['result']
    if isinstance(result, list):  # trace_block
        return {'frames': [dict(f, tx=r.get('transactionPosition')) for r in result for f in frames([r])]}
    if 'structLogs' in result:
        return structlog(result)
    if 'trace' in result or 'vmTrace' in result:
        out = {'frames': frames(result.get('trace'))}
        if result.get('vmTrace'):
            out['ops'] = ops(result['vmTrace'])
        return out
    return {'calltree': calltree(result)}


def main(run):
    run = Path(run)
    path = run / 'observations.json'
    observations = json.loads(path.read_text()) if path.exists() else json.load(gzip.open(str(path) + '.gz'))
    out = {}
    for case, by_client in observations.items():
        if case.startswith('_'):
            continue
        out[case] = {client: summarize(json.loads(obs['raw_response']) if 'raw_response' in obs else None)
                     for client, obs in sorted(by_client.items())}
    json.dump(out, sys.stdout, indent=1)


if __name__ == '__main__':
    main(sys.argv[1])

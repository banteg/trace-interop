"""Explicit proposed assertions. These are not a client-majority oracle."""
from __future__ import annotations

import re


def evaluate(case, observation, peers):
    """Return independently scoped rule checks; absence means no automated assertion."""
    name, request = case['name'], case['request']
    method, params = request['method'], request.get('params', [])
    response = observation.get('response') or {}
    result = response.get('result')
    status = observation['status']
    checks = []

    def check(topic, ok, requirement, detail=''):
        checks.append({'topic': topic, 'status': 'matches' if ok else 'change_needed',
                       'requirement': requirement, 'detail': detail})

    if method.startswith('trace_'):
        if status == 'unsupported':
            checks.append({'topic': 'H01', 'status': 'unsupported', 'requirement': method,
                           'detail': 'Method coverage remains a profile decision.'})
            return checks
        if status in ['harness_error', 'transport_error']:
            return checks
        if method == 'trace_rawTransaction':
            check('H25', status not in ['malformed_json', 'invalid_envelope'],
                  'Return one complete JSON-RPC response, including on validation failure.')
        if status in ['malformed_json', 'invalid_envelope']:
            return checks

    def other(n):
        return peers.get(n, {}).get('response', {}).get('result')

    if method == 'trace_get' and isinstance(params[1], list) and all(isinstance(x,str) for x in params[1]):
        path = [int(x, 16) for x in params[1]]
        missing = 'missing' in name or '0xffff' in params[1]
        if missing:
            check('H06', status == 'result' and result is None, 'A missing transaction or tree path returns null.')
        else:
            # Only known-positive corpus cases imply existence.
            positive = name in ['get-root','get-transfer-root','get-zero','get-one','get-nested-positive','get-nested-parent']
            if positive:
                check('H02', isinstance(result,dict) and result.get('traceAddress') == path,
                      f'Return one object whose traceAddress equals {path}.',
                      f'Observed {result.get("traceAddress") if isinstance(result,dict) else type(result).__name__}.')
    if name in ['transaction-missing','replay-missing','get-missing-tx']:
        check('H06', status == 'result' and result is None, 'Unknown transaction returns null, not an empty collection or RPC error.')
    if method == 'trace_replayTransaction' and isinstance(result, dict):
        check('H07', result.get('transactionHash') == params[0], 'Individual replay includes its transactionHash.')
    if method in ['trace_call','trace_rawTransaction','trace_replayTransaction'] and isinstance(result,dict):
        modes = params[1]
        if isinstance(modes,list):
            if 'trace' not in modes: check('H08', result.get('trace') == [], 'Unrequested trace is an empty array.')
            for key in ['vmTrace','stateDiff']:
                if key not in modes: check('H08', key in result and result[key] is None, f'Unrequested {key} is null.')
            check('H08', isinstance(result.get('output'),str) and re.fullmatch(r'0x(?:[0-9a-f]{2})*',result['output']) is not None,
                  'Output remains a byte string under every trace selection.')
    if name in ['state-only-nonempty-output','vm-only-nonempty-output']:
        check('H08', isinstance(result,dict) and result.get('output') == '0x'+f'{42:064x}', 'The return42 contract still returns word 42.')
    if name in ['empty-types','call-empty-types','call-empty-types-priced']:
        check('H11', status == 'result' and isinstance(result,dict), 'An empty trace-type selection executes successfully.')
    if name == 'call-identity':
        frames = result.get('trace',[]) if isinstance(result,dict) else []
        check('H22', bool(frames) and frames[0].get('result',{}).get('output') == params[0].get('data', params[0].get('input','0x')),
              'The identity precompile call frame preserves its input as return bytes.')
    if name == 'call-siblings-revert-ok':
        frames = result.get('trace',[]) if isinstance(result,dict) else []
        good = next((f for f in frames if f.get('traceAddress') == [1]),None)
        check('H24', good is not None and 'error' not in good and good.get('result',{}).get('output') == '0x'+f'{42:064x}',
              'The successful second sibling retains its output and has no error.')
    if name in ['constructor','call-constructor','call-constructor-priced'] and isinstance(result,dict) and result.get('vmTrace') is not None:
        check('H19', result['vmTrace'].get('code') == params[0].get('data',params[0].get('input','0x')), 'Creation vmTrace.code is executing initcode.')
    if method == 'trace_call' and isinstance(result,dict):
        for frame in result.get('trace',[]):
            if frame.get('type') == 'create' and 'error' not in frame:
                value = frame.get('result') or {}
                check('H10', all(k in value for k in ['address','code','gasUsed']), 'Successful creation uses address, code and gasUsed.')
    if name == 'call-mcopy' and isinstance(result,dict):
        vm = result.get('vmTrace') or {}
        op = next((o for o in vm.get('ops',[]) if o.get('pc') == 11),{})
        check('H20', (op.get('ex') or {}).get('mem') == {'off':32,'data':'0x'+f'{42:064x}'}, 'MCOPY reports its same-step write of word 42 at offset 32.')
    if isinstance(result,dict) and result.get('vmTrace'):
        stack = [result['vmTrace']]
        valid = True
        while stack:
            vm = stack.pop()
            for op in vm.get('ops',[]):
                valid &= all(isinstance(v,str) and re.fullmatch(r'0x(?:0|[1-9a-f][0-9a-f]*)',v) is not None for v in (op.get('ex') or {}).get('push',[]))
                if op.get('sub'): stack.append(op['sub'])
        check('H21', valid, 'Stack words use minimal hex quantities at every depth.')
    if method == 'trace_filter' and isinstance(params[0],dict):
        filt = params[0]
        if name in ['filter-both','filter-from','filter-to','filter-empty','filter-all','filter-from-empty-to-set','filter-to-empty-from-set','filter-created-to','filter-creator-from','filter-suicide-from','filter-suicide-beneficiary']:
            tree = other('transaction-tree')
            if isinstance(tree,list) and 'mode' not in filt:
                def matches(frame):
                    action=frame['action']; kind=frame['type']
                    frm=action.get('from'); to=action.get('to')
                    if kind=='create': to=(frame.get('result') or {}).get('address')
                    if kind=='suicide': frm,to=action.get('address'),action.get('refundAddress')
                    if kind=='reward': frm,to=None,action.get('author')
                    return (not filt.get('fromAddress') or frm in filt['fromAddress']) and (not filt.get('toAddress') or to in filt['toAddress'])
                # The fixture block contains multiple transactions; use block-wide baseline when available.
                baseline = other('block-tree') or other('block-2')
                if isinstance(baseline,list):
                    expected=[f for f in baseline if matches(f)]
                    identity=lambda f:(f.get('transactionHash'),f.get('traceAddress'),f.get('type'),f.get('action'))
                    topic='H23' if any(s in name for s in ['created','creator','suicide']) else 'H04' if 'empty' in name else 'H03'
                    check(topic, isinstance(result,list) and [identity(f) for f in result] == [identity(f) for f in expected],
                          'Address matching is OR within each list, AND across lists, with action-specific endpoints.',
                          f'Expected {len(expected)} records from this client\'s block trace.')
    if name == 'filter-two-blocks':
        a,b=other('block-2'),other('block-3')
        if isinstance(a,list) and isinstance(b,list):
            check('H27', result == a+b, 'Range traces equal concatenated per-block traces in canonical order.')
    if name == 'many-storage-write-revert-read':
        check('H16', isinstance(result,list) and [r.get('output') for r in result] == ['0x'+f'{42:064x}','0x','0x'+f'{42:064x}'], 'Sequential calls retain prior writes and roll back reverted writes.')
    if name in ['get-path-wrong-type','call-wrong-type','call-unknown-mode','call-scalar-mode','raw-invalid']:
        check('H14', status == 'rpc_error' and response['error']['code'] == -32602, 'Malformed input returns invalid params (-32602).')
    if name in ['raw-nonce-high','raw-valid-current-nonce-high']:
        check('H13', status == 'rpc_error', 'A signed nonce mismatch is rejected rather than replaced.')
    return checks

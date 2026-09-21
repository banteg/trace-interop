"""Explicit proposed assertions. These are not a client-majority oracle."""
from __future__ import annotations

import re


def is_extension_request(request):
    return request['method'] == 'trace_rawTransaction' and len(request.get('params', [])) > 2


def evaluate(case, observation, peers):
    """Return independently scoped rule checks; absence means no automated assertion."""
    name, request = case['name'], case['request']
    context = case.get('context', {})
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

    if is_extension_request(request):
        if status == 'result':
            detail = 'The third-argument request returned a result; this does not prove which block state was used.'
        elif status == 'rpc_error' and response['error']['code'] == -32602:
            detail = 'The third-argument request was rejected as invalid params.'
        else:
            detail = 'The third-argument request returned an error; extension support is not established.'
        checks.append({'topic': 'H12', 'status': 'observation',
                       'requirement': 'Observe the explicit block-selector extension separately from the two-argument baseline.',
                       'detail': detail})
        return checks

    def other(n):
        return peers.get(n, {}).get('response', {}).get('result')

    if method == 'trace_get' and isinstance(params[1], list) and all(isinstance(x,str) for x in params[1]):
        path = [int(x, 16) for x in params[1]]
        missing = 'missing' in name or '0xffff' in params[1]
        if missing:
            check('H06', status == 'result' and result is None, 'A missing transaction or tree path returns null.')
        else:
            tree = other('transaction-tree')
            reference = [f for f in tree if isinstance(f,dict) and f.get('transactionHash') == params[0]] if isinstance(tree,list) else []
            if reference:
                expected = next((f for f in reference if f.get('traceAddress') == path),None)
                check('H02', status == 'result' and result == expected,
                      f'Return the transaction-tree record at {path}, or null if absent.',
                      'Compared with the same client and transaction; precompile inclusion can shift sibling indexes.')
            elif name in ['get-root','get-transfer-root','get-zero','get-one']:
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
    if context.get('_chain') == 'precompiles' and method == 'trace_call':
        frames = result.get('trace',[]) if isinstance(result,dict) else []
        root = next((f for f in frames if f.get('traceAddress') == []),None)
        if name.startswith('nested-'):
            value = int(params[0].get('value','0x0'),16)
            children = [f for f in frames if f.get('traceAddress') != []]
            expected = 1 if value else 0
            check('H29', root is not None and root.get('subtraces') == expected and len(children) == expected
                  and (not expected or children[0].get('traceAddress') == [0]),
                  'Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.')
            check('H24', root is not None and 'error' not in root,
                  'A handled precompile failure must not mark the successful parent as failed.')
        else:
            check('H29', len(frames) == 1 and root is not None, 'Retain the root precompile frame, even with zero value.')
            if name == 'root-failed':
                check('H09', root is not None and bool(root.get('error')),
                      'A failed root precompile reports its own execution error.')
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
        check('H13', status == 'rpc_error', 'Proposed admission policy: reject a signed nonce mismatch rather than replace it; client agreement is pending.')

    if method == 'trace_block' and isinstance(result,list):
        block=params[0]
        headers=context.get('headers',[])
        header=next((h for h in headers if h.get('number')==block),None)
        if header is None and context.get('_chain')=='initial':
            header={'difficulty':'0x0'}
        if header and int(header.get('difficulty','0x1'),16)==0:
            check('H05', not any(f.get('type')=='reward' for f in result), 'A PoS block has no synthetic PoW reward records.')
    frames=result.get('trace',[]) if isinstance(result,dict) else result if method in ['trace_block','trace_transaction'] and isinstance(result,list) else []
    failed=[f for f in frames if 'error' in f]
    if failed:
        check('H09', all('result' in f and ('revert' not in f['error'].lower() or isinstance(f['result'],dict) and 'output' in f['result'] and 'gasUsed' in f['result']) for f in failed), 'Failed frames have an explicit result; REVERT preserves return bytes and measured gas.')
    if name in ['call-tree-trace','call-tree-stateDiff','call-tree-vmTrace','call-constructor','call-empty-types'] and params[0].get('gasPrice')=='0x0':
        check('H15', status=='result' and isinstance(result,dict), 'Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.')
    contracts=context.get('contracts',{})
    if name=='prefunded-empty' and isinstance(result,dict):
        change=(result.get('stateDiff') or {}).get(params[0]['to'],{})
        check('H17', change.get('code')=='=' and change.get('nonce')=='=', 'An existing prefunded account does not acquire creation markers for empty code or zero nonce.')
    if name in ['auth-set','auth-replace','auth-clear','auth-set-revert'] and contracts:
        authority='undelegated' if name in ['auth-set','auth-set-revert'] else 'delegated'
        destination={'auth-set':'return42','auth-replace':'revert','auth-set-revert':'revert'}.get(name)
        before='0x'+contracts[authority]['code'];after='0xef0100'+contracts[destination]['address'][2:] if destination else '0x'
        change=(result.get('stateDiff') or {}).get(contracts[authority]['address'],{}).get('code') if isinstance(result,dict) else None
        check('H18', change=={'*':{'from':before,'to':after}}, 'EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.')
    if name in ['destroy-trace-55','destroy-trace-56']:
        change=(result.get('stateDiff') or {}).get(params[0]['to'],{}) if isinstance(result,dict) else {}
        before_cancun=name.endswith('55')
        ok=isinstance(change.get('code'),dict) and '-' in change['code'] and isinstance(change.get('nonce'),dict) and '-' in change['nonce'] if before_cancun else change.get('code')=='=' and change.get('nonce')=='='
        check('H26', ok, 'Delete code/nonce before Cancun; preserve an existing account after EIP-6780.')
    if name.startswith('filter-across-'):
        boundary=int(name.rsplit('-',1)[1]); a,b=other('block-'+str(boundary-1)),other('block-'+str(boundary))
        if isinstance(a,list) and isinstance(b,list):check('H27', result==a+b, 'A fork-crossing range equals the corresponding per-block traces.')
    if name.startswith('filter-') and name.removeprefix('filter-').isdigit():
        block=other('block-'+name.removeprefix('filter-'))
        if isinstance(block,list):check('H27', result==block, 'A single-block filter agrees with trace_block at the same fork.')
    if name.startswith('system-beacon-'):
        _,_,block,slot=name.split('-'); headers=context.get('headers',[])
        h=next((h for h in headers if h.get('number')=='0x38'),None)
        if h:
            expected='0x'+('0'*64 if int(block)<56 else f'{560:064x}' if slot=='560' else h['parentBeaconBlockRoot'][2:])
            check('H28', status=='result' and result==expected, 'Historical beacon-root storage excludes the following block system update.')
    if name in ['beacon-call-55','beacon-call-56']:
        h=next((h for h in context.get('headers',[]) if h.get('number')=='0x38'),None)
        if h:check('H28', isinstance(result,dict) and result.get('output')==('0x' if name.endswith('55') else h['parentBeaconBlockRoot']), 'Historical trace_call uses only system changes through the selected block.')
    if context.get('_chain')=='pruned' and method.startswith('trace_') and name.startswith('old-'):
        check('H06', status=='rpc_error' and response['error']['code']==4444, 'Unavailable historical state uses the proposed pruned-history error (4444).')
    return checks

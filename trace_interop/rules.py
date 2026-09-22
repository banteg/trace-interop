"""Explicit proposed assertions. These are not a client-majority oracle."""
from __future__ import annotations

import re


def is_extension_request(request):
    return request['method'] == 'trace_rawTransaction' and len(request.get('params', [])) > 2


def mapping(value):
    return value if isinstance(value, dict) else {}


def sequence(value):
    return value if isinstance(value, list) else []


def embedded_error(response):
    value = mapping(response).get('result')
    return isinstance(value, dict) and value.get('jsonrpc') == '2.0' and 'error' in value


def evaluate(case, observation, peers, invalid_params=None):
    """Return independently scoped rule checks; absence means no automated assertion."""
    name, request = case['name'], case['request']
    context = case.get('context', {})
    method, params = request['method'], request.get('params', [])
    response = mapping(observation.get('response'))
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
        if method == 'trace_rawTransaction' or embedded_error(response):
            check('H25', status not in ['malformed_json', 'invalid_envelope'] and not embedded_error(response),
                  'Return one complete JSON-RPC response; never wrap an error envelope as a successful result.')
        if status in ['malformed_json', 'invalid_envelope']:
            return checks

    if is_extension_request(request):
        if status == 'result':
            detail = 'The third-argument request returned a result; this does not prove which block state was used.'
        elif status == 'rpc_error' and mapping(response.get('error')).get('code') == -32602:
            detail = 'The third-argument request was rejected as invalid params.'
        else:
            detail = 'The third-argument request returned an error; extension support is not established.'
        checks.append({'topic': 'H12', 'status': 'observation',
                       'requirement': 'Observe the explicit block-selector extension separately from the two-argument baseline.',
                       'detail': detail})
        return checks

    def other(n):
        return mapping(mapping(peers.get(n)).get('response')).get('result')

    if invalid_params:
        check('H14', status == 'rpc_error' and mapping(response.get('error')).get('code') == -32602,
              'Malformed input returns invalid params (-32602).', '; '.join(invalid_params))
        if method == 'trace_filter' and params and isinstance(params[0],dict) and 'mode' in params[0]:
            check('H03', status == 'rpc_error' and mapping(response.get('error')).get('code') == -32602,
                  'The portable filter profile rejects the mode extension as invalid params.')
        return checks

    if method == 'trace_get' and len(params) > 1 and isinstance(params[1], list) and all(isinstance(x,str) and re.fullmatch(r'0x(?:0|[1-9a-f][0-9a-f]*)', x) for x in params[1]):
        path = [int(x, 16) for x in params[1]]
        missing = 'missing' in name or '0xffff' in params[1]
        if missing and name != 'get-missing-tx':
            check('H06', status == 'result' and result is None, 'A missing transaction or tree path returns null.')
        elif not missing:
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
            else:
                checks.append({'topic': 'H02', 'status': 'unassessed',
                               'requirement': 'Compare the requested path with the transaction tree.',
                               'detail': 'The reference transaction tree was unavailable; path selection was not assessed.'})
    if name in ['transaction-missing','replay-missing','get-missing-tx']:
        check('H06', status == 'result' and result is None, 'Unknown transaction returns null, not an empty collection or RPC error.')
    if method == 'trace_replayTransaction' and isinstance(result, dict):
        check('H07', result.get('transactionHash') == params[0], 'Individual replay includes its transactionHash.')
    if method in ['trace_call','trace_rawTransaction','trace_replayTransaction'] and isinstance(result,dict):
        modes = params[1] if len(params) > 1 else None
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
    if context.get('_chain') in ['precompiles','precompile-values'] and method in ['trace_call','trace_callMany']:
        execution = result
        if 'execution_index' in case:
            index=case['execution_index']
            execution=result[index] if isinstance(result,list) and len(result)>index else None
        frames = [f for f in sequence(mapping(execution).get('trace')) if isinstance(f, dict)]
        root = next((f for f in frames if f.get('traceAddress') == []),None)
        if name.startswith('nested-'):
            value = case['precompile_value'] if 'precompile_value' in case else int(params[0].get('value','0x0'),16)
            children = [f for f in frames if f.get('traceAddress') != []]
            expected = 1 if value else 0
            check('H29', root is not None and root.get('subtraces') == expected and len(children) == expected
                  and (not expected or children[0].get('traceAddress') == [0]),
                  'Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.')
            check('H24', root is not None and 'error' not in root,
                  'A handled precompile failure must not mark the successful parent as failed.')
            if 'expected_call_success' in case:
                check('H29', mapping(execution).get('output') == '0x'+f'{int(case["expected_call_success"]):064x}',
                      'The constructor returns the precompile call success bit; a funded successful call must return one.')
                if 'funded_creation_address' in case:
                    funding=mapping(result[0]) if isinstance(result,list) and result else {}
                    funding_frames=sequence(funding.get('trace'))
                    funding_root=next((f for f in funding_frames if isinstance(f,dict) and f.get('traceAddress')==[]),{})
                    check('H29', mapping(mapping(root).get('result')).get('address') == case['funded_creation_address']
                          and 'error' not in funding_root and mapping(funding_root.get('action')).get('to') == case['funded_creation_address']
                          and mapping(funding_root.get('action')).get('value') == '0x1',
                          'The preceding simulated transfer funds the actual zero-value creation address with one wei.')
        else:
            check('H29', len(frames) == 1 and root is not None, 'Retain the root precompile frame, even with zero value.')
            if name == 'root-failed':
                check('H09', root is not None and bool(root.get('error')),
                      'A failed root precompile reports its own execution error.')
    if name == 'call-identity':
        frames = [f for f in sequence(mapping(result).get('trace')) if isinstance(f, dict)]
        check('H22', bool(frames) and mapping(frames[0].get('result')).get('output') == params[0].get('data', params[0].get('input','0x')),
              'The identity precompile call frame preserves its input as return bytes.')
    if name == 'call-siblings-revert-ok':
        frames = [f for f in sequence(mapping(result).get('trace')) if isinstance(f, dict)]
        good = next((f for f in frames if f.get('traceAddress') == [1]),None)
        check('H24', good is not None and 'error' not in good and mapping(good.get('result')).get('output') == '0x'+f'{42:064x}',
              'The successful second sibling retains its output and has no error.')
    if name in ['constructor','call-constructor','call-constructor-priced'] and isinstance(result,dict) and result.get('vmTrace') is not None:
        check('H19', mapping(result['vmTrace']).get('code') == params[0].get('data',params[0].get('input','0x')), 'Creation vmTrace.code is executing initcode.')
    if method == 'trace_call' and isinstance(result,dict):
        raw_frames = result.get('trace', [])
        if not isinstance(raw_frames, list) or any(not isinstance(f, dict) for f in raw_frames):
            check('H08', False, 'The execution trace is an array of frame objects.')
        for frame in (f for f in sequence(raw_frames) if isinstance(f, dict)):
            if frame.get('type') == 'create' and 'error' not in frame:
                value = mapping(frame.get('result'))
                check('H10', all(k in value for k in ['address','code','gasUsed']), 'Successful creation uses address, code and gasUsed.')
    if name == 'call-mcopy' and isinstance(result,dict):
        vm = mapping(result.get('vmTrace'))
        op = next((o for o in sequence(vm.get('ops')) if isinstance(o, dict) and o.get('pc') == 11),{})
        check('H20', mapping(op.get('ex')).get('mem') == {'off':32,'data':'0x'+f'{42:064x}'}, 'MCOPY reports its same-step write of word 42 at offset 32.')
    if isinstance(result,dict) and result.get('vmTrace'):
        stack = [result['vmTrace']]
        valid = True
        while stack:
            vm = stack.pop()
            if not isinstance(vm, dict) or not isinstance(vm.get('ops'), list):
                valid = False
                continue
            for op in vm['ops']:
                if not isinstance(op, dict):
                    valid = False
                    continue
                ex = op.get('ex')
                if ex is not None:
                    push = mapping(ex).get('push')
                    valid &= isinstance(push, list) and all(isinstance(v,str) and re.fullmatch(r'0x(?:0|[1-9a-f][0-9a-f]*)',v) is not None for v in sequence(push))
                if op.get('sub') is not None: stack.append(op['sub'])
        check('H21', valid, 'Stack words use minimal hex quantities at every depth.')
    if method == 'trace_filter' and params and isinstance(params[0],dict):
        filt = params[0]
        filter_cases = ['filter-both','filter-from','filter-to','filter-empty','filter-all',
                        'filter-from-null','filter-to-null','filter-both-null',
                        'filter-from-empty-to-set','filter-to-empty-from-set','filter-created-to',
                        'filter-creator-from','filter-suicide-from','filter-suicide-beneficiary',
                        'filter-from-only-intersection','filter-to-only-intersection']
        if name in filter_cases and 'mode' not in filt:
            def address(value):
                return value.lower() if isinstance(value, str) else None
            def matches(frame):
                action=mapping(mapping(frame).get('action')); kind=mapping(frame).get('type')
                frm=action.get('from'); to=action.get('to')
                if kind=='create': to=mapping(frame.get('result')).get('address')
                if kind=='suicide': frm,to=action.get('address'),action.get('refundAddress')
                if kind=='reward': frm,to=None,action.get('author')
                return (not filt.get('fromAddress') or address(frm) in [address(v) for v in sequence(filt['fromAddress'])]) and (not filt.get('toAddress') or address(to) in [address(v) for v in sequence(filt['toAddress'])])
            baseline = other('block-tree')
            if not isinstance(baseline, list): baseline = other('block-2')
            topic='H23' if any(t in name for t in ['created','creator','suicide']) else 'H04' if any(t in name for t in ['empty','null']) else 'H03'
            if isinstance(baseline,list) and all(isinstance(f,dict) for f in baseline):
                expected=[f for f in baseline if matches(f)]
                identity=lambda f:(mapping(f).get('transactionHash'),mapping(f).get('traceAddress'),mapping(f).get('type'),mapping(f).get('action'))
                check(topic, isinstance(result,list) and all(isinstance(f,dict) for f in result) and [identity(f) for f in result] == [identity(f) for f in expected],
                      'Compare address bytes: OR within each list, AND across lists; missing/null/empty lists are unrestricted.',
                      f'Expected {len(expected)} records from this client\'s block trace.')
            else:
                checks.append({'topic': topic, 'status': 'unassessed', 'requirement': 'Compare filtering with the block trace.',
                               'detail': 'The reference block trace was unavailable.'})
    if name == 'filter-two-blocks':
        a,b=other('block-2'),other('block-3')
        if isinstance(a,list) and isinstance(b,list):
            check('H27', result == a+b, 'Range traces equal concatenated per-block traces in canonical order.')
    if method == 'trace_callMany' and params and isinstance(params[0], list):
        check('H16', status == 'result' and isinstance(result,list) and len(result) == len(params[0])
              and all(isinstance(r,dict) and isinstance(r.get('output'),str) and isinstance(r.get('trace'),list) for r in sequence(result)),
              'Return one execution envelope per input call, in order.')
    if name == 'many-storage-write-read':
        check('H16', isinstance(result,list) and [mapping(r).get('output') for r in result] == ['0x'+f'{42:064x}']*2,
              'The second call reads the first call’s simulated write.')
    if name == 'many-storage-write-revert-read':
        check('H16', isinstance(result,list) and [mapping(r).get('output') for r in result] == ['0x'+f'{42:064x}','0x','0x'+f'{42:064x}'], 'Sequential calls retain prior writes and roll back reverted writes.')
    if name in ['get-path-wrong-type','call-wrong-type','call-unknown-mode','call-scalar-mode','raw-invalid']:
        check('H14', status == 'rpc_error' and mapping(response.get('error')).get('code') == -32602, 'Malformed input returns invalid params (-32602).')
    if name == 'raw-nonce-high' or name.startswith('raw-nonce-high-'):
        check('H13', status == 'rpc_error', 'Proposed admission policy: reject a signed nonce mismatch rather than replace it; client agreement is pending.')

    if name.startswith('missing-block-'):
        check('H06', status == 'rpc_error' and mapping(response.get('error')).get('code') == -32001,
              'An unknown selected block or range endpoint returns Resource not found (-32001).')
    if name == 'call-unknown-field':
        check('H14', status == 'result' and mapping(result).get('output') == '0x'+f'{42:064x}',
              'Unknown call-object fields are ignored without changing execution output.')

    if method == 'trace_block' and isinstance(result,list):
        block=params[0]
        headers=context.get('headers',[])
        header=next((h for h in headers if h.get('number')==block),None)
        if header is None and context.get('_chain')=='initial':
            header={'difficulty':'0x0'}
        if header and int(header.get('difficulty','0x1'),16)==0:
            check('H05', not any(mapping(f).get('type')=='reward' for f in result), 'A PoS block has no synthetic PoW reward records.')
    envelopes = [result] if isinstance(result, dict) else sequence(result) if method in ['trace_callMany', 'trace_replayBlockTransactions'] else []
    frame_values = [mapping(e).get('trace', []) for e in envelopes]
    if method in ['trace_block', 'trace_transaction', 'trace_filter']:
        frame_values = [result] if isinstance(result, list) else []
    elif method == 'trace_get' and isinstance(result, dict):
        frame_values = [[result]]
    frames = [f for values in frame_values for f in sequence(values) if isinstance(f, dict)]
    failed = [f for f in frames if 'error' in f]
    if failed:
        check('H09', all(isinstance(f['error'], str) and bool(f['error']) and 'result' in f
              and (f['result'] is None or isinstance(f['result'], dict)) for f in failed),
              'Failed frames have an error string and an explicit object or null result.')
    # Identify known REVERT paths from the fixture, never from implementation-specific error text.
    revert_path = [] if name == 'transaction-revert' or name.startswith('replay-revert-') else [0] if name == 'call-siblings-revert-ok' else [1] if name == 'call-siblings-ok-revert' else None
    if revert_path is not None and frames:
        reverted = next((f for f in frames if f.get('traceAddress') == revert_path), None)
        value = mapping(mapping(reverted).get('result'))
        check('H09', reverted is not None and isinstance(reverted.get('error'), str)
              and isinstance(value.get('output'), str) and isinstance(value.get('gasUsed'), str),
              'The fixture REVERT frame preserves return bytes and measured gas regardless of its error wording.')
    calls = params[:1] if method == 'trace_call' else [p[0] for p in params[0] if isinstance(p,list) and p] if method == 'trace_callMany' and params and isinstance(params[0],list) else []
    if any(mapping(call).get('gasPrice') == '0x0' for call in calls):
        ok = status == 'result' and not embedded_error(response) and (isinstance(result,dict) if method == 'trace_call' else isinstance(result,list) and len(result) == len(calls))
        check('H15', ok, 'Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.')
    contracts=context.get('contracts',{})
    if name=='prefunded-empty' and isinstance(result,dict):
        change=mapping(result.get('stateDiff')).get(params[0]['to'],{})
        check('H17', mapping(change).get('code')=='=' and mapping(change).get('nonce')=='=', 'An existing prefunded account does not acquire creation markers for empty code or zero nonce.')
    if name in ['auth-set','auth-replace','auth-clear','auth-set-revert'] and contracts:
        authority='undelegated' if name in ['auth-set','auth-set-revert'] else 'delegated'
        destination={'auth-set':'return42','auth-replace':'revert','auth-set-revert':'revert'}.get(name)
        before='0x'+contracts[authority]['code'];after='0xef0100'+contracts[destination]['address'][2:] if destination else '0x'
        change=mapping(result.get('stateDiff')).get(contracts[authority]['address'],{}) if isinstance(result,dict) else {}
        change = mapping(change).get('code') if isinstance(result,dict) else None
        check('H18', change=={'*':{'from':before,'to':after}}, 'EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.')
    if name in ['destroy-trace-55','destroy-trace-56']:
        change=mapping(result.get('stateDiff')).get(params[0]['to'],{}) if isinstance(result,dict) else {}
        before_cancun=name.endswith('55')
        ok=isinstance(mapping(change).get('code'),dict) and '-' in change['code'] and isinstance(mapping(change).get('nonce'),dict) and '-' in change['nonce'] if before_cancun else mapping(change).get('code')=='=' and mapping(change).get('nonce')=='='
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
        check('H06', status=='rpc_error' and mapping(response.get('error')).get('code')==4444, 'Unavailable historical state uses the proposed pruned-history error (4444).')
    return checks

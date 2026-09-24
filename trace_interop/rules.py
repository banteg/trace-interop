"""Explicit proposed assertions. These are not a client-majority oracle."""
from __future__ import annotations

import re

from .oracles import anchored_reference, REVERT_OUTPUT, REVERT_GAS
from .vm_model import encoding_valid


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
        if method == 'trace_rawTransaction' or embedded_error(response) or status in ['malformed_json','invalid_envelope']:
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
        obs = mapping(peers.get(n))
        return mapping(obs.get('response')).get('result') if obs.get('status') == 'result' else None

    def reference(n):
        return anchored_reference(context, peers, n)

    if invalid_params:
        check('H14', status == 'rpc_error' and mapping(response.get('error')).get('code') == -32602,
              'Malformed input returns invalid params (-32602).', '; '.join(invalid_params))
        if method == 'trace_filter' and params and isinstance(params[0],dict) and 'mode' in params[0]:
            check('H03', status == 'rpc_error' and mapping(response.get('error')).get('code') == -32602,
                  'Unknown mode values return invalid params (-32602).')
        return checks

    if context.get('_chain') == 'h30':
        number_48 = '0x' + f'{48:064x}'
        if name == 'filter-no-bounds':
            head = other('filter-head-only')
            check('H30', status == 'result' and isinstance(result, list) and len(result) == 3
                  and all(isinstance(frame, dict) and frame.get('blockNumber') == 48 for frame in result)
                  and result == head,
                  'Omitting both range bounds selects latest only, as an explicit head-only query does.')
        if name == 'filter-to-2-implicit-from':
            check('H30', status == 'rpc_error' and isinstance(response.get('error'), dict),
                  'An omitted fromBlock resolves to latest; an earlier explicit toBlock gives a range error, not a historical search.')
        if name in ['call-number-default', 'call-number-latest']:
            check('H31', status == 'result' and mapping(result).get('output') == number_48,
                  'An omitted or explicit latest trace_call block uses the frozen head (NUMBER 48).')
        if name in ['many-number-default', 'many-number-latest']:
            check('H31', status == 'result' and isinstance(result, list) and len(result) == 1
                  and mapping(result[0]).get('output') == number_48,
                  'trace_callMany accepts an omitted block and uses latest (NUMBER 48).')
        if name == 'filter-earliest':
            explicit = other('filter-0-to-2')
            check('H32', status == 'result' and isinstance(result, list) and isinstance(explicit, list)
                  and result == explicit,
                  'The earliest tag resolves like explicit block 0 on this fixture.')
        if name == 'filter-safe':
            check('H32', status == 'result' and isinstance(result, list) and len(result) == 3
                  and all(isinstance(frame, dict) and frame.get('blockNumber') == 48 for frame in result),
                  'The safe tag resolves to the fixture safe head, block 48.')
        if name in ['filter-pending', 'call-number-pending', 'many-number-pending']:
            if status == 'rpc_error':
                code = mapping(response.get('error')).get('code')
                detail = f'{name}: RPC error {code}.'
            elif name == 'filter-pending' and isinstance(result, list):
                blocks = sorted({frame.get('blockNumber') for frame in result if isinstance(frame, dict)})
                detail = f'{name}: {len(result)} records from blocks {blocks}.'
            else:
                execution = result[0] if isinstance(result, list) and result else result
                output = mapping(execution).get('output')
                detail = f'{name}: NUMBER {int(output, 16)}.' if isinstance(output, str) and output.startswith('0x') else f'{name}: {status}.'
            checks.append({'topic': 'H32', 'status': 'observation',
                           'requirement': 'Record pending behavior without assuming a settled state or localization policy.',
                           'detail': detail})
            if name == 'filter-pending':
                check('H32', status != 'rpc_error' or mapping(response.get('error')).get('code') != -32603,
                      'A valid pending tag must not trigger an internal error; support remains a policy choice.')

    if method == 'trace_get' and len(params) > 1 and isinstance(params[1], list) and all(isinstance(x,str) and re.fullmatch(r'0x(?:0|[1-9a-f][0-9a-f]*)', x) for x in params[1]):
        path = [int(x, 16) for x in params[1]]
        missing = 'missing' in name or '0xffff' in params[1]
        if missing and name != 'get-missing-tx':
            check('H06', status == 'result' and result is None, 'A missing transaction or tree path returns null.')
        elif not missing:
            tree_name = next((c['name'] for c in context.get('cases', [])
                              if c['request']['method'] == 'trace_transaction' and c['request']['params'] == params[:1]), 'transaction-tree')
            tree = reference(tree_name)
            tx_frames = [f for f in tree if isinstance(f,dict) and f.get('transactionHash') == params[0]] if isinstance(tree,list) else []
            if tx_frames:
                expected = next((f for f in tx_frames if f.get('traceAddress') == path),None)
                check('H02', status == 'result' and result == expected,
                      f'Return the transaction-tree record at {path}, or null if absent.',
                      'Compared with the same client and transaction; precompile inclusion can shift sibling indexes.')
            else:
                checks.append({'topic': 'H02', 'status': 'unassessed',
                               'requirement': 'Compare the requested path with the transaction tree.',
                               'detail': 'The reference tree did not establish the independent fixture inventory; path selection was not assessed.'})
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
        expected = '0x'+f'{42:064x}' if name == 'empty-types' else '0xffee'
        check('H11', status == 'result' and mapping(result).get('output') == expected,
              'An empty trace-type selection executes and preserves the fixture return bytes.',
              'Expected '+expected)
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
            if expected:
                child = children[0] if len(children) == 1 else {}
                action = mapping(child.get('action'))
                call_type = name.split('-')[1]
                caller = case.get('funded_creation_address', '0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41')
                success = case.get('expected_call_success', name.endswith('-success'))
                input_bytes = '0x'+f'{0 if success else 42:064x}'+'0'*192
                check('H29', child.get('type') == 'call' and all(action.get(k) == v for k,v in
                      [('from',caller), ('to','0x'+'0'*39+'6'), ('callType',call_type), ('value',hex(value)), ('input',input_bytes)])
                      and (not child.get('error') and mapping(child.get('result')).get('output') == '0x'+'0'*128 if success
                           else isinstance(child.get('error'), str) and bool(child['error'])),
                      'The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.')
            check('H24', root is not None and 'error' not in root,
                  'A handled precompile failure must not mark the successful parent as failed.')
            if 'expected_call_success' in case:
                check('H29', mapping(execution).get('output') == '0x'+f'{int(case["expected_call_success"]):064x}',
                      'The constructor returns the precompile call success bit; a funded successful call must return one.')
                if 'funded_creation_address' in case:
                    funding=mapping(result[0]) if isinstance(result,list) and result else {}
                    funding_frames=sequence(funding.get('trace'))
                    funding_root=next((f for f in funding_frames if isinstance(f,dict) and f.get('traceAddress')==[]),{})
                    target=case['funded_creation_address']
                    created=mapping(mapping(root).get('result')).get('address')
                    code_change=mapping(mapping(mapping(execution).get('stateDiff')).get(target)).get('code')
                    installed=mapping(mapping(code_change).get('*')).get('to', mapping(code_change).get('+'))
                    creation_verified=created == target if created is not None else installed == mapping(execution).get('output') and isinstance(installed,str)
                    check('H29', creation_verified and 'error' not in funding_root and mapping(funding_root.get('action')).get('to') == case['funded_creation_address']
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
                valid &= encoding_valid(op.get('ex'))
                if op.get('sub') is not None: stack.append(op['sub'])
        check('H21', valid, 'Stack words and storage operands use minimal hex quantities at every depth.')
    if method == 'trace_filter' and params and isinstance(params[0],dict):
        filt = params[0]
        filter_cases = ['filter-both','filter-from','filter-to','filter-empty','filter-all',
                        'filter-from-null','filter-to-null','filter-both-null',
                        'filter-from-empty-to-set','filter-to-empty-from-set','filter-created-to',
                        'filter-creator-from','filter-suicide-from','filter-suicide-beneficiary',
                        'filter-from-only-intersection','filter-to-only-intersection',
                        'filter-from-only-union','filter-to-only-union',
                        'filter-intersection','filter-union']
        if name in filter_cases:
            def address(value):
                return value.lower() if isinstance(value, str) else None
            def matches(frame):
                action=mapping(mapping(frame).get('action')); kind=mapping(frame).get('type')
                frm=action.get('from'); to=action.get('to')
                # A failed CREATE has no recipient, even if a client reports its would-be address.
                if kind=='create': to=None if 'error' in frame else mapping(frame.get('result')).get('address')
                if kind=='suicide': frm,to=action.get('address'),action.get('refundAddress')
                if kind=='reward': frm,to=None,action.get('author')
                senders=[address(v) for v in sequence(filt.get('fromAddress'))]
                recipients=[address(v) for v in sequence(filt.get('toAddress'))]
                sides=[s for s,values in [(address(frm) in senders, senders), (address(to) in recipients, recipients)] if values]
                return any(sides) if filt.get('mode') == 'union' and sides else all(sides)
            baseline = reference('block-tree')
            if not isinstance(baseline, list): baseline = reference('block-2')
            topic='H23' if any(t in name for t in ['created','creator','suicide']) else 'H04' if any(t in name for t in ['empty','null']) else 'H03'
            if isinstance(baseline,list) and all(isinstance(f,dict) for f in baseline):
                expected=[f for f in baseline if matches(f)]
                identity=lambda f:(mapping(f).get('transactionHash'),mapping(f).get('traceAddress'),mapping(f).get('type'),mapping(f).get('action'))
                check(topic, isinstance(result,list) and all(isinstance(f,dict) for f in result) and [identity(f) for f in result] == [identity(f) for f in expected],
                      'Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted.',
                      f'Expected {len(expected)} records from this client\'s block trace.')
            else:
                checks.append({'topic': topic, 'status': 'unassessed', 'requirement': 'Compare filtering with the block trace.',
                               'detail': 'The reference block trace did not establish the independent fixture inventory.'})
    if name == 'filter-two-blocks':
        a,b=reference('block-2'),reference('block-3')
        if isinstance(a,list) and isinstance(b,list):
            check('H27', result == a+b, 'Range traces equal concatenated per-block traces in canonical order.')
    if name == 'filter-two-blocks' and not any(c['topic']=='H27' for c in checks):
        checks.append({'topic':'H27','status':'unassessed','requirement':'Compare anchored per-block traces.', 'detail':'Independent reference inventory unavailable.'})
    # H15 deliberately submits invalid and unresolved-default requests. An RPC
    # rejection there must not become a spurious sequential-envelope failure.
    if (method == 'trace_callMany' and context.get('_chain') != 'h30' and params and isinstance(params[0], list)
            and (not case.get('fee_policy') or status == 'result')):
        check('H16', status == 'result' and isinstance(result,list) and len(result) == len(params[0])
              and all(isinstance(r,dict) and isinstance(r.get('output'),str) and isinstance(r.get('trace'),list) for r in sequence(result)),
              'Return one execution envelope per input call, in order.')
    probe = name.rsplit('/',1)[-1]
    if probe == 'many-storage-write-read':
        check('H16', isinstance(result,list) and [mapping(r).get('output') for r in result] == ['0x'+f'{42:064x}']*2,
              'The second call reads the first call’s simulated write.')
    if probe == 'many-storage-write-revert-read':
        check('H16', isinstance(result,list) and [mapping(r).get('output') for r in result] == ['0x'+f'{42:064x}','0x','0x'+f'{42:064x}'], 'Sequential calls retain prior writes and roll back reverted writes.')
    if probe in ['many-storage-write-read','many-storage-write-revert-read']:
        # Both storage probes use nonce 133 at the frozen chain-a head. No gas
        # accounting policy is inferred: only nonce progression and storage are checked.
        sender, target = params[0][0][0]['from'], params[0][0][0]['to']
        slot, value = '0x'+'00'*32, '0x'+f'{42:064x}'
        diffs = [mapping(r).get('stateDiff') for r in sequence(result)]
        valid = len(diffs) == len(params[0]) and all(isinstance(d,dict) for d in diffs)
        nonce = context.get('nonce')
        check('H16', valid and isinstance(nonce,int) and all(
            mapping(mapping(d).get(sender)).get('nonce') == {'*':{'from':hex(nonce+i),'to':hex(nonce+i+1)}}
            for i,d in enumerate(diffs)), 'Each call reports its own sender nonce transition, including a reverted call.')
        storage = [mapping(mapping(d).get(target)).get('storage',{}) for d in diffs]
        # The target account exists at both endpoints, so its slots change with '*'
        # even from zero, as in Parity and every native client; slots never use '='.
        first = storage[0] if storage else None
        check('H16', valid and first == {slot:{'*':{'from':slot,'to':value}}}
              and all(s == {} for s in storage[1:]),
              'Only the first call writes slot zero; reverted writes and later reads add no storage transition.')
    if context.get('_chain') == 'callmany-isolation' and case.get('isolation_after'):
        before, simulation = case['isolation_before'], case['isolation_after']
        phases = context.get('_scenario_phases')
        ordered = phases == context.get('scenario_phases') and isinstance(phases,list)
        phases_needed = [n.split('/')[0] for n in [before,simulation,name]]
        ordered = ordered and all(p in phases for p in phases_needed)
        ordered = ordered and phases.index(phases_needed[0]) < phases.index(phases_needed[1]) < phases.index(phases_needed[2])
        word42 = '0x'+f'{42:064x}'
        executions = other(simulation)
        ran = isinstance(executions,list) and len(executions) == (3 if 'revert' in simulation else 2)
        # The write must actually have executed; an unsupported/error response
        # followed by an unchanged slot cannot establish simulation isolation.
        ran = ran and all(isinstance(r,dict) for r in executions) and executions[0].get('output') == word42 and executions[-1].get('output') == word42
        if ordered and other(before) == '0x'+'00'*32 and ran:
            check('H16', status == 'result' and result == '0x'+'00'*32,
                  'Canonical storage remains unchanged after the ordered multi-call simulation.')
        else:
            checks.append({'topic':'H16','status':'unassessed',
                           'requirement':'Check canonical storage after the ordered simulation.',
                           'detail':'Ordered capture, initial zero slot or successful simulated write/read not established.'})
    if name in ['get-path-wrong-type','call-wrong-type','call-unknown-mode','call-scalar-mode','raw-invalid']:
        check('H14', status == 'rpc_error' and mapping(response.get('error')).get('code') == -32602, 'Malformed input returns invalid params (-32602).')
    invalid_raw = ['raw-nonce-high', 'raw-wrong-chain', 'raw-insufficient-funds', 'raw-low-gas', 'raw-below-basefee']
    reject_raw = (any(name == n or name.startswith(n+'-') for n in invalid_raw)
                  or name == 'raw-valid-default-block' or case.get('validation') == 'reject')
    if method == 'trace_rawTransaction' and reject_raw:
        check('H13', status == 'rpc_error',
              'Reject a signed transaction that fails execution validity at the selected state before EVM execution.',
              case.get('reason', 'Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.'))
        if status == 'rpc_error':
            check('H13', mapping(response.get('error')).get('code') == -32003,
                  'Proposed transaction-validation error code: -32003 (Transaction rejected).',
                  'Error-code alignment is separate from whether validation occurred; current clients also use -32000.')
    if method == 'trace_rawTransaction' and case.get('validation') == 'execute':
        check('H13', status == 'result' and mapping(result).get('output') == case['expected_output'] and not embedded_error(response),
              'The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection.')
        modes = params[1] if isinstance(params[1], list) else []
        if 'stateDiff' in modes:
            diff = mapping(result).get('stateDiff')
            check('H13', isinstance(diff, dict) and bool(diff), 'Requested stateDiff records the signed execution state changes.')
            if case.get('expected_execution_error'):
                marker = mapping(diff).get(case['marker'].lower())
                check('H13', marker is None or isinstance(marker, dict) and marker.get('storage', {}) == {},
                      'The first-opcode out-of-gas control cannot commit a marker storage write.')
            else:
                if 'signed_create_address' in case:
                    account = mapping(mapping(diff).get(case['signed_create_address'].lower()))
                    code = mapping(account.get('code'))
                    ok = code.get('+', mapping(code.get('*')).get('to')) == case['expected_output']
                    requirement = 'Creation stateDiff installs the constructor ADDRESS bytes at the signed creation address.'
                else:
                    slot = mapping(mapping(mapping(diff).get(case['marker'].lower())).get('storage')).get('0x'+'0'*64)
                    ok = mapping(slot).get('*') == {'from':'0x'+'0'*64, 'to':'0x'+f'{42:064x}'} or mapping(slot).get('+') == '0x'+f'{42:064x}'
                    requirement = 'Marker stateDiff records slot zero changing from zero to word 42.'
                check('H13', ok, requirement)
        if 'vmTrace' in modes:
            vm = mapping(mapping(result).get('vmTrace'))
            code = '0x3060005260206000f3' if 'signed_create_address' in case else '0x602a600055602a60005260206000f3'
            expected_pcs = [0] if case.get('expected_execution_error') else [0,1,3,4,6,8] if 'signed_create_address' in case else [0,2,4,5,7,9,10,12,14]
            ops = sequence(vm.get('ops'))
            check('H13', vm.get('code') == code and [mapping(op).get('pc') for op in ops] == expected_pcs,
                  'Requested vmTrace contains the executing fixture bytecode and its opcode sequence.')
        if isinstance(params[1], list) and 'trace' in params[1]:
            trace = sequence(mapping(result).get('trace'))
            root = next((f for f in trace if isinstance(f, dict) and f.get('traceAddress') == []), {})
            root_ok = bool(root) and 'error' not in root and isinstance(root.get('result'), dict)
            if case.get('expected_execution_error'):
                root_ok = bool(root) and isinstance(root.get('error'), str) and bool(root['error'])
            check('H13', root_ok, 'The valid signed control reports its expected execution success or halt in a root frame.')
            if 'signed_create_address' in case:
                check('H13', str(mapping(root.get('result')).get('address', '')).lower() == case['signed_create_address'].lower(),
                      'Valid creation uses the address derived from the matching signed and state nonce.')

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
    trace_selected = method in ['trace_transaction','trace_block','trace_filter','trace_get'] or (len(params)>1 and isinstance(params[1],list) and 'trace' in params[1])
    if revert_path is not None and trace_selected and status == 'result':
        reverted = next((f for f in frames if f.get('traceAddress') == revert_path), None)
        value = mapping(mapping(reverted).get('result'))
        expected_output, expected_gas = ('0x', '0x6') if name.startswith('call-siblings-') else (REVERT_OUTPUT, REVERT_GAS)
        check('H09', reverted is not None and isinstance(reverted.get('error'), str)
              and bool(reverted['error']) and value.get('output') == expected_output and value.get('gasUsed') == expected_gas,
              'The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording.',
              f'Expected output {expected_output}, gasUsed {expected_gas}; derived from frozen bytecode.')
    calls = params[:1] if method == 'trace_call' else [p[0] for p in params[0] if isinstance(p,list) and p] if method == 'trace_callMany' and params and isinstance(params[0],list) else []
    if not case.get('fee_policy') and any(mapping(call).get('gasPrice') == '0x0' for call in calls):
        ok = status == 'result' and not embedded_error(response) and (isinstance(result,dict) if method == 'trace_call' else isinstance(result,list) and len(result) == len(calls))
        check('H15', ok, 'Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.')
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
        # This fixture account has genesis code 0x611008ff, nonce zero and no storage;
        # it is untouched by the mined fixture transactions.
        ok=(mapping(change).get('code') == {'-':'0x611008ff'}
            and mapping(change).get('nonce') == {'-':'0x0'}
            and mapping(change).get('storage') == {}) if before_cancun else mapping(change).get('code')=='=' and mapping(change).get('nonce')=='='
        check('H26', ok, 'Report the exact deleted code, nonce and empty storage before Cancun; preserve an existing account after EIP-6780.')
    if name.startswith('filter-across-'):
        boundary=int(name.rsplit('-',1)[1]); a,b=reference('block-'+str(boundary-1)),reference('block-'+str(boundary))
        if isinstance(a,list) and isinstance(b,list):check('H27', result==a+b, 'A fork-crossing range equals the corresponding per-block traces.')
    if name.startswith('filter-') and name.removeprefix('filter-').isdigit():
        block=reference('block-'+name.removeprefix('filter-'))
        if isinstance(block,list):check('H27', result==block, 'A single-block filter agrees with trace_block at the same fork.')
    if (name.startswith('filter-across-') or name.removeprefix('filter-').isdigit()) and not any(c['topic']=='H27' for c in checks):
        checks.append({'topic':'H27','status':'unassessed','requirement':'Compare anchored per-block traces.', 'detail':'Independent reference inventory unavailable.'})
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

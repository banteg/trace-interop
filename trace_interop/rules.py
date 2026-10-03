"""Explicit proposed assertions. These are not a client-majority oracle."""
from __future__ import annotations

import json
import re

from .oracles import anchor, IDENTITY, REVERT_OUTPUT, REVERT_GAS
from .vm_model import UnsupportedProgram, encoding_valid, execute


def is_extension_request(request):
    return request['method'] == 'trace_rawTransaction' and len(request.get('params', [])) > 2


def mapping(value):
    return value if isinstance(value, dict) else {}


def sequence(value):
    return value if isinstance(value, list) else []


def deleted_storage_shape(storage):
    """Deletion wipes every slot; optional details contain only old 32-byte words."""
    return isinstance(storage, dict) and all(
        isinstance(slot, str) and re.fullmatch(r'0x[0-9a-fA-F]{64}', slot)
        and isinstance(change, dict) and set(change) == {'-'}
        and isinstance(change['-'], str) and re.fullmatch(r'0x[0-9a-fA-F]{64}', change['-'])
        for slot, change in storage.items())


# Signed-transaction fixtures and the independent violation each one carries.
RAW_VIOLATIONS = [
    ('raw-nonce-high', 'nonce_high'), ('raw-wrong-chain', 'chain'), ('raw-insufficient-funds', 'funds'),
    ('raw-low-gas', 'intrinsic'), ('raw-below-basefee', 'base_fee'), ('raw-valid-default-block', 'nonce_low'),
    ('nonce below selected state', 'nonce_low'), ('creation nonce below selected state', 'nonce_low'),
    ('nonce above selected state', 'nonce_high'), ('creation nonce above selected state', 'nonce_high'),
    ('wrong chain identity', 'chain'), ('insufficient balance for value alone', 'funds'),
    ('value is affordable but upfront gas plus value is not', 'funds'),
    ('gas limit below 21000 intrinsic gas', 'intrinsic'), ('gas price below selected block base fee', 'base_fee'),
    ('EIP-3607 ordinary-code sender (not delegation)', 'sender')]
# Records whose filter membership follows per-action from/to equivalents (H23), not action.from/to.
SPECIAL_ACTIONS = ('create', 'suicide', 'reward')
# Unsigned simulations; H16 defers their fee accounting to H15's policy.
SIMULATIONS = ('trace_call', 'trace_callMany')
# Recommended eth_sendRawTransaction error groups (execution-apis #650); -32003 is the generic fallback.
RAW_CODES = {'nonce_low': 1, 'nonce_high': 2, 'intrinsic': 800, 'priority': 804, 'base_fee': 806, 'funds': 809}


# JSON-RPC 2.0 base-protocol errors: parse error, invalid request, method not found and internal error.
# They report a failure of the protocol or server, not a rejection of the request, so they never
# serve as an error the draft requires; any other code does, since the draft only recommends codes.
PROTOCOL_FAILURES = (-32700, -32600, -32601, -32603)


def rejection(status, response):
    """Whether a response is an error that rejects the request, whatever its (recommended) code."""
    return status == 'rpc_error' and mapping(mapping(response).get('error')).get('code') not in PROTOCOL_FAILURES


def recommended_note(code, recommended):
    """A note when an error's code differs from the recommended one. The draft requires the error
    response and recommends its code (H14), so a different code is reported, never a failure."""
    wanted = recommended if isinstance(recommended, list) else [recommended]
    return '' if recommended is None or code in wanted else f' ({" or ".join(map(str, wanted))} recommended)'


def violation(message):
    """Classify a validation error message; None when it names no known violation."""
    message = str(message).lower()
    # A gasPrice beside dynamic fee fields is a field combination (H14), whatever fee its message names.
    for kind, pattern in [('fee_fields', r'both gasprice and'), ('nonce_low', r'nonce too low'), ('nonce_high', r'nonce too high'),
                          ('chain', r'chain ?id'), ('intrinsic', r'intrinsic gas'),
                          ('funds', r'insufficient (?:funds|balance)|exceeds account balance'),
                          ('priority', r'(?:priority|\btip\b).*(?:fee|cap)'),
                          ('base_fee', r'base ?fee'), ('sender', r'\beoa\b')]:
        if re.search(pattern, message):
            return kind
    return None


# The block parameter's position for each method that selects one block.
BLOCK_PARAMETER = {'trace_block': 0, 'trace_replayBlockTransactions': 0, 'trace_call': 2, 'trace_callMany': 1}


def accounting_topic(method):
    """The decision that judges a response's fee accounting: H16 for signed and mined transactions,
    H15 for unsigned simulations, whose policy H16 defers to."""
    return 'H15' if method in SIMULATIONS else 'H16'


def page_dependencies(method, params, records):
    """Decisions a trace_filter page depends on besides its own. An address-filtered page shifts when a
    CREATE, SELFDESTRUCT or reward record in its range matches differently, so a page over such records
    depends on H23's per-action matching."""
    filt = mapping(params[0]) if method == 'trace_filter' and params else {}
    paged = {'after', 'count'} & set(filt)
    filtered = sequence(filt.get('fromAddress')) or sequence(filt.get('toAddress'))
    return ['H23'] if paged and filtered and any(mapping(r).get('type') in SPECIAL_ACTIONS for r in records) else []


def selects_pending(method, params):
    position = BLOCK_PARAMETER.get(method)
    return position is not None and len(params) > position and params[position] == 'pending'


def observed_number(call, output, context):
    """Which block NUMBER a simulated program observed, from the bounded VM model of its code:
    'head', 'next' or 'neither'; None when the model cannot tell them apart."""
    head = mapping(context.get('_environment')).get('NUMBER')
    data = call.get('data', call.get('input', '0x'))
    code = data if 'to' not in call else mapping(context.get('_codes')).get(str(call['to']).lower())
    if head is None or not isinstance(code, str):
        return None
    try:
        outputs = {label: execute(code, 10_000_000, '0x' if 'to' not in call else data,
                                  {'NUMBER': number, 'FRESH_ACCOUNT': 'to' not in call})[1]
                   for label, number in [('head', head), ('next', head+1)]}
    except (UnsupportedProgram, ValueError):
        return None
    if outputs['head'] == outputs['next']:
        return None
    return next((label for label, value in outputs.items() if value == output), 'neither')


def pending_check(method, params, status, response, result, context):
    """H32: a block method or simulation accepts `pending` only with a real pending environment, the
    block after the head; a client without one rejects it (-32602 recommended) rather than substituting latest."""
    requirement = ('Accept pending only with a real pending environment, the block after the head; '
                   'otherwise reject it (-32602 recommended), never evaluating latest instead.')
    head = mapping(context.get('_environment')).get('NUMBER')

    def verdict(value, detail):
        return {'topic': 'H32', 'status': value, 'requirement': requirement, 'detail': detail, 'role': 'rejection'}
    if status == 'rpc_error':
        code = mapping(response.get('error')).get('code')
        return verdict('matches' if rejection(status, response) else 'change_needed', f'RPC error {code}{recommended_note(code, -32602)}.')
    if status != 'result' or head is None:
        return verdict('blocked', f'No block witness: {status}.')
    if method in ['trace_call', 'trace_callMany']:
        first = sequence(params[0])[:1] if method == 'trace_callMany' else [[params[0]]]
        call = mapping(sequence(first[0])[0]) if first and sequence(first[0]) else {}
        execution = mapping(result) if method == 'trace_call' else mapping(sequence(result)[0]) if sequence(result) else {}
        observed = observed_number(call, execution.get('output'), context)
        if observed is None:
            return verdict('unassessed', 'The bounded VM model cannot show which block number this program observes.')
        return verdict('matches' if observed == 'next' else 'change_needed',
                       {'next': 'Executed in the pending block.', 'head': 'Executed at the head block, as latest.',
                        'neither': 'The output matches neither the head nor the pending block.'}[observed])
    if not isinstance(result, list):
        return verdict('change_needed', f'Expected a list; got {str(result)[:80]}.')
    if not result:
        return verdict('blocked', 'An empty result names no block, so it cannot show a pending environment.')
    if method == 'trace_block':
        numbers = sorted({mapping(f).get('blockNumber') for f in result}, key=str)
        return verdict('matches' if numbers == [head+1] else 'change_needed', f'Records from blocks {numbers}; the head is {head}.')
    canonical = {t['hash'] for b in mapping(context.get('_blocks')).values() for t in b['transactions']}
    replayed = {mapping(e).get('transactionHash') for e in result}
    return verdict('change_needed' if canonical & replayed else 'matches',
                   f'{len(result)} envelopes, {len(canonical & replayed)} of them canonical transactions.')


def embedded_error(response):
    value = mapping(response).get('result')
    return isinstance(value, dict) and value.get('jsonrpc') == '2.0' and 'error' in value


def calltree_frames(method, params, result, context):
    """Each complete frame list of the fixture calltree transaction in a mined-trace result.

    An address-filtered trace_filter can drop the calltree's children, so only an unfiltered
    range is complete; a list without the calltree root does not contain the transaction.
    """
    hashes = {t.get('txhash') for t in sequence(mapping(context.get('txinfo')).get('tx-calltree')) if isinstance(t, dict)}
    if method in ['trace_transaction', 'trace_block'] or (
            method == 'trace_filter' and params and not {'fromAddress', 'toAddress'} & set(mapping(params[0]))):
        lists = [[f for f in sequence(result) if isinstance(f, dict) and f.get('transactionHash') == h] for h in hashes]
    elif method == 'trace_replayTransaction' and params and params[0] in hashes:
        lists = [sequence(mapping(result).get('trace'))]
    elif method == 'trace_replayBlockTransactions':
        lists = [sequence(r.get('trace')) for r in sequence(result) if isinstance(r, dict) and r.get('transactionHash') in hashes]
    else:
        return []
    return [[f for f in frames if isinstance(f, dict)] for frames in lists
            if any(isinstance(f, dict) and f.get('traceAddress') == [] for f in frames)]


def evaluate(case, observation, peers, invalid_params=None):
    """Return independently scoped rule checks; absence means no automated assertion."""
    name, request = case['name'], case['request']
    context = case.get('context', {})
    method, params = request['method'], request.get('params', [])
    response = mapping(observation.get('response'))
    result = response.get('result')
    status = observation['status']
    checks = []

    def check(topic, ok, requirement, detail='', **tags):
        # tags: `role` and `depends`, which coverage.isolate and report.assess_runs resolve.
        checks.append({'topic': topic, 'status': 'matches' if ok else 'change_needed',
                       'requirement': requirement, 'detail': detail, **{k: v for k, v in tags.items() if v}})

    def rejected(topic, requirement, recommended, **tags):
        # The draft requires the error response itself; its code is only recommended.
        code = mapping(response.get('error')).get('code')
        note = recommended_note(code, recommended) if status == 'rpc_error' else ''
        check(topic, rejection(status, response), requirement, f'Code {code}{note}.' if note else '', **tags)

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
        # A case with an H12 state probe (probes.state_check) classifies which state the selector used.
        if not any(p['topic'] == 'H12' for p in case.get('probes', [])):
            if status == 'result':
                detail = 'The third-argument request returned a result; this does not prove which block state was used.'
            elif status == 'rpc_error' and mapping(response.get('error')).get('code') == -32602:
                detail = 'The third-argument request was rejected as invalid params.'
            else:
                detail = 'The third-argument request returned an error; extension support is not established.'
            checks.append({'topic': 'H12', 'status': 'observation', 'extension': True,
                           'requirement': 'Observe the explicit block-selector extension separately from the two-argument baseline.',
                           'detail': detail})
        return checks

    def other(n):
        obs = mapping(peers.get(n))
        return mapping(obs.get('response')).get('result') if obs.get('status') == 'result' else None

    mismatched = []
    def reference(n):
        frames, mismatch = anchor(context, peers, n)
        if mismatch: mismatched.append(f'{n}: {mismatch}')
        return frames

    if selects_pending(method, params):
        checks.append(pending_check(method, params, status, response, result, context))
    if invalid_params:
        # The schema-derived check yields to a decision that owns this rejection, such as pending_check
        # for the block methods, whose schema omits pending (coverage.isolate).
        code = mapping(response.get('error')).get('code')
        note = recommended_note(code, -32602) if status == 'rpc_error' else ''
        check('H14', rejection(status, response), 'Malformed input returns an error (-32602 recommended).',
              '; '.join(invalid_params) + (f'. Code {code}{note}.' if note else ''), role='schema')
        if method == 'trace_filter' and params and isinstance(params[0],dict) and 'mode' in params[0]:
            rejected('H03', 'Unknown mode values are rejected (-32602 recommended).', -32602, role='rejection')
        if method == 'trace_filter' and params and isinstance(params[0],dict) and 'pending' in [params[0].get('fromBlock'), params[0].get('toBlock')]:
            rejected('H32', 'trace_filter range bounds exclude pending, as eth_getLogs does (-32602 recommended).', -32602, role='rejection')
        return checks

    if context.get('_chain') == 'h30':
        number_48 = '0x' + f'{48:064x}'
        if name == 'filter-no-bounds':
            head = other('filter-head-only')
            check('H30', status == 'result' and isinstance(result, list) and len(result) == 3
                  and all(isinstance(frame, dict) and frame.get('blockNumber') == 48 for frame in result)
                  and result == head,
                  'Omitting both range bounds selects latest only, as an explicit head-only query does.', role='result')
        if name == 'filter-to-2-implicit-from':
            rejected('H30', 'An omitted fromBlock resolves to latest; an earlier explicit toBlock is a reversed range and is rejected '
                     '(-32602 recommended, as eth_getLogs), not a historical search.', -32602)
        if name in ['call-number-default', 'call-number-latest']:
            check('H31', status == 'result' and mapping(result).get('output') == number_48,
                  'An omitted or explicit latest trace_call block uses the frozen head (NUMBER 48).', role='result')
        if name in ['many-number-default', 'many-number-latest']:
            check('H31', status == 'result' and isinstance(result, list) and len(result) == 1
                  and mapping(result[0]).get('output') == number_48,
                  'trace_callMany accepts an omitted block and uses latest (NUMBER 48).', role='result')
        if name == 'filter-earliest':
            explicit = other('filter-0-to-2')
            check('H32', status == 'result' and isinstance(result, list) and isinstance(explicit, list)
                  and result == explicit,
                  'The earliest tag resolves like explicit block 0 on this fixture.', role='result')
        if name == 'filter-safe':
            check('H32', status == 'result' and isinstance(result, list) and len(result) == 3
                  and all(isinstance(frame, dict) and frame.get('blockNumber') == 48 for frame in result),
                  'The safe tag resolves to the fixture safe head, block 48.', role='result')
        if name == 'filter-pending':
            if status == 'rpc_error':
                detail = f'{name}: RPC error {mapping(response.get("error")).get("code")}.'
            elif isinstance(result, list):
                blocks = sorted({frame.get('blockNumber') for frame in result if isinstance(frame, dict)})
                detail = f'{name}: {len(result)} records from blocks {blocks}.'
            else:
                detail = f'{name}: {status}.'
            checks.append({'topic': 'H32', 'status': 'observation',
                           'requirement': 'Record pending behavior without assuming a settled state or localization policy.',
                           'detail': detail})
            check('H32', status != 'rpc_error' or mapping(response.get('error')).get('code') != -32603,
                  'A valid pending tag must not trigger an internal error; support remains a policy choice.')

    if method == 'trace_get' and len(params) > 1 and isinstance(params[1], list) and all(isinstance(x,str) and re.fullmatch(r'0x(?:0|[1-9a-f][0-9a-f]*)', x) for x in params[1]):
        path = [int(x, 16) for x in params[1]]
        missing = 'missing' in name or '0xffff' in params[1]
        if missing and name != 'get-missing-tx':
            # A missing path within an existing transaction is path selection; a missing transaction is H06's.
            check('H02', status == 'result' and result is None, 'A missing selected frame is null, not an empty collection.')
        elif not missing:
            tree_name = next((c['name'] for c in context.get('cases', [])
                              if c['request']['method'] == 'trace_transaction' and c['request']['params'] == params[:1]), 'transaction-tree')
            tree = reference(tree_name)
            tx_frames = [f for f in tree if isinstance(f,dict) and f.get('transactionHash') == params[0]] if isinstance(tree,list) else []
            if tx_frames:
                expected = next((f for f in tx_frames if f.get('traceAddress') == path),None)
                check('H02', status == 'result' and result == expected,
                      f'Return the transaction-tree record at {path}, or null if absent.',
                      'Compared with the same client and transaction; precompile inclusion can shift sibling indexes.', role='result')
            else:
                checks.append({'topic': 'H02', 'status': 'unassessed',
                               'requirement': 'Compare the requested path with the transaction tree.',
                               'detail': 'The reference tree did not establish the independent fixture inventory; path selection was not assessed.'})
    if name in ['transaction-missing','replay-missing','get-missing-tx']:
        check('H06', status == 'result' and result is None, 'Unknown transaction returns null, not an empty collection or RPC error.')
    if method == 'trace_replayTransaction' and isinstance(result, dict):
        got = result.get('transactionHash', 'absent')
        check('H07', got == params[0], 'Individual replay includes its transactionHash.',
              '' if got == params[0] else f'transactionHash {got!r}, expected {params[0]}.')
    if method in ['trace_call','trace_rawTransaction','trace_replayTransaction'] and isinstance(result,dict):
        modes = params[1] if len(params) > 1 else None
        if isinstance(modes,list):
            if 'trace' not in modes: check('H08', result.get('trace') == [], 'Unrequested trace is an empty array.')
            for key in ['vmTrace','stateDiff']:
                if key not in modes: check('H08', key in result and result[key] is None, f'Unrequested {key} is null.')
            check('H08', isinstance(result.get('output'),str) and re.fullmatch(r'0x(?:[0-9a-f]{2})*',result['output']) is not None,
                  'Output remains a byte string under every trace selection.')
    if name in ['state-only-nonempty-output','vm-only-nonempty-output']:
        check('H08', isinstance(result,dict) and result.get('output') == '0x'+f'{42:064x}', 'The return42 contract still returns word 42.', role='result')
    if name in ['empty-types','call-empty-types','call-empty-types-priced']:
        expected = '0x'+f'{42:064x}' if name == 'empty-types' else '0xffee'
        check('H11', status == 'result' and mapping(result).get('output') == expected,
              'An empty trace-type selection executes and preserves the fixture return bytes.',
              'Expected '+expected, role='result')
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
    for frames in calltree_frames(method, params, result, context):
        check('H29', not any(mapping(f.get('action')).get('to') == IDENTITY for f in frames),
              'Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call.',
              ', '.join(f'frame {f.get("traceAddress")} calls the identity precompile' for f in frames if mapping(f.get('action')).get('to') == IDENTITY))
    if name == 'call-identity':
        frames = [f for f in sequence(mapping(result).get('trace')) if isinstance(f, dict)]
        check('H22', bool(frames) and mapping(frames[0].get('result')).get('output') == params[0].get('data', params[0].get('input','0x')),
              'The identity precompile call frame preserves its input as return bytes.', role='result')
    if name == 'call-siblings-revert-ok':
        frames = [f for f in sequence(mapping(result).get('trace')) if isinstance(f, dict)]
        good = next((f for f in frames if f.get('traceAddress') == [1]),None)
        check('H24', good is not None and 'error' not in good and mapping(good.get('result')).get('output') == '0x'+f'{42:064x}',
              'The successful second sibling retains its output and has no error.', role='result')
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
        stack = [(result['vmTrace'], 'root')]
        invalid = []  # each offending step, named by its pc path from the root
        while stack:
            vm, where = stack.pop(0)
            if not isinstance(vm, dict) or not isinstance(vm.get('ops'), list):
                invalid.append(f'{where}: no ops list')
                continue
            for op in vm['ops']:
                if not isinstance(op, dict):
                    invalid.append(f'{where}: step {op!r}')
                    continue
                if not encoding_valid(op.get('ex')):
                    invalid.append(f'{where} pc {op.get("pc")}: ex {json.dumps(op.get("ex"))[:200]}')
                if op.get('sub') is not None: stack.append((op['sub'], f'{where} pc {op.get("pc")} sub'))
        check('H21', not invalid, 'Stack words and storage operands use minimal hex quantities at every depth.',
              f'First at {invalid[0]} ({len(invalid)} in total).' if invalid else '')
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
                listed=isinstance(result,list) and all(isinstance(f,dict) for f in result)
                requirement='Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted.'
                if topic == 'H23':
                    check(topic, listed and [identity(f) for f in result] == [identity(f) for f in expected],
                          requirement, f'Expected {len(expected)} records from this client\'s block trace.')
                else:
                    # A CREATE, SELFDESTRUCT or reward record matches by its own from/to equivalents (H23), so
                    # this case's list semantics are judged on the ordinary records and H23 on the rest.
                    special=lambda f:mapping(f).get('type') in SPECIAL_ACTIONS
                    ordinary=lambda frames:[identity(f) for f in frames if not special(f)]
                    ok=listed and ordinary(result) == ordinary(expected)
                    check(topic, ok, requirement,
                          f'Expected {sum(not special(f) for f in expected)} ordinary records from this client\'s block trace.')
                    actions=[identity(f) for f in expected if special(f)]
                    got=[identity(f) for f in result if special(f)] if listed else []
                    if actions or got:
                        requirement='A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents.'
                        if ok:
                            check('H23', got == actions, requirement, f'Expected {len(actions)} such records from this client\'s block trace; got {len(got)}.')
                        else:
                            checks.append({'topic': 'H23', 'status': 'blocked', 'requirement': requirement,
                                           'detail': f'The {topic} list semantics differ, so the special-action records cannot be judged separately.'})
            else:
                checks.append({'topic': topic, 'status': 'unassessed', 'requirement': 'Compare filtering with the block trace.',
                               'detail': 'The reference block trace did not establish the independent fixture inventory.'})
    if name == 'filter-two-blocks':
        a,b=reference('block-2'),reference('block-3')
        if isinstance(a,list) and isinstance(b,list):
            check('H27', result == a+b, 'Range traces equal concatenated per-block traces in canonical order.', role='result')
    if name == 'filter-two-blocks' and not any(c['topic']=='H27' for c in checks):
        checks.append({'topic':'H27','status':'unassessed','requirement':'Compare anchored per-block traces.', 'detail':'Independent reference inventory unavailable.'})
    # H15 deliberately submits invalid and blob-default requests. An RPC
    # rejection there must not become a spurious sequential-envelope failure, and
    # a case whose probe requires a rejection has no envelopes to count.
    rejects = any(p['kind'] == 'error' for p in case.get('probes', []))
    if (method == 'trace_callMany' and context.get('_chain') != 'h30' and params and isinstance(params[0], list)
            and not rejects and (not case.get('fee_policy') or status == 'result')):
        check('H16', status == 'result' and isinstance(result,list) and len(result) == len(params[0])
              and all(isinstance(r,dict) and isinstance(r.get('output'),str) and isinstance(r.get('trace'),list) for r in sequence(result)),
              'Return one execution envelope per input call, in order.', role='result')
    probe = name.rsplit('/',1)[-1]
    if probe == 'many-storage-write-read':
        check('H16', isinstance(result,list) and [mapping(r).get('output') for r in result] == ['0x'+f'{42:064x}']*2,
              'The second call reads the first call’s simulated write.', role='result')
    if probe == 'many-storage-write-revert-read':
        check('H16', isinstance(result,list) and [mapping(r).get('output') for r in result] == ['0x'+f'{42:064x}','0x','0x'+f'{42:064x}'], 'Sequential calls retain prior writes and roll back reverted writes.', role='result')
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
            for i,d in enumerate(diffs)), 'Each call reports its own sender nonce transition, including a reverted call.', role='result')
        storage = [mapping(mapping(d).get(target)).get('storage',{}) for d in diffs]
        # The target account exists at both endpoints, so its slots change with '*'
        # even from zero, as in Parity and every native client; slots never use '='.
        first = storage[0] if storage else None
        check('H16', valid and first == {slot:{'*':{'from':slot,'to':value}}}
              and all(s == {} for s in storage[1:]),
              'Only the first call writes slot zero; reverted writes and later reads add no storage transition.', role='result')
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
                  'Canonical storage remains unchanged after the ordered multi-call simulation.', role='result')
        else:
            checks.append({'topic':'H16','status':'unassessed',
                           'requirement':'Check canonical storage after the ordered simulation.',
                           'detail':'Ordered capture, initial zero slot or successful simulated write/read not established.'})
    if name in ['get-path-wrong-type','call-wrong-type','call-unknown-mode','call-scalar-mode','raw-invalid']:
        rejected('H14', 'Malformed input returns an error (-32602 recommended).', -32602)
    expected_violation = next((kind for label, kind in RAW_VIOLATIONS
                               if name == label or name.startswith(label+'-') or case.get('reason') == label), None)
    if method == 'trace_rawTransaction' and expected_violation:
        requirement = 'Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation.'
        reason = case.get('reason') or 'Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.'
        error = mapping(response.get('error'))
        observed = violation(error.get('message'))
        if status != 'rpc_error':
            check('H13', False, requirement, reason)
        elif observed is None or not rejection(status, response):
            checks.append({'topic': 'H13', 'status': 'blocked', 'requirement': requirement,
                           'detail': f'The error does not identify a validation failure: {error.get("code")} '+str(error.get('message'))[:120]})
        else:
            # The eth_sendRawTransaction error group, or -32003, is recommended, not required.
            codes = ([RAW_CODES[expected_violation]] if expected_violation in RAW_CODES else []) + [-32003]
            check('H13', observed == expected_violation, requirement,
                  f'Expected {expected_violation}; the error identifies {observed}; code {error.get("code")}'
                  f'{recommended_note(error.get("code"), codes)}. {reason}')
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
            pcs = [mapping(op).get('pc') for op in sequence(vm.get('ops'))]
            # What vmTrace holds is not a validation property: its bytecode is H19's, its operations H20's.
            check('H19', vm.get('code') == code, 'Requested vmTrace holds the executing fixture bytecode.',
                  f'Expected {code}; got {vm.get("code")}.')
            check('H20', pcs == expected_pcs, 'Requested vmTrace lists every operation that began executing, in order.',
                  f'Expected pcs {expected_pcs}; got {pcs}.')
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

    if name.startswith('missing-block-') and method == 'trace_filter':
        rejected('H06', 'A range bound beyond the head returns an error (-32602 recommended), as eth_getLogs does; never a clamped or partial result.', -32602)
    elif name.startswith('missing-block-') and method in ('trace_block', 'trace_replayBlockTransactions'):
        if status == 'result' and 'result' in response and result is None:
            check('H06', True, 'An unknown selected block returns null or an error (-32001 recommended), never a successful collection.')
        else:
            rejected('H06', 'An unknown selected block returns null or an error (-32001 recommended), never a successful collection.', -32001)
    elif name.startswith('missing-block-'):
        rejected('H06', 'An unknown single selected block returns an error (-32001 recommended), never null or a result.', -32001)
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
    def first(frames, ok):
        bad = next((f for f in frames if not ok(f)), None)
        return '' if bad is None else f'First at traceAddress {bad.get("traceAddress")}: error {bad.get("error")!r}, result {json.dumps(bad.get("result"))[:200]}.'
    if failed:
        detail = first(failed, lambda f: isinstance(f['error'], str) and bool(f['error'])
                       and (f.get('result') is None or isinstance(f['result'], dict)))
        check('H09', not detail, 'Failed frames have an error string; an exceptional halt omits result or sets it to null.', detail)
        reverted = [f for f in failed if f['error'] == 'Reverted']
        if reverted:
            detail = first(reverted, lambda f: isinstance(f.get('result'), dict) and {'gasUsed', 'output'} <= set(f['result'])
                           and not {'address', 'code'} & set(f['result']))
            check('H09', not detail, 'A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.', detail)
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
        balance=mapping(context.get('_alloc',{}).get(params[0]['to'])).get('balance')
        ok=(mapping(change).get('code') == {'-':'0x611008ff'}
            and mapping(change).get('nonce') == {'-':'0x0'}
            and (balance is None or mapping(change).get('balance') == {'-':hex(int(balance,16))})
            and deleted_storage_shape(mapping(change).get('storage'))
            and all(int(slot['-'], 16) == 0 for slot in change['storage'].values())) if before_cancun else mapping(change).get('code')=='=' and mapping(change).get('nonce')=='='
        check('H26', ok, 'Report the exact deleted balance, code and nonce before Cancun; optional slot deletions match the known zero pre-values. Preserve an existing account after EIP-6780.')
    diffs = [mapping(e).get('stateDiff') for e in ([result] if isinstance(result, dict) else sequence(result)
                                                   if method in ['trace_callMany', 'trace_replayBlockTransactions'] else [])]
    deleted = [(address, account) for diff in diffs for address, account in mapping(diff).items()
               if any(isinstance(mapping(account).get(k), dict) and '-' in account[k] for k in ['balance', 'nonce', 'code'])]
    if deleted:
        check('H26', all(deleted_storage_shape(mapping(account).get('storage')) for _, account in deleted),
              'A deleted account reports storage {} or optional old-slot - entries; account deletion implies every slot is wiped.',
              '; '.join(address for address, account in deleted if not deleted_storage_shape(mapping(account).get('storage')))[:200])
    if name.startswith('filter-across-'):
        boundary=int(name.rsplit('-',1)[1]); a,b=reference('block-'+str(boundary-1)),reference('block-'+str(boundary))
        if isinstance(a,list) and isinstance(b,list):check('H27', result==a+b, 'A fork-crossing range equals the corresponding per-block traces.', role='result')
    if name.startswith('filter-') and name.removeprefix('filter-').isdigit():
        block=reference('block-'+name.removeprefix('filter-'))
        if isinstance(block,list):check('H27', result==block, 'A single-block filter agrees with trace_block at the same fork.', role='result')
    if (name.startswith('filter-across-') or name.removeprefix('filter-').isdigit()) and not any(c['topic']=='H27' for c in checks):
        checks.append({'topic':'H27','status':'unassessed','requirement':'Compare anchored per-block traces.', 'detail':'Independent reference inventory unavailable.'})
    if name.startswith('system-beacon-'):
        _,_,block,slot=name.split('-'); headers=context.get('headers',[])
        h=next((h for h in headers if h.get('number')=='0x38'),None)
        if h:
            expected='0x'+('0'*64 if int(block)<56 else f'{560:064x}' if slot=='560' else h['parentBeaconBlockRoot'][2:])
            check('H28', status=='result' and result==expected, 'Historical beacon-root storage excludes the following block system update.', role='result')
    if name in ['beacon-call-55','beacon-call-56']:
        h=next((h for h in context.get('headers',[]) if h.get('number')=='0x38'),None)
        if h:check('H28', isinstance(result,dict) and result.get('output')==('0x' if name.endswith('55') else h['parentBeaconBlockRoot']), 'Historical trace_call uses only system changes through the selected block.', role='result')
    if context.get('_chain')=='pruned' and method.startswith('trace_') and name.startswith('old-'):
        rejected('H06', 'Unavailable historical state returns an error (4444, pruned history, recommended), never a result or null.', 4444)
    # A reference that contradicts its anchored fixture actions is a client
    # difference, not an unestablished inventory.
    for c in checks:
        if c['status'] == 'unassessed' and mismatched:
            c.update(status='change_needed', detail='Reference frames contradict the fixture: '+'; '.join(mismatched))
    return checks

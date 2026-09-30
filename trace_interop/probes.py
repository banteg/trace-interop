"""Declarative probe expectations carried by the corpus, never learned from a response.

A case lists `probes`: each names its decision topic, a kind and the expected values
its generator derived from frozen chain data, fixture bytecode or the bounded VM
model. Each kind checks one property, so a verdict names the property that differs.
An `error` probe requires an error response; its optional `recommended` code is reported, not required.
A probe may declare `depends` ({topic, reason}): an error response then blocks it, since
the error cannot separate its property from that dependency. A probe with `observe` (a
reason) records its outcome as an observation, never as a verdict; with `extension` it is
extension evidence, which does not hold a topic's verdict open (presentation.verdict).
A `block-hash` probe (H33) classifies which block a trace_filter blockHash selected.
"""
from .rules import (
    deleted_storage_shape,
    embedded_error,
    page_dependencies,
    recommended_note,
    rejection,
    violation,
)
from .vm_model import UnsupportedProgram, execute, store_words, words
from .chain_model import resolve_block


def mapping(value):
    return value if isinstance(value, dict) else {}


def sequence(value):
    return value if isinstance(value, list) else []


def same(actual, expected):
    """Compare a frame against its expected subset. Hex strings compare case-insensitively
    (addresses), labels exactly; `error: None` requires no error and `error: '*'` any non-empty label;
    `absent` lists result keys that must be missing; `result: None` requires an omitted or null result."""
    for key, want in expected.items():
        if key == 'absent':
            if set(want) & set(mapping(actual.get('result'))):
                return False
        elif key == 'error' and want is None:
            if 'error' in actual:
                return False
        elif key == 'error' and want == '*':
            if not isinstance(actual.get('error'), str) or not actual['error']:
                return False
        elif key == 'result' and want is None:
            if actual.get('result') is not None:
                return False
        elif isinstance(want, dict):
            if not isinstance(actual.get(key), dict) or not same(actual[key], want):
                return False
        elif isinstance(want, str) and want.startswith('0x') and isinstance(actual.get(key), str):
            if actual[key].lower() != want.lower():
                return False
        elif actual.get(key) != want or type(actual.get(key)) is not type(want):
            return False
    return True


def first_difference(actual, expected):
    if not isinstance(actual, list):
        return f'expected a list of {len(expected)} records, got {type(actual).__name__}'
    for i, want in enumerate(expected):
        if i >= len(actual):
            return f'record {i} missing; expected {want}'
        if not isinstance(actual[i], dict) or not same(actual[i], want):
            return f'record {i}: expected {want}, got {actual[i]}'
    if len(actual) > len(expected):
        return f'{len(actual)-len(expected)} unexpected extra records, first {actual[len(expected)]}'
    return ''


def quantity(value):
    try:
        return int(value, 16) if isinstance(value, str) else None
    except ValueError:
        return None


def witness_values(witness, result):
    """Each named witness read from a result: a 32-byte output word, or the value a stateDiff
    account field changed from, i.e. its value in the state the transaction ran against."""
    output = mapping(result).get('output')
    data = output[2:] if isinstance(output, str) and output.startswith('0x') else ''
    diff = mapping(mapping(result).get('stateDiff'))
    values = {}
    for name, source in witness.items():
        if 'word' in source:
            value = quantity('0x'+data[64*source['word']:64*source['word']+64]) if len(data) >= 64*source['word']+64 else None
        else:
            value = quantity(mapping(mapping(mapping(diff.get(source['account'])).get(source['field'])).get('*')).get('from'))
        values[name] = value
    return values


def candidate(candidates, values):
    """The first candidate label whose every witness equals the observed value, or None."""
    return next((label for label, want in candidates
                 if all(values.get(k) is not None and values[k] == quantity(v) for k, v in want.items())), None)


def state_check(probe, status, response, result):
    """H12: which state, and with `environments` which block environment, a request ran against.
    An `observe` probe classifies an explicit selector against its `expected` and `default` (the
    two-argument choice) candidates as honored, ignored or rejected; otherwise the expected
    candidates are required. Witness values are shown only when no candidate explains them."""
    expected, observe = probe['expected'], 'observe' in probe
    prefix = 'Selector '+probe['selector']+': ' if 'selector' in probe else ''
    if status != 'result' or embedded_error(response):
        error = mapping(response.get('error') or mapping(result).get('error'))
        code, message = error.get('code'), str(error.get('message', ''))[:120]
        if code == -32602:
            detail = f'rejected as invalid params (-32602: {message}).'
        elif violation(message):
            detail = f'rejected as {violation(message)} ({code}: {message}), although valid at the expected state.'
        else:
            detail = f'{status} {code}: {message}.'
        if observe:
            return {'topic': probe['topic'], 'status': 'observation', 'requirement': probe['requirement'],
                    'detail': prefix+detail, **({'extension': True} if probe.get('extension') else {})}
        return {'topic': probe['topic'], 'status': 'change_needed', 'requirement': probe['requirement'],
                'detail': prefix+'Expected an execution; '+detail, 'role': 'result'}
    values = witness_values(probe['witness'], result)
    state = candidate(probe['states'], values)
    environment = candidate(probe['environments'], values)
    ran = (state or 'an unrecognised state') + (
        ' in ' + (environment or 'an unrecognised environment') if probe['environments'] else '')
    if state is None or probe['environments'] and environment is None:
        ran += ' (' + ', '.join(f'{k} {"none" if v is None else hex(v)}' for k, v in values.items()) + ')'
    matched = state == expected['state'] and environment == expected.get('environment')
    if not observe:
        target = expected['state'] + (' in '+expected['environment'] if 'environment' in expected else '')
        return {'topic': probe['topic'], 'status': 'matches' if matched else 'change_needed',
                'requirement': probe['requirement'], 'role': 'result',
                'detail': f'Ran against {ran}.' if matched else f'Expected {target}; ran against {ran}.'}
    default = probe.get('default', {})
    if matched:
        detail = f'honored: {ran}.'
    elif state == default.get('state') and environment == default.get('environment'):
        detail = f'ignored, running as the two-argument request: {ran}.'
    elif state == expected['state']:
        detail = f'state honored, environment not: {ran}.'
    else:
        detail = f'neither the selected nor the two-argument state: {ran}.'
    return {'topic': probe['topic'], 'status': 'observation', 'requirement': probe['requirement'],
            'detail': prefix+detail, **({'extension': True} if probe.get('extension') else {})}


def block_hash_check(probe, case, status, response, result, reference):
    """H33: whether a trace_filter blockHash selected exactly the block it names. A selection is
    compared with the numeric filter `reference` of the same build, restricted to that block, or with
    `expected`; with `reject` the request must be an error. `allow_reject` permits an explicit
    rejection of the optional capability without establishing support. The detail classifies the response as
    honored, rejected, answered another block (records localized elsewhere, such as the head),
    [] where the block has records, or partial (the block's records, but not the equivalent's)."""
    block = probe['block']
    wanted = (int(block['number'], 16), block['hash']) if block else None
    head = mapping(case.get('context', {}).get('_head')).get('number')

    def at(record):
        return (mapping(record).get('blockNumber'), mapping(record).get('blockHash'))

    def name(number, digest=None):
        text = f'block {hex(number)}' if type(number) is int else f'block {number!r}'
        if type(number) is int and head and number == int(head, 16):
            text += ' (the head)'
        if wanted and number == wanted[0] and digest != wanted[1]:
            text += f' with hash {str(digest)[:10]}…'
        return text

    def described(records):
        places = list(dict.fromkeys(at(r) for r in records))
        count = f'{len(records)} {"record" if len(records) == 1 else "records"}'
        numbers = [n for n, _ in places if type(n) is int]
        if len(places) > 3 and len(numbers) == len(places):
            return f'{count} from {len(places)} blocks, {name(min(numbers))} to {name(max(numbers))}'
        return f'{count} from {", ".join(name(*place) for place in places)}'
    requested = f'block {block["number"]}' if block else 'the requested block'

    def verdict(ok, detail, role):
        return {'topic': probe['topic'], 'status': 'matches' if ok else 'change_needed',
                'requirement': probe['requirement'], 'detail': detail, 'role': role}

    def blocked(detail):
        return {'topic': probe['topic'], 'status': 'blocked', 'requirement': probe['requirement'], 'detail': detail}
    role = 'rejection' if probe.get('reject') else 'result'
    # Optional hash selection may be rejected even when its numeric control is unavailable.
    # Judge the rejection first; only an accepted collection needs a selection oracle.
    if probe.get('allow_reject') and (status == 'rpc_error' or embedded_error(response)):
        error = mapping(response.get('error') or mapping(result).get('error'))
        code, message = error.get('code'), str(error.get('message', ''))[:120]
        if not rejection(status, response):
            return verdict(False, f'Failed with {code}: {message}, a server failure rather than a rejection.', 'rejection')
        return verdict(True, f'Rejected optional hash selection ({code}: {message}); this does not establish support.', 'rejection')
    if status == 'result' and (not isinstance(result, list) or not all(isinstance(r, dict) for r in result)):
        return verdict(False, f'Expected a list of trace records; observed {status} {str(result)[:120]}.', role)
    # An accepted selection needs the twin's records or an independent expected result.
    # Without either oracle its identity is unassessed. `reject` permits no collection.
    has = None
    if not probe.get('reject'):
        if 'expected' in probe:
            expected, source = probe['expected'], requested
        elif reference is None:
            return blocked(f'The numeric equivalent {probe["reference"]} returned no result.')
        else:
            expected, source = [r for r in reference if at(r) == wanted], f'the numeric equivalent {probe["reference"]}'
            if probe.get('nonempty') and not expected:
                return blocked(f'The numeric equivalent {probe["reference"]} has no records from {requested}, so it cannot show which block was selected.')
        has = f'{source} has ' + (described(expected) if expected else '[]')
    if status == 'rpc_error' or embedded_error(response):
        error = mapping(response.get('error') or mapping(result).get('error'))
        code, message = error.get('code'), str(error.get('message', ''))[:120]
        if not rejection(status, response):
            return verdict(False, f'Failed with {code}: {message}, a server failure rather than a rejection.', role)
        if has is None:
            return verdict(True, f'Rejected ({code}: {message}){recommended_note(code, probe.get("recommended"))}.', role)
        return verdict(False, f'Rejected ({code}: {message}), where {has}.', role)
    if status != 'result' or not isinstance(result, list) or not all(isinstance(r, dict) for r in result):
        return verdict(False, f'Expected a list of trace records; observed {status} {str(result)[:120]}.', role)
    elsewhere = [r for r in result if at(r) != wanted]
    if has is None:
        if not result:
            count = mapping(sequence(case['request'].get('params'))[0]).get('count')
            return verdict(False, 'Accepted: returned []' + (', the count 0 shortcut before validating the selector.' if count == 0 else '.'), role)
        if elsewhere:
            return verdict(False, f'Accepted: answered another block, {described(result)}.', role)
        return verdict(False, f'Accepted: answered {requested}’s {len(result)} records.', role)
    if result == expected:
        return verdict(True, f'Honored: {described(result) if result else "[]"}, the same as {source}'
                       + ('.' if result else '; an empty result alone cannot show which block was selected.'), role)
    if elsewhere:
        return verdict(False, f'Answered another block: {described(result)}, where {has}.', role)
    if not result:
        return verdict(False, f'Returned [] where {has}.', role)
    index = next((i for i, (got, want) in enumerate(zip(result, expected)) if got != want), min(len(result), len(expected)))
    return verdict(False, f'Partial: {described(result)}, where {has}; they first differ at record {index}.', role)


def model_steps(case):
    model = case['model']
    call = case['request']['params'][0]
    environment = {'FRESH_ACCOUNT': 'to' not in call}
    return execute(model['code'], 10_000_000, '0x' if 'to' not in call else call.get('data', call.get('input', '0x')), environment)[0]['ops']


def assess(case, observation, peers):
    probes = case.get('probes')
    if not probes:
        return []
    method = case['request']['method']
    status = observation.get('status')
    response = mapping(observation.get('response'))
    result = response.get('result')
    checks = []

    def add(topic, ok, requirement, detail='', **tags):
        if 'observe' in probe:
            checks.append({'topic': topic, 'status': 'observation', 'requirement': requirement,
                           'detail': probe['observe']+(' Observed: '+detail if detail else '')})
            return
        checks.append({'topic': topic, 'status': 'matches' if ok else 'change_needed',
                       'requirement': requirement, 'detail': detail, **{k: v for k, v in tags.items() if v}})

    def envelope(index):
        if method == 'trace_callMany':
            return mapping(result[index]) if isinstance(result, list) and index is not None and index < len(result) else {}
        return mapping(result)

    def peer_result(name):
        peer = mapping(peers.get(name))
        return mapping(peer.get('response')).get('result') if peer.get('status') == 'result' else None

    for probe in probes:
        topic, kind = probe['topic'], probe['kind']
        requirement = probe['requirement']
        # These frozen probes captured the earlier universal-zero proposal. Keep their
        # responses, but do not turn either normalization or rejection into agreement.
        if topic == 'H15' and kind == 'frame' and case['name'] in ['blob-fee-zero', 'blob-fee-defaulted']:
            frames = sequence(mapping(result).get('trace'))
            frame = next((f for f in frames if isinstance(f, dict) and same(f, probe['select'])), {})
            word = mapping(frame.get('result')).get('code')
            error = mapping(response.get('error') or mapping(result).get('error'))
            detail = (f'Observed deployed BLOBBASEFEE word {word}.' if status == 'result'
                      else f'Observed {status} {error.get("code")}: {error.get("message")}.')
            checks.append({'topic': topic, 'status': 'unassessed' if status == 'result' or rejection(status, response) else 'blocked',
                           'requirement': 'Blob defaults, validation and BLOBBASEFEE for omitted or zero pricing remain separately unresolved.',
                           'detail': detail+' The retained universal-zero expectation no longer defines conformance.'})
            continue
        # Grandfather canonical hash-to-height range endpoints as optional extensions.
        # This frozen pair has identical endpoints and a numeric page with the same count.
        if topic == 'H32' and kind == 'error' and case['name'] in ['filter-hash-bounds', 'filter-hash-object-bounds']:
            bound = case['request']['params'][0]['fromBlock']
            block = resolve_block(case.get('context', {}), mapping(bound).get('blockHash') if isinstance(bound, dict) else bound)
            if block is None:
                checks.append({'topic': topic, 'status': 'blocked', 'requirement': 'Resolve the optional hash range endpoint.',
                               'detail': 'No independent canonical header is available for this endpoint.'})
                continue
            selected = dict(block, number=hex(block['number']))
            revised = dict(probe, block=selected, reference='filter-block-2', nonempty=True, allow_reject=True,
                           requirement='Reject unsupported canonical hash range bounds, or return the same canonical page as the numeric range.')
            reference = peer_result(revised['reference'])
            checks.append(block_hash_check(revised, case, status, response, result,
                                           reference if isinstance(reference, list) else None))
            continue
        if kind == 'state':
            checks.append(state_check(probe, status, response, result))
            continue
        if kind == 'block-hash':
            reference = peer_result(probe['reference']) if 'reference' in probe else None
            checks.append(block_hash_check(probe, case, status, response, result,
                                           reference if isinstance(reference, list) else None))
            continue
        if kind == 'error':
            # Any error response satisfies the rule; a `recommended` code is reported, never required.
            error = mapping(response.get('error'))
            add(topic, rejection(status, response), requirement,
                f'Observed {status}' + (f' {error.get("code")}: {str(error.get("message"))[:120]}'
                                        + recommended_note(error.get('code'), probe.get('recommended')) if status == 'rpc_error'
                                        else f' with output {str(mapping(result).get("output", result))[:140]}'),
                role='rejection')
            continue
        if status != 'result' or embedded_error(response):
            # An error envelope wrapped as a result (H25) carries no result either.
            error = mapping(response.get('error') or mapping(result).get('error'))
            observed = f'{status} {error.get("code", "")} {str(error.get("message", ""))[:120]}'.strip()
            if 'depends' in probe and not (kind == 'same-output' and isinstance(peer_result(probe['reference']), str)):
                checks.append({'topic': topic, 'status': 'blocked', 'requirement': requirement,
                               'detail': f'Depends on {probe["depends"]["topic"]}: {probe["depends"]["reason"]} Observed {observed}.'})
                continue
            add(topic, False, requirement, f'Expected a result; observed {observed}', role='result')
            continue
        if kind == 'records':
            detail = first_difference(result, probe['expected'])
            depends = [] if topic == 'H23' else page_dependencies(method, case['request'].get('params', []), probe['expected'])
            add(topic, not detail, requirement, detail, depends=depends)
        elif kind == 'outputs':
            expected = probe['expected']
            if method == 'trace_callMany':
                outputs = [mapping(e).get('output') for e in result] if isinstance(result, list) else None
            else:  # A plain read such as eth_getStorageAt returns its word as the result.
                outputs = [mapping(result).get('output') if method.startswith('trace_') else result]
            ok = outputs is not None and len(outputs) == len(expected) and all(
                want is None or isinstance(got, str) and got.lower() == want for got, want in zip(outputs, expected))
            add(topic, ok, requirement, f'Expected {expected}; got {outputs}')
        elif kind == 'same-output':
            reference = peer_result(probe['reference'])
            reference = mapping(reference).get('output') if isinstance(reference, dict) else reference
            if not isinstance(reference, str):
                checks.append({'topic': topic, 'status': 'blocked', 'requirement': requirement,
                               'detail': 'The reference '+probe['reference']+' returned no successful output.'})
                continue
            output = envelope(probe.get('index')).get('output')
            add(topic, output == reference, requirement, f'Reference {reference[:140]}; got {str(output)[:140]}')
        elif kind == 'gas-output-bound':
            reference = peer_result(probe['reference'])
            output = envelope(probe.get('index')).get('output') if method.startswith('trace_') else result
            if not isinstance(reference, str) or len(reference) != 66 or quantity(reference) is None:
                checks.append({'topic': topic, 'status': 'blocked', 'requirement': requirement,
                               'detail': 'The cap reference '+probe['reference']+' returned no GAS word.'})
                continue
            ok = isinstance(output, str) and len(output) == 66 and quantity(output) is not None and quantity(output) <= quantity(reference)
            add(topic, ok, requirement, f'Cap GAS word {reference}; got {str(output)[:140]}')
        elif kind == 'same-result':
            # The whole result equals the reference request's, e.g. explicit nulls against omitted members.
            reference = peer_result(probe['reference'])
            if reference is None:
                checks.append({'topic': topic, 'status': 'blocked', 'requirement': requirement,
                               'detail': 'The reference '+probe['reference']+' returned no result.'})
                continue
            add(topic, status == 'result' and result == reference, requirement,
                f'Reference {str(reference)[:140]}; got ' + (str(result)[:140] if status == 'result' else f'{status} {mapping(response.get("error")).get("code")}'))
        elif kind == 'frames':
            frames = envelope(probe.get('index')).get('trace')
            detail = first_difference(frames, probe['expected'])
            add(topic, not detail, requirement, detail)
        elif kind == 'frame':
            # One frame's fields, where another probe owns whether the frame exists.
            frame = next((f for f in sequence(envelope(probe.get('index')).get('trace'))
                          if isinstance(f, dict) and same(f, probe['select'])), None)
            if frame is None:
                checks.append({'topic': topic, 'status': 'blocked', 'requirement': requirement,
                               'detail': f'No frame matches {probe["select"]}.'})
                continue
            add(topic, same(frame, probe['expected']), requirement, f'Expected {probe["expected"]}; got {frame}')
        elif kind == 'depth':
            # Attempts beyond the call depth limit: under the deepest executed frame, one failed frame per
            # attempt, with an error, no result and no children. With `labels`, only their error labels are
            # judged, and a missing attempt is blocked because the frame probe owns its presence.
            frames = [f for f in sequence(envelope(probe.get('index')).get('trace')) if isinstance(f, dict)]
            path = lambda f: sequence(f.get('traceAddress'))
            executed = [f for f in frames if not f.get('error')]
            deepest = max(executed, key=lambda f: len(path(f)), default=None)
            depth = len(path(deepest)) if deepest else -1
            attempts = [f for f in frames if len(path(f)) == depth + 1]
            shapes = [(f.get('type'), f.get('error'), f.get('result'), f.get('subtraces')) for f in attempts]
            ok = (depth == probe['depth'] and [f.get('type') for f in attempts] == probe['attempts']
                  and all(f.get('error') and f.get('result') is None and f.get('subtraces') == 0 for f in attempts)
                  and deepest.get('subtraces') == len(attempts))
            if 'labels' in probe:
                if [f.get('type') for f in attempts] != probe['attempts']:
                    checks.append({'topic': topic, 'status': 'blocked', 'requirement': requirement,
                                   'detail': f'No failed attempts {probe["attempts"]} under the deepest executed frame at depth {depth}.'})
                    continue
                add(topic, [f.get('error') for f in attempts] == probe['labels'], requirement,
                    f'Expected labels {probe["labels"]}; got {[f.get("error") for f in attempts]}.')
            else:
                add(topic, ok, requirement, f'Deepest executed frame at depth {depth} with subtraces {deepest.get("subtraces") if deepest else None}; attempts beyond it (type, error, result, subtraces): {shapes}.')
        elif kind == 'deleted-storage':
            diff = envelope(probe.get('index')).get('stateDiff')
            storage = mapping(mapping(diff).get(probe['address'])).get('storage')
            ok = deleted_storage_shape(storage) and all(
                int(change['-'], 16) == int(probe['expected'].get(slot.lower(), '0x'+'0'*64), 16)
                for slot, change in storage.items())
            add(topic, ok, requirement, f'Known pre-state slots {probe["expected"]}; got {storage}')
        elif kind == 'account':
            diff = envelope(probe.get('index')).get('stateDiff')
            account = mapping(mapping(diff).get(probe['address']))
            ok = isinstance(diff, dict) and bool(account) and same(account, probe['expected'])
            add(topic, ok, requirement, f'Expected {probe["expected"]}; got {account or diff}')
        elif kind == 'subs':
            ops = sequence(mapping(envelope(probe.get('index')).get('vmTrace')).get('ops'))
            by_pc = {op.get('pc'): op for op in ops if isinstance(op, dict)}
            missing = [pc for pc in probe['null'] + probe['object'] if pc not in by_pc]
            wrong = [pc for pc in probe['null'] if pc in by_pc and by_pc[pc].get('sub') is not None]
            wrong += [pc for pc in probe['object'] if pc in by_pc and not isinstance(by_pc[pc].get('sub'), dict)]
            add(topic, not missing and not wrong, requirement,
                f'Operations missing at pc {missing}; wrong sub at pc {wrong}.' if missing or wrong else '')
        elif kind in ['push', 'store', 'end']:
            vm = mapping(mapping(result).get('vmTrace'))
            ops = vm.get('ops')
            try:
                model = model_steps(case)
            except UnsupportedProgram as exc:
                checks.append({'topic': topic, 'status': 'unassessed', 'requirement': requirement,
                               'detail': 'The bounded VM model cannot establish this program: '+str(exc)})
                continue
            if not isinstance(ops, list) or [mapping(o).get('pc') for o in ops[:len(model)]] != [o['pc'] for o in model]:
                add(topic, False, requirement, f'Root operations do not follow the modelled pcs {[o["pc"] for o in model]}; got {[mapping(o).get("pc") for o in sequence(ops)]}')
                continue
            if kind == 'end':
                code_size = len(vm.get('code', '0x'))//2-1 if isinstance(vm.get('code'), str) else None
                extra = [mapping(o).get('pc') for o in ops[len(model):]]
                add(topic, not extra, requirement,
                    f'Extra operations after the last instruction at pc {extra}; code size {code_size}.' if extra else '')
                continue
            bad = []
            for got, want in zip(ops, model):
                ex = mapping(mapping(got).get('ex'))
                if kind == 'push' and want['op'].startswith(('DUP', 'SWAP')) and words(ex.get('push')) != words(want['ex']['push']):
                    bad.append(f'{want["op"]} at pc {want["pc"]}: expected {want["ex"]["push"]}, got {ex.get("push")}')
                if kind == 'store' and (store_words(ex.get('store')) != store_words(want['ex']['store'])
                                        or ex.get('store') is not None and store_words(ex['store']) is None):
                    bad.append(f'{want["op"]} at pc {want["pc"]}: expected {want["ex"]["store"]}, got {ex.get("store")}')
            add(topic, not bad, requirement, '; '.join(bad[:4]))
        else:
            raise ValueError('unknown probe kind: '+kind)
    return checks

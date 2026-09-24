"""Declarative probe expectations carried by the corpus, never learned from a response.

A case lists `probes`: each names its decision topic, a kind and the expected values
its generator derived from frozen chain data, fixture bytecode or the bounded VM
model. Each kind checks one property, so a verdict names the property that differs.
"""
from .vm_model import UnsupportedProgram, execute, store_words, words


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

    def add(topic, ok, requirement, detail=''):
        checks.append({'topic': topic, 'status': 'matches' if ok else 'change_needed',
                       'requirement': requirement, 'detail': detail})

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
        if kind == 'error':
            error = mapping(response.get('error'))
            code = probe.get('code')
            ok = status == 'rpc_error' and (code is None or error.get('code') == code)
            add(topic, ok, requirement,
                f'Observed {status}' + (f' {error.get("code")}: {str(error.get("message"))[:120]}' if status == 'rpc_error'
                                        else f' with output {str(mapping(result).get("output", result))[:140]}'))
            continue
        if status != 'result':
            error = mapping(response.get('error'))
            add(topic, False, requirement, f'Expected a result; observed {status} {error.get("code", "")} {str(error.get("message", ""))[:120]}'.strip())
            continue
        if kind == 'records':
            detail = first_difference(result, probe['expected'])
            add(topic, not detail, requirement, detail)
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


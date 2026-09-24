"""Exact assertions for the mined-probes chain.

The corpus derives every expectation from the frozen chain bytes, genesis and hand-
calculated gas (scripts/build_mined_probes_fixtures.py); no client response is an input.
Per-transaction assertions apply wherever that transaction appears: individual and block
replay, trace_transaction and trace_block. Filter cases pin their exact frame identities.
"""
from .execution_models import balance_delta


def obj(value):
    return value if isinstance(value, dict) else {}


def seq(value):
    return value if isinstance(value, list) else []


def check_frame(frames, want):
    """Return a mismatch description for one expected frame, or None."""
    frame = next((f for f in frames if f.get('traceAddress') == want['traceAddress']), None)
    label = f'{want["type"]} {want["traceAddress"]}'
    if frame is None:
        return label+': missing'
    problems = []
    if frame.get('type') != want['type']:
        problems.append(f'type {frame.get("type")}')
    action = obj(frame.get('action'))
    problems += [f'action.{k} {action.get(k)} != {v}' for k, v in want['action'].items() if action.get(k) != v]
    if want['error'] is None:
        if 'error' in frame:
            problems.append(f'unexpected error {frame["error"]!r}')
    elif frame.get('error') != want['error']:
        problems.append(f'error {frame.get("error")!r} != {want["error"]!r}')
    if 'result' in want and frame.get('result') != want['result']:
        problems.append(f'result {frame.get("result")} != {want["result"]}')
    if 'output' in want and obj(frame.get('result')).get('output') != want['output']:
        problems.append(f'result.output {obj(frame.get("result")).get("output")} != {want["output"]}')
    return label+': '+'; '.join(problems) if problems else None


def assess_transaction(probe, topics, envelope, frames, selection):
    """Checks for one transaction's expectations visible in this response."""
    checks = []
    diff = envelope.get('stateDiff') if envelope is not None else None

    def add(assertion, ok, detail=''):
        checks.append({'topic': assertion['topic'], 'status': 'matches' if ok else 'change_needed',
                       'requirement': assertion['requirement'], 'detail': '' if ok else detail})

    for assertion in probe['assertions']:
        if assertion['topic'] not in topics:
            continue
        kind = assertion['kind']
        if kind in ['tree', 'frame'] and 'trace' in selection:
            if kind == 'tree':
                got = [[f.get('traceAddress'), f.get('type')] for f in frames]
                add(assertion, got == assertion['frames'], f'Expected {assertion["frames"]}, got {got}.')
            else:
                problem = check_frame(frames, assertion)
                add(assertion, problem is None, problem or '')
        elif kind == 'output' and envelope is not None:
            add(assertion, envelope.get('output') == assertion['value'],
                f'Expected {assertion["value"]}, got {envelope.get("output")}.')
        elif kind in ['account', 'delta'] and 'stateDiff' in selection:
            if not isinstance(diff, dict):
                add(assertion, False, 'No stateDiff object was returned.')
                continue
            account = diff.get(assertion['address'])
            if kind == 'account':
                add(assertion, account == assertion['diff'],
                    f'{assertion["address"]}: expected {assertion["diff"]}, got {account}.')
            else:
                account = obj(account)
                nonce = balance_delta(account.get('nonce', '='))
                balance = balance_delta(account.get('balance', '='))
                add(assertion, balance == assertion['balance'] and nonce == assertion['nonce'],
                    f'{assertion["address"]}: expected balance delta {assertion["balance"]} and nonce delta '
                    f'{assertion["nonce"]}, got {balance} and {nonce}.')
        elif kind == 'store' and 'vmTrace' in selection:
            ops = seq(obj(envelope.get('vmTrace')).get('ops')) if envelope is not None else []
            code = obj(envelope.get('vmTrace')).get('code') if envelope is not None else None
            try:
                raw = bytes.fromhex(code[2:])
                writes = [obj(obj(op).get('ex')).get('store') for op in ops
                          if isinstance(obj(op).get('pc'), int) and 0 <= op['pc'] < len(raw) and raw[op['pc']] == 0x55]
            except (TypeError, ValueError):
                writes = None
            want = [{'key': k, 'val': v} for k, v in assertion['writes']]
            add(assertion, writes == want, f'Expected root SSTORE effects {want}, got {writes}.')
    return checks


def assess(case, observation, peers):
    """Exact mined-probe checks for the topics the case declares."""
    context = case.get('context', {})
    probes = context.get('probes')
    topics = set(case.get('topics', []))
    if not probes or not topics or observation.get('status') != 'result':
        return []
    request = case['request']
    method, params = request['method'], request.get('params', [])
    result = obj(observation.get('response')).get('result')
    checks = []
    if method == 'trace_filter':
        if 'expected_frames' in case:
            got = [[obj(f).get('transactionHash'), obj(f).get('traceAddress'), obj(f).get('type')] for f in seq(result)]
            checks.append({'topic': case['topics'][0], 'status': 'matches' if isinstance(result, list) and got == case['expected_frames'] else 'change_needed',
                           'requirement': case['requirement'], 'detail': f'Expected {case["expected_frames"]}, got {got}.'})
        return checks
    blocks = context.get('_blocks', {})
    if method in ['trace_replayTransaction', 'trace_transaction']:
        hashes = [params[0]] if params and params[0] in probes else []
    elif method in ['trace_replayBlockTransactions', 'trace_block']:
        hashes = [t['hash'] for t in obj(blocks.get(params[0] if params else None)).get('transactions', [])]
    else:
        return []
    selection = set(params[1]) if method.startswith('trace_replay') and len(params) > 1 and isinstance(params[1], list) else {'trace'}
    for i, txhash in enumerate(hashes):
        if method == 'trace_replayBlockTransactions':
            envelopes = seq(result)
            envelope = obj(envelopes[i]) if i < len(envelopes) else {}
            if envelope.get('transactionHash') != txhash:
                envelope = {}  # A replay envelope must identify its transaction; H07 reports order.
        elif method == 'trace_replayTransaction':
            envelope = obj(result)
        else:
            envelope = None
        if envelope is not None:
            frames = [f for f in seq(envelope.get('trace')) if isinstance(f, dict)]
        else:
            frames = [f for f in seq(result) if isinstance(f, dict) and f.get('transactionHash') == txhash]
        checks += assess_transaction(probes[txhash], topics, envelope, frames, selection)
    return checks

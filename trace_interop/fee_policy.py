"""Independent H15 oracles for the frozen, empty-block Prague chain.

No trace response supplies expected gas or balances. Tiny creation programs make
upfront payment and prior-call settlement observable even without stateDiff.
"""
from .execution_models import balance_delta, created_address, quantity
from .vm_model import intrinsic

SENDER = '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf'
MINER = '0x' + '00' * 20
EMPTY = '0x' + '00' * 18 + '4444'
BALANCE = 10**18
GAS = 200_000
PROGRAMS = {
    # Seven words: gas price, base fee, number, timestamp, gas limit,
    # CALLER BALANCE (after upfront payment/value), COINBASE BALANCE (before tip).
    'environment': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3',
    'refund': '0x6001600055600060005560006000f3',
    'revert': '0x602a60005260206000fd',
    'out-of-gas': '0x63ffffffff51',
}


def gas_used(program, gas_limit=GAS):
    if program == 'transfer':
        return 21000
    if program == 'out-of-gas':
        return gas_limit
    initial = intrinsic(PROGRAMS[program], True)
    if program == 'environment':
        # Five 2-gas reads, two warm BALANCE reads (CALLER/COINBASE),
        # seven PUSH/MSTORE pairs, seven new memory words and RETURN pushes.
        return initial + 5*2 + 2*(2+100) + 7*6 + 7*3 + 6 + 224*200
    if program == 'revert':
        return initial + 18
    # Cold zero->one SSTORE (22100), warm dirty reset (100), six PUSH1s.
    # Reset-to-original refund is 19900, limited to 1/5 of spent gas (EIP-3529).
    spent = initial + 22100 + 100 + 18
    return spent - min(19900, spent//5)


def expected_steps(case):
    """Compute execution expectations from requests and frozen header/prestate."""
    params = case['request']['params']
    pairs = params[0] if case['request']['method'] == 'trace_callMany' else [[params[0], params[1]]]
    env = case['context']['_environment']
    base = env['BASEFEE']
    sender_balance = BALANCE
    miner_balance = 0
    nonce = 10
    steps = []
    for (call, modes), program in zip(pairs, case['fee_policy']['programs'], strict=True):
        sender = call['from']
        if sender != SENDER:
            before, tx_nonce = 0, 0
        else:
            before, tx_nonce = sender_balance, nonce
        cap = int(call.get('gasPrice', call.get('maxFeePerGas', '0x0')), 16)
        tip_cap = int(call.get('gasPrice', call.get('maxPriorityFeePerGas', '0x0')), 16)
        price = min(cap, base + tip_cap)
        gas_limit = int(call['gas'], 16)
        value = int(call.get('value', '0x0'), 16)
        used = gas_used(program, gas_limit)
        failed = program in ['revert', 'out-of-gas']
        sent = 0 if failed else value
        paid = used * price
        tip = used * max(price-base, 0)
        output = '0x'
        if program == 'environment':
            words = [price, base, env['NUMBER'], env['TIMESTAMP'], env['GASLIMIT'],
                     before-gas_limit*price-value, miner_balance]
            output += ''.join(f'{word:064x}' for word in words)
        elif program == 'revert':
            output += f'{42:064x}'
        recipient = call.get('to') or created_address(sender, tx_nonce)
        steps.append(dict(output=output, modes=modes, failed=failed, used=used,
                          sender=sender, before=before, after=before-paid-sent,
                          nonce=tx_nonce, miner_before=miner_balance, miner_after=miner_balance+tip,
                          recipient=recipient, sent=sent, burn=used*min(price, base)))
        if sender == SENDER:
            sender_balance = before-paid-sent
            nonce += 1
        miner_balance += tip
    return steps


def assess(case, observation):
    policy = case.get('fee_policy')
    if not policy:
        return []
    checks = []
    def add(ok, requirement, detail=''):
        checks.append(dict(topic='H15', status='matches' if ok else 'change_needed',
                           requirement=requirement, detail=detail))
    if policy['admission'] == 'observe':
        return [dict(topic='H15', status='unassessed', requirement='Observe unresolved fee defaults.',
                     detail='Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.')]
    status = observation.get('status')
    if status not in ['result', 'rpc_error']:
        return [dict(topic='H15', status='blocked', requirement='Inspect the fee-policy response.', detail=str(status))]
    response = observation.get('response', {})
    if policy['admission'] == 'reject':
        error = response.get('error', {})
        # Do not credit internal/parse/method-not-found errors as fee validation.
        add(status == 'rpc_error' and error.get('code') in [-32000, -32003, -32602],
            'Reject this independently invalid fee/funding request before execution.', policy['reason'])
        return checks
    result = response.get('result')
    envelopes = result if case['request']['method'] == 'trace_callMany' else [result]
    steps = expected_steps(case)
    admitted = status == 'result' and isinstance(envelopes, list) and len(envelopes) == len(steps) and all(
        isinstance(e, dict) and 'output' in e and 'error' not in e for e in envelopes)
    add(admitted, 'Execute each valid simulation and return one envelope per call.')
    if not admitted:
        return checks
    def account_bounds(account, before, after, field='balance'):
        change = account.get(field, '=')
        if before == after:
            return change == '=' or change == {'+': hex(after)} or change == {'*': {'from': hex(before), 'to': hex(after)}}
        if change == {'+': hex(after)}:
            return before == 0
        pair = change.get('*') if isinstance(change, dict) else None
        return isinstance(pair, dict) and quantity(pair.get('from')) == before and quantity(pair.get('to')) == after
    for i, (envelope, step) in enumerate(zip(envelopes, steps, strict=True)):
        add(envelope.get('output') == step['output'],
            f'Call {i}: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE.',
            f'Expected output {step["output"]}; independently charged gas {step["used"]}.')
        if 'trace' in step['modes']:
            trace = envelope.get('trace')
            roots = [f for f in trace if isinstance(f, dict) and f.get('traceAddress') == []] if isinstance(trace, list) else []
            add(len(roots) == 1 and bool(roots[0].get('error')) == step['failed'],
                f'Call {i}: distinguish admission from the known execution success/failure.')
        if 'stateDiff' not in step['modes']:
            continue
        diff = envelope.get('stateDiff')
        if not isinstance(diff, dict) or any(not isinstance(a, dict) for a in diff.values()):
            add(False, f'Call {i}: return the requested stateDiff.')
            continue
        sender = diff.get(step['sender'], {})
        miner = diff.get(MINER, {})
        deltas = [balance_delta(a.get('balance', '=')) for a in diff.values()]
        add(account_bounds(sender, step['before'], step['after'])
            and account_bounds(sender, step['nonce'], step['nonce']+1, 'nonce')
            and account_bounds(miner, step['miner_before'], step['miner_after'])
            and (not step['sent'] or balance_delta(diff.get(step['recipient'], {}).get('balance', '=')) == step['sent'])
            and all(d is not None for d in deltas) and sum(deltas) == -step['burn'],
            f'Call {i}: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.',
            f'Sender {step["before"]}->{step["after"]}; miner {step["miner_before"]}->{step["miner_after"]}; burn {step["burn"]}.')
    return checks

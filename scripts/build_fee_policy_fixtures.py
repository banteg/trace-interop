"""Generate H15 fee boundaries, funding and selection-independent settlement probes."""
from itertools import combinations
from pathlib import Path

from trace_interop.cli import read, write, sha
from trace_interop.fee_policy import SENDER, MINER, EMPTY, BALANCE, GAS, PROGRAMS

ROOT = Path(__file__).resolve().parents[1]


def build():
    head = read(ROOT/'fixtures/chains/raw-validation/headblock.json')
    base = int(head['baseFeePerGas'], 16)
    cases = []
    def add(name, method, params, **extra):
        cases.append(dict(name=name, request=dict(jsonrpc='2.0', id=1, method=method, params=params), **extra))
    for label, address, balance, nonce in [('sender', SENDER, BALANCE, 10), ('miner', MINER, 0, 0), ('empty', EMPTY, 0, 0)]:
        for field, method, expected in [('balance', 'eth_getBalance', hex(balance)), ('nonce', 'eth_getTransactionCount', hex(nonce)), ('code', 'eth_getCode', '0x')]:
            add('_control/'+label+'-'+field, method, [address, 'latest'], expected_control=expected)
    def legacy(price):
        return dict(gasPrice=hex(price))
    def typed(cap, tip):
        return dict(maxFeePerGas=hex(cap), maxPriorityFeePerGas=hex(tip))
    def call(fees, program='environment', **extra):
        tx = dict(from_=SENDER, gas=hex(GAS), value='0x7', **fees)
        tx['from'] = tx.pop('from_')
        if program == 'transfer':
            tx.update(to=EMPTY, data='0x')
        else:
            tx['data'] = PROGRAMS[program]
        tx.update(extra)
        return tx
    variants = [
        ('legacy-zero', legacy(0), 'accept'),
        ('legacy-one', legacy(1), 'reject'),
        ('legacy-below-base', legacy(base-1), 'reject'),
        ('legacy-at-base', legacy(base), 'accept'),
        ('legacy-above-base', legacy(base+1), 'accept'),
        ('typed-zero', typed(0, 0), 'accept'),
        ('typed-one', typed(1, 0), 'reject'),
        ('typed-below-base', typed(base-1, 0), 'reject'),
        ('typed-below-base-positive-tip', typed(base-1, 1), 'reject'),
        ('typed-at-base', typed(base, 0), 'accept'),
        ('typed-tip-equals-cap', typed(base, base), 'accept'),
        ('typed-zero-tip', typed(2*base, 0), 'accept'),
        ('typed-tip-limited', typed(2*base, 1), 'accept'),
        ('typed-cap-limited', typed(base+1, base), 'accept'),
        ('typed-tip-over-cap', typed(base, base+1), 'reject'),
        ('typed-zero-cap-positive-tip', typed(0, 1), 'reject'),
    ]
    selections = [list(c) for n in range(4) for c in combinations(['trace', 'stateDiff', 'vmTrace'], n)]
    def emit(name, calls, programs, admission='accept', reason='', both=False):
        for modes in selections:
            suffix = '-'.join(modes) or 'none'
            policy = dict(admission=admission, programs=programs, reason=reason)
            if both:
                add(name+'/call/'+suffix, 'trace_call', [calls[0], modes, 'latest'], fee_policy=policy)
            add(name+'/many/'+suffix, 'trace_callMany', [[[tx, modes] for tx in calls], 'latest'], fee_policy=policy)
    for name, fees, admission in variants:
        emit(name, [call(fees)], ['environment'], admission, 'Positive cap/price below BASEFEE or priority cap above total cap.', both=True)
    for family, fees in [('legacy', legacy(base+1)), ('typed', typed(2*base, 1)), ('free', legacy(0)), ('typed-free', typed(0, 0))]:
        cap = int(fees.get('gasPrice', fees.get('maxFeePerGas')), 16)
        for offset, label in [(0, 'exact'), (1, 'short')]:
            # One wei either side of value + gasLimit * feeCap affordability.
            tx = call(fees, value=hex(BALANCE-GAS*cap+offset))
            emit('funding-'+family+'-'+label, [tx], ['environment'], 'accept' if offset == 0 else 'reject',
                 'Value plus the applicable maximum upfront gas commitment exceeds sender balance.', both=True)
    emit('funding-typed-effective-only', [call(typed(2*base, 1), value=hex(BALANCE-GAS*(base+1)))],
         ['environment'], 'reject', 'Affordable at effective price, but not at the EIP-1559 fee cap.', both=True)
    for price, label in [(0, 'free'), (base+1, 'priced')]:
        emit('empty-sender-'+label, [call(legacy(price), **{'from': EMPTY, 'value': '0x0'})], ['environment'],
             'accept' if price == 0 else 'reject', 'An unfunded sender cannot afford positive gas fees.', both=True)
    for family, free, priced in [('legacy', legacy(0), legacy(base+1)), ('typed', typed(0, 0), typed(2*base, 1))]:
        for label, sequence in [('free-priced-free', [free, priced, free]), ('priced-free-priced', [priced, free, priced])]:
            emit(f'mixed-{family}-{label}', [call(fees) for fees in sequence], ['environment']*3)
        invalid = legacy(base-1) if family == 'legacy' else typed(base-1, 0)
        for label, sequence in [('free-then-invalid', [free, invalid]), ('invalid-then-free', [invalid, free])]:
            emit(f'mixed-{family}-{label}', [call(fees) for fees in sequence], ['environment']*2,
                 'reject', 'A free call does not exempt another call from fee validation.')
        for index, modes in enumerate(selections):
            # The preceding calls request different components, including none.
            pairs = [[call(fees), selections[(index+offset)%8]] for offset, fees in enumerate([priced, free, priced])]
            add(f'mixed-{family}-selections/many/'+('-'.join(modes) or 'none'), 'trace_callMany', [pairs, 'latest'],
                fee_policy=dict(admission='accept', programs=['environment']*3, reason=''))
        for program in ['refund', 'revert', 'out-of-gas']:
            emit(f'{family}-{program}', [call(priced, program)], [program], both=True)
            emit(f'{family}-{program}-then-observe', [call(priced, program), call(priced)], [program, 'environment'])
    # A second call affordable before, but not after, the first call's fee debit.
    first = call(legacy(base+1), 'transfer', value='0x0')
    second = call(legacy(base+1), 'transfer', value=hex(BALANCE-GAS*(base+1)))
    emit('sequential-funding', [first, second], ['transfer', 'transfer'], 'reject',
         'Second call funding must use the post-fee balance of the first call.')
    # Omitted fee fields default to zero, as in eth_call and eth_simulateV1.
    for name, fees, admission in [('omitted', {}, 'accept'), ('cap-only-zero', {'maxFeePerGas':'0x0'}, 'accept'),
                                  ('cap-only-positive', {'maxFeePerGas':hex(2*base)}, 'accept'),
                                  ('tip-only-zero', {'maxPriorityFeePerGas':'0x0'}, 'accept'),
                                  ('tip-only-positive', {'maxPriorityFeePerGas':'0x1'}, 'reject')]:
        emit('defaults-'+name, [call(fees)], ['environment'], admission,
             'The omitted fee cap defaults to zero, below the supplied priority fee.' if admission == 'reject' else '', both=True)
    return dict(description='H15 unsigned fee policy on the frozen Prague chain; all eight trace selections. Omitted fee fields default to zero.', cases=cases)


if __name__ == '__main__':
    write(ROOT/'fixtures/corpora/fee-policy.json', build())
    checksums = read(ROOT/'fixtures/checksums.json')
    checksums['corpora/fee-policy.json'] = sha(ROOT/'fixtures/corpora/fee-policy.json')
    write(ROOT/'fixtures/checksums.json', checksums)

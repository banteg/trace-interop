"""Generate the mined-probes corpus with independently derived expectations.

The chain comes from fixtures/generators/mined_probes_test.go; txinfo.json only names
each transaction's role. Every expected value below is derived from the frozen chain
bytes, genesis and the probe programs: header fields, recovered senders, hand-counted
opcode gas, EIP-3529 refunds and EIP-4844 blob fees. No client response is an input.
"""
from pathlib import Path

from trace_interop.chain_model import load_chain
from trace_interop.cli import read, sha, write
from trace_interop.execution_models import created_address
from trace_interop.vm_model import execute, intrinsic

ROOT = Path(__file__).resolve().parents[1]
CHAIN = ROOT/'fixtures/chains/mined-probes'
SENDER = '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf'  # public fixture key 1
BEACON_ROOTS = '0x000f3df6d732807ef1319fb7b8bb8522d0beac02'
HISTORY = '0x0000f90827f1c53a10cb7a02335b175320002935'
BEACON_READER, HISTORY_READER = '0x'+'0'*36+'4788', '0x'+'0'*36+'2935'
FACTORY, DESTRUCT = '0x'+'0'*36+'fac0', '0x'+'0'*36+'de57'
REFUND, REFUND_CAPPED = '0x'+'0'*36+'5501', '0x'+'0'*36+'5502'
DELEGATE_A, DELEGATE_B = '0x'+'0'*35+'7702a', '0x'+'0'*35+'7702b'
BLOB_RECIPIENT = '0x'+'0'*36+'b10b'
REVERT_INIT, DESTROY_INIT = '0x63deadbeef5f526004601cfd', '0x30ff'
BLOB_GAS_PER_BLOB, BEACON_RING = 131072, 8191


def word(value):
    return '0x'+f'{value:064x}'


def fake_exponential(factor, numerator, denominator):
    """EIP-4844 blob base fee approximation."""
    i, output, accumulator = 1, 0, factor*denominator
    while accumulator > 0:
        output += accumulator
        accumulator = accumulator*numerator//(denominator*i)
        i += 1
    return output//denominator


def memory_expansion(words):
    return 3*words + words*words//512


def factory_execution(initcode, child):
    """Gas of the factory program 365f5f37365f34f05f5260205ff3 around one CREATE child.

    CALLDATASIZE PUSH0 PUSH0, CALLDATACOPY (3 + 3/word + expansion), CALLDATASIZE PUSH0
    CALLVALUE, CREATE (32000 + 2/initcode word; the child's unused gas returns), then PUSH0
    MSTORE (memory already expanded) PUSH1 PUSH0 RETURN.
    """
    words = (len(bytes.fromhex(initcode[2:]))+31)//32
    return 6 + 3+3*words+memory_expansion(words) + 6 + 32000+2*words + child + 2+3+3+2


# SELFDESTRUCT to its own (warm, non-empty) address costs 5000, after ADDRESS (2).
DESTROY_SELF = 2 + 5000


def receipt_gas(tx, execution, refund=0):
    """Prague receipt gas: EIP-3529 capped refund, then the EIP-7623 calldata floor."""
    data = bytes.fromhex(tx['data'][2:])
    spent = intrinsic(tx['data'], tx['to'] is None) + execution
    floor = 21000 + 10*sum(1 if b == 0 else 4 for b in data)
    return max(spent - min(refund, spent//5), floor)


def corpus():
    """The corpus derived from the frozen chain; building it twice gives identical bytes."""
    genesis = read(CHAIN/'genesis.json')
    alloc = {'0x'+a.removeprefix('0x').lower(): v for a, v in genesis['alloc'].items()}
    blocks = load_chain(CHAIN/'chain.rlp')
    info = read(CHAIN/'txinfo.json')['trace-mined-probes']
    authorities = info.pop('authorities')
    txs, where = {}, {}
    for role, entry in info.items():
        block = blocks[entry['block']]
        tx = block['transactions'][entry['indexInBlock']]
        if tx['hash'] != entry['txhash'] or tx['sender'] != SENDER:
            raise ValueError(f'txinfo does not match the frozen chain: {role}')
        txs[role], where[role] = tx, block
    miner = blocks['0x1']['miner']
    if miner in alloc:
        raise ValueError('the first fee payment must create the fee recipient')

    probes, anchors, destroyed, cases = {}, {}, {}, []

    def case(name, method, params, **extra):
        cases.append({'name': name, 'request': {'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}, **extra})

    def assertion(role, topic, kind, requirement, **fields):
        probes.setdefault(txs[role]['hash'], {'role': role, 'assertions': []})['assertions'].append(
            dict(topic=topic, kind=kind, requirement=requirement, **fields))

    def frame(role, topic, requirement, trace_address, kind, action, error=None, **fields):
        assertion(role, topic, 'frame', requirement, traceAddress=trace_address, type=kind, action=action, error=error, **fields)

    def price(role):
        tx, block = txs[role], where[role]
        paid = min(tx['price_cap'], block['base_fee']+tx['tip_cap'])
        return paid, paid-block['base_fee']

    def fees(role, gas, value=0, blob=0, topic='H16'):
        paid, tip = price(role)
        assertion(role, topic, 'delta', 'The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once.',
                  address=SENDER, balance=-(value+gas*paid+blob), nonce=1)
        assertion(role, topic, 'delta', 'The fee recipient gains exactly the priority fee on the receipt gas.',
                  address=miner, balance=gas*tip, nonce=0)

    def receipt(role, **fields):
        case('_control/receipt-'+role, 'eth_getTransactionReceipt', [txs[role]['hash']],
             expected_control_fields={'transactionHash': txs[role]['hash'], 'blockHash': where[role]['hash'], **fields})

    def unchanged(storage):
        return {'balance': '=', 'nonce': '=', 'code': '=', 'storage': storage}

    def changed(before, after):
        return {'*': {'from': before, 'to': after}}

    # Block 1: one-blob transfer to an absent recipient; the first fee payment creates the miner.
    blob_price = fake_exponential(1, blocks['0x1']['excess_blob_gas'], genesis['config']['blobSchedule']['prague']['baseFeeUpdateFraction'])
    _, blob_tip = price('blob-transfer')
    receipt('blob-transfer', status='0x1', gasUsed=hex(21000), blobGasUsed=hex(BLOB_GAS_PER_BLOB), blobGasPrice=hex(blob_price))
    fees('blob-transfer', 21000, value=7, blob=BLOB_GAS_PER_BLOB*blob_price)
    for address, balance in [(BLOB_RECIPIENT, 7), (miner, 21000*blob_tip)]:
        assertion('blob-transfer', 'H17', 'account', 'An absent account funded by the transaction is born with balance, zero nonce and empty code markers.',
                  address=address, diff={'balance': {'+': hex(balance)}, 'nonce': {'+': '0x0'}, 'code': {'+': '0x'}, 'storage': {}})

    # Block 2: reads of the block's own pre-transaction EIP-4788 and EIP-2935 writes.
    block2 = blocks['0x2']
    root, parent = int(block2['parent_beacon_root'], 16), int(block2['parent_hash'], 16)
    for role, reader, system, argument, value in [('beacon-root-read', BEACON_READER, BEACON_ROOTS, block2['timestamp'], root),
                                                  ('history-read', HISTORY_READER, HISTORY, block2['number']-1, parent)]:
        receipt(role, status='0x1')
        requirement = 'Replay applies the block’s pre-transaction system call, so the read returns the value the block stored.'
        assertion(role, 'H28', 'output', requirement, value=word(value))
        assertion(role, 'H28', 'account', requirement+' The reader records STATICCALL success and the word in slots 1 and 0.',
                  address=reader, diff=unchanged({word(0): changed(word(0), word(value)), word(1): changed(word(0), word(1))}))
        for other in [BEACON_ROOTS, HISTORY]:
            assertion(role, 'H28', 'account', 'Block-level system writes belong to no transaction’s stateDiff.', address=other, diff=None)
        assertion(role, 'H28', 'tree', 'The reader makes one STATICCALL to the system contract.', frames=[[[], 'call'], [[0], 'call']])
        frame(role, 'H28', requirement, [0], 'call', {'from': reader, 'to': system, 'callType': 'staticcall', 'input': word(argument)},
              output=word(value))
        frame(role, 'H28', requirement, [], 'call', {'from': SENDER, 'to': reader, 'callType': 'call', 'value': '0x0'}, output=word(value))
        assertion(role, 'H28', 'store', 'The vmTrace SSTOREs write the observed success flag and word.', writes=[['0x1', '0x1'], ['0x0', hex(value)]])
    case('_control/beacon-reader-root', 'eth_getStorageAt', [BEACON_READER, '0x0', 'latest'], expected_control=word(root))
    case('_control/beacon-reader-success', 'eth_getStorageAt', [BEACON_READER, '0x1', 'latest'], expected_control=word(1))
    case('_control/beacon-buffer-root', 'eth_getStorageAt', [BEACON_ROOTS, hex(block2['timestamp'] % BEACON_RING + BEACON_RING), 'latest'], expected_control=word(root))
    case('_control/history-reader-hash', 'eth_getStorageAt', [HISTORY_READER, '0x0', 'latest'], expected_control=word(parent))
    case('_control/history-reader-success', 'eth_getStorageAt', [HISTORY_READER, '0x1', 'latest'], expected_control=word(1))
    case('_control/history-buffer-parent', 'eth_getStorageAt', [HISTORY, hex((block2['number']-1) % BEACON_RING), 'latest'], expected_control=word(parent))

    # Block 3: a reverted top-level CREATE and a factory whose nested CREATE reverts.
    revert_steps, revert_output, reverted = execute(REVERT_INIT, 10**6)
    assert reverted and revert_output == '0xdeadbeef'
    revert_gas = 10**6 - revert_steps['ops'][-1]['ex']['used']
    failed = {'gasUsed': hex(revert_gas), 'output': revert_output}
    tx = txs['create-revert']
    would_be = created_address(SENDER, tx['nonce'])
    gas = receipt_gas(tx, revert_gas)
    receipt('create-revert', status='0x0', gasUsed=hex(gas))
    fees('create-revert', gas)
    assertion('create-revert', 'H09', 'tree', 'A reverted top-level CREATE is one failed create frame.', frames=[[[], 'create']])
    frame('create-revert', 'H09', 'A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas.',
          [], 'create', {'from': SENDER, 'value': '0x0', 'gas': hex(tx['gas']-intrinsic(tx['data'], True)), 'init': REVERT_INIT},
          error='Reverted', result=failed)
    assertion('create-revert', 'H09', 'output', 'Replay output carries the revert bytes.', value=revert_output)
    assertion('create-revert', 'H17', 'account', 'The would-be address of a reverted CREATE is absent at both endpoints and has no account diff.',
              address=would_be, diff=None)

    tx = txs['factory-create-revert']
    nested = created_address(FACTORY, int(alloc[FACTORY]['nonce'], 16))
    execution = factory_execution(REVERT_INIT, revert_gas)
    gas = receipt_gas(tx, execution)
    receipt('factory-create-revert', status='0x1', gasUsed=hex(gas))
    fees('factory-create-revert', gas)
    assertion('factory-create-revert', 'H09', 'tree', 'The factory call contains its failed nested create frame.', frames=[[[], 'call'], [[0], 'create']])
    frame('factory-create-revert', 'H09', 'The handled nested failure leaves the root successful; root gasUsed is its execution gas, action.gas excludes intrinsic gas.',
          [], 'call', {'from': SENDER, 'to': FACTORY, 'callType': 'call', 'value': '0x0', 'input': REVERT_INIT,
                       'gas': hex(tx['gas']-intrinsic(tx['data']))}, result={'gasUsed': hex(execution), 'output': word(0)})
    frame('factory-create-revert', 'H09', 'A reverted nested CREATE reports error Reverted and result {gasUsed, output} without address or code.',
          [0], 'create', {'from': FACTORY, 'value': '0x0', 'init': REVERT_INIT}, error='Reverted', result=failed)
    assertion('factory-create-revert', 'H17', 'account', 'The would-be address of a reverted nested CREATE has no account diff.', address=nested, diff=None)
    assertion('factory-create-revert', 'H16', 'account', 'The creator’s nonce increment survives its child’s REVERT.',
              address=FACTORY, diff={'balance': '=', 'nonce': changed('0x1', '0x2'), 'code': '=', 'storage': {}})
    block3 = [txs['create-revert']['hash'], txs['factory-create-revert']['hash']]
    for name, filt, expected, requirement in [
            ('failed-create-recipient', {'toAddress': [would_be]}, [], 'A failed top-level CREATE has no created-address match.'),
            ('failed-nested-create-recipient', {'toAddress': [nested]}, [], 'A failed nested CREATE has no created-address match.'),
            ('failed-create-creator', {'fromAddress': [SENDER]}, [[block3[0], [], 'create'], [block3[1], [], 'call']],
             'A failed CREATE still matches its creator.'),
            ('failed-nested-create-creator', {'fromAddress': [FACTORY]}, [[block3[1], [0], 'create']], 'A failed nested CREATE matches its creating contract.'),
            ('failed-create-union', {'fromAddress': [FACTORY], 'toAddress': [nested], 'mode': 'union'}, [[block3[1], [0], 'create']],
             'Union mode retains the creator match of a failed CREATE.'),
            ('failed-create-intersection', {'fromAddress': [FACTORY], 'toAddress': [nested]}, [],
             'A failed CREATE has no recipient side, so an intersection with its would-be address is empty.')]:
        case('filter-'+name, 'trace_filter', [dict(fromBlock='0x3', toBlock='0x3', **filt)], topics=['H23'],
             expected_frames=expected, requirement=requirement)

    # Block 4: EIP-6780 SELFDESTRUCT to self, of a pre-existing contract and in the creating transaction.
    destruct = alloc[DESTRUCT]
    receipt('selfdestruct-self', status='0x1', gasUsed=hex(receipt_gas(txs['selfdestruct-self'], DESTROY_SELF)))
    fees('selfdestruct-self', receipt_gas(txs['selfdestruct-self'], DESTROY_SELF))
    assertion('selfdestruct-self', 'H26', 'tree', 'SELFDESTRUCT emits one suicide frame under the call.', frames=[[[], 'call'], [[0], 'suicide']])
    frame('selfdestruct-self', 'H26', 'The suicide frame records the contract’s whole balance transferred to itself.',
          [0], 'suicide', {'address': DESTRUCT, 'refundAddress': DESTRUCT, 'balance': destruct['balance']})
    assertion('selfdestruct-self', 'H26', 'account', 'A pre-existing contract survives SELFDESTRUCT after Cancun with its balance, code and storage, so it has no account diff.',
              address=DESTRUCT, diff=None)
    case('_control/destruct-code', 'eth_getCode', [DESTRUCT, 'latest'], expected_control=destruct['code'])
    case('_control/destruct-balance', 'eth_getBalance', [DESTRUCT, 'latest'], expected_control=destruct['balance'])
    case('_control/destruct-storage', 'eth_getStorageAt', [DESTRUCT, '0x1', 'latest'], expected_control=destruct['storage'][word(1)])
    factory_nonce = int(alloc[FACTORY]['nonce'], 16)+1
    for role in ['create-destroy-absent', 'create-destroy-prefunded']:
        tx = txs[role]
        child = created_address(FACTORY, factory_nonce)
        prefund = int(alloc.get(child, {}).get('balance', '0x0'), 16)
        if (role == 'create-destroy-prefunded') != bool(prefund):
            raise ValueError('prefunded creation address does not match the genesis design')
        execution = factory_execution(DESTROY_INIT, DESTROY_SELF)
        gas = receipt_gas(tx, execution)
        receipt(role, status='0x1', gasUsed=hex(gas))
        fees(role, gas, value=tx['value'])
        destroyed[tx['hash']] = tx['value']+prefund
        assertion(role, 'H26', 'tree', 'The creation and its SELFDESTRUCT both appear.', frames=[[[], 'call'], [[0], 'create'], [[0, 0], 'suicide']])
        frame(role, 'H26', 'The factory call returns the created address word.', [], 'call',
              {'from': SENDER, 'to': FACTORY, 'value': hex(tx['value']), 'input': DESTROY_INIT}, result={'gasUsed': hex(execution), 'output': word(int(child, 16))})
        frame(role, 'H26', 'The creation succeeds with empty code before destroying itself.', [0], 'create',
              {'from': FACTORY, 'value': hex(tx['value']), 'init': DESTROY_INIT}, result={'address': child, 'code': '0x', 'gasUsed': hex(DESTROY_SELF)})
        frame(role, 'H26', 'The suicide frame transfers the new contract’s whole balance, including any prefunded wei, to itself.',
              [0, 0], 'suicide', {'address': child, 'refundAddress': child, 'balance': hex(tx['value']+prefund)})
        if prefund:
            assertion(role, 'H26', 'account', 'A prefunded address destroyed in its creating transaction is a deletion: - markers for its pre-state and storage {}.',
                      address=child, diff={'balance': {'-': hex(prefund)}, 'nonce': {'-': '0x0'}, 'code': {'-': '0x'}, 'storage': {}})
        else:
            assertion(role, 'H26', 'account', 'An account created and destroyed in one transaction is absent at both endpoints and has no account diff.',
                      address=child, diff=None)
        assertion(role, 'H16', 'account', 'The factory forwards the value it received, so only its nonce changes.',
                  address=FACTORY, diff={'balance': '=', 'nonce': changed(hex(factory_nonce), hex(factory_nonce+1)), 'code': '=', 'storage': {}})
        case(f'_control/{role}-balance', 'eth_getBalance', [child, 'latest'], expected_control='0x0')
        case(f'_control/{role}-code', 'eth_getCode', [child, 'latest'], expected_control='0x')
        factory_nonce += 1
    case('_control/factory-nonce', 'eth_getTransactionCount', [FACTORY, 'latest'], expected_control=hex(factory_nonce))
    destroy = [txs[r]['hash'] for r in ['selfdestruct-self', 'create-destroy-absent', 'create-destroy-prefunded']]
    absent_child = created_address(FACTORY, int(alloc[FACTORY]['nonce'], 16)+1)
    for name, filt, expected, requirement in [
            ('destroyed-recipient', {'toAddress': [absent_child]}, [[destroy[1], [0], 'create'], [destroy[1], [0, 0], 'suicide']],
             'A created-then-destroyed address matches its creation and its SELFDESTRUCT beneficiary.'),
            ('self-destruct-from', {'fromAddress': [DESTRUCT]}, [[destroy[0], [0], 'suicide']],
             'A SELFDESTRUCT matches fromAddress by its executing account.'),
            ('self-destruct-to', {'toAddress': [DESTRUCT]}, [[destroy[0], [], 'call'], [destroy[0], [0], 'suicide']],
             'A SELFDESTRUCT to self also matches toAddress as its own beneficiary.')]:
        case('filter-'+name, 'trace_filter', [dict(fromBlock='0x4', toBlock='0x4', **filt)], topics=['H23'],
             expected_frames=expected, requirement=requirement)

    # Block 5: SSTORE clears of pre-existing nonzero slots; the second refund hits the cap.
    for role, target in [('refund-clear', REFUND), ('refund-capped', REFUND_CAPPED)]:
        tx = txs[role]
        storage = {int(k, 16): int(v, 16) for k, v in alloc[target]['storage'].items()}
        steps, _, _ = execute(alloc[target]['code'], tx['gas']-intrinsic(tx['data']), environment={'STORAGE': storage})
        execution = tx['gas']-intrinsic(tx['data'])-steps['ops'][-1]['ex']['used']
        gas = receipt_gas(tx, execution, steps['refund'])
        anchors[tx['hash']] = {hex(k): hex(v) for k, v in storage.items()}
        receipt(role, status='0x1', gasUsed=hex(gas))
        fees(role, gas)
        assertion(role, 'H09', 'tree', 'The storage program is one call frame.', frames=[[[], 'call']])
        frame(role, 'H09', f'Root gasUsed is execution gas before the refund ({execution}, refund {steps["refund"]}, receipt {gas}).',
              [], 'call', {'from': SENDER, 'to': target, 'value': '0x0', 'gas': hex(tx['gas']-intrinsic(tx['data']))},
              result={'gasUsed': hex(execution), 'output': '0x'})
        assertion(role, 'H16', 'account', 'Cleared slots change from their genesis values to zero.',
                  address=target, diff=unchanged({word(k): changed(word(v), word(0)) for k, v in sorted(storage.items())}))
        for k in sorted(storage):
            case(f'_control/{role}-slot-{k}', 'eth_getStorageAt', [target, hex(k), 'latest'], expected_control=word(0))

    # Block 6: EIP-7702 tuples folded per authority.
    tx = txs['authorizations']
    receipt('authorizations', status='0x1')
    delegated = {a: '0xef0100'+a[2:] for a in [DELEGATE_A, DELEGATE_B]}
    existing, absent, restoring = (authorities[k].lower() for k in ['existing', 'absent', 'restoring'])
    if absent in alloc or alloc.get(restoring, {}).get('code') != delegated[DELEGATE_A]:
        raise ValueError('authority pre-state does not match the genesis design')
    requirement = 'Tuples fold per authority in order: two valid tuples replace A with B, the stale-nonce tuple is skipped, and the nonce advances once per applied tuple.'
    assertion('authorizations', 'H18', 'account', requirement, address=existing,
              diff={'balance': '=', 'nonce': changed('0x5', '0x7'), 'code': changed('0x', delegated[DELEGATE_B]), 'storage': {}})
    assertion('authorizations', 'H18', 'account', 'An absent authority is born with creation markers for zero balance, nonce one and its delegation.',
              address=absent, diff={'balance': {'+': '0x0'}, 'nonce': {'+': '0x1'}, 'code': {'+': delegated[DELEGATE_A]}, 'storage': {}})
    assertion('authorizations', 'H18', 'account', 'Tuples that end at the original delegation report no code change, but the nonce advances twice.',
              address=restoring, diff={'balance': '=', 'nonce': changed('0x3', '0x5'), 'code': '=', 'storage': {}})
    for label, address, code, nonce in [('existing', existing, delegated[DELEGATE_B], '0x7'), ('absent', absent, delegated[DELEGATE_A], '0x1'),
                                        ('restoring', restoring, delegated[DELEGATE_A], '0x5')]:
        case(f'_control/authority-{label}-code', 'eth_getCode', [address, 'latest'], expected_control=code)
        case(f'_control/authority-{label}-nonce', 'eth_getTransactionCount', [address, 'latest'], expected_control=nonce)
    case('_control/sender-nonce', 'eth_getTransactionCount', [SENDER, 'latest'], expected_control=hex(len(txs)))
    case('_control/blob-recipient-balance', 'eth_getBalance', [BLOB_RECIPIENT, 'latest'], expected_control='0x7')

    topics = {'blob-transfer': ['H16', 'H17'], 'beacon-root-read': ['H16', 'H28'], 'history-read': ['H16', 'H28'],
              'create-revert': ['H09', 'H16', 'H17'], 'factory-create-revert': ['H09', 'H16', 'H17'],
              'selfdestruct-self': ['H16', 'H26'], 'create-destroy-absent': ['H16', 'H26'], 'create-destroy-prefunded': ['H16', 'H26'],
              'refund-clear': ['H09', 'H16', 'H19', 'H20'], 'refund-capped': ['H09', 'H16', 'H19', 'H20'], 'authorizations': ['H16', 'H17', 'H18']}
    trace_topics = {'H09', 'H26', 'H28'}  # Families visible without stateDiff or vmTrace.
    for role, tx in txs.items():
        case('replay-'+role, 'trace_replayTransaction', [tx['hash'], ['trace', 'stateDiff', 'vmTrace']], topics=topics[role])
        if trace_topics & set(topics[role]):
            case('transaction-'+role, 'trace_transaction', [tx['hash']], topics=sorted(trace_topics & set(topics[role])))
    for number, block in blocks.items():
        roles = [r for r, t in txs.items() if where[r] is block]
        replay = sorted({t for r in roles for t in topics[r]} - {'H19', 'H20'})
        case('replay-block-'+str(block['number']), 'trace_replayBlockTransactions', [number, ['trace', 'stateDiff']], topics=replay)
        if trace_topics & set(replay):
            case('block-'+str(block['number']), 'trace_block', [number], topics=sorted(trace_topics & set(replay)))
    return {'description': 'Mined Prague probes: own-block system reads, failed and self-destructing creations, capped SSTORE refunds, '
                           'folded EIP-7702 tuples and a blob fee. Expectations derive from the frozen chain and hand-counted gas.',
            'probes': probes, 'storage_anchors': anchors, 'destroyed_wei': destroyed, 'cases': cases}


def main():
    write(ROOT/'fixtures/corpora/mined-probes.json', corpus())
    checksums = read(ROOT/'fixtures/checksums.json')
    for path in sorted([*CHAIN.iterdir(), ROOT/'fixtures/corpora/mined-probes.json', ROOT/'fixtures/generators/mined_probes_test.go']):
        checksums[str(path.relative_to(ROOT/'fixtures'))] = sha(path)
    write(ROOT/'fixtures/checksums.json', dict(sorted(checksums.items())))


if __name__ == '__main__':
    main()

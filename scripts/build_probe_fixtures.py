"""Generate probes that run on the existing frozen chains.

probes-prague (raw-validation chain): vmTrace push arity/order, store, running off the
code end, CALL/CREATE precheck failures, a CREATE2 collision, a reverted CREATE, callMany
item isolation and call-object fields. Each program is supplied as creation initcode or
deployed by an earlier callMany item, so every expectation follows from the bytecode,
the Prague gas schedule and the frozen genesis state.

probes-forks (forks chain): reward matching, pagination across block boundaries and
reward records, a reversed range, genesis and the callMany twin of the historical
beacon-root call. Expected records are decoded from the frozen chain (headers, uncles
and transactions), never taken from a client.
"""
from pathlib import Path

import rlp
from eth_hash.auto import keccak
from eth_keys import keys

from trace_interop.chain_model import load_chain
from trace_interop.cli import read, sha, write
from trace_interop.execution_models import created_address, opcodes
from trace_interop.vm_model import execute

ROOT = Path(__file__).resolve().parents[1]
OPS = {'STOP': 0x00, 'SUB': 0x03, 'ISZERO': 0x15, 'BALANCE': 0x31, 'CALLER': 0x33, 'CALLDATALOAD': 0x35,
       'CALLDATASIZE': 0x36, 'CODECOPY': 0x39, 'EXTCODESIZE': 0x3b, 'RETURNDATASIZE': 0x3d, 'POP': 0x50,
       'MSTORE': 0x52, 'SLOAD': 0x54, 'SSTORE': 0x55, 'JUMPI': 0x57, 'GAS': 0x5a, 'JUMPDEST': 0x5b,
       'TLOAD': 0x5c, 'TSTORE': 0x5d, 'DUP1': 0x80, 'SWAP1': 0x90, 'CREATE': 0xf0, 'CALL': 0xf1,
       'RETURN': 0xf3, 'CREATE2': 0xf5, 'REVERT': 0xfd, 'SELFDESTRUCT': 0xff}
NAMES = {v: k for k, v in OPS.items()}


def asm(*items):
    """Assemble mnemonics; an integer is pushed with the smallest PUSHn (n >= 1)."""
    out = ''
    for item in items:
        if isinstance(item, int):
            size = max(1, (item.bit_length()+7)//8)
            out += f'{0x5f+size:02x}' + item.to_bytes(size, 'big').hex()
        else:
            out += f'{OPS[item]:02x}'
    return out


def pcs(code, name):
    raw = bytes.fromhex(code)
    positions, i = [], 0
    while i < len(raw):
        if raw[i] == OPS[name]:
            positions.append(i)
        i += 1+(raw[i]-0x5f if 0x60 <= raw[i] <= 0x7f else 0)
    return positions


def deploy(runtime, prefix=''):
    """Initcode: run prefix, then copy the runtime appended after this loader and return it."""
    loader = 11
    assert len(runtime)//2 < 256
    return prefix + f'60{len(runtime)//2:02x}8060{len(prefix)//2+loader:02x}6000396000f3' + runtime


def word(value):
    return f'{value:064x}'


def words(*values):
    return '0x'+''.join(word(v) for v in values)


def case(cases, name, method, params, **extra):
    cases.append(dict(name=name, request={'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}, **extra))


def probe(topic, kind, requirement, **fields):
    return dict(topic=topic, kind=kind, requirement=requirement, **fields)


def prague():
    genesis = read(ROOT/'fixtures/chains/raw-validation/genesis.json')
    chain_id = genesis['config']['chainId']
    alloc = {'0x'+a.lower(): v for a, v in genesis['alloc'].items()}
    key = keys.PrivateKey((1).to_bytes(32, 'big'))  # Public fixture key 1 (docs/h13-validation.md).
    sender = key.public_key.to_checksum_address().lower()
    nonce = int(alloc[sender]['nonce'], 16)
    balance = alloc[sender]['balance']
    marker = '0x0000000000000000000000000000000000001002'  # SSTORE 42 to slot 0, return word 42.
    marker_code = alloc[marker]['code']
    assert marker_code == '0x602a600055602a60005260206000f3'
    funder = '0x0c2c51a0990aee1d73c1228de158688341557508'  # Prefunded genesis account, no code.
    assert 'code' not in alloc[funder]
    root = created_address(sender, nonce)  # Every trace_call creation below deploys here.
    empty_probe = '0x000000000000000000000000000000000000c0de'
    beneficiary = '0x000000000000000000000000000000000000beef'
    for address in [root, empty_probe, beneficiary, created_address(sender, nonce+1)]:
        assert address not in alloc
    gas, price = '0x493e0', '0x77359400'
    cases = []
    for label, address, want in [('sender', sender, {'nonce': hex(nonce), 'balance': balance, 'code': '0x'}),
                                 ('creation', root, {'nonce': '0x0', 'balance': '0x0', 'code': '0x'}),
                                 ('marker', marker, {'code': marker_code}),
                                 ('empty-probe', empty_probe, {'nonce': '0x0', 'balance': '0x0', 'code': '0x'}),
                                 ('beneficiary', beneficiary, {'balance': '0x0', 'code': '0x'}),
                                 ('funder', funder, {'code': '0x'})]:
        for field, value in want.items():
            method = {'nonce': 'eth_getTransactionCount', 'balance': 'eth_getBalance', 'code': 'eth_getCode'}[field]
            case(cases, f'_control/{label}-{field}', method, [address, 'latest'], expected_control=value)
    case(cases, '_control/marker-slot', 'eth_getStorageAt', [marker, '0x0', 'latest'], expected_control='0x'+word(0))
    case(cases, '_control/chain-id', 'eth_chainId', [], expected_control=hex(chain_id))

    def creation(code, gas=gas, **fields):
        return dict({'from': sender, 'gas': gas, 'gasPrice': price, 'data': '0x'+code}, **fields)

    # vmTrace push arity/order, store and implicit STOP (H20, H21): straight-line programs
    # the bounded VM model executes, including the creation's own fresh storage.
    vm_programs = {
        'vm-push-order': ('600160026003829190805050505050600080f3', 'push',
                          'DUPn and SWAPn push the top n+1 stack words after execution, deepest first.'),
        'vm-store': ('602a600155602a600155600254600760035d60035c600080f3', 'store',
                     'store is set by each completed SSTORE with its key and value, including an unchanged warm write; SLOAD, TSTORE and TLOAD never set it.'),
        'vm-off-end': ('600160020150', 'end',
                       'Code that runs off its end has no synthetic STOP; every pc lies inside code.'),
    }
    for name, (code, kind, requirement) in vm_programs.items():
        for suffix, modes in [('', ['trace', 'stateDiff', 'vmTrace']), ('-vm-only', ['vmTrace'])]:
            if kind != 'store' and suffix:
                continue
            case(cases, name+suffix, 'trace_call', [creation(code), modes, 'latest'],
                 model={'code': '0x'+code, 'creation': True, 'environment': False},
                 probes=[probe('H20', kind, requirement + (' Its presence does not depend on selecting stateDiff.' if kind == 'store' else ''))])

    # CALL/CREATE precheck failures and a CREATE2 collision (H29, H20 sub placement, H09 label).
    child_init = asm(0, 0, 'RETURN')  # Deploys empty code.
    create_frame = lambda path, **extra: dict({'traceAddress': path, 'type': 'create', 'subtraces': 0}, **extra)
    call_frame = lambda path: {'traceAddress': path, 'type': 'call', 'subtraces': 0, 'error': None,
                               'action': {'from': root, 'to': marker, 'value': '0x0', 'callType': 'call'},
                               'result': {'output': words(42)}}
    root_frame = lambda children, **result: {'traceAddress': [], 'type': 'create', 'subtraces': children, 'error': None,
                                             'action': {'from': sender, 'value': '0x0'}, 'result': dict({'address': root}, **result)}
    precheck = 'A CALL or CREATE that fails its balance precheck emits no frame; the next sibling keeps traceAddress [0] and the parent counts only emitted frames.'
    code = asm(0, 0, 0, 0, 1, int(marker, 16), 'GAS', 'CALL', 0, 'MSTORE',
               0, 0, 0, 0, 0, int(marker, 16), 'GAS', 'CALL', 32, 'MSTORE', 64, 0, 'RETURN')
    failed, succeeded = pcs(code, 'CALL')
    case(cases, 'precheck-call-value', 'trace_call', [creation(code), ['trace', 'vmTrace'], 'latest'], probes=[
        probe('H29', 'frames', precheck, expected=[root_frame(1), call_frame([0])]),
        probe('H29', 'outputs', 'The caller continues: the failed CALL pushes 0 and the next CALL succeeds.', expected=[words(0, 1)]),
        probe('H20', 'subs', 'The CALL whose precheck failed has sub null; the sibling that entered a frame has a sub.',
              null=[failed], object=[succeeded])])
    code = asm(int(child_init, 16), 0, 'MSTORE', 5, 27, 1, 'CREATE', 32, 'MSTORE',
               5, 27, 0, 'CREATE', 64, 'MSTORE', 64, 32, 'RETURN')
    child = created_address(root, 1)  # The failed precheck does not consume the creator nonce.
    failed, succeeded = pcs(code, 'CREATE')
    case(cases, 'precheck-create-value', 'trace_call', [creation(code), ['trace', 'vmTrace'], 'latest'], probes=[
        probe('H29', 'frames', precheck, expected=[
            root_frame(1), create_frame([0], error=None, action={'from': root, 'value': '0x0', 'init': '0x'+child_init},
                                        result={'address': child, 'code': '0x'})]),
        probe('H29', 'outputs', 'The caller continues: the failed CREATE pushes 0 and the next CREATE uses the unchanged creator nonce.',
              expected=[words(0, int(child, 16))]),
        probe('H20', 'subs', 'The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub.',
              null=[failed], object=[succeeded])])
    salt = 0x2a
    code = asm(int(child_init, 16), 0, 'MSTORE', salt, 5, 27, 0, 'CREATE2', 32, 'MSTORE',
               salt, 5, 27, 0, 'CREATE2', 64, 'MSTORE',
               0, 0, 0, 0, 0, int(marker, 16), 'GAS', 'CALL', 96, 'MSTORE', 96, 32, 'RETURN')
    child = '0x'+keccak(b'\xff'+bytes.fromhex(root[2:])+salt.to_bytes(32, 'big')+keccak(bytes.fromhex(child_init)))[12:].hex()
    action = {'from': root, 'value': '0x0', 'init': '0x'+child_init}
    # H29 owns the frame's presence and place (any error label); H09 owns the label.
    case(cases, 'create2-collision', 'trace_call', [creation(code, gas='0x4c4b40'), ['trace'], 'latest'], probes=[
        probe('H29', 'frames', 'A CREATE2 address collision emits a failed create frame with no result; the caller continues with a later sibling at [2].',
              expected=[root_frame(3), create_frame([0], error=None, action=action, result={'address': child, 'code': '0x'}),
                        create_frame([1], error='*', action=action, result=None), call_frame([2])]),
        probe('H09', 'frame', 'A CREATE2 address collision frame has error "Contract address collision".',
              select={'traceAddress': [1], 'type': 'create'}, expected={'error': 'Contract address collision'}),
        probe('H29', 'outputs', 'The collision pushes 0 and the caller continues to a successful CALL.',
              expected=[words(int(child, 16), 0, 1)])])

    # A reverted CREATE inside a call (H09): result {gasUsed, output}, never address or code.
    revert_init = asm(0xdeadbeef, 0, 'MSTORE', 4, 28, 'REVERT')
    steps = execute('0x'+revert_init, 1_000_000)[0]['ops']
    code = asm(int(revert_init, 16), 0, 'MSTORE', len(revert_init)//2, 32-len(revert_init)//2, 0, 'CREATE', 0, 'MSTORE',
               'RETURNDATASIZE', 32, 'MSTORE', 64, 0, 'RETURN')
    case(cases, 'create-reverted', 'trace_call', [creation(code), ['trace'], 'latest'], probes=[
        probe('H09', 'frames', 'A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code.',
              expected=[root_frame(1), create_frame([0], error='Reverted', action={'from': root, 'value': '0x0', 'init': '0x'+revert_init},
                                                    result={'gasUsed': hex(sum(s['cost'] for s in steps)), 'output': '0xdeadbeef'},
                                                    absent=['address', 'code'])]),
        probe('H09', 'outputs', 'The caller sees CREATE push 0 and four bytes of return data.', expected=[words(0, 4)])])

    # trace_callMany item isolation (H16, H26): each item is a separate transaction.
    def item(fields, modes=('trace',)):
        return [dict({'from': sender, 'gas': gas, 'gasPrice': price}, **fields), list(modes)]
    contract = created_address(sender, nonce)  # Deployed by item 0 of each bundle.
    runtime = '3615600b5760003560005d5b60005c60005260206000f3'  # TSTORE(0, calldata word) if any; return TLOAD(0).
    assert pcs(runtime, 'JUMPDEST') == [0x0b]
    case(cases, 'many-transient', 'trace_callMany', [[item({'data': '0x'+deploy(runtime)}),
                                                      item({'to': contract, 'data': words(42)}),
                                                      item({'to': contract, 'data': '0x'})], 'latest'], probes=[
        probe('H16', 'outputs', 'Transient storage written in one item is visible within it and reset for the next item.',
              expected=['0x'+runtime, words(42), words(0)])])
    measure_balance = asm('GAS', int(empty_probe, 16), 'BALANCE', 'POP', 'GAS', 'SWAP1', 'SUB')
    measure_sload = asm('GAS', 0, 'SLOAD', 'POP', 'GAS', 'SWAP1', 'SUB')
    runtime = (measure_balance+asm(0, 'MSTORE')+measure_balance+asm(32, 'MSTORE')
               + measure_sload+asm(64, 'MSTORE')+measure_sload+asm(96, 'MSTORE')+asm(128, 0, 'RETURN'))
    warm_up = asm(int(empty_probe, 16), 'BALANCE', 'POP', 0, 'SLOAD', 'POP')
    # PUSH 3 + BALANCE (2600 cold, 100 warm) or SLOAD (2100 cold, 100 warm) + POP 2 + GAS 2.
    case(cases, 'many-warm', 'trace_callMany', [[item({'data': '0x'+deploy(runtime, warm_up)}),
                                                 item({'to': contract, 'data': '0x'})], 'latest'], probes=[
        probe('H16', 'outputs', 'Accounts and slots warmed by one item are cold again in the next: BALANCE then SLOAD cost cold, then warm.',
              expected=['0x'+runtime, words(2607, 107, 2107, 107)])])
    runtime = asm(int(beneficiary, 16), 'SELFDESTRUCT')
    probe_code = asm(int(contract, 16), 'EXTCODESIZE', 0, 'MSTORE', int(beneficiary, 16), 'BALANCE', 32, 'MSTORE', 64, 0, 'RETURN')
    bundle = lambda modes: [[item({'data': '0x'+deploy(runtime), 'value': '0x5'}),
                             item({'to': contract, 'data': '0x'}, modes), item({'data': '0x'+probe_code})], 'latest']
    case(cases, 'many-selfdestruct', 'trace_callMany', bundle(['trace']), probes=[
        probe('H16', 'outputs', 'A contract created by an earlier item survives SELFDESTRUCT in a later item (EIP-6780): its code remains and its balance moves.',
              expected=['0x'+runtime, '0x', words(len(runtime)//2, 5)])])
    case(cases, 'many-selfdestruct-diff', 'trace_callMany', bundle(['trace', 'stateDiff']), probes=[
        probe('H26', 'account', 'SELFDESTRUCT of a contract created by an earlier item keeps the account: balance changes, code and nonce are unchanged, no deletion markers.',
              index=1, address=contract, expected={'balance': {'*': {'from': '0x5', 'to': '0x0'}}, 'code': '=', 'nonce': '='})])
    runtime = asm('GAS', 2, 0, 'SSTORE', 'GAS', 'SWAP1', 'SUB', 0, 'MSTORE', 32, 0, 'RETURN')
    # The next item rewrites slot 0 from its committed 1: clean and cold, 2100 + 2900, plus PUSH, PUSH and GAS.
    case(cases, 'many-original-value', 'trace_callMany', [[item({'data': '0x'+deploy(runtime, asm(1, 0, 'SSTORE'))}),
                                                           item({'to': contract, 'data': '0x'})], 'latest'], probes=[
        probe('H16', 'outputs', 'Each item snapshots original storage: a slot committed by the previous item is clean and cold (5000 gas), not dirty.',
              expected=['0x'+runtime, words(5008)])])

    # Call-object fields (H14): every defined field takes effect or is rejected.
    ret42, ret1 = asm(42, 0, 'MSTORE', 32, 0, 'RETURN'), asm(1, 0, 'MSTORE', 32, 0, 'RETURN')
    base = {'from': sender, 'gas': gas, 'gasPrice': price}
    effect = lambda text, output: probe('H14', 'outputs', text, expected=[output])
    case(cases, 'field-input-only', 'trace_call', [dict(base, input='0x'+ret42), ['trace'], 'latest'],
         probes=[effect('input alone supplies the initcode, which returns word 42.', words(42))])
    case(cases, 'field-data-input-equal', 'trace_call', [dict(base, data='0x'+ret42, input='0x'+ret42), ['trace'], 'latest'],
         probes=[effect('Equal data and input execute once as the initcode.', words(42))])
    case(cases, 'field-data-input-differ', 'trace_call', [dict(base, data='0x'+ret42, input='0x'+ret1), ['trace'], 'latest'],
         probes=[probe('H14', 'error', 'Disagreeing data and input are invalid params (-32602).', code=-32602)])
    sload_gas = asm('GAS', 0, 'SLOAD', 'POP', 'GAS', 'SWAP1', 'SUB', 0, 'MSTORE', 32, 0, 'RETURN')
    case(cases, 'field-access-list', 'trace_call', [dict(base, data='0x'+sload_gas, accessList=[{'address': root, 'storageKeys': ['0x'+word(0)]}]), ['trace'], 'latest'],
         probes=[effect('An access-listed slot of the creation address is warm: PUSH, SLOAD 100, POP and GAS cost 107.', words(107))])
    case(cases, 'field-access-list-absent', 'trace_call', [dict(base, data='0x'+sload_gas), ['trace'], 'latest'],
         probes=[effect('Without an access list the same SLOAD is cold: 2107.', words(2107))])
    digest = keccak(b'\x05'+rlp.encode([chain_id, bytes.fromhex(marker[2:]), nonce]))
    signature = key.sign_msg_hash(digest)
    authorization = {'chainId': hex(chain_id), 'address': marker, 'nonce': hex(nonce), 'yParity': hex(signature.v),
                     'r': hex(signature.r), 's': hex(signature.s)}
    delegated = {'from': funder, 'to': sender, 'gas': gas, 'gasPrice': price, 'data': '0x'}
    # Legacy gasPrice with an authorizationList is no transaction type, so this capture
    # records what each server does; the -1559 twins below carry the H14 assertion.
    case(cases, 'field-authorization', 'trace_call', [dict(delegated, authorizationList=[authorization]), ['trace'], 'latest'],
         probes=[dict(effect('A valid authorization delegates key 1 to the marker contract, which returns word 42.', words(42)),
                      observe='Legacy gasPrice with an authorizationList is not a representable transaction type, so a rejection, a crash or a dropped list does not isolate the authorization field; field-authorization-1559 asserts it.')])
    case(cases, 'field-authorization-absent', 'trace_call', [delegated, ['trace'], 'latest'],
         probes=[effect('Without the authorization the same call reaches an EOA and returns no bytes.', '0x')])
    typed = {'from': funder, 'to': sender, 'gas': gas, 'maxFeePerGas': price, 'maxPriorityFeePerGas': price, 'data': '0x'}
    case(cases, 'field-authorization-1559', 'trace_call', [dict(typed, authorizationList=[authorization]), ['trace'], 'latest'],
         probes=[effect('A valid authorization on an EIP-1559-priced call delegates key 1 to the marker contract, which returns word 42.', words(42))])
    case(cases, 'field-authorization-absent-1559', 'trace_call', [typed, ['trace'], 'latest'],
         probes=[effect('Without the authorization the same EIP-1559-priced call reaches an EOA and returns no bytes.', '0x')])
    caller = '0x'+asm('CALLER', 0, 'MSTORE', 32, 0, 'RETURN')
    fee_default = {'topic': 'H15', 'reason': 'The zero-address sender is unfunded, so the call runs only if its fees are zero; an error rejects the fee, not the from default.'}
    case(cases, 'field-from-omitted', 'trace_call', [{'gas': gas, 'input': caller}, ['trace'], 'latest'],
         probes=[dict(effect('An omitted from defaults to the zero address, observed by CALLER.', words(0)), depends=fee_default)])
    # Explicit zero fees (the H15 exemption) and data rather than input (H14) leave only the from default under test.
    case(cases, 'field-from-omitted-zero-fee', 'trace_call', [{'gas': gas, 'gasPrice': '0x0', 'data': caller}, ['trace'], 'latest'],
         probes=[dict(effect('An omitted from defaults to the zero address, observed by CALLER, on an explicitly zero-fee call.', words(0)), depends=fee_default)])
    gas_call = {'from': sender, 'input': '0x'+asm('GAS', 0, 'MSTORE', 32, 0, 'RETURN')}
    case(cases, 'field-gas-omitted-eth-call', 'eth_call', [gas_call, 'latest'])
    case(cases, 'field-gas-omitted', 'trace_call', [gas_call, ['trace'], 'latest'],
         probes=[probe('H14', 'same-output', 'An omitted gas runs with the server execution cap, as eth_call does: GAS reports the same value.',
                       reference='field-gas-omitted-eth-call')])
    case(cases, 'field-chain-id', 'trace_call', [dict(base, input='0x'+ret42, chainId=hex(chain_id)), ['trace'], 'latest'],
         probes=[effect('A matching chainId is accepted and the initcode returns word 42.', words(42))])
    case(cases, 'field-chain-id-mismatch', 'trace_call', [dict(base, input='0x'+ret42, chainId='0x1'), ['trace'], 'latest'],
         probes=[probe('H14', 'error', 'A chainId that does not match the chain rejects the request.'),
                 probe('H14', 'error', 'A validation failure without a listed code is invalid params (-32602).', code=-32602)])
    return {'description': 'Programs on the raw-validation chain: vmTrace push, store and code end; precheck failures, collision and reverted CREATE; callMany item isolation; call-object fields.',
                'model_nonce': nonce, 'cases': cases}


def forks():
    chain = ROOT/'fixtures/chains/forks'
    blocks = load_chain(chain/'chain.rlp')
    genesis = read(chain/'genesis.json')
    forkenv = read(chain/'forkenv.json')
    headers = {h['number']: h for h in read(chain/'headers.json')}
    codes = {'0x'+a.lower(): v.get('code', '0x') for a, v in genesis['alloc'].items()}
    coinbase = '0x'+'00'*20
    sender = '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f'
    base_reward = lambda n: (5 if n < int(forkenv['HIVE_FORK_BYZANTIUM']) else 3 if n < int(forkenv['HIVE_FORK_CONSTANTINOPLE']) else 2)*10**18

    def records(first, last):
        """Per block, the root frame of each transaction, then the block reward and uncle rewards."""
        out = []
        for n in range(first, last+1):
            block = blocks[hex(n)]
            assert block['difficulty'] > 0 and block['miner'] == coinbase
            for i, tx in enumerate(block['transactions']):
                # Only code-free or non-calling targets: each transaction is exactly its root frame.
                code = codes.get(tx['to'], '0x')
                assert tx['to'] not in [None, coinbase] and not {0xf0, 0xf1, 0xf2, 0xf4, 0xf5, 0xfa, 0xff} & set(opcodes(code)), tx
                out.append({'type': 'call', 'blockNumber': n, 'blockHash': block['hash'], 'transactionHash': tx['hash'],
                            'transactionPosition': i, 'traceAddress': [], 'subtraces': 0,
                            'action': {'from': tx['sender'], 'to': tx['to'], 'value': hex(tx['value']), 'callType': 'call'}})
            out += reward_records(n)
        return out

    def reward_records(n):
        block = blocks[hex(n)]
        reward = base_reward(n)
        rewards = [('block', block['miner'], reward+len(block['uncles'])*reward//32)]
        rewards += [('uncle', u['miner'], (u['number']+8-n)*reward//8) for u in block['uncles']]
        return [{'type': 'reward', 'blockNumber': n, 'blockHash': block['hash'], 'traceAddress': [], 'subtraces': 0,
                 'action': {'author': author, 'rewardType': kind, 'value': hex(value)}} for kind, author, value in rewards]

    to_coinbase = lambda r: r['type'] == 'reward' and r['action']['author'] == coinbase
    from_sender = lambda r: r['type'] == 'call' and r['action']['from'] == sender
    cases = []
    beacon = '0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02'
    timestamp = int(headers['0x38']['timestamp'], 16)
    history = 8191  # EIP-4788 ring buffer length.
    # Block 56 wrote the ring-buffer slots: the chain state every build must show. Block 55
    # state predates that write, which is the H28 property itself, so those reads are
    # probes, not setup controls (the names are kept for the captured requests).
    for number, stored, root in [('0x37', 0, 0), ('0x38', timestamp, int(headers['0x38']['parentBeaconBlockRoot'], 16))]:
        n = int(number, 16)
        slots = [('timestamp', hex(timestamp % history), stored), ('root', hex(timestamp % history + history), root)]
        for label, slot, value in slots:
            if value:
                case(cases, f'_control/beacon-{label}-{n}', 'eth_getStorageAt', [beacon, slot, number], expected_control='0x'+word(value))
            else:
                case(cases, f'_control/beacon-{label}-{n}', 'eth_getStorageAt', [beacon, slot, number], probes=[
                    probe('H28', 'outputs', f'State at block {n} predates block {n+1}\'s beacon-root write: the {label} slot reads zero.', expected=['0x'+word(0)])])
    rewards = [r for r in records(2, 5) if to_coinbase(r)]
    requirement = 'A reward matches toAddress by author, after its block\'s transactions: block reward, then uncle rewards in ommer order.'
    case(cases, 'rewards-to', 'trace_filter', [{'fromBlock': '0x2', 'toBlock': '0x5', 'toAddress': [coinbase]}],
         probes=[probe('H23', 'records', requirement, expected=rewards)])
    intersection = 'A reward has no from side, so an intersection with a populated fromAddress excludes it.'
    case(cases, 'rewards-intersection', 'trace_filter', [{'fromBlock': '0x2', 'toBlock': '0x5', 'fromAddress': [sender], 'toAddress': [coinbase], 'mode': 'intersection'}],
         probes=[probe('H23', 'records', intersection, expected=[],
                       depends={'topic': 'H03', 'reason': 'The request names the default mode explicitly, so a server that rejects the mode field fails before matching rewards.'})])
    # Intersection is the default: omitting mode leaves only reward matching under test.
    case(cases, 'rewards-intersection-default', 'trace_filter', [{'fromBlock': '0x2', 'toBlock': '0x5', 'fromAddress': [sender], 'toAddress': [coinbase]}],
         probes=[probe('H23', 'records', intersection+' Intersection is the default mode.', expected=[])])
    union = [r for r in records(2, 3) if to_coinbase(r) or from_sender(r)]
    case(cases, 'rewards-union', 'trace_filter', [{'fromBlock': '0x2', 'toBlock': '0x3', 'fromAddress': [sender], 'toAddress': [coinbase], 'mode': 'union'}],
         probes=[probe('H23', 'records', 'In union mode a toAddress match by author suffices for a reward; sender roots precede their block\'s rewards.', expected=union)])
    selected = [r for r in records(2, 5) if from_sender(r)]
    case(cases, 'sender-skip', 'trace_filter', [{'fromBlock': '0x2', 'toBlock': '0x5', 'fromAddress': [sender], 'after': 2, 'count': 3}],
         probes=[probe('H03', 'records', 'Filter first, then skip after matching records and take count, across block boundaries.', expected=selected[2:5])])
    selected = [r for r in records(2, 4) if to_coinbase(r) or from_sender(r)]
    case(cases, 'rewards-window', 'trace_filter', [{'fromBlock': '0x2', 'toBlock': '0x4', 'fromAddress': [sender], 'toAddress': [coinbase], 'mode': 'union', 'after': 3, 'count': 5}],
         probes=[probe('H03', 'records', 'A page over matching records crosses a block boundary and reward records in block, transaction, reward order.', expected=selected[3:8])])
    case(cases, 'range-reversed', 'trace_filter', [{'fromBlock': '0x3', 'toBlock': '0x2'}],
         probes=[probe('H06', 'error', 'An explicit fromBlock above toBlock is invalid params (-32602), as eth_getLogs does.', code=-32602)])
    genesis_requirement = 'The genesis block has no transaction or reward records.'
    case(cases, 'genesis-block', 'trace_block', ['0x0'], probes=[probe('H05', 'records', genesis_requirement, expected=[])])
    case(cases, 'genesis-replay', 'trace_replayBlockTransactions', ['0x0', ['trace']], probes=[probe('H05', 'records', genesis_requirement+' Block replay returns [].', expected=[])])
    case(cases, 'genesis-filter', 'trace_filter', [{'fromBlock': '0x0', 'toBlock': '0x0'}], probes=[probe('H05', 'records', genesis_requirement, expected=[])])
    # Block 1 only deploys contracts whose initcode makes no calls, so no frame of blocks 1-2 has the coinbase as recipient.
    assert all(tx['to'] is None and not {0xf1, 0xf2, 0xf4, 0xfa, 0xff} & set(opcodes(tx['data'])) for tx in blocks['0x1']['transactions'])
    case(cases, 'genesis-range-rewards', 'trace_filter', [{'fromBlock': '0x0', 'toBlock': '0x2', 'toAddress': [coinbase]}],
         probes=[probe('H05', 'records', 'A range from genesis contributes no genesis reward; blocks 1 and 2 contribute their block rewards.',
                       expected=reward_records(1)+reward_records(2))])
    call = {'from': sender, 'to': beacon, 'data': '0x'+word(timestamp), 'gas': '0x927c0', 'gasPrice': '0x77359400'}
    for number, output in [('0x37', '0x'), ('0x38', headers['0x38']['parentBeaconBlockRoot'])]:
        n = int(number, 16)
        case(cases, f'beacon-trace-{n}', 'trace_call', [call, ['trace'], number],
             probes=[probe('H28', 'outputs', f'trace_call at block {n} reads the beacon root of timestamp {timestamp} only if block {n} stored it.', expected=[output])])
        case(cases, f'beacon-many-{n}', 'trace_callMany', [[[call, ['trace']]], number],
             probes=[probe('H28', 'outputs', f'The first trace_callMany item at block {n} runs on the same post-block state as trace_call.', expected=[output]),
                     probe('H28', 'same-output', 'The one-item trace_callMany output equals trace_call at the same block.', reference=f'beacon-trace-{n}', index=0)])
    return {'description': 'Reward matching and pagination, reversed range, genesis and the callMany beacon-root twin on the frozen PoW-to-PoS forks chain.', 'cases': cases}


if __name__ == '__main__':
    checksums = read(ROOT/'fixtures/checksums.json')
    for name, corpus in [('probes-prague', prague()), ('probes-forks', forks())]:
        path = ROOT/'fixtures/corpora'/(name+'.json')
        write(path, corpus)
        checksums['corpora/'+name+'.json'] = sha(path)
    write(ROOT/'fixtures/checksums.json', checksums)

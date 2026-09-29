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

raw-selector (chain a): H12 state witnesses for trace_rawTransaction. One signed creation,
valid at every block, returns NUMBER, a witness account's BALANCE and BASEFEE; it is sent
with two arguments and with explicit latest, number, hash, EIP-1898 and pending selectors.
The initial corpus's signed cases gain the same probe, read from the sender's stateDiff nonce.
Candidate states and environments come from the frozen headers, genesis and transactions.

h30, reorg and reorg-safe (chain a and branch B): H33 trace_filter blockHash cases, each compared
with the numeric filter of the same block (the h30 `filter-block-2…` twins, the reorg phases'
`filter-tail`), plus genesis, conflicting, null, unknown and malformed hashes.
"""
import json
from pathlib import Path

import rlp
from eth_hash.auto import keccak
from eth_keys import keys

from trace_interop.chain_model import decode_transaction, fake_exponential, load_chain
from trace_interop.cli import read, sha, write
from trace_interop.execution_models import created_address, opcodes
from trace_interop.vm_model import execute, intrinsic

ROOT = Path(__file__).resolve().parents[1]
OPS = {'STOP': 0x00, 'SUB': 0x03, 'ADDRESS': 0x30, 'DUP6': 0x85, 'ISZERO': 0x15, 'BALANCE': 0x31, 'CALLER': 0x33, 'CALLDATALOAD': 0x35,
       'CALLDATASIZE': 0x36, 'CODECOPY': 0x39, 'EXTCODESIZE': 0x3b, 'RETURNDATASIZE': 0x3d, 'POP': 0x50,
       'NUMBER': 0x43, 'BASEFEE': 0x48, 'BLOBBASEFEE': 0x4a, 'MSTORE': 0x52, 'MSTORE8': 0x53, 'SLOAD': 0x54, 'SSTORE': 0x55, 'JUMPI': 0x57, 'GAS': 0x5a, 'JUMPDEST': 0x5b,
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
    # A precheck failure keeps its frame, as geth, Erigon, Reth and Besu debug tracers do: an error, no result and no
    # children. H29 owns the frame; H09 owns the label.
    precheck = ('A CALL or CREATE that fails its balance precheck emits a failed frame with no result and no subtraces; '
                'the next sibling follows at [1] and the parent counts both.')
    label = 'A {} that fails its balance precheck has error "Insufficient balance for transfer".'
    debug_calls = {}
    code = asm(0, 0, 0, 0, 1, int(marker, 16), 'GAS', 'CALL', 0, 'MSTORE',
               0, 0, 0, 0, 0, int(marker, 16), 'GAS', 'CALL', 32, 'MSTORE', 64, 0, 'RETURN')
    failed, succeeded = pcs(code, 'CALL')
    debug_calls['precheck-call-value'] = creation(code)
    case(cases, 'precheck-call-value', 'trace_call', [creation(code), ['trace', 'vmTrace'], 'latest'], probes=[
        probe('H29', 'frames', precheck, expected=[
            root_frame(2), {'traceAddress': [0], 'type': 'call', 'subtraces': 0, 'error': '*', 'result': None,
                            'action': {'from': root, 'to': marker, 'value': '0x1', 'callType': 'call'}},
            call_frame([1])]),
        probe('H09', 'frame', label.format('CALL'), select={'traceAddress': [0], 'type': 'call', 'action': {'value': '0x1'}},
              expected={'error': 'Insufficient balance for transfer'}),
        probe('H29', 'outputs', 'The caller continues: the failed CALL pushes 0 and the next CALL succeeds.', expected=[words(0, 1)]),
        probe('H20', 'subs', 'The CALL whose precheck failed has sub null; the sibling that entered a frame has a sub.',
              null=[failed], object=[succeeded])])
    code = asm(int(child_init, 16), 0, 'MSTORE', 5, 27, 1, 'CREATE', 32, 'MSTORE',
               5, 27, 0, 'CREATE', 64, 'MSTORE', 64, 32, 'RETURN')
    child = created_address(root, 1)  # The failed precheck does not consume the creator nonce.
    failed, succeeded = pcs(code, 'CREATE')
    debug_calls['precheck-create-value'] = creation(code)
    case(cases, 'precheck-create-value', 'trace_call', [creation(code), ['trace', 'vmTrace'], 'latest'], probes=[
        probe('H29', 'frames', precheck, expected=[
            root_frame(2), create_frame([0], error='*', action={'from': root, 'value': '0x1', 'init': '0x'+child_init}, result=None),
            create_frame([1], error=None, action={'from': root, 'value': '0x0', 'init': '0x'+child_init},
                         result={'address': child, 'code': '0x'})]),
        probe('H09', 'frame', label.format('CREATE'), select={'traceAddress': [0], 'type': 'create', 'action': {'value': '0x1'}},
              expected={'error': 'Insufficient balance for transfer'}),
        probe('H29', 'outputs', 'The caller continues: the failed CREATE pushes 0 and the next CREATE uses the unchanged creator nonce.',
              expected=[words(0, int(child, 16))]),
        probe('H20', 'subs', 'The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub.',
              null=[failed], object=[succeeded])])
    # The same calls through geth-style debug tracers: supporting references for H29, not assertions.
    for name, call in debug_calls.items():
        for tracer in ('callTracer', 'flatCallTracer'):
            case(cases, f'{name}-debug-{tracer}', 'debug_traceCall', [call, 'latest', {'tracer': tracer}])
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

    # Code the creation cannot deposit (H09 labels): above the EIP-170 size limit, beginning with 0xEF (EIP-3541),
    # or costing more deposit gas than the child has. Each halts the child, which consumes its gas; the caller keeps
    # the 1/64 it withheld and returns CREATE's 0.
    max_code_size = 0x6000
    deposit_size = 24000  # Within the size limit, at 200 gas a byte beyond the child's forwarded gas below.
    for name, init, label, requirement in [
            ('create-code-size-limit', asm(max_code_size+1, 0, 'RETURN'), 'Out of gas',
             'Code above the EIP-170 size limit fails the creation with "Out of gas", as Parity and EIP-170 report it.'),
            ('create-code-deposit-oog', asm(deposit_size, 0, 'RETURN'), 'Out of gas',
             'Code whose deposit costs more than the child\'s remaining gas fails the creation with "Out of gas".'),
            ('create-ef-prefix', asm(0xef, 0, 'MSTORE8', 1, 0, 'RETURN'), 'Invalid code',
             'Code beginning with 0xEF (EIP-3541) fails the creation with "Invalid code", as OpenEthereum reports it.')]:
        code = asm(int(init, 16), 0, 'MSTORE', len(init)//2, 32-len(init)//2, 0, 'CREATE', 0, 'MSTORE', 32, 0, 'RETURN')
        # The deposit case forwards 63/64 of about 1.3M gas, far below the 4.8M its deposit costs, while the caller
        # keeps enough for its own 32-byte deposit; the others have ample gas, so only their code fails them.
        limit = hex(intrinsic(code, True)+1_300_000) if name == 'create-code-deposit-oog' else '0x4c4b40'
        assert name != 'create-code-deposit-oog' or 200*deposit_size > 1_300_000 > 64*(200*32+100)
        case(cases, name, 'trace_call', [creation(code, gas=limit), ['trace'], 'latest'], probes=[
            probe('H09', 'frames', 'The failed creation frame has an error and no result; the caller continues.',
                  expected=[root_frame(1), create_frame([0], error='*', action={'from': root, 'value': '0x0', 'init': '0x'+init}, result=None)]),
            probe('H09', 'frame', requirement, select={'traceAddress': [0], 'type': 'create'}, expected={'error': label}),
            probe('H09', 'outputs', 'The caller sees CREATE push 0.', expected=[words(0)])])

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
         probes=[probe('H14', 'error', 'Disagreeing data and input are rejected (-32602 recommended).', recommended=-32602)])
    # An explicit null for an optional member or parameter is the same as omitting it (H14).
    nulls = dict(base, data='0x'+ret42, **dict.fromkeys(['input', 'value', 'nonce', 'maxFeePerBlobGas', 'chainId', 'type', 'accessList',
                                                        'blobVersionedHashes', 'authorizationList', 'maxFeePerGas', 'maxPriorityFeePerGas']))
    case(cases, 'field-null-members', 'trace_call', [nulls, ['trace'], 'latest'],
         probes=[effect('Explicit null members are omitted, so the initcode in data runs and returns word 42.', words(42))])
    case(cases, 'field-null-block', 'trace_call', [dict(base, data='0x'+ret42), ['trace'], None],
         probes=[effect('A null block parameter is latest.', words(42))])
    case(cases, 'callmany-null-block', 'trace_callMany', [[[dict(base, data='0x'+ret42), ['trace']]], None],
         probes=[effect('A null trace_callMany block parameter is latest.', words(42))])
    # Without fee fields nothing else selects a transaction type, so a null list must not select one either.
    unpriced = {'from': sender, 'gas': gas, 'data': '0x'+ret42}
    for member in ['accessList', 'blobVersionedHashes', 'authorizationList']:
        case(cases, f'field-null-{member}-unpriced', 'trace_call', [dict(unpriced, **{member: None}), ['trace'], 'latest'],
             probes=[effect(f'A null {member} is omitted and selects no transaction type, so the unpriced initcode returns word 42.', words(42))])
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
    # Legacy gasPrice with an authorizationList matches no signed transaction type; whether a
    # simulation accepts the mix is an open input policy. This case records each server's
    # answer; the -1559 twins below carry the canonical H14 authorization assertion.
    case(cases, 'field-authorization', 'trace_call', [dict(delegated, authorizationList=[authorization]), ['trace'], 'latest'],
         probes=[dict(effect('A valid authorization delegates key 1 to the marker contract, which returns word 42.', words(42)),
                      observe='Mixing legacy gasPrice with an authorizationList is an open input policy, since no signed transaction type carries both; the response does not isolate the authorization field, which field-authorization-1559 asserts with EIP-1559 fees.')])
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
         probes=[probe('H14', 'same-output', 'Omitted gas follows the client\'s eth_call default at the selected state: GAS reports the same value.',
                       reference='field-gas-omitted-eth-call')])
    # A zero-price, explicitly over-cap call discovers this server's cap without
    # making any one implementation's default budget a portable constant.
    cap_reference = 'field-gas-cap-eth-call'
    case(cases, cap_reference, 'eth_call', [dict(gas_call, gas=hex(2**64-1), gasPrice='0x0'), 'latest'])
    for label, gas_price in [('allowance', int(balance, 16)//100_000), ('funded', int(price, 16))]:
        priced = dict(gas_call, gasPrice=hex(gas_price))
        reference = f'field-gas-omitted-{label}-eth-call'
        bounded = probe('H15', 'gas-output-bound', 'A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree.',
                        reference=cap_reference)
        dependency = {'topic': 'H15', 'reason': 'The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control.'}
        case(cases, reference, 'eth_call', [priced, 'latest'], probes=[dict(bounded, depends=dependency)])
        paired = probe('H15', 'same-output', 'A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit.',
                       reference=reference, depends=dependency)
        case(cases, f'field-gas-omitted-{label}', 'trace_call', [priced, ['trace'], 'latest'],
             probes=[paired, dict(bounded, depends=dependency)])
        case(cases, f'field-gas-omitted-{label}-many', 'trace_callMany', [[[priced, ['trace']]], 'latest'],
             probes=[dict(paired, index=0), dict(bounded, index=0, depends=dependency)])
    case(cases, 'field-chain-id', 'trace_call', [dict(base, input='0x'+ret42, chainId=hex(chain_id)), ['trace'], 'latest'],
         probes=[effect('A matching chainId is accepted and the initcode returns word 42.', words(42))])
    case(cases, 'field-chain-id-mismatch', 'trace_call', [dict(base, input='0x'+ret42, chainId='0x1'), ['trace'], 'latest'],
         probes=[probe('H14', 'error', 'A chainId that does not match the chain rejects the request; it is invalid regardless of state '
                       '(-32602 recommended).', recommended=-32602)])
    # BLOBBASEFEE is 0 exactly when maxFeePerBlobGas is 0 or defaulted (H15). A blob call needs a recipient, so it
    # calls the genesis CREATE2 factory, whose child deploys the BLOBBASEFEE word it read as its code.
    factory = '0x4e59b44847b379578588920ca78fbf26c0b4956c'
    assert alloc[factory]['code'].startswith('0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe03601600081')
    head = read(ROOT/'fixtures/chains/raw-validation/headblock.json')
    blob_base_fee = fake_exponential(1, int(head['excessBlobGas'], 16), genesis['config']['blobSchedule']['prague']['baseFeeUpdateFraction'])
    blob_init = asm('BLOBBASEFEE', 0, 'MSTORE', 32, 0, 'RETURN')
    versioned = next(iter(read(ROOT/'fixtures/blobs.json')))
    blob_call = {'from': sender, 'to': factory, 'gas': gas, 'maxFeePerGas': price, 'maxPriorityFeePerGas': price,
                 'data': '0x'+word(0)+blob_init}
    for name, fields, value, requirement in [
            ('blob-fee-defaulted', {'blobVersionedHashes': [versioned]}, 0,
             'With blobVersionedHashes and no maxFeePerBlobGas, the blob fee cap defaults to 0, so BLOBBASEFEE is 0.'),
            ('blob-fee-zero', {'blobVersionedHashes': [versioned], 'maxFeePerBlobGas': '0x0'}, 0,
             'An explicit zero maxFeePerBlobGas runs with BLOBBASEFEE 0.'),
            ('blob-fee-priced', {'blobVersionedHashes': [versioned], 'maxFeePerBlobGas': hex(blob_base_fee)}, blob_base_fee,
             'A maxFeePerBlobGas that covers the blob base fee keeps the selected block\'s BLOBBASEFEE.'),
            ('blob-fee-none', {}, blob_base_fee, 'A call without blob fields keeps the selected block\'s BLOBBASEFEE.')]:
        case(cases, name, 'trace_call', [dict(blob_call, **fields), ['trace'], 'latest'], probes=[
            probe('H15', 'frame', requirement+' The factory\'s CREATE2 child deploys the word it read.',
                  select={'traceAddress': [0], 'type': 'create'}, expected={'error': None, 'result': {'code': words(value)}})])
    # A supplied nonce is accepted but neither validated nor used: the creation address follows the state nonce (H15).
    address = asm('ADDRESS', 0, 'MSTORE', 32, 0, 'RETURN')
    for name, supplied in [('field-nonce-above', nonce+3), ('field-nonce-below', nonce-3)]:
        case(cases, name, 'trace_call', [creation(address, nonce=hex(supplied)), ['trace'], 'latest'], probes=[
            probe('H15', 'outputs', f'A supplied nonce {supplied} is ignored: the creation runs at the address of state nonce {nonce}.',
                  expected=[words(int(root, 16))])])
    return {'description': 'Programs on the raw-validation chain: vmTrace push, store and code end; precheck failures, collision, reverted and undeployable CREATEs; callMany item isolation; call-object fields; blob fee and nonce handling.',
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
    funder = '0x0c2c51a0990aee1d73c1228de158688341557508'
    assert not any(tx['sender'] == funder for b in blocks.values() if b['number'] <= 55 for tx in b['transactions'])
    assert int(genesis['alloc'][funder[2:]].get('nonce', '0x0'), 16) == 0
    address = created_address(funder, 0)
    assert address not in codes
    # Empty calldata writes 42 to slot zero; nonempty calldata deletes the account.
    runtime = '36156008576000ff5b602a60005500'
    base = {'from': funder, 'gas': '0x493e0', 'gasPrice': '0x77359400'}
    bundle = [[dict(base, data='0x'+deploy(runtime)), ['trace', 'stateDiff']],
              [dict(base, to=address, data='0x'), ['trace', 'stateDiff']],
              [dict(base, to=address, data='0x01'), ['trace', 'stateDiff']]]
    case(cases, 'many-write-delete-storage', 'trace_callMany', [bundle, '0x37'], probes=[
        probe('H26', 'account', 'Before Cancun the final item deletes the account created by an earlier item.',
              index=2, address=address, expected={'balance': {'-': '0x0'}, 'nonce': {'-': '0x1'}, 'code': {'-': '0x'+runtime}}),
        probe('H26', 'deleted-storage', 'Account deletion wipes all storage; optional - entries report the item\'s pre-values, including slot zero written to 42 by the preceding item.',
              index=2, address=address, expected={'0x'+word(0): '0x'+word(42)})])
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
         probes=[probe('H06', 'error', 'An explicit fromBlock above toBlock is rejected (-32602 recommended), as eth_getLogs does.', recommended=-32602)])
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
    # An explicit null trace_filter member is the same as omitting it (H14).
    case(cases, 'filter-null-members', 'trace_filter',
         [{'fromBlock': '0x2', 'toBlock': '0x5', **dict.fromkeys(['fromAddress', 'toAddress', 'mode', 'after', 'count'])}],
         probes=[probe('H14', 'records', 'Null mode, after, count and address lists are omitted, so blocks 2-5 return every record.',
                       expected=records(2, 5))])
    # The fromBlock twin names the head by number: a null or omitted fromBlock is latest, so the range is valid
    # without depending on block tag support (H32).
    for bound, twin in [('toBlock', {'fromBlock': '0x2'}), ('fromBlock', {'toBlock': read(chain/'headblock.json')['number']})]:
        case(cases, f'filter-omitted-{bound}', 'trace_filter', [twin])
        case(cases, f'filter-null-{bound}', 'trace_filter', [dict(twin, **{bound: None})],
             probes=[probe('H14', 'same-result', f'A null {bound} is omitted, so it resolves to the same latest head.',
                           reference=f'filter-omitted-{bound}')])
    # Call depth limit (H29, H09). Before EIP-150 a CALL forwards exactly the gas it requests, so at a Homestead
    # block a contract that calls itself reaches the 1024 limit for well under a million gas; after EIP-150 the
    # 63/64 rule puts that depth out of reach of any practical gas cap. Each frame keeps 512 gas for its own exit.
    # Only the deepest frame's CALL returns 0; it then also attempts a CREATE, which fails the same check.
    head = asm(0, 0, 0, 0, 0, 'ADDRESS', 0x200, 'GAS', 'SUB', 'CALL')
    fail = asm(0, 0, 0, 'CREATE', 'POP')
    runtime = head + asm(len(head)//2 + 3 + len(fail)//2, 'JUMPI') + fail + asm('JUMPDEST', 'STOP')
    child = deploy(runtime)
    loader = lambda offset: asm(len(child)//2, offset, 0, 'CODECOPY', len(child)//2, 0, 0, 'CREATE',
                                0, 0, 0, 0, 0, 'DUP6', 0x200, 'GAS', 'SUB', 'CALL', 'POP', 'POP', 'STOP')
    root = loader(len(loader(0))//2) + child
    assert len(loader(len(loader(0))//2)) == len(loader(0))
    homestead = hex(int(forkenv['HIVE_FORK_TANGERINE']) - 1)
    case(cases, 'depth-limit', 'trace_call', [{'from': sender, 'data': '0x'+root, 'gas': '0x200000', 'gasPrice': '0x0'}, ['trace'], homestead],
         probes=[probe('H29', 'depth', 'Under the deepest executed frame, at depth 1024, the CALL and CREATE that fail the depth precheck each emit a failed frame with no result and no subtraces.',
                       depth=1024, attempts=['call', 'create']),
                 probe('H09', 'depth', 'A CALL or CREATE that fails the depth precheck has error "Max call depth exceeded".',
                       depth=1024, attempts=['call', 'create'], labels=['Max call depth exceeded']*2)])
    return {'description': 'Reward matching and pagination, reversed range, genesis, the callMany beacon-root twin and the call depth limit at a Homestead block on the frozen PoW-to-PoS forks chain.', 'cases': cases}


def next_base_fee(header):
    """The EIP-1559 base fee of the block after `header` (elasticity 2, denominator 8)."""
    base, used, target = (int(header[k], 16) for k in ['baseFeePerGas', 'gasUsed', 'gasLimit'])
    target //= 2
    if used == target:
        return base
    delta = base*abs(used-target)//target//8
    return base + max(delta, 1) if used > target else base - delta


def sign_legacy(key, chain_id, nonce, gas_price, gas, to, value, data):
    """An EIP-155 legacy transaction, signed deterministically (RFC 6979)."""
    fields = [nonce, gas_price, gas, bytes.fromhex(to[2:]) if to else b'', value, bytes.fromhex(data[2:])]
    signature = key.sign_msg_hash(keccak(rlp.encode(fields+[chain_id, 0, 0])))
    return '0x'+rlp.encode(fields+[signature.v+35+2*chain_id, signature.r, signature.s]).hex()


def state_probe(requirement, witness, states, expected, environments=(), **fields):
    """H12: which state (and block environment) a signed transaction ran against, read from `witness`
    (output words or a stateDiff account field) and matched against candidates derived from the chain."""
    return probe('H12', 'state', requirement, witness=witness, states=[list(s) for s in states],
                 environments=[list(e) for e in environments], expected=expected, **fields)


# The extension probes record behavior; H12 keeps the explicit selector outside the baseline.
EXTENSION = 'Explicit third block selector (extension outside the two-argument baseline).'


def selector():
    """raw-selector (chain a): one signed creation from an account that never transacts on the chain,
    so it is valid at every block, returns NUMBER, BALANCE(witness) and BASEFEE. The witness account
    receives one-wei transfers in some blocks, so its balance names the state the transaction ran against."""
    chain = ROOT/'fixtures/chains/a'
    genesis = read(chain/'genesis.json')
    chain_id = genesis['config']['chainId']
    alloc = {'0x'+a.lower(): v for a, v in genesis['alloc'].items()}
    blocks = load_chain(chain/'chain.rlp')
    headers = {h['number']: h for h in read(chain/'headers.json')}
    head = read(chain/'headblock.json')
    headstate = {a.lower(): v for a, v in read(chain/'headstate.json')['accounts'].items()}
    top = int(head['number'], 16)
    # Hive's public hivechain key for 0x84E75c28… (cmd/hivechain/accounts.go at the pinned Hive revision):
    # funded in genesis and never a sender or recipient on this chain, so its nonce is 0 at every block.
    key = keys.PrivateKey(bytes.fromhex('f6a8f1603b8368f3ca373292b7310c53bec7b508aecacd442554ebc1c5d0c856'))
    sender = key.public_key.to_checksum_address().lower()
    witness = '0x4a0f1452281bcec5bd90c3dce6162a5995bfe9df'  # A prefunded hivechain account with one-wei receipts.
    transactions = [t for b in blocks.values() for t in b['transactions']]
    assert not any(sender in [t['sender'].lower(), str(t['to']).lower()] for t in transactions)
    assert 'code' not in alloc[witness] and not any(t['sender'].lower() == witness for t in transactions)
    # No withdrawal or internal transfer reaches the witness: its genesis balance plus the values sent to it
    # equals its head balance.
    received = {n: sum(t['value'] for b in blocks.values() if b['number'] <= n for t in b['transactions']
                       if str(t['to']).lower() == witness) for n in range(top+1)}
    balance = lambda n: int(alloc[witness]['balance'], 16) + received[n]
    assert balance(top) == int(headstate[witness]['balance'])
    # A block whose own transactions change the witness balance, with a later change before the head, so
    # the selected block's post-state, its parent's post-state (the selected block's pre-state) and latest differ.
    selected = next(n for n in range(top//2, top) if received[n] != received[n-1] and received[top] != received[n])
    number = hex(selected)
    gas_price = 0x77359400
    assert all(gas_price >= b['base_fee'] for b in blocks.values())
    code = asm('NUMBER', 0, 'MSTORE', int(witness, 16), 'BALANCE', 32, 'MSTORE', 'BASEFEE', 64, 'MSTORE', 96, 0, 'RETURN')
    raw = sign_legacy(key, chain_id, 0, gas_price, 0x30d40, None, 0, '0x'+code)

    def at(n):
        return {'NUMBER': hex(n), 'BASEFEE': headers[hex(n)]['baseFeePerGas']}
    states = [(f'the block {number} post-state', {'BALANCE': hex(balance(selected))}),
              (f'the block {hex(selected-1)} post-state (the block {number} pre-state)', {'BALANCE': hex(balance(selected-1))}),
              (f'the latest (block {head["number"]}) post-state', {'BALANCE': hex(balance(top))})]
    environments = [(f'the block {number} environment', at(selected)),
                    (f'the block {hex(selected+1)} environment', at(selected+1)),
                    (f'the head (block {head["number"]}) environment', at(top)),
                    (f'the pending block {hex(top+1)} environment', {'NUMBER': hex(top+1), 'BASEFEE': hex(next_base_fee(head))})]
    words = {'NUMBER': {'word': 0}, 'BALANCE': {'word': 1}, 'BASEFEE': {'word': 2}}
    latest = {'state': states[2][0], 'environment': environments[2][0]}
    cases = []
    for label, address, field, block, value in [
            ('witness-balance-parent', witness, 'balance', hex(selected-1), hex(balance(selected-1))),
            ('witness-balance-selected', witness, 'balance', number, hex(balance(selected))),
            ('witness-balance-latest', witness, 'balance', 'latest', hex(balance(top))),
            ('sender-nonce-selected', sender, 'nonce', number, '0x0'),
            ('sender-nonce-latest', sender, 'nonce', 'latest', '0x0'),
            ('sender-balance-latest', sender, 'balance', 'latest', alloc[sender]['balance'])]:
        method = {'nonce': 'eth_getTransactionCount', 'balance': 'eth_getBalance'}[field]
        case(cases, '_control/'+label, method, [address, block], expected_control=value)
    case(cases, '_control/selected-block', 'eth_getBlockByNumber', [number, False],
         expected_control_fields={'hash': headers[number]['hash'], 'baseFeePerGas': headers[number]['baseFeePerGas']})
    baseline = ('The two-argument request runs against latest: the head block post-state and environment, '
                'as trace_call at latest (H31).')
    case(cases, 'raw-state-default', 'trace_rawTransaction', [raw, ['trace']],
         probes=[state_probe(baseline, words, states, latest, environments)])
    selected_state = {'state': states[0][0], 'environment': environments[0][0]}
    pending = {'state': states[2][0], 'environment': environments[3][0]}
    for name, block, expected, selector in [
            ('latest', 'latest', latest, 'latest'), ('number', number, selected_state, f'block {number} by number'),
            ('hash', headers[number]['hash'], selected_state, f'block {number} by hash'),
            ('hash-object', {'blockHash': headers[number]['hash']}, selected_state, f'block {number} as an EIP-1898 object'),
            ('pending', 'pending', pending, 'pending')]:
        case(cases, f'raw-state-{name}', 'trace_rawTransaction', [raw, ['trace'], block],
             probes=[state_probe('Record which state and block environment an explicit third selector uses.', words,
                                 states, expected, environments, default=latest, selector=selector,
                                 observe=EXTENSION, extension=True)])
    return {'description': f'H12: one signed creation, valid at every block, returns NUMBER, BALANCE({witness}) and '
                           f'BASEFEE, sent with two arguments and with latest, block {number} by number, hash and '
                           'EIP-1898 object, and pending.', 'cases': cases}


def annotate_initial():
    """H12 state witnesses for the initial corpus's signed transactions: the sender nonce a stateDiff
    starts from names the state the transaction ran against."""
    chain = ROOT/'fixtures/chains/initial'
    blocks = load_chain(chain/'chain.rlp')
    alloc = {'0x'+a.lower(): v for a, v in read(chain/'genesis.json')['alloc'].items()}
    top = int(read(chain/'headblock.json')['number'], 16)
    corpus = read(ROOT/'fixtures/corpora/initial.json')
    by_name = {c['name']: c for c in corpus['cases']}

    def nonce(sender, n):
        return int(alloc[sender].get('nonce', '0x0'), 16) + sum(
            t['sender'].lower() == sender for b in blocks.values() if b['number'] <= n for t in b['transactions'])

    def states(sender, numbers):
        return [((f'the latest (block {hex(n)}) post-state' if n == top else f'the block {hex(n)} post-state')
                 + f', sender nonce {nonce(sender, n)}', {'NONCE': hex(nonce(sender, n))}) for n in numbers]
    for name, selected in [('raw-valid', 0), ('raw-valid-current-nonce', None)]:
        request = by_name[name]['request']
        params = request['params']
        assert request['method'] == 'trace_rawTransaction' and 'stateDiff' in params[1]
        tx = decode_transaction(bytes.fromhex(params[0][2:]))
        sender = tx['sender'].lower()
        witness = {'NONCE': {'account': sender, 'field': 'nonce'}}
        if selected is None:
            candidates = states(sender, [top, top-1])
            assert len(params) == 2 and tx['nonce'] == nonce(sender, top) != nonce(sender, top-1)
            by_name[name]['probes'] = [state_probe('The two-argument request runs against the latest post-state.',
                                                   witness, candidates, {'state': candidates[0][0]})]
        else:
            candidates = states(sender, [int(params[2], 16), top])
            assert int(params[2], 16) == selected and tx['nonce'] == nonce(sender, selected) != nonce(sender, top)
            by_name[name]['probes'] = [state_probe('Record which state an explicit third selector uses.', witness, candidates,
                                                   {'state': candidates[0][0]}, default={'state': candidates[1][0]},
                                                   selector=f'block {params[2]} by number', observe=EXTENSION, extension=True)]
    return corpus


def hash_probe(requirement, block, **fields):
    """H33: which block a trace_filter blockHash selects. `block` is the {number, hash} the hash names
    (None for an unknown hash); the result must equal `reference`'s records at that block, equal
    `expected`, or, with `reject`, be an error."""
    return probe('H33', 'block-hash', requirement, block=block, **fields)


def replace_cases(corpus, cases):
    """The hand-written corpus with `cases` appended, replacing earlier generated cases of the same names."""
    names = {c['name'] for c in cases}
    return dict(corpus, cases=[c for c in corpus['cases'] if c['name'] not in names]+cases)


def annotate_blockhash():
    """H33 blockHash selection on chain a (h30) and across the reorg scenarios. Each hash case is
    compared with the numeric filter of the same block from the same build, so equality shows that
    the hash selected that block; the frozen chains name every hash and address."""
    chain = ROOT/'fixtures/chains/a'
    blocks = load_chain(chain/'chain.rlp')
    alternate = load_chain(ROOT/'fixtures/chains/b/chain.rlp')
    block = blocks['0x2']
    selected = {'number': '0x2', 'hash': block['hash']}
    genesis = {'number': '0x0', 'hash': blocks['0x1']['parent_hash']}
    head = read(chain/'headblock.json')
    senders = sorted({t['sender'].lower() for t in block['transactions']})
    recipients = sorted({t['to'].lower() for t in block['transactions'] if t['to']})
    coinbase = block['miner']
    # Every block after genesis on chain a is proof of stake, so none has a reward record; the coinbase, one of
    # block 2's recipients, matches a call and any synthetic reward a build emits (H05), as the numeric filter does.
    assert block['difficulty'] == 0 and all(b['difficulty'] == 0 for b in blocks.values())
    assert coinbase in recipients and all(t['sender'].lower() != coinbase for b in blocks.values() for t in b['transactions'])
    # The senders and recipients also transact in other blocks, so a build that scans a wider range than the
    # hashed block (Erigon 3.7.0 scans from genesis to latest when both bounds are omitted) returns more than the twin.
    elsewhere = [t for b in blocks.values() if b['number'] != 2 for t in b['transactions']]
    assert {t['sender'].lower() for t in elsewhere} >= set(senders) and {str(t['to']).lower() for t in elsewhere} & set(recipients)
    known = {b['hash'] for b in [*blocks.values(), *alternate.values()]} | {genesis['hash']}
    unknown = '0x'+keccak(b'trace-interop H33 unknown block').hex()
    assert unknown not in known and int(head['number'], 16) > 2
    cases = []
    discriminating = 'A blockHash selects exactly that block: the result equals the numeric single-block filter, each record localized with the requested hash, never another block’s records.'
    for suffix, extra, requirement, nonempty in [
            ('', {'count': 3}, discriminating, True),
            ('-address-from', {'fromAddress': senders},
             'Address matching applies to the hash-selected block as to the numeric single-block filter.', True),
            ('-address-to', {'toAddress': recipients},
             'Recipient matching, including a reward matched by its author, applies to the hash-selected block as to the numeric single-block filter.', True),
            ('-union', {'fromAddress': senders, 'toAddress': [coinbase], 'mode': 'union'},
             'mode union applies to the hash-selected block as to the numeric single-block filter.', True),
            ('-page', {'after': 1, 'count': 1},
             'after and count page the hash-selected block’s records as they page the numeric single-block filter.', True),
            ('-page-past-end', {'after': 1000, 'count': 1},
             'A page past the end of the hash-selected block is [], as for the numeric single-block filter; alone it cannot show which block was selected.', False),
            ('-empty', {'fromAddress': [coinbase]},
             'A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected.', False)]:
        twin = 'filter-block-2'+suffix
        case(cases, twin, 'trace_filter', [{'fromBlock': '0x2', 'toBlock': '0x2', **extra}])
        case(cases, 'filter-blockhash'+suffix, 'trace_filter', [{'blockHash': selected['hash'], **extra}],
             probes=[hash_probe(requirement, selected, reference=twin, nonempty=nonempty)])
    case(cases, 'filter-blockhash-genesis', 'trace_filter', [{'blockHash': genesis['hash']}],
         probes=[hash_probe('The genesis hash selects the genesis block, which has no trace records: [].', genesis, expected=[])])
    case(cases, 'filter-blockhash-and-range', 'trace_filter', [{'blockHash': selected['hash'], 'fromBlock': '0x2', 'count': 3}],
         probes=[hash_probe('A non-null blockHash with a non-null fromBlock or toBlock is rejected (-32602 recommended), never answered by either selector.',
                            selected, reject=True, recommended=-32602)])
    case(cases, 'filter-blockhash-null-bounds', 'trace_filter', [{'blockHash': selected['hash'], 'fromBlock': None, 'toBlock': None, 'count': 3}],
         probes=[hash_probe('Null fromBlock and toBlock are omitted, so a blockHash with null bounds selects that block.',
                            selected, reference='filter-block-2', nonempty=True)])
    case(cases, 'filter-blockhash-null', 'trace_filter', [{'blockHash': None, 'fromBlock': '0x2', 'toBlock': '0x2', 'count': 3}],
         probes=[hash_probe('A null blockHash is omitted, so the numeric range applies.', selected, reference='filter-block-2', nonempty=True)])
    for suffix, extra, requirement in [
            ('', {}, 'An unknown hash is an error (-32001 recommended), never [] or another block’s records.'),
            ('-count-zero', {'count': 0}, 'An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass.')]:
        case(cases, 'filter-blockhash-unknown'+suffix, 'trace_filter', [{'blockHash': unknown, **extra}],
             probes=[hash_probe(requirement, None, reject=True, recommended=-32001)])
    for suffix, value, requirement in [
            ('short', selected['hash'][:10], 'A blockHash that is not a 32-byte hash is rejected (-32602 recommended).'),
            ('object', {'blockHash': selected['hash']}, 'blockHash takes a bare 32-byte hash, not an EIP-1898 object: it is rejected (-32602 recommended).')]:
        case(cases, 'filter-blockhash-malformed-'+suffix, 'trace_filter', [{'blockHash': value}],
             probes=[hash_probe(requirement, selected, reject=True, recommended=-32602)])
    corpora = {'h30': replace_cases(read(ROOT/'fixtures/corpora/h30.json'), cases)}
    for name in ['reorg', 'reorg-safe']:
        corpus = read(ROOT/'fixtures/corpora'/(name+'.json'))
        # Branch B replaces A's tail at the same heights with empty blocks; a tail block with records on A
        # has none on B, so a replacement's [] is what a hash selection must never return for A.
        tail = next(c['request']['params'][0] for c in corpus['cases'] if c['name'] == 'before/block-tail')
        heads = {branch: {h['number']: h['hash'] for h in corpus['heads_'+branch]} for branch in 'ab'}
        a, b = ({'number': tail, 'hash': heads[branch][tail]} for branch in 'ab')
        assert a['hash'] == blocks[tail]['hash'] and b['hash'] == alternate[tail]['hash'] != a['hash']
        assert blocks[tail]['transactions'] and not alternate[tail]['transactions']
        assert {p['params'][0]['blockHash'] for p in corpus['plan']['payloads']} >= {b['hash']}
        cases = []
        for phase, branch, expectation, requirement in [
                ('before', a, 'reference', f'Before the switch, branch A’s block {tail} is canonical: its hash selects A’s records, as the numeric range does.'),
                ('after', a, 'reject', f'After the switch to branch B, A’s block {tail} is noncanonical: its hash is an error (-32001 recommended), never B’s [] or records.'),
                ('restored', a, 'reference', f'Once branch A is restored, the hash of its block {tail} selects A’s records again.'),
                ('before', b, 'reject', f'Before B’s payloads arrive, B’s block {tail} is unknown: an error (-32001 recommended).'),
                ('after', b, 'reference', f'After the switch, B’s block {tail} is canonical: its hash selects that block, which has no records, as the numeric range shows.'),
                ('restored', b, 'reject', f'Once branch A is restored, B’s block {tail} is noncanonical: an error (-32001 recommended), never A’s records.')]:
            fields = ({'reject': True, 'recommended': -32001} if expectation == 'reject'
                      else {'reference': phase+'/filter-tail', 'nonempty': branch is a})
            case(cases, f'{phase}/filter-hash-{"a" if branch is a else "b"}', 'trace_filter', [{'blockHash': branch['hash']}],
                 probes=[hash_probe(requirement, branch, **fields)])
        corpora[name] = replace_cases(corpus, cases)
    return corpora


if __name__ == '__main__':
    checksums = read(ROOT/'fixtures/checksums.json')
    for name, corpus in [('probes-prague', prague()), ('probes-forks', forks()), ('raw-selector', selector()),
                         ('initial', annotate_initial()), *annotate_blockhash().items()]:
        path = ROOT/'fixtures/corpora'/(name+'.json')
        if name in ['initial', 'h30', 'reorg', 'reorg-safe']:  # Hand-written: keep its key order and layout.
            path.write_text(json.dumps(corpus, indent=2)+'\n')
        else:
            write(path, corpus)
        checksums['corpora/'+name+'.json'] = sha(path)
    write(ROOT/'fixtures/checksums.json', checksums)

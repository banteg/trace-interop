"""Build the amsterdam-gas probe corpus and its chain directory.

The chain is the execution-apis rpc-compat chain (Amsterdam from timestamp 570, head 0x3c).
Usage: uv run python build_corpus.py <execution-apis tests dir> <output chain dir> <output corpus>
"""
import json
import shutil
import sys
from pathlib import Path

import rlp
from eth_keys import keys
from eth_utils import keccak

from trace_interop.chain_model import load_chain

OPS = {'STOP': 0x00, 'SSTORE': 0x55, 'MSTORE': 0x52, 'CREATE': 0xf0, 'CALL': 0xf1, 'RETURN': 0xf3,
       'DELEGATECALL': 0xf4, 'REVERT': 0xfd, 'GAS': 0x5a, 'POP': 0x50, 'JUMPDEST': 0x5b, 'JUMP': 0x56,
       'DUP1': 0x80, 'DUP5': 0x84, 'DUP6': 0x85}

SENDER = '0x0c2c51a0990aee1d73c1228de158688341557508'  # funded in genesis, nonce 0 at the head
# testgen's key for SENDER (execution-apis tools/chain/accounts.json)
KEY = keys.PrivateKey(bytes.fromhex('bfcd0e032489319f4e5ca03e643b2025db624be6cf99cbfed90c4502e3754850'))
FEE_CAP, TIP = 10**9, 1  # the head base fee is 0xbc78d4
FACTORY = '0x4e59b44847b379578588920ca78fbf26c0b4956c'  # CREATE2 deployment proxy: salt ‖ initcode
STORAGE = '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df'  # stores keccak(calldata) in a new slot per call
PURE = '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2'  # returns block environment words, no state
FRESH = '0x00000000000000000000000000000000000a5e7d'  # no account at the head
LOW, HIGH = 1_000_000, 30_000_000  # HIGH exceeds the EIP-7825 cap of 2^24, so it seeds a reservoir


def asm(*items):
    out = bytearray()
    for item in items:
        if isinstance(item, str):
            out.append(OPS[item])
        else:  # (n, value): PUSHn value
            n, value = item
            out.append(0x5f + n)
            out += value.to_bytes(n, 'big') if isinstance(value, int) else value
    return bytes(out)


def push(value):
    if isinstance(value, bytes):
        return (len(value), value)
    return (max(1, (value.bit_length() + 7) // 8), value)


def deployer(runtime):
    """Initcode returning `runtime` (at most 23 bytes)."""
    n = len(runtime)
    return asm(push(runtime), push(0), 'MSTORE', push(n), push(32 - n), 'RETURN')


def create(runtime):
    """Deploy `runtime` with CREATE; leaves the address on the stack."""
    init = deployer(runtime)
    return asm(push(init), push(0), 'MSTORE', push(len(init)), push(32 - len(init)), push(0), 'CREATE')


def call_top(gas=None, value=0):
    """CALL the address on top of the stack, keeping it below the success flag."""
    return asm(push(0), push(0), push(0), push(0), push(value), 'DUP6', push(gas) if gas else 'GAS', 'CALL')


def call_addr(address, gas=None, value=0):
    return asm(push(0), push(0), push(0), push(0), push(value), push(bytes.fromhex(address[2:])),
               push(gas) if gas else 'GAS', 'CALL')


def delegatecall_top():
    return asm(push(0), push(0), push(0), push(0), 'DUP5', 'GAS', 'DELEGATECALL')


def sstore(slot, value):
    return asm(push(value), push(slot), 'SSTORE')


CLEAR10 = sstore(0x10, 0) + asm('STOP')
STORE20 = sstore(0x20, 1) + asm('STOP')
STORE20_REVERT = sstore(0x20, 1) + asm(push(0), 'DUP1', 'REVERT')
LOOP = asm('JUMPDEST', push(0), 'JUMP')

# Each program runs as initcode: as the root of a creation call, or nested under the factory.
PROGRAMS = {
    'sstore-new': ('creates slot 0x10', sstore(0x10, 1)),
    'sstore-clear': ('creates slot 0x10, then clears it in the same frame (state gas refill)',
                     sstore(0x10, 1) + sstore(0x10, 0)),
    'sstore-clear-child': ('creates slot 0x10, then a DELEGATECALL child clears it (refill in another frame)',
                           create(CLEAR10) + sstore(0x10, 1) + delegatecall_top()),
    'sstore-new-child': ('a CALL child creates a slot in its own storage',
                         create(STORE20) + call_top()),
    'sstore-child-revert': ('a CALL child creates a slot, then reverts',
                            create(STORE20_REVERT) + call_top()),
    'create': ('CREATE deploys a 6-byte runtime (account creation and code deposit)', create(CLEAR10)),
    'call-new-account': ('CALL sends 1 wei to an address with no account (new account charge)',
                         call_addr(FRESH, value=1)),
    'oog-state-child': ('a CALL child given 50000 gas creates a slot (state charge above its gas_left)',
                        create(STORE20) + call_top(gas=50_000)),
    'oog-exec-child': ('a CALL child given 30000 gas loops until out of execution gas',
                       create(LOOP) + call_top(gas=30_000)),
}


def call(to, data, gas, value=0):
    obj = {'from': SENDER, 'gas': hex(gas), 'input': data, 'value': hex(value)}
    if to:
        obj['to'] = to
    return obj


def sign(chain_id, obj):
    """The call object as a signed type-2 transaction from SENDER."""
    to = bytes.fromhex(obj['to'][2:]) if 'to' in obj else b''
    fields = [chain_id, 0, TIP, FEE_CAP, int(obj['gas'], 16), to, int(obj['value'], 16),
              bytes.fromhex(obj['input'][2:]), []]
    signature = KEY.sign_msg_hash(keccak(b'\x02' + rlp.encode(fields)))
    return '0x' + (b'\x02' + rlp.encode(fields + [signature.v, signature.r, signature.s])).hex()


def request(method, params):
    return {'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}


def cases(blocks, chain_id):
    out = []

    def add(name, method, params, note):
        out.append({'name': name, 'note': note, 'request': request(method, params)})

    def probe(name, obj, note):
        """An unsigned trace_call and the same transaction signed for trace_rawTransaction, whose
        gas limit is split into gas_left and a reservoir as in a block."""
        add(name, 'trace_call', [obj, ['trace', 'vmTrace'], 'latest'], note)
        add(name + '/raw', 'trace_rawTransaction', [sign(chain_id, obj), ['trace', 'vmTrace']],
            note + '; signed, executed on the head state')

    for gas, label in [(LOW, 'low'), (HIGH, 'high')]:
        roots = {'plain-call': (call(PURE, '0x', gas), 'CALL to a contract that touches no state'),
                 'transfer-new-account': (call(FRESH, '0x', gas, 1), 'value transfer to an address with no account'),
                 'sstore-root': (call(STORAGE, '0x01', gas), 'root CALL whose frame creates a slot')}
        for name, (obj, note) in roots.items():
            probe(f'{name}/{label}', obj, note)
        for name, (note, code) in PROGRAMS.items():
            value = 1 if name == 'call-new-account' else 0
            init = '0x' + (code + asm('STOP')).hex()
            via_factory = call(FACTORY, '0x' + bytes(32).hex() + init[2:], gas, value)
            probe(f'{name}/create-root/{label}', call(None, init, gas, value), note + '; runs as the root creation')
            probe(f'{name}/factory/{label}', via_factory, note + '; runs in a CREATE2 frame under a root CALL to the factory')
            add(f'{name}/factory/{label}/callTracer', 'debug_traceCall', [via_factory, 'latest', {'tracer': 'callTracer'}],
                'geth-style call tracer for the same call')
            if name in ('sstore-clear', 'sstore-clear-child', 'oog-state-child', 'create'):
                add(f'{name}/factory/{label}/structLogger', 'debug_traceCall',
                    [via_factory, 'latest', {'disableStorage': True, 'disableStack': True}],
                    'geth-style struct logger for the same call')
    probe('sstore-root/oog', call(STORAGE, '0x01', 100_000),
          'root CALL with 100000 gas whose new slot needs more than its gas_left')
    for number, block in sorted(blocks.items(), key=lambda kv: int(kv[0], 16)):
        if block['timestamp'] < 570:
            continue
        add(f'mined/block/{number}', 'trace_block', [number], 'mined Amsterdam block')
        for index, tx in enumerate(block['transactions']):
            add(f'mined/{number}/{index}', 'trace_replayTransaction', [tx['hash'], ['trace', 'vmTrace']],
                f'mined Amsterdam transaction to {tx["to"]} with gas {tx["gas"]}')
            add(f'mined/{number}/{index}/callTracer', 'debug_traceTransaction', [tx['hash'], {'tracer': 'callTracer'}],
                'geth-style call tracer for the same transaction')
    return out


def main(tests, chain_dir, corpus_path):
    tests, chain_dir = Path(tests), Path(chain_dir)
    chain_dir.mkdir(parents=True, exist_ok=True)
    for name in ['genesis.json', 'chain.rlp', 'forkenv.json', 'headfcu.json']:
        shutil.copy2(tests / name, chain_dir / name)
    latest = (tests / 'eth_getBlockByNumber/get-latest.io').read_text().splitlines()
    head = json.loads(next(line[3:] for line in latest if line.startswith('<< ')))['result']
    head.pop('transactions')
    (chain_dir / 'headblock.json').write_text(json.dumps(head, indent=2) + '\n')
    blocks = load_chain(chain_dir / 'chain.rlp')
    chain_id = json.loads((tests / 'genesis.json').read_text())['config']['chainId']
    Path(corpus_path).write_text(json.dumps({'cases': cases(blocks, chain_id)}, indent=2) + '\n')


if __name__ == '__main__':
    main(*sys.argv[1:])

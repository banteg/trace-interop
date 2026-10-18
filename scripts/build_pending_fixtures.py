"""Generate the pending corpus: a pooled transaction for H32's pending block methods.

On the frozen chain-a head an empty pending block traces as `[]`, which names no block, so
it cannot show a pending environment. In this ordered scenario the pool phase sends one signed
EIP-1559 transfer and checks that it is pooled, not mined; the trace phase then traces the pending
block, which must be block head+1 holding that transaction. The head block has transactions, so a
client that answers with latest returns canonical records instead of `[]`.
"""
from pathlib import Path

import rlp
from eth_hash.auto import keccak
from eth_keys import keys

from trace_interop.chain_model import load_chain
from trace_interop.cli import read, sha, write

ROOT = Path(__file__).resolve().parents[1]
CHAIN = ROOT/'fixtures/chains/a'
# Hive's public hivechain key for 0x84E75c28… (cmd/hivechain/accounts.go at the pinned Hive revision):
# funded in genesis and never a sender or recipient on this chain, so its nonce is 0 at the head.
KEY = keys.PrivateKey(bytes.fromhex('f6a8f1603b8368f3ca373292b7310c53bec7b508aecacd442554ebc1c5d0c856'))
RECIPIENT = '0x'+'0'*36+'0931'


def sign_dynamic(key, chain_id, nonce, tip, fee_cap, gas, to, value):
    fields = [chain_id, nonce, tip, fee_cap, gas, bytes.fromhex(to[2:]), value, b'', []]
    signature = key.sign_msg_hash(keccak(b'\x02'+rlp.encode(fields)))
    raw = b'\x02'+rlp.encode(fields+[signature.v, signature.r, signature.s])
    return '0x'+raw.hex(), '0x'+keccak(raw).hex()


def corpus():
    chain_id = read(CHAIN/'genesis.json')['config']['chainId']
    head = read(CHAIN/'headblock.json')
    state = {a.lower(): v for a, v in read(CHAIN/'headstate.json')['accounts'].items()}
    blocks = load_chain(CHAIN/'chain.rlp')
    sender = KEY.public_key.to_checksum_address().lower()
    transactions = [t for b in blocks.values() for t in b['transactions']]
    assert state[sender]['nonce'] == 0 and RECIPIENT not in state
    assert not any(sender == t['sender'].lower() or RECIPIENT == str(t['to']).lower() for t in transactions)
    assert blocks[head['number']]['transactions'], 'a latest answer must differ from an empty pending block'
    # A 1 gwei tip clears the default pool minimums; a 2 gwei cap covers any next base fee from 0x199876.
    tip, fee_cap, gas, value = 10**9, 2*10**9, 21000, 1
    assert int(state[sender]['balance']) >= fee_cap*gas + value
    raw, txhash = sign_dynamic(KEY, chain_id, 0, tip, fee_cap, gas, RECIPIENT, value)
    cases = []

    def case(name, method, params, **extra):
        cases.append({'name': name, 'request': {'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}, **extra})
    case('pool/send', 'eth_sendRawTransaction', [raw], expected_control=txhash)
    case('pool/pooled', 'eth_getTransactionByHash', [txhash],
         expected_control_fields={'hash': txhash, 'blockHash': None, 'blockNumber': None})
    case('trace/block', 'trace_block', ['pending'])
    case('trace/replay', 'trace_replayBlockTransactions', ['pending', ['trace']])
    return {'description': 'One pooled EIP-1559 transfer on the frozen chain-a head (public hivechain key 0x84E75c28…), '
                           'then trace_block and trace_replayBlockTransactions at pending (H32).',
            'scenario_phases': ['pool', 'trace'], 'sender': sender, 'pending_transaction': txhash, 'cases': cases}


def main():
    path = ROOT/'fixtures/corpora/pending.json'
    write(path, corpus())
    checksums = read(ROOT/'fixtures/checksums.json')
    checksums['corpora/pending.json'] = sha(path)
    write(ROOT/'fixtures/checksums.json', dict(sorted(checksums.items())))


if __name__ == '__main__':
    main()

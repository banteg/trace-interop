"""Replica captures: replay a frozen chain block by block into a client without an Engine API.

Hive imports a chain through the Engine API. Anvil has none, so it starts from the chain's
genesis, mines each block with the fixture's environment, and every block is compared with the
fixture header before any case is sent. Block hashes necessarily differ (the replica cannot set a
parent beacon root), so requests are sent with the replica's hashes and each parsed response maps
them back; the wire bytes stay verbatim.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import time
import urllib.request

import rlp
from eth_hash.auto import keccak

# Clients captured by replay rather than Hive.
REPLICA_CLIENTS = {'anvil'}
# Timestamp-activated forks in genesis-config order; a replica runs exactly one of them.
FORKS = ['shanghai', 'cancun', 'prague', 'osaka']
# Header fields a replayed block must reproduce, by header index. The state root and hash cannot
# match: the EIP-4788 and EIP-2935 system contracts store the replica's beacon roots and hashes.
# Withdrawals are credited separately, so the withdrawals root is not compared either.
QUANTITIES = {'gasLimit': 9, 'gasUsed': 10, 'timestamp': 11, 'baseFeePerGas': 15, 'blobGasUsed': 17, 'excessBlobGas': 18}
DATA = {'miner': 2, 'transactionsRoot': 4, 'receiptsRoot': 5, 'logsBloom': 6, 'mixHash': 13, 'requestsHash': 20}
BLOB_SIZE = 131072


def hardfork(genesis):
    """The one fork a chain runs from genesis, or None when any fork activates later."""
    config = genesis['config']
    schedule = [v for k, v in config.items() if k.endswith(('Block', 'Time')) and isinstance(v, int)]
    active = [f for f in FORKS if config.get(f + 'Time') == 0]
    return active[-1] if active and not any(schedule) else None


def blocks(chain):
    raw, offset = (Path(chain)/'chain.rlp').read_bytes(), 0
    while offset < len(raw):
        block, _, offset = rlp.codec.consume_item(raw, offset)
        yield block


def number(value):
    return int.from_bytes(value, 'big')


def hexbytes(value):
    return '0x' + bytes(value).hex()


def canonical(tx):
    return rlp.encode(tx) if isinstance(tx, list) else bytes(tx)


def expected_header(block):
    header = block[0]
    fields = {'transactions': [hexbytes(keccak(canonical(tx))) for tx in block[1]]}
    fields.update({k: hex(number(header[i])) for k, i in QUANTITIES.items() if i < len(header)})
    fields.update({k: hexbytes(header[i]) for k, i in DATA.items() if i < len(header)})
    return fields


def network_form(tx, sidecars):
    """A block-body transaction as eth_sendRawTransaction accepts it: type 3 needs its sidecar."""
    tx = canonical(tx)
    if tx[0] != 3:
        return tx
    body = rlp.decode(tx[1:])
    blobs, commitments, proofs = [], [], []
    for versioned in body[10]:
        sidecar = sidecars[hexbytes(versioned)]
        commitment = bytes.fromhex(sidecar['commitment'][2:])
        if b'\x01' + hashlib.sha256(commitment).digest()[1:] != versioned:
            raise ValueError(f'blob commitment does not match {hexbytes(versioned)}')
        blobs.append(bytes.fromhex(sidecar['blob'][2:]).ljust(BLOB_SIZE, b'\0'))
        commitments.append(commitment)
        proofs.append(bytes.fromhex(sidecar['proof'][2:]))
    return b'\x03' + rlp.encode([body, blobs, commitments, proofs])


def translate(text, mapping):
    """Replace every hash in `mapping`, with or without its 0x prefix."""
    for old, new in mapping.items():
        text = text.replace(old[2:], new[2:])
    return text


class Rpc:
    def __init__(self, url):
        self.url = url

    def raw(self, request):
        data = json.dumps(request).encode()
        req = urllib.request.Request(self.url, data, {'Content-Type': 'application/json'})
        with urllib.request.urlopen(req, timeout=300) as response:
            return response.read().decode()

    def __call__(self, method, *params):
        reply = json.loads(self.raw({'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': list(params)}))
        if 'error' in reply:
            raise ValueError(f'replica {method} failed: {reply["error"]}')
        return reply['result']

    def wait(self, seconds=60):
        deadline = time.monotonic() + seconds
        while True:
            try:
                return self('eth_chainId')
            except OSError:
                if time.monotonic() > deadline:
                    raise ValueError('replica RPC did not become ready')
                time.sleep(0.2)


def replay(rpc, chain, sidecars):
    """Mine every fixture block; return per-block comparisons and the fixture→replica hash map."""
    compared, hashes = [], {}
    for block in blocks(chain):
        header = block[0]
        n = hex(number(header[8]))
        if n == '0x1':
            hashes[hexbytes(header[0])] = rpc('eth_getBlockByNumber', '0x0', False)['hash']
        rpc('anvil_setNextBlockTimestamp', number(header[11]))
        rpc('anvil_setNextBlockBaseFeePerGas', hex(number(header[15])))
        rpc('anvil_setNextBlockPrevRandao', hexbytes(header[13]))
        rpc('anvil_setCoinbase', hexbytes(header[2]))
        for tx in block[1]:
            rpc('eth_sendRawTransaction', hexbytes(network_form(tx, sidecars)))
        rpc('evm_mine')
        mined = rpc('eth_getBlockByNumber', n, False)
        expected = expected_header(block)
        compared.append({'number': n, 'hash': mined['hash'],
                         'differs': sorted(k for k, v in expected.items() if mined.get(k) != v)})
        hashes[hexbytes(keccak(rlp.encode(header)))] = mined['hash']
        # Withdrawals credit balances after the block's transactions; the replica has no
        # withdrawals, so the credit is applied before the next block.
        for withdrawal in block[3] if len(block) > 3 else []:
            address = hexbytes(withdrawal[2])
            balance = int(rpc('eth_getBalance', address, 'latest'), 16)
            rpc('anvil_setBalance', address, hex(balance + number(withdrawal[3]) * 10**9))
    return compared, hashes


def divergence(record):
    """Why a replica differs from its fixture, or None when every block reproduced."""
    differing = [f'block {b["number"]} ({", ".join(b["differs"])})' for b in record['blocks'] if b['differs']]
    return 'Replayed chain differs from the fixture at ' + '; '.join(differing) if differing else None


def anvil_command(chain):
    genesis = json.loads((Path(chain)/'genesis.json').read_text())
    fork = hardfork(genesis)
    if fork is None:
        raise ValueError('a replica runs one hardfork; this chain activates forks after genesis')
    return ['anvil', '--host', '0.0.0.0', '--port', '8545', '--init', '/chain/genesis.json',
            '--hardfork', fork, '--chain-id', str(genesis['config']['chainId']),
            '--gas-limit', str(int(genesis['gasLimit'], 16)), '--order', 'fifo', '--no-mining']


def capture(out, chain, cases, names, image_for):
    """Replay `chain` into each named build, send `cases` in order and retain every exchange.

    `image_for(name)` returns the verified local image of a locked build. Returns the per-build
    records the manifest keeps for setup verification and response mapping.
    """
    from .cli import ROOT, run
    folder = Path(out)/'replica'
    folder.mkdir(parents=True)
    sidecars = json.loads((ROOT/'fixtures/blobs.json').read_text())
    command = anvil_command(chain)
    records = {}
    for name in names:
        # The Foundry image's entrypoint is `/bin/sh -c`, so the command is one argument.
        container = run('docker', 'run', '-d', '-p', '127.0.0.1::8545', '-v', f'{Path(chain).resolve()}:/chain:ro',
                        image_for(name), ' '.join(command), capture=True).strip()
        try:
            port = run('docker', 'port', container, '8545/tcp', capture=True).split()[0].rsplit(':', 1)[1]
            rpc = Rpc(f'http://127.0.0.1:{port}')
            rpc.wait()
            about = dict(line.split(': ', 1) for line in run('docker', 'exec', container, 'anvil', '--version', capture=True).splitlines() if ': ' in line)
            compared, hashes = replay(rpc, chain, sidecars)
            with (folder/(name + '.exchanges.log')).open('w') as log:
                for case in cases:
                    request = json.loads(translate(json.dumps(case['request']), hashes))
                    try:
                        exchange = {'case': case['name'], 'request': request, 'raw_response': rpc.raw(request)}
                    except OSError as exc:
                        exchange = {'case': case['name'], 'request': request, 'error': repr(exc)}
                    log.write(json.dumps(exchange) + '\n')
        finally:
            logs = subprocess.run(['docker', 'logs', container], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
            (folder/(name + '.log')).write_bytes(logs.stdout)
            subprocess.run(['docker', 'rm', '-f', container], stdout=subprocess.DEVNULL, check=False)
        records[name] = {'command': command, 'version': f'anvil Version: {about["anvil Version"]}+{about["Commit SHA"][:8]}',
                         'blocks': compared, 'hashes': hashes}
    return records


def exchanges(out, name):
    from .cli import log_bytes
    return [json.loads(line) for line in log_bytes(Path(out)/'replica'/(name + '.exchanges.log')).decode().splitlines()]

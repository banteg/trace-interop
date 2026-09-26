"""Replica captures: replayability, faithful block comparison and hash mapping."""
import copy
import json
import tempfile
import unittest
from pathlib import Path

import rlp

from trace_interop.chain_model import load_chain
from trace_interop.cli import ROOT, collect, compatible, log_bytes, read, write
from trace_interop.replica import blocks, expected_header, hardfork, network_form, replay, translate

CHAINS = ROOT/'fixtures/chains'
HEAD = read(CHAINS/'initial/headblock.json')
REPLICA_HEAD = '0x' + 'ab' * 32


def request(method, *params):
    return {'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': list(params)}


class Replayability(unittest.TestCase):
    def test_only_chains_running_one_fork_from_genesis_replay(self):
        self.assertEqual(hardfork(read(CHAINS/'initial/genesis.json')), 'prague')
        self.assertIsNone(hardfork(read(CHAINS/'forks/genesis.json')))

    def test_replica_builds_skip_hive_scenarios_and_multi_fork_chains(self):
        anvil, reth, besu = ({'client': c} for c in ('anvil', 'reth', 'besu'))
        for corpus, expected in [('initial', True), ('mined-probes', True), ('callmany-isolation', True),
                                 ('forks', False), ('probes-forks', False), ('reorg-safe', False), ('pruned', False)]:
            with self.subTest(corpus=corpus):
                self.assertEqual(compatible(corpus, anvil), expected)
        self.assertTrue(compatible('pruned', reth))
        self.assertFalse(compatible('pruned', besu))
        self.assertTrue(compatible('forks', besu))


class BlockComparison(unittest.TestCase):
    def test_expected_header_uses_the_fixture_transactions_and_fields(self):
        chain = load_chain(CHAINS/'initial/chain.rlp')
        for block in blocks(CHAINS/'initial'):
            number = hex(int.from_bytes(block[0][8], 'big'))
            expected = expected_header(block)
            self.assertEqual(expected['transactions'], [t['hash'] for t in chain[number]['transactions']])
            if number == HEAD['number']:
                for field in ['gasLimit', 'gasUsed', 'timestamp', 'baseFeePerGas', 'receiptsRoot', 'transactionsRoot', 'logsBloom', 'mixHash', 'requestsHash', 'miner']:
                    self.assertEqual(expected[field], HEAD[field], field)

    def test_blob_transactions_regain_a_verified_sidecar(self):
        sidecars = read(ROOT/'fixtures/blobs.json')
        tx = next(bytes(t) for b in blocks(CHAINS/'initial') for t in b[1] if not isinstance(t, list) and t[0] == 3)
        wrapped = rlp.decode(network_form(tx, sidecars)[1:])
        self.assertEqual(rlp.encode(wrapped[0]), tx[1:])
        self.assertEqual([len(b) for b in wrapped[1]], [131072])
        tampered = copy.deepcopy(sidecars)
        entry = next(iter(tampered.values()))
        entry['commitment'] = entry['commitment'][:-2] + '00'
        with self.assertRaisesRegex(ValueError, 'commitment does not match'):
            network_form(tx, tampered)

    def test_replay_mines_each_block_and_credits_withdrawals_after_it(self):
        class Node:
            def __init__(self):
                self.calls, self.mined, self.balance = [], {}, {}

            def __call__(self, method, *params):
                self.calls.append(method)
                if method == 'evm_mine':
                    block = fixture[len(self.mined)]
                    self.mined[hex(len(self.mined) + 1)] = dict(expected_header(block), hash='0x%064x' % (len(self.mined) + 1))
                if method == 'eth_getBlockByNumber':
                    return {'hash': '0x' + '00' * 32} if params[0] == '0x0' else self.mined[params[0]]
                if method == 'eth_getBalance':
                    return hex(self.balance.get(params[0], 0))
                if method == 'anvil_setBalance':
                    self.balance[params[0]] = int(params[1], 16)
        fixture = list(blocks(CHAINS/'initial'))
        node = Node()
        compared, hashes = replay(node, CHAINS/'initial', read(ROOT/'fixtures/blobs.json'))
        self.assertEqual(len(compared), len(fixture))
        self.assertFalse(any(b['differs'] for b in compared))
        self.assertEqual(hashes[HEAD['hash']], '0x%064x' % int(HEAD['number'], 16))
        self.assertIn(HEAD['parentHash'], hashes)
        # A block's withdrawals follow its mining, never precede it.
        first = next(i for i, b in enumerate(fixture) if len(b) > 3 and b[3])
        mines = [i for i, m in enumerate(node.calls) if m == 'evm_mine']
        self.assertLess(mines[first], node.calls.index('anvil_setBalance'))
        self.assertTrue(node.balance)

    def test_translation_covers_prefixed_and_embedded_hashes(self):
        mapping = {'0x' + '11' * 32: '0x' + '22' * 32}
        text = json.dumps({'hash': '0x' + '11' * 32, 'mem': '0x00' + '11' * 32})
        self.assertEqual(json.loads(translate(text, mapping)), {'hash': '0x' + '22' * 32, 'mem': '0x00' + '22' * 32})


class ReplicaCollection(unittest.TestCase):
    def run_folder(self, folder, head=None, differs=()):
        replica_block = '0x' + 'cd' * 32
        cases = [{'name': '_control/head', 'request': request('eth_getBlockByNumber', HEAD['number'], False)},
                 {'name': '_control/latest', 'request': request('eth_getBlockByNumber', 'latest', False)},
                 {'name': 'block-hash', 'request': request('trace_block', HEAD['parentHash'])},
                 {'name': 'offline', 'request': request('trace_block', '0x2')}]
        hashes = {HEAD['hash']: REPLICA_HEAD, HEAD['parentHash']: replica_block}
        replayed = dict(head or HEAD, hash=REPLICA_HEAD, stateRoot='0x' + 'ee' * 32)
        write(folder/'manifest.json', {'corpus': 'initial', 'selected_cases': cases, 'head': HEAD, 'clients': {'anvil_development': {'client': 'anvil'}},
                                       'replica': {'anvil_development': {'version': 'anvil Version: 1.8.4-nightly+5a99f1a8', 'hashes': hashes,
                                                                         'blocks': [{'number': HEAD['number'], 'hash': REPLICA_HEAD, 'differs': list(differs)}]}}})
        exchanges = [{'case': '_control/head', 'request': cases[0]['request'], 'raw_response': json.dumps({'jsonrpc': '2.0', 'id': 1, 'result': replayed})},
                     {'case': '_control/latest', 'request': cases[1]['request'], 'raw_response': json.dumps({'jsonrpc': '2.0', 'id': 1, 'result': replayed})},
                     {'case': 'block-hash', 'request': request('trace_block', replica_block), 'raw_response': json.dumps({'jsonrpc': '2.0', 'id': 1, 'result': [{'blockHash': replica_block}]})},
                     {'case': 'offline', 'request': cases[3]['request'], 'error': 'ConnectionResetError()'}]
        (folder/'replica').mkdir()
        (folder/'replica/anvil_development.exchanges.log').write_text(''.join(json.dumps(e) + '\n' for e in exchanges))
        return collect(folder), replica_block

    def test_responses_map_back_to_fixture_hashes_and_keep_wire_bytes(self):
        from trace_interop.cli import load_observations
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d)
            summary, replica_block = self.run_folder(folder)
            observations = load_observations(folder)
            block = observations['block-hash']['anvil_development']
            self.assertEqual(block['response']['result'], [{'blockHash': HEAD['parentHash']}])
            self.assertIn(replica_block, block['raw_response'])
            self.assertEqual(observations['offline']['anvil_development']['status'], 'transport_error')
            self.assertEqual(summary['versions'], {'anvil_development': 'anvil Version: 1.8.4-nightly+5a99f1a8'})
            # The state root is the only head field a faithful replica may not reproduce.
            self.assertTrue(summary['eligible']['anvil_development'])
            self.assertEqual(summary['transport_errors'], [['offline', 'anvil_development']])
            self.assertTrue(log_bytes(folder/'replica/anvil_development.exchanges.log'))

    def test_a_differing_block_or_head_root_makes_the_replica_ineligible(self):
        for head, differs, reason in [(None, ['receiptsRoot'], 'differs from the fixture at block'),
                                      (dict(HEAD, transactionsRoot='0x' + '00' * 32), [], 'frozen canonical head')]:
            with self.subTest(reason=reason), tempfile.TemporaryDirectory() as d:
                summary, _ = self.run_folder(Path(d), head, differs)
                self.assertFalse(summary['eligible']['anvil_development'])
                self.assertIn(reason, summary['scenario']['anvil_development']['detail'])

    def test_a_request_the_manifest_did_not_select_is_a_harness_error(self):
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d)
            self.run_folder(folder)
            log = folder/'replica/anvil_development.exchanges.log'
            text = log_bytes(log).decode().replace('"trace_block", "params": ["0x2"]', '"trace_block", "params": ["0x3"]')
            Path(str(log) + '.gz').unlink()
            log.write_text(text)
            from trace_interop.cli import replica_observations
            observed = replica_observations(folder, read(folder/'manifest.json'), 'anvil_development')
            self.assertEqual(observed['offline']['status'], 'harness_error')


if __name__ == '__main__':
    unittest.main()

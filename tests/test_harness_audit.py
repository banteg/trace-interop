"""Counterexamples from the 2026-10-14 harness audit: malformed or contradictory client
responses are differences, never passes, skipped checks or crashes."""
import copy
import unittest

from eth_hash.auto import keccak
from test_execution_anchor_regressions import capture
from test_laws import CALL, case, frame, laws, located, ok

from scripts.build_fee_compat_fixtures import build as fee_compat
from scripts.build_fee_policy_fixtures import build as fee_policy
from trace_interop.cli import ROOT, read
from trace_interop.fee_policy import (
    BALANCE,
    MINER,
    SENDER,
    assess,
    assess_compatibility,
    expected_steps,
)
from trace_interop.isolation import isolate, resolve_dependencies
from trace_interop.oracles import IDENTITY, TREE, anchor
from trace_interop.scenarios import verify_setup, verify_state


def checksummed(address):
    digest = keccak(address[2:].lower().encode()).hex()
    return '0x' + ''.join(c.upper() if int(d, 16) >= 8 else c for c, d in zip(address[2:].lower(), digest))


class LawAudit(unittest.TestCase):
    def test_every_replay_is_compared_with_stored_frames(self):
        stored = [located([], 1), located([0])]
        replay = {'output': '0x', 'trace': [frame([], 1), frame([0])], 'stateDiff': None, 'vmTrace': None}
        cases = [case('stored', 'trace_transaction', ['0x' + '11' * 32]),
                 case('replay', 'trace_replayTransaction', ['0x' + '11' * 32, ['trace']]),
                 case('vm', 'trace_replayTransaction', ['0x' + '11' * 32, ['trace', 'vmTrace']]),
                 case('block', 'trace_replayBlockTransactions', ['0x2', ['trace']])]
        responses = {'stored': ok(stored), 'replay': ok(replay), 'vm': ok(replay), 'block': ok([replay])}
        self.assertEqual({law for law in laws(cases, responses) if law[0] == 'L07'}, {('L07', True)})
        for name, wrong in [('vm', ok(dict(replay, trace=[frame([])]))), ('block', ok([dict(replay, trace=[frame([])])]))]:
            with self.subTest(name=name):
                self.assertIn(('L07', False), laws(cases, responses | {name: wrong}))

    def test_malformed_records_violate_tree_and_filter_laws(self):
        stored = case('stored', 'trace_transaction', ['0x' + '11' * 32])
        self.assertIn(('L01', False), laws([stored], {'stored': ok([located([]), None])}))
        many = case('many', 'trace_callMany', [[[CALL, ['trace']]], '0x2'])
        self.assertIn(('L01', False), laws([many], {'many': ok([{'output': '0x', 'trace': [frame([]), 'bad']}])}))
        block = case('block', 'trace_block', ['0x2'])
        addressed = case('filter', 'trace_filter', [{'fromBlock': '0x2', 'toBlock': '0x2', 'fromAddress': [CALL['from']]}])
        for result in [[None], [located([]), 7]]:
            with self.subTest(result=result):
                self.assertIn(('L10', False), laws([block, addressed], {'block': ok([located([])]), 'filter': ok(result)}))


class MalformedResponses(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        header = read(ROOT/'fixtures/chains/raw-validation/headblock.json')
        environment = {k: int(header[v], 16) for k, v in [('BASEFEE', 'baseFeePerGas'), ('NUMBER', 'number'), ('TIMESTAMP', 'timestamp'), ('GASLIMIT', 'gasLimit')]}
        cls.cases = {c['name']: dict(c, context={'_environment': environment}) for c in fee_policy()['cases'] + fee_compat()['cases']}

    def test_fee_policy_null_response_and_error(self):
        for name, observation in [('typed-tip-limited/call/stateDiff', {'status': 'result', 'response': None}),
                                  ('legacy-one/call/none', {'status': 'rpc_error', 'response': None}),
                                  ('legacy-one/call/none', {'status': 'rpc_error', 'response': {'error': None}}),
                                  ('legacy-one/call/none', {'status': 'rpc_error', 'response': {'error': 'insufficient funds'}})]:
            with self.subTest(name=name, observation=observation):
                checks = assess(self.cases[name], observation)
                self.assertTrue(checks)
                self.assertNotIn('matches', [c['status'] for c in checks])

    def test_fee_compatibility_null_response(self):
        case = self.cases['legacy-zero/trace/trace']
        good = {'status': 'result', 'response': {'result': '0x01'}}
        for observation, peers in [({'status': 'result', 'response': None}, {case['fee_reference']: good}),
                                   ({'status': 'rpc_error', 'response': {'error': None}}, {case['fee_reference']: good}),
                                   ({'status': 'result', 'response': {'result': {'output': '0x01'}}}, {case['fee_reference']: {'status': 'result', 'response': None}})]:
            with self.subTest(observation=observation, peers=peers):
                self.assertEqual(assess_compatibility(case, observation, peers)[0]['status'], 'blocked')

    def test_scenario_controls_with_null_response(self):
        null = {'c': {'status': 'result', 'response': None}}
        self.assertFalse(verify_state('pruned', {}, {'old-header': null, 'old-nonce': {'c': {'status': 'rpc_error', 'response': None}}}, 'c')[0])
        self.assertFalse(verify_state('x', {'cases': [{'name': 'n', 'expected_control': '0x1'}]}, {'n': null}, 'c')[0])
        head = {k: '0x1' for k in ['number', 'hash', 'stateRoot', 'transactionsRoot', 'receiptsRoot']}
        request = lambda method, params: {'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}
        manifest = {'head': head, 'selected_cases': [{'name': '_control/head', 'request': request('eth_getBlockByNumber', ['0x1', False])},
                                                     {'name': '_control/latest', 'request': request('eth_getBlockByNumber', ['latest', False])},
                                                     {'name': 'height', 'request': request('eth_blockNumber', [])}]}
        observations = {'_control/head': {'c': {'status': 'result', 'response': {'result': head}}},
                        '_control/latest': {'c': {'status': 'result', 'response': {'result': head}}}, 'height': null}
        self.assertFalse(verify_setup(manifest, {}, observations, 'c')[0])
        self.assertFalse(verify_setup(dict(manifest, head={}), {}, observations, 'c')[0])

    def test_checksummed_state_diff_keys_settle(self):
        case = self.cases['typed-tip-limited/call/stateDiff']
        step = expected_steps(case)[0]
        price = 765625001
        output = '0x'+''.join(f'{word:064x}' for word in [price, 765625000, 2, 20, 100000000, BALANCE-200000*price-7, 0])
        sender_after = BALANCE-98623*price-7
        diff = {checksummed(SENDER): {'balance': {'*': {'from': hex(BALANCE), 'to': hex(sender_after)}}, 'nonce': {'*': {'from': '0xa', 'to': '0xb'}}},
                MINER: {'balance': {'+': hex(98623)}},
                checksummed(step['recipient']): {'balance': {'+': '0x7'}}}
        self.assertNotEqual(checksummed(SENDER), SENDER)
        self.assertNotEqual(checksummed(step['recipient']), step['recipient'])
        observation = {'status': 'result', 'response': {'result': {'output': output, 'stateDiff': diff}}}
        self.assertEqual({c['status'] for c in assess(case, observation)}, {'matches'})
        diff[checksummed(SENDER)]['nonce'] = '='
        self.assertIn('change_needed', [c['status'] for c in assess(case, observation)])


class IsolationAudit(unittest.TestCase):
    def test_owned_error_is_never_charged_to_the_result_check(self):
        call = {'name': 'call', 'request': {'method': 'trace_call', 'params': [CALL, ['trace'], 'latest']}}
        funds = {'status': 'rpc_error', 'response': {'error': {'code': -32000, 'message': 'insufficient funds for gas * price + value'}}}
        # Without the owner's check the rejection is unjudged, not the result check's defect.
        result = {'topic': 'H11', 'status': 'change_needed', 'role': 'result', 'requirement': 'Execute.', 'detail': ''}
        self.assertEqual([c['status'] for c in isolate(call, funds, [result])], ['blocked'])
        for owner, expected in [('change_needed', 'blocked'), ('blocked', 'blocked'), ('matches', 'not_applicable')]:
            with self.subTest(owner=owner):
                checks = [result, {'topic': 'H15', 'status': owner, 'role': 'rejection', 'requirement': 'Reject.', 'detail': ''}]
                self.assertEqual(isolate(call, funds, checks)[0]['status'], expected)

    def test_unjudged_own_dependency_falls_back_to_the_run(self):
        def records(own):
            return [{'case': 'page', 'checks': [{'topic': 'H03', 'status': 'change_needed', 'depends': ['H23'], 'detail': ''},
                                                {'topic': 'H23', 'status': own, 'detail': ''}]},
                    {'case': 'union', 'checks': [{'topic': 'H23', 'status': 'change_needed', 'detail': ''}]}]
        for own, expected in [('blocked', 'blocked'), ('unassessed', 'blocked'), ('change_needed', 'blocked'), ('matches', 'change_needed')]:
            with self.subTest(own=own):
                self.assertEqual(resolve_dependencies(records(own))[0]['checks'][0]['status'], expected)

    def test_successful_eth_call_differs_from_any_failed_trace_root(self):
        case = next(c for c in fee_compat()['cases'] if c['name'] == 'legacy-zero/trace/trace')
        output = '0x2a'
        trace = lambda error: {'status': 'result', 'response': {'result': {'output': output, 'trace': [{'traceAddress': [], 'error': error}]}}}
        error = lambda message: {'status': 'rpc_error', 'response': {'error': {'code': -32000, 'message': message}}}
        halt = error('EVM error: OutOfFunds')
        for eth, observation, expected in [({'status': 'result', 'response': {'result': output}}, trace('Out of gas'), 'change_needed'),
                                           (error('insufficient funds'), trace('Reverted'), 'change_needed'),
                                           (halt, trace('Out of gas'), 'blocked'),
                                           (halt, trace('Insufficient balance for transfer'), 'matches')]:
            with self.subTest(eth=eth, observation=observation):
                checks = assess_compatibility(case, observation, {case['fee_reference']: eth})
                self.assertEqual(checks[0]['status'], expected, checks)
        self.assertIn('unclassified root execution error: Out of gas', assess_compatibility(
            case, trace('Out of gas'), {case['fee_reference']: {'status': 'result', 'response': {'result': output}}})[0]['detail'])


class AnchorAudit(unittest.TestCase):
    def setUp(self):
        _, _, case, _, self.peers, _ = capture('a', 'filter-all', 'go-ethereum_trace')
        self.context = case['context']
        self.frames = self.peers['block-2']['response']['result']
        self.assertIsNotNone(anchor(self.context, self.peers, 'block-2')[0])

    def mismatch(self, frames):
        peers = copy.deepcopy(self.peers)
        peers['block-2']['response']['result'] = frames
        return anchor(self.context, peers, 'block-2')

    def test_structural_contradictions_are_mismatches(self):
        root = next(i for i, f in enumerate(self.frames) if f['action'].get('to') == TREE)
        create = next(i for i, f in enumerate(self.frames) if f['type'] == 'create' and f['traceAddress'] == [6])
        def changed(index, **fields):
            frames = copy.deepcopy(self.frames)
            frames[index].update(fields)
            return frames
        duplicate = copy.deepcopy(self.frames)
        duplicate.insert(root+1, dict(copy.deepcopy(self.frames[root]), subtraces=0))
        precompile = changed(root+1, action=dict(self.frames[root+1]['action'], to=IDENTITY))
        no_suicide = [f for f in changed(create, subtraces=0) if f['type'] != 'suicide']
        for label, frames in [('duplicate root', duplicate), ('wrong subtraces', changed(root, subtraces=6)),
                              ('invalid path', changed(root+1, traceAddress=['0x0'])),
                              ('six ordinary calls', precompile), ('missing suicide', no_suicide),
                              ('non-object record', self.frames + [None]), ('null result', None)]:
            with self.subTest(label=label):
                reference, mismatch = self.mismatch(frames)
                self.assertIsNone(reference)
                self.assertTrue(mismatch)

    def test_rewards_stay_with_h05(self):
        # A fabricated PoS reward is H05's defect; failing the reference would charge it to every filter decision.
        reward = {'type': 'reward', 'action': {'author': '0x' + '00' * 20, 'rewardType': 'block', 'value': '0x0'},
                  'traceAddress': [], 'subtraces': 0, 'blockNumber': 2, 'blockHash': self.frames[0]['blockHash']}
        self.assertEqual(self.mismatch(self.frames + [reward]), (self.frames + [reward], None))
        empty = {'cases': [{'name': 'block', 'request': {'method': 'trace_block', 'params': ['0x2']}}],
                 '_blocks': {'0x2': {'transactions': [], 'difficulty': 0}}}
        self.assertEqual(anchor(empty, {'block': ok([])}, 'block'), ([], None))
        self.assertEqual(anchor(empty, {'block': ok([reward])}, 'block'), (None, None))
        reference, mismatch = anchor(empty, {'block': ok([located([])])}, 'block')
        self.assertIsNone(reference)
        self.assertIn('empty proof-of-stake block', mismatch)


if __name__ == '__main__':
    unittest.main()

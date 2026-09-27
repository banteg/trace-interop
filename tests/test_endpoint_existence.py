"""Endpoint existence in stateDiff: a temporary account is omitted (H26), a born account has + markers (H17)."""
import copy
import unittest

from trace_interop.cli import ROOT, load_observations
from trace_interop.coverage import supplement
from trace_interop.report import run_context

EVAL = ROOT/'evidence/2026-09-27/eval/initial'


class EndpointExistenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.context = run_context(ROOT, {'corpus': 'initial'})
        cls.observations = load_observations(EVAL)

    def checks(self, name, client, topic, observation=None, expected=()):
        case = dict(next(c for c in self.context['cases'] if c['name'] == name), context=self.context)
        peers = {n: clients.get(client, {}) for n, clients in self.observations.items()}
        return [c for c in supplement(case, observation or peers[name], peers, [], list(expected)) if c['topic'] == topic]

    def created_child(self, trace_case, client):
        """The calltree child address a client's own trace reports, to corroborate the model."""
        result = self.observations[trace_case][client]['response']['result']
        frames = result['trace'] if isinstance(result, dict) else result
        return next(f['result']['address'] for f in frames if f['type'] == 'create')

    def test_temporary_account_is_derived_from_the_chain(self):
        for name, trace_case in [('call-tree-stateDiff', 'call-tree-trace'), ('replay-tree-stateDiff', 'replay-tree-trace')]:
            with self.subTest(case=name):
                [check] = self.checks(name, 'reth_development', 'H26')
                self.assertEqual(check['status'], 'matches')
                self.assertIn(self.created_child(trace_case, 'go-ethereum_trace'), check['detail'])

    def test_omitted_temporary_account_matches(self):
        for client in ['anvil_release', 'reth_development', 'nethermind_development', 'go-ethereum_trace']:
            for name in ['call-tree-stateDiff', 'replay-tree-stateDiff', 'replay-block-tree']:
                with self.subTest(client=client, case=name):
                    self.assertEqual({c['status'] for c in self.checks(name, client, 'H26')}, {'matches'})

    def test_false_death_of_a_temporary_account_is_an_h26_difference(self):
        for name in ['call-tree-stateDiff', 'replay-tree-stateDiff', 'replay-block-tree']:
            with self.subTest(case=name):
                failed = [c for c in self.checks(name, 'anvil_development', 'H26') if c['status'] == 'change_needed']
                self.assertEqual(len(failed), 1)
                self.assertIn("{'-': '0x0'}", failed[0]['detail'])
        # The reported temporary account is H26's alone, not also an H17 marker failure.
        h17 = self.checks('replay-tree-stateDiff', 'anvil_development', 'H17', expected=['H17'])
        self.assertEqual({c['status'] for c in h17}, {'matches'})

    def test_born_account_needs_creation_markers(self):
        # Block 0x2's third transaction deploys a contract; the Anvil nightly reports it with * markers.
        born = self.observations['replay-block-tree']['reth_development']['response']['result'][2]['stateDiff']
        address = next(a for a, account in born.items() if account['nonce'] == {'+': '0x1'})
        h17 = self.checks('replay-block-tree', 'anvil_development', 'H17', expected=['H17'])
        self.assertEqual([c['status'] for c in h17].count('change_needed'), 1)
        self.assertIn(address+': new account lacks creation markers', next(c['detail'] for c in h17 if c['status'] == 'change_needed'))

    def test_correct_born_markers_match_and_omission_differs(self):
        h17 = self.checks('replay-block-tree', 'reth_development', 'H17', expected=['H17'])
        self.assertEqual({c['status'] for c in h17}, {'matches'})
        observation = copy.deepcopy(self.observations['replay-block-tree']['reth_development'])
        diff = observation['response']['result'][2]['stateDiff']
        address = next(a for a, account in diff.items() if account['nonce'] == {'+': '0x1'})
        del diff[address]
        h17 = self.checks('replay-block-tree', 'reth_development', 'H17', observation, expected=['H17'])
        self.assertEqual([c['detail'] for c in h17 if c['status'] == 'change_needed'], [address+': new account omitted'])


if __name__ == '__main__':
    unittest.main()

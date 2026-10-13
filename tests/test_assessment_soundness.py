"""Counterexamples from the 2026-10-14 harness audit: vacuous passes, crashes and case-sensitive lookups."""
import copy
import unittest

from trace_interop.cli import ROOT, load_observations, read
from trace_interop.coverage import properties
from trace_interop.report import run_context
from trace_interop.rules import evaluate, pending_check

RUN = '2026-10-11/eval/'
CLIENT = 'go-ethereum_trace'


def captured(corpus, name, client=CLIENT):
    """A captured case with the frozen chain context every report assessment uses."""
    folder = ROOT/'evidence'/RUN/corpus
    manifest = read(folder/'manifest.json')
    observations = load_observations(folder)
    case = next(c for c in manifest['selected_cases'] if c['name'] == name)
    context = dict(run_context(ROOT, manifest), cases=manifest['selected_cases'])
    return dict(case, context=context), copy.deepcopy(observations[name][client]), {
        n: clients.get(client, {}) for n, clients in observations.items()}


def statuses(checks, topic):
    return [c['status'] for c in checks if c['topic'] == topic]


def assessed(case, observation, peers, topics):
    return properties(case, observation, peers, evaluate(case, observation, peers), topics)


class VmTraceEncoding(unittest.TestCase):
    def h21(self, ex, code='0x00'):
        case = {'name': 'replay-block-tree', 'topics': ['H21'], 'context': {},
                'request': {'method': 'trace_replayBlockTransactions', 'params': ['0x2', ['vmTrace']]}}
        op = {'pc': 0, 'cost': 3, 'ex': ex, 'sub': None}
        observation = {'status': 'result', 'response': {'result': [{'vmTrace': {'code': code, 'ops': [op]}}]}}
        return statuses(properties(case, observation, {}, [], {'H21'}), 'H21')

    def test_ex_must_be_an_object_or_null(self):
        good = {'used': 97, 'push': [], 'mem': None, 'store': None}
        self.assertEqual(self.h21(good), ['matches'])
        self.assertEqual(self.h21(None), ['matches'])
        for ex in ['corrupted', [], 123, {}, {'push': []}, dict(good, used=None)]:
            with self.subTest(ex=ex):
                self.assertEqual(self.h21(ex), ['change_needed'])

    def test_code_is_a_byte_string(self):
        for code in ['0x123', '0xAB', None, 7]:
            with self.subTest(code=code):
                self.assertEqual(self.h21(None, code), ['change_needed'])

    def test_captured_replay_still_matches(self):
        case, observation, peers = captured('initial', 'replay-block-tree')
        self.assertEqual(set(statuses(assessed(case, observation, peers, {'H21'}), 'H21')), {'matches'})
        observation['response']['result'][0]['vmTrace']['ops'][0]['ex'] = {}
        self.assertIn('change_needed', statuses(assessed(case, observation, peers, {'H21'}), 'H21'))


class CreationFields(unittest.TestCase):
    def mutate(self, corpus, name, change, topics=frozenset({'H10'})):
        case, observation, peers = captured(corpus, name)
        self.assertEqual(set(statuses(assessed(case, observation, peers, topics), 'H10')), {'matches'})
        change(observation['response']['result'])
        return statuses(assessed(case, observation, peers, topics), 'H10')

    def test_creation_values_are_well_formed(self):
        def root(result):
            return result['trace'][0]
        mutations = {
            'null values': lambda r: root(r).update(result={'address': None, 'code': None, 'gasUsed': None}),
            'uppercase code': lambda r: root(r)['result'].update(code='0xAB'),
            'non-minimal gasUsed': lambda r: root(r)['result'].update(gasUsed='0x0da'),
            'short address': lambda r: root(r)['result'].update(address='0x1234'),
            'missing creationMethod': lambda r: root(r)['action'].pop('creationMethod'),
            'unknown creationMethod': lambda r: root(r)['action'].update(creationMethod='create3'),
        }
        for label, change in mutations.items():
            with self.subTest(label=label):
                self.assertIn('change_needed', self.mutate('initial', 'call-constructor-priced', change))

    def test_failed_creation_still_names_its_method(self):
        def fail(result):
            result['trace'][0].update(error='Out of gas', result=None)
            result['trace'][0]['action'].pop('creationMethod')
        self.assertIn('change_needed', self.mutate('initial', 'call-constructor-priced', fail))

    def test_requested_creation_trace_has_its_root(self):
        self.assertEqual(['change_needed'], self.mutate('initial', 'call-constructor-priced', lambda r: r.update(trace=[]), set()))

    def test_mined_creation_frames_are_checked(self):
        def strip(result):
            create = next(f for f in result if f['type'] == 'create' and 'error' not in f)
            create['result'] = {'address': None, 'code': None, 'gasUsed': None}
        self.assertIn('change_needed', self.mutate('initial', 'block-tree', strip))


class PosRewards(unittest.TestCase):
    def test_empty_or_malformed_records_are_not_reward_free(self):
        for name in ['block-transfer', 'block-tree', 'filter-all', 'filter-empty']:
            # An empty list shows no omitted reward; its missing inventory is H02's, H03's or H04's difference.
            for bad, verdict in [([], 'blocked'), ([None], 'change_needed'), (['frame'], 'change_needed'), ({}, 'change_needed')]:
                with self.subTest(name=name, bad=bad):
                    case, observation, peers = captured('initial', name)
                    self.assertEqual(statuses(assessed(case, observation, peers, {'H05'}), 'H05'), ['matches'])
                    observation['response']['result'] = bad
                    self.assertEqual(statuses(assessed(case, observation, peers, {'H05'}), 'H05'), [verdict])

    def test_partial_records_are_not_reward_free(self):
        case, observation, peers = captured('initial', 'block-tree')
        result = observation['response']['result']
        observation['response']['result'] = [f for f in result if f['transactionHash'] == result[0]['transactionHash']]
        self.assertEqual(statuses(assessed(case, observation, peers, {'H05'}), 'H05'), ['blocked'])
        result.append(dict(result[0], type='reward', transactionHash=None))
        observation['response']['result'] = result
        self.assertEqual(statuses(assessed(case, observation, peers, {'H05'}), 'H05'), ['change_needed'])

    def test_address_filtered_selection_may_be_empty(self):
        case, observation, peers = captured('fork-followup', 'withdrawal-filter-52')
        self.assertEqual(observation['response']['result'], [])
        self.assertEqual(statuses(assessed(case, observation, peers, {'H05'}), 'H05'), ['matches'])
        observation['response']['result'] = [None]
        self.assertEqual(statuses(assessed(case, observation, peers, {'H05'}), 'H05'), ['change_needed'])


class UnhashableValues(unittest.TestCase):
    context = {'_environment': {'NUMBER': 48}, '_blocks': {'0x30': {'transactions': [{'hash': '0x' + '11'*32}]}}}

    def test_pending_block_numbers(self):
        for result in [[{'blockNumber': []}], [{'blockNumber': {}}, {'blockNumber': 49}], [{'blockNumber': 49}, {'blockNumber': None}, {'blockNumber': '0x31'}]]:
            with self.subTest(result=result):
                check = pending_check('trace_block', ['pending'], 'result', {'result': result}, result, self.context)
                self.assertEqual(check['status'], 'change_needed')
        result = [{'blockNumber': 49}, {'blockNumber': 49}]
        self.assertEqual(pending_check('trace_block', ['pending'], 'result', {'result': result}, result, self.context)['status'], 'matches')

    def test_pending_replay_hashes(self):
        for result in [[{'transactionHash': []}], [{'transactionHash': {}}], [None]]:
            with self.subTest(result=result):
                check = pending_check('trace_replayBlockTransactions', ['pending', ['trace']], 'result', {'result': result}, result, self.context)
                self.assertEqual(check['status'], 'change_needed')
        result = [{'transactionHash': '0x' + '22'*32}]
        check = pending_check('trace_replayBlockTransactions', ['pending', ['trace']], 'result', {'result': result}, result, self.context)
        self.assertEqual(check['status'], 'matches')

    def test_pending_filter_observation(self):
        case = {'name': 'filter-pending', 'context': {'_chain': 'h30'},
                'request': {'method': 'trace_filter', 'params': [{'fromBlock': 'pending', 'toBlock': 'pending', 'count': 3}]}}
        for result in [[{'blockNumber': 48}, {'blockNumber': None}, {'blockNumber': '0x30'}], [{'blockNumber': []}]]:
            with self.subTest(result=result):
                checks = evaluate(case, {'status': 'result', 'response': {'result': result}}, {})
                self.assertIn('observation', statuses(checks, 'H32'))


class ChecksummedStateDiff(unittest.TestCase):
    def checksum(self, observation, address):
        diff = observation['response']['result']['stateDiff']
        diff['0x' + address[2:].upper()] = diff.pop(address)

    def destroyed(self):
        """destroy-trace-55 with its account moved to an address that has letters to checksum."""
        case, observation, peers = captured('fork-followup', 'destroy-trace-55')
        old, new = case['request']['params'][0]['to'], '0x' + 'ab'*20
        case['request']['params'][0]['to'] = new
        case['context']['_alloc'][new] = case['context']['_alloc'].pop(old)
        diff = observation['response']['result']['stateDiff']
        diff[new] = diff.pop(old)
        return case, observation, peers, new

    def test_rule_lookups_ignore_address_case(self):
        for corpus, name, topic, address in [
                ('a', 'prefunded-empty', 'H17', lambda c: c['request']['params'][0]['to']),
                ('a', 'auth-set', 'H18', lambda c: c['context']['contracts']['undelegated']['address'])]:
            with self.subTest(name=name):
                case, observation, peers = captured(corpus, name)
                self.assertEqual(statuses(evaluate(case, observation, peers), topic), ['matches'])
                self.checksum(observation, address(case))
                self.assertEqual(statuses(evaluate(case, observation, peers), topic), ['matches'])
        case, observation, peers, address = self.destroyed()
        self.assertEqual(statuses(evaluate(case, observation, peers), 'H26'), ['matches'] * 2)
        self.checksum(observation, address)
        self.assertEqual(statuses(evaluate(case, observation, peers), 'H26'), ['matches'] * 2)

    def test_conflicting_spellings_fail(self):
        case, observation, peers, address = self.destroyed()
        diff = observation['response']['result']['stateDiff']
        diff['0x' + address[2:].upper()] = {'balance': '=', 'code': '=', 'nonce': '=', 'storage': {}}
        self.assertIn('change_needed', statuses(evaluate(case, observation, peers), 'H26'))

    def test_model_creation_lookup_ignores_address_case(self):
        case, observation, peers = captured('coverage', 'model-return42')
        before = statuses(assessed(case, observation, peers, set(case.get('topics', []))), 'H17')
        self.assertIn('matches', before)
        root = observation['response']['result']['trace'][0]
        self.checksum(observation, root['result']['address'])
        self.assertEqual(statuses(assessed(case, observation, peers, set(case.get('topics', []))), 'H17'), before)

    def test_unknown_deleted_balance_is_unassessed(self):
        case, observation, peers = captured('fork-followup', 'destroy-trace-55')
        del case['context']['_alloc']
        exact = [c['status'] for c in evaluate(case, observation, peers) if c['requirement'].startswith('Report the exact deleted balance')]
        self.assertEqual(exact, ['unassessed'])


if __name__ == '__main__':
    unittest.main()

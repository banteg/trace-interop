"""One defect is judged under the one decision whose rule it breaks (trace_interop.isolation).

Each leak test assesses a captured response of the 2026-09-26 matrix. `raw` checks are tagged by their
assertion sites but not yet isolated; the pipeline reports the isolated ones.
"""
from functools import lru_cache
import re
import unittest

from trace_interop.cli import ROOT, load_observations, read
from trace_interop.coverage import properties
from trace_interop.inventory import report_runs
from trace_interop.isolation import error_owner, isolate, resolve_dependencies
from trace_interop.report import run_context
from trace_interop.rules import accounting_topic, evaluate, mapping
from trace_interop.scenarios import assessed_cases
from trace_interop.validation import request_errors

MATRIX = ROOT/'evidence/2026-09-26/anvil'
DECISIONS = {d['id']: d for d in read(ROOT/'decisions/ledger.json')['items']}
METHODS = {m['name']: m for m in read(ROOT/'spec/trace-openrpc.json')['methods']}
ACCOUNTING = r'^(Account balance deltas|Transfer \d+: exact)'


@lru_cache(maxsize=None)
def captured_run(folder):
    manifest = read(folder/'manifest.json')
    context = run_context(ROOT, manifest)
    cases = assessed_cases(manifest['selected_cases'], context['cases'])
    return dict(context, cases=cases), {c['name']: c for c in cases}, load_observations(folder)


def raw(corpus, name, client):
    """(case, observation, checks) for one captured response, before isolation."""
    context, cases, observations = captured_run(MATRIX/corpus)
    case = dict(cases[name], context=context)
    peers = {n: clients.get(client, {}) for n, clients in observations.items()}
    expected = [t for t, d in DECISIONS.items() if f'{corpus}/{name}' in d['cases']]
    checks = evaluate(case, peers[name], peers, invalid_params=request_errors(case['request'], METHODS))
    return case, peers[name], properties(case, peers[name], peers, checks, expected)


def assessed(corpus, name, client):
    return isolate(*raw(corpus, name, client))


def statuses(checks, topic, pattern=''):
    return [c['status'] for c in checks if c['topic'] == topic and re.search(pattern, c['requirement'])]


class LeakTests(unittest.TestCase):
    def test_unsigned_accounting_is_judged_under_h15(self):
        # Before: 21 Erigon and 20 Reth H16 failures were unsigned trace_call/trace_callMany accounting.
        for client in ['erigon_development', 'reth_development']:
            for corpus, name in [('initial', 'call-transfer-stateDiff'), ('coverage', 'model-transfer'),
                                 ('coverage', 'model-many-transfers'), ('a', 'many-storage-write-read')]:
                with self.subTest(client=client, case=name):
                    checks = assessed(corpus, name, client)
                    self.assertIn('change_needed', statuses(checks, 'H15', ACCOUNTING))
                    self.assertEqual(statuses(checks, 'H16', ACCOUNTING), [])
                    self.assertNotIn('change_needed', statuses(checks, 'H16'))
        # Mined replay accounting stays H16.
        checks = assessed('mined-probes', 'replay-block-2', 'besu_development')
        self.assertIn('change_needed', statuses(checks, 'H16', ACCOUNTING))
        self.assertEqual(statuses(checks, 'H15', ACCOUNTING), [])
        # A single unsigned call declared under H16 has nothing H16 judges.
        self.assertEqual(statuses(assessed('initial', 'call-tree-stateDiff', 'erigon_development'), 'H16'), ['not_applicable'])

    def test_missing_transaction_lookup_is_h06(self):
        # Before: Nethermind's only H02 failure was trace_get of a transaction that is not in the chain.
        checks = assessed('initial', 'get-missing-tx', 'nethermind_development')
        self.assertEqual(statuses(checks, 'H06'), ['change_needed'])
        self.assertEqual(statuses(checks, 'H02'), ['not_applicable'])
        # A missing path within an existing transaction is H02's path selection.
        checks = assessed('initial', 'get-missing', 'nethermind_release')
        self.assertEqual(statuses(checks, 'H02'), ['change_needed'])
        self.assertEqual(statuses(checks, 'H06'), ['not_applicable'])

    def test_result_checks_are_blocked_on_owned_errors(self):
        for corpus, name, client, topic, owner in [
                ('initial', 'call-many', 'erigon_development', 'H16', 'H15'),
                ('initial', 'call-empty-types', 'erigon_development', 'H11', 'H15'),
                ('fee-policy', 'defaults-cap-only-zero/many/none', 'besu_development', 'H16', 'H25'),
                ('initial', 'call-many', 'besu_development', 'H16', 'H25')]:
            with self.subTest(client=client, case=name):
                case, observation, checks = raw(corpus, name, client)
                self.assertEqual(statuses(checks, topic), ['change_needed'])
                isolated = isolate(case, observation, checks)
                self.assertEqual(statuses(isolated, topic), ['blocked'])
                self.assertIn(owner+' owns this error', next(c['detail'] for c in isolated if c['topic'] == topic))
                self.assertIn('change_needed', statuses(isolated, owner))
        # No rule identifies Nethermind's leaked collection exception, so the empty selection still differs (H11).
        checks = assessed('initial', 'call-empty-types', 'nethermind_release')
        self.assertEqual(statuses(checks, 'H11'), ['change_needed'])

    def test_paging_depends_on_reward_matching(self):
        client = 'nethermind_development'
        window = {'case': 'rewards-window', 'checks': raw('probes-forks', 'rewards-window', client)[2]}
        union = {'case': 'rewards-union', 'checks': assessed('probes-forks', 'rewards-union', client)}
        self.assertEqual([(c['status'], c['depends']) for c in window['checks'] if c['topic'] == 'H03'], [('change_needed', ['H23'])])
        self.assertEqual(statuses(union['checks'], 'H23'), ['change_needed'])
        resolve_dependencies([window, union])
        self.assertEqual(statuses(window['checks'], 'H03'), ['blocked'])
        self.assertIn('Depends on H23, which differs for this build in rewards-union', window['checks'][0]['detail'])
        # While H23 matches, the page is judged on its own.
        window = {'case': 'rewards-window', 'checks': raw('probes-forks', 'rewards-window', client)[2]}
        resolve_dependencies([window, {'case': 'rewards-union', 'checks': [dict(c, status='matches') for c in union['checks']]}])
        self.assertEqual(statuses(window['checks'], 'H03'), ['change_needed'])

    def test_vmtrace_content_is_not_validation(self):
        checks = assessed('raw-validation', 'raw-validation-execution-oog-valid-all', 'nethermind_development')
        self.assertEqual(statuses(checks, 'H13', 'vmTrace'), [])
        self.assertEqual(statuses(checks, 'H19', 'vmTrace'), ['matches'])
        self.assertEqual(statuses(checks, 'H20', 'vmTrace'), ['change_needed'])

    def test_schema_rejection_yields_to_the_owning_decision(self):
        for corpus, name, client, owner in [('h30', 'filter-pending', 'besu_development', 'H32'),
                                            ('a', 'filter-both-unknown-mode', 'nethermind_development', 'H03')]:
            with self.subTest(client=client, case=name):
                case, observation, checks = raw(corpus, name, client)
                self.assertEqual(statuses(checks, 'H14'), ['change_needed'])
                isolated = isolate(case, observation, checks)
                self.assertEqual(statuses(isolated, 'H14'), ['not_applicable'])
                self.assertTrue(next(c['detail'] for c in isolated if c['topic'] == 'H14').startswith(owner+' owns'))
                self.assertEqual(statuses(isolated, owner), ['change_needed'])


class LeakGuard(unittest.TestCase):
    """No response in the published assessment fails two decisions for one defect."""
    CLASSES = {
        'rejection code': r'-32602|invalid params',
        'null lookup': r'\bnull\b',
        # Checks that read an executed result; acceptance and envelope-form checks judge the error itself.
        'executed result': r'^(?!Return one complete JSON-RPC)(?!.*accept).*(execut|envelope|return bytes|returns word|output)',
    }

    @classmethod
    def setUpClass(cls):
        cls.records = read(ROOT/'reports/checks.json')
        cls.runs = {path.name: path for path in report_runs(ROOT)}

    def error_owner(self, record):
        observations = captured_run(self.runs[record['run']])[2]
        observation = observations[record['case']][record['client']]
        return error_owner(record['method'], mapping(observation.get('response')))

    def test_one_decision_per_defect(self):
        for record in self.records:
            failing = [c for c in record['checks'] if c['status'] == 'change_needed']
            where = (record['client'], record['corpus'], record['case'])
            for check in record['checks']:
                if re.search(ACCOUNTING, check['requirement']):
                    self.assertEqual(check['topic'], accounting_topic(record['method']), where)
                if 'vmTrace' in check['requirement']:
                    self.assertNotEqual(check['topic'], 'H13', where)
            for name, pattern in self.CLASSES.items():
                topics = {c['topic'] for c in failing if re.search(pattern, c['requirement'])}
                if len(topics) < 2:
                    continue
                # An error no decision's rule identifies cannot be attributed; every other double failure is a leak.
                self.assertEqual(name, 'executed result', (where, topics))
                self.assertIsNone(self.error_owner(record), (where, topics))

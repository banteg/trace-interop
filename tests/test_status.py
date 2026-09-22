import copy
from pathlib import Path
import unittest

from trace_interop.status import decision_status, NATIVE_CLIENTS


class DecisionStatusTests(unittest.TestCase):
    def setUp(self):
        self.decision = {'id': 'H03', 'cases': ['a/filter']}
        self.position = {'policy': 'converged', 'note': 'Direction agreed.', 'sources': [{'label': 'Client review', 'url': 'https://example.org/review'}]}
        self.records = [dict(build_id='sha256:build', captured_at='2026-09-23T00:00:00+00:00', client=f'{family}_{channel}', corpus='a', case='filter', eligible=True,
                             checks=[{'topic': 'H03', 'status': 'matches'}], schema={'status': 'valid'})
                        for family in NATIVE_CLIENTS for channel in ['development', 'release']]

    def label(self, records=None, position=None):
        return decision_status(self.decision, self.records if records is None else records,
                               self.position if position is None else position)

    def test_milestones_require_policy_and_both_channels(self):
        self.assertEqual(self.label(position={}), '⚪ Under review')
        self.assertEqual(self.label(position=dict(self.position, policy='diverging')), '🔀 Diverging')
        self.assertEqual(self.label(records=[]), '🤝 Converged')
        self.assertEqual(self.label(records=[r for r in self.records if r['client'].endswith('_development')]), '🧪 Harmonized · dev')
        self.assertEqual(self.label(), '✅ Harmonized · stable')

    def test_incomplete_or_failing_evidence_blocks_harmonization(self):
        for status in ['change_needed', 'unsupported', 'unassessed', 'observation']:
            records = copy.deepcopy(self.records)
            records[0]['checks'][0]['status'] = status
            self.assertEqual(self.label(records), '🤝 Converged')
        for change in [{'eligible': False}, {'checks': []}, {'schema': {'status': 'invalid'}}]:
            records = copy.deepcopy(self.records); records[0].update(change)
            self.assertEqual(self.label(records), '🤝 Converged')
        self.assertEqual(self.label(self.records[1:]), '🤝 Converged')

    def test_missing_declared_case_and_empty_scope_block_harmonization(self):
        self.decision['cases'].append('a/uncaptured')
        self.assertEqual(self.label(), '🤝 Converged')
        self.decision['cases'] = []
        self.assertEqual(self.label(), '🤝 Converged')

    def test_geth_fork_cannot_replace_native_client(self):
        records = copy.deepcopy(self.records)
        records[0]['client'] = 'go-ethereum_trace'
        self.assertEqual(self.label(records), '🤝 Converged')

    def test_policy_conclusions_require_provenance(self):
        for position in [{'policy': 'converged'}, {'policy': 'diverging'}, {'policy': 'typo'}]:
            with self.assertRaises(ValueError): self.label(position=position)

    def test_published_status_is_consistent_across_views(self):
        root = Path(__file__).resolve().parents[1]
        index = (root/'decisions/README.md').read_text()
        overview = (root/'reports/README.md').read_text()
        self.assertIn('## Status key', index)
        for topic, label in [('H03', '🤝 Converged'), ('H13', '🤝 Converged')]:
            page = (root/f'reports/decisions/{topic}.md').read_text()
            self.assertIn(f'**Status: {label}**', page)
            self.assertIn('Policy evidence:', page)
            self.assertTrue(any(topic in line and label in line for line in index.splitlines()))
            self.assertTrue(any(topic in line and label in line for line in overview.splitlines()))

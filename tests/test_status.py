import copy
from pathlib import Path
import unittest

from trace_interop.presentation import check_fixes, merged_fixes
from trace_interop.status import check_positions, client_positions, decision_status, NATIVE_CLIENTS


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

    def test_build_provenance_is_required(self):
        for change in [{'build_id':None}, {'captured_at':None}, {'captured_at':'bad'}, {'captured_at':'2026-09-23'}]:
            records = copy.deepcopy(self.records); records[0].update(change)
            self.assertEqual(self.label(records),'🤝 Converged')
        records = copy.deepcopy(self.records)
        records.append(dict(records[0],build_id='ambiguous-build'))
        self.assertEqual(self.label(records),'🤝 Converged')

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


class ClientPositionTests(unittest.TestCase):
    source = {'label': 'Client review', 'url': 'https://example.org/review'}

    def entry(self, **change):
        return {'position': 'agree', 'note': 'Agrees.', 'sources': [self.source]} | change

    def test_positions_need_known_clients_decisions_and_provenance(self):
        check_positions({'H03': {'positions': {'erigon': self.entry()}}}, {'H03'})
        for status in [{'H99': {'positions': {}}}, {'H03': {'positions': {'geth': self.entry()}}},
                       *({'H03': {'positions': {'erigon': self.entry(**change)}}} for change in
                         [{'position': 'maybe'}, {'note': ''}, {'sources': []}, {'sources': [{'label': 'No link'}]}])]:
            with self.subTest(status=status), self.assertRaises(ValueError):
                check_positions(status, {'H03'})

    def test_merged_complete_fixes_imply_agreement(self):
        prs = [dict(url=f'https://github.com/paradigmxyz/reth/pull/{n}', title='fix: trace', client=client, decisions=['H03'],
                    state=state, draft=False, merged_at='2026-09-22T00:00:00Z' if state == 'merged' else None, **extra)
               for n, (client, state, extra) in enumerate([('reth', 'merged', {}), ('reth', 'open', {}), ('reth', 'merged', {'partial': ['H03']}),
                                                           ('geth', 'merged', {}), (None, 'merged', {}), ('erigon', 'merged', {'uptake': {'merge_commit': 'a' * 40}})], 1)]
        fixes = check_fixes({'repositories': {'paradigmxyz/reth': 'Reth'}, 'prs': prs}, {'H03', 'H04'}, [*NATIVE_CLIENTS, 'geth'])
        self.assertEqual(merged_fixes(fixes, 'H03'), [('reth', {'label': 'Reth #1', 'url': prs[0]['url']}),
                                                      ('erigon', {'label': 'Reth #6', 'url': prs[5]['url']})])
        self.assertEqual(merged_fixes(fixes, 'H04'), [])

    def test_recorded_positions_win_and_keep_fix_sources(self):
        fix = {'label': 'Erigon #1', 'url': 'https://example.org/fix'}
        positions = client_positions({'erigon': self.entry(position='conditional')}, [('erigon', fix), ('reth', fix)])
        self.assertEqual(positions['erigon'], self.entry(position='conditional', sources=[self.source, fix]))
        self.assertEqual(positions['reth']['position'], 'agree')
        self.assertEqual(positions['reth']['sources'], [fix])
        self.assertEqual(client_positions({}, []), {})

    def test_published_positions(self):
        root = Path(__file__).resolve().parents[1]
        page = (root/'reports/decisions/H03.md').read_text()
        self.assertIn('| Erigon | 👍 Agrees |', page)
        self.assertIn('| Besu | · No response |', page)
        self.assertIn('[Alloy #4216](https://github.com/alloy-rs/alloy/pull/4216)', page)
        index = (root/'decisions/README.md').read_text()
        self.assertTrue(any('[H03]' in line and '| ·👍·👍 |' in line for line in index.splitlines()))
        self.assertIn('### Client positions', index)

"""Guard against misleading verdicts in maintainer reports."""
import json
import re
import unittest
from pathlib import Path

from trace_interop.presentation import outcome, verdict, examples, source_url, build_rows, build_label, version_label, coverage_summary


class ReportVerdictTests(unittest.TestCase):
    def test_expected_rpc_error_is_not_a_failed_check(self):
        entry = {'record': {'eligible': True, 'status': 'rpc_error'},
                 'observation': {'response': {'error': {'code': -32602}}}}
        self.assertEqual(outcome(entry), 'RPC error `-32602`')
        self.assertEqual(verdict([{'status': 'matches'}]), 'Checked cases agree')

    def test_extension_observation_is_neither_pass_nor_failure(self):
        self.assertEqual(verdict([{'status': 'matches'}, {'status': 'observation'}]), 'Policy open')
        self.assertEqual(verdict([{'status': 'change_needed'}, {'status': 'observation'}]), 'Differs')

    def test_setup_failure_cannot_be_reported_as_observed_behavior(self):
        entry = {'record': {'eligible': False, 'status': 'result'},
                 'observation': {'response': {'result': []}}}
        self.assertEqual(outcome(entry), 'Setup incomplete; not assessed')
        self.assertEqual(verdict([]), 'Not assessed')

    def test_one_difference_cannot_be_hidden_by_matching_cases(self):
        checks = [{'status': 'matches'}] * 20 + [{'status': 'change_needed'}]
        self.assertEqual(verdict(checks), 'Differs')
        self.assertEqual(verdict([{'status': 'unsupported'}]), 'Method unavailable')

    def test_missing_object_is_distinct_from_empty_collection(self):
        entry = {'record': {'eligible': True, 'status': 'result'},
                 'observation': {'response': {'result': None}}}
        self.assertEqual(outcome(entry), '`null`')
        entry['observation']['response']['result'] = []
        self.assertEqual(outcome(entry), '`[]`')

    def test_examples_prioritize_counterexample_over_success(self):
        checks = [{'status': 'matches', 'corpus': 'a', 'case': 'first'},
                  {'status': 'change_needed', 'corpus': 'z', 'case': 'counterexample'}]
        self.assertIn('counterexample.md', examples(Path('/reports'), Path('/reports/clients'), checks, 1))

    def test_examples_link_to_the_reason_for_an_open_or_partial_verdict(self):
        for status in ['observation', 'blocked', 'unassessed']:
            checks = [{'status':'matches', 'corpus':'a', 'case':'first'},
                      {'status':status, 'corpus':'z', 'case':'reason'}]
            self.assertIn('reason.md', examples(Path('/reports'), Path('/reports/clients'), checks, 1))

    def test_commit_dates_match_exact_version_not_image_or_channel(self):
        runs = [
            {'path': Path('/reports/run1.json'), 'versions': {'reth_development': 'old'},
             'manifest': {'started_at': '2026-09-21T01:00:00+04:00', 'clients': {
                 'reth_development': {'image_id': 'one', 'created': '2026-09-19T05:00:00Z',
                                      'labels': {'org.opencontainers.image.created': '2000-01-01T00:00:00Z'}}}}},
            {'path': Path('/reports/run2.json'), 'versions': {'reth_development': 'new'},
             'manifest': {'started_at': '2026-09-21T12:00:00Z', 'clients': {
                 'reth_development': {'image_id': 'two'}}}},
        ]
        revisions = {'reth_development': [{'version': 'old', 'committed_at': '2026-09-18T12:00:00Z',
                                             'repository': 'https://github.com/paradigmxyz/reth', 'commit': 'a' * 40}]}
        rows = build_rows(['reth_development'], runs, revisions, Path('/reports/clients'))
        self.assertEqual(rows[0][0], '`old`')
        self.assertEqual(rows[0][2], '2026-09-18')
        self.assertIn('/commit/' + 'a' * 40, rows[0][1])
        self.assertIn('2026-09-20', rows[0][3])
        self.assertEqual(rows[1][:3], ['`new`', 'Not recorded', 'Not recorded'])
        self.assertEqual(build_label('reth_development', 'old', revisions), 'old · aaaaaaaa')
        self.assertEqual(build_label('reth_development', 'new', revisions), 'new · commit not recorded')
        self.assertIn('2026-09-21', rows[1][3])

    def test_build_versions_omit_platform_and_duplicate_commit(self):
        for version,expected in [
            ('Reth Version: 2.6.0+73a3a008','2.6.0'),
            ('3.8.0-dev-e26d9bd4','3.8.0-dev'),
            ('2.1.0-unstable+2a3b2531','2.1.0-unstable'),
            ('besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25','26.9-develop'),
            ('Geth/v1.17.7-unstable-fa8ecb92-2026-09-24/linux-amd64/go1.26.1','1.17.7-unstable'),
        ]:
            self.assertEqual(version_label(version), expected)

    def test_open_policy_is_distinct_from_blocked_or_uncovered_cases(self):
        matched = dict(status='matches',corpus='fee-policy',case='priced')
        opened = dict(status='observation',corpus='fee-policy',case='defaults')
        blocked = dict(status='blocked',corpus='fee-policy',case='invalid',detail='Cannot inspect this property: malformed_json.')
        self.assertEqual(verdict([matched, opened]), 'Policy open')
        self.assertEqual(verdict([matched, opened, blocked]), 'Partially assessed')
        self.assertEqual(coverage_summary([matched, opened, blocked, blocked]),
                         '1 blocked case: malformed JSON response. 1 policy-open case.')
        self.assertEqual(verdict([matched, dict(status='unassessed')]), 'Partially assessed')

    def test_source_catalog_uses_immutable_revisions_and_line_anchors(self):
        root = Path(__file__).resolve().parents[1]
        catalog = json.loads((root/'decisions/sources.json').read_text())
        for client, refs in catalog.items():
            for ref in refs.values():
                with self.subTest(client=client, path=ref['path']):
                    self.assertRegex(ref['commit'], r'^[a-f0-9]{40}$')
                    self.assertRegex(ref['sha256'], r'^[a-f0-9]{64}$')
                    self.assertGreater(ref['line'], 0)
                    self.assertTrue(ref['anchor'])
                    self.assertTrue(source_url(ref).endswith(f'#L{ref["line"]}'))

    def test_generated_reports_have_no_broken_local_file_links(self):
        root = Path(__file__).resolve().parents[1]
        paths = [root/'README.md', root/'decisions/README.md', *(root/'reports').rglob('*.md'), *(root/'docs').rglob('*.md')]
        for path in paths:
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                target = target.split('#')[0]
                with self.subTest(page=str(path.relative_to(root)), target=target):
                    self.assertTrue((path.parent/target).exists(), target)

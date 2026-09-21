"""Guard against misleading verdicts in maintainer reports."""
import json
import re
import unittest
from pathlib import Path

from trace_interop.presentation import outcome, verdict, examples, source_url


class ReportVerdictTests(unittest.TestCase):
    def test_expected_rpc_error_is_not_a_failed_check(self):
        entry = {'record': {'eligible': True, 'status': 'rpc_error'},
                 'observation': {'response': {'error': {'code': -32602}}}}
        self.assertEqual(outcome(entry), 'RPC error `-32602`')
        self.assertEqual(verdict([{'status': 'matches'}]), 'Checked cases agree')

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
        paths = [root/'README.md', root/'decisions/README.md', *(root/'reports').rglob('*.md')]
        for path in paths:
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                target = target.split('#')[0]
                with self.subTest(page=str(path.relative_to(root)), target=target):
                    self.assertTrue((path.parent/target).exists(), target)

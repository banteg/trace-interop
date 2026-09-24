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


class ResultValidatorTests(unittest.TestCase):
    def test_precrawled_validator_matches_plain_validation_of_recursive_vm_traces(self):
        from jsonschema import Draft201909Validator
        from trace_interop.report import result_validator
        root = Path(__file__).resolve().parents[1]
        schema = next(m for m in json.loads((root/'spec/trace-openrpc.json').read_text())['methods'] if m['name'] == 'trace_call')['result']['schema']
        vm = {'code': '0x0', 'ops': []}
        for _ in range(4):
            vm = {'code': '0x00', 'ops': [{'pc': 0, 'cost': 0, 'ex': {'used': 1, 'push': ['0x00'], 'mem': None, 'store': None}, 'sub': vm}]}
        value = {'output': None, 'trace': [], 'stateDiff': None, 'vmTrace': vm}
        errors = lambda validator: sorted((list(e.absolute_path), e.message) for e in validator.iter_errors(value))
        self.assertTrue(errors(result_validator(schema)))
        self.assertEqual(errors(result_validator(schema)), errors(Draft201909Validator(schema)))


class ChangesPageTests(unittest.TestCase):
    def test_flips_and_build_changes_are_grouped_by_client(self):
        import tempfile
        from collections import defaultdict
        from trace_interop.presentation import changes_page
        editorial = {'clients': {f: {'name': f.capitalize()} for f in ['besu', 'reth', 'geth']}}
        decisions = {'H02': {'title': 'Lookup'}, 'H03': {'title': 'Filters'}}
        def matrix(builds, checks):
            by_client = defaultdict(lambda: defaultdict(list))
            for (client, topic), status in checks.items():
                by_client[client][topic].append({'status': status})
            return [{'client': c, 'version': v} for c, v in builds.items()], by_client
        before = matrix({'besu_development': 'a', 'reth_release': 'r', 'go-ethereum_trace': 'g'},
                        {('besu_development', 'H02'): 'change_needed', ('besu_development', 'H03'): 'matches', ('reth_release', 'H02'): 'matches'})
        after = matrix({'besu_development': 'b', 'reth_release': 'r', 'besu_release': 's'},
                       {('besu_development', 'H02'): 'matches', ('besu_development', 'H03'): 'matches', ('reth_release', 'H02'): 'matches'})
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ['old', 'new']:
                (root/name).mkdir()
                (root/name/'preflight.json').write_text(json.dumps({'checked_at': name}))
            text = changes_page({'matrix': root/'old', 'records': before[0], 'by_client': before[1]}, *after,
                                decisions, editorial, {}, root/'new', root/'reports')
        rows = [line for line in text.splitlines() if line.startswith('| [')]
        self.assertEqual(rows, ['| [H02 · Lookup](decisions/H02.md) | Besu dev | ⚠️ Differs | ✅ Checked cases agree |'])
        self.assertIn('### [Besu](clients/besu.md)', text)
        self.assertNotIn('### [Reth]', text)
        for row in ['| Besu stable | — | s · commit not recorded | New |', '| Besu dev | a · commit not recorded | b · commit not recorded | Updated |',
                    '| Geth | g · commit not recorded | — | Removed |', '| Reth stable | r · commit not recorded | r · commit not recorded | Unchanged |']:
            self.assertIn(row, text)
        self.assertIn('1 verdict changed for 1 client.', text)

    def test_published_changes_page_is_linked(self):
        root = Path(__file__).resolve().parents[1]
        selection = json.loads((root/'reports.lock.json').read_text())
        self.assertNotEqual(selection['previous'], selection['matrix'])
        self.assertIn(selection['previous'], (root/'reports/changes.md').read_text())
        self.assertIn('(changes.md)', (root/'reports/README.md').read_text())
        self.assertIn('(reports/changes.md)', (root/'README.md').read_text())

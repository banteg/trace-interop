"""Counterexamples from the 2026-10-14 harness audit: request validation, reports, fix refresh, case selection and tooling."""
from collections import defaultdict
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

from test_fixes import BESU, BUILDS, FAMILIES, LIBRARIES, REPOSITORIES, catalog

ROOT = Path(__file__).resolve().parents[1]


def script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/(name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FoldedMemberTests(unittest.TestCase):
    """A member matched case-insensitively takes effect for every keyword, never only for properties (H14)."""

    def errors(self, method, params):
        from trace_interop.validation import request_errors
        methods = {m['name']: m for m in json.loads((ROOT/'spec/trace-openrpc.json').read_text())['methods']}
        return request_errors({'method': method, 'params': params}, methods)

    def test_folded_members_meet_conditional_and_negated_requirements(self):
        block = '0x' + '11' * 32
        for name in ['blockHash', 'BLOCKHASH']:
            self.assertTrue(self.errors('trace_filter', [{name: block, 'fromBlock': '0x2'}]), name)
        self.assertFalse(self.errors('trace_filter', [{'BLOCKHASH': block}]))
        for state in ['state', 'STATE']:
            self.assertTrue(self.errors('trace_call', [{}, ['trace'], 'latest', {'0x' + '11' * 20: {state: {}, 'stateDiff': {}}}]), state)
        self.assertFalse(self.errors('trace_call', [{}, ['trace'], 'latest', {'0x' + '11' * 20: {'STATE': {}}}]))


class ReportSourceTests(unittest.TestCase):
    def test_fix_catalog_is_an_assessment_source(self):
        from trace_interop.report import ASSESSMENT_SOURCES
        self.assertIn('decisions/fixes.json', ASSESSMENT_SOURCES)

    def test_a_closed_prerequisite_is_drawn(self):
        from trace_interop.presentation import fixes_page
        text = fixes_page(catalog({'state': 'closed'}, {'depends_on': [f'{BESU}1']}), ROOT, ROOT/'docs', FAMILIES)
        self.assertIn('Besu_1["Besu #1"]:::closed', text)
        self.assertIn('classDef closed ', text)

    def test_examples_prefer_a_passing_baseline_to_extension_evidence(self):
        from trace_interop.presentation import examples
        checks = [{'status': 'observation', 'extension': True, 'corpus': 'a', 'case': f'extension-{i}'} for i in range(2)]
        checks.append({'status': 'matches', 'corpus': 'z', 'case': 'baseline'})
        self.assertIn('baseline.md', examples(Path('/reports'), Path('/reports/clients'), checks, 1))


class FamilyPlacementTests(unittest.TestCase):
    """Each build's own verdict places a decision on its family page."""
    BUILDS = ['besu_release', 'besu_development']

    def place(self, release, development):
        from trace_interop.presentation import placements
        by_client = defaultdict(lambda: defaultdict(list))
        for client, statuses in zip(self.BUILDS, [release, development]):
            by_client[client]['H15'] = [{'status': s, 'corpus': 'a', 'case': f'{client}-{i}'} for i, s in enumerate(statuses)]
        return {section: dict(found) for section, found in placements(self.BUILDS, by_client, ['H15']).items() if found}

    def test_a_difference_does_not_hide_another_builds_gaps(self):
        self.assertEqual(self.place(['change_needed'], ['matches', 'blocked']),
                         {'differs': {'H15': ['besu_release']}, 'gaps': {'H15': ['besu_development']}})

    def test_gaps_do_not_hide_another_builds_agreement(self):
        self.assertEqual(self.place(['blocked'], ['matches']),
                         {'gaps': {'H15': ['besu_release']}, 'agree': {'H15': ['besu_development']}})

    def test_one_build_places_as_before(self):
        self.assertEqual(self.place(['matches', 'observation'], ['matches']),
                         {'observations': {'H15': ['besu_release']}, 'agree': {'H15': ['besu_development']}})
        self.assertEqual(self.place([], ['control']), {'unchecked': {'H15': self.BUILDS}})


class RefreshTests(unittest.TestCase):
    def test_a_fork_branch_named_like_the_base_is_not_a_route(self):
        module = script('refresh_fixes')
        dev = BUILDS['besu_development']['commit']
        infos = {f'{BESU}1': ('m1', 'main', 'main', True), f'{BESU}2': ('m2', 'main', 'fix/a', False),
                 f'{BESU}3': ('m3', 'fix/a', 'fix/b', False)}

        class FakeGitHub(module.GitHub):
            def pr(self, url):
                commit, base, head, fork = infos[url]
                return {'title': 't', 'state': 'MERGED', 'isDraft': False, 'mergedAt': '2026-09-24T00:00:00Z', 'mergeCommit': {'oid': commit},
                        'baseRefName': base, 'headRefName': head, 'isCrossRepository': fork}

            def contains(self, repo, commit, ref):
                return ref == dev and commit in ('m1', 'm2')

        prs = [{'url': url, 'title': 't', 'client': 'besu', 'decisions': ['H10'], 'state': 'open', 'draft': False, 'merged_at': None} for url in infos]
        builds = {c: ref for c, ref in BUILDS.items() if c.startswith('besu')}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'fixes.json'
            path.write_text(json.dumps({'checked_at': '2026-01-01', 'repositories': REPOSITORIES, 'libraries': LIBRARIES, 'prs': prs}))
            with contextlib.redirect_stdout(io.StringIO()):
                fork, native, through = module.refresh(path, FakeGitHub(), builds)['prs']
        self.assertEqual(native['uptake'], {'merge_commit': 'm2', 'builds': {BUILDS['besu_release']['commit']: False, dev: True}})
        self.assertNotIn('via', fork['uptake'])
        self.assertEqual((through['uptake']['via'], through['uptake']['builds'][dev]), (f'{BESU}2', True))

    def test_cargo_requirements(self):
        module = script('refresh_fixes')
        for requirement, release, expected in [('0.0', '0.0.5', True), ('0.0', '0.1.0', False), ('0', '0.9.1', True), ('0.0.0', '0.0.1', False),
                                               ('>=0.44', '0.50.0', True), ('>=0.44', '0.43.9', False), ('<=1.2', '1.2.9', True),
                                               ('<=1.2', '1.3.0', False), ('>1.2', '1.2.9', False), ('>1.2', '1.3.0', True), ('<1.2', '1.1.9', True),
                                               ('>=1.2, <1.5', '1.4.9', True), ('>=1.2, <1.5', '1.5.0', False), ('~1.2', '1.2.9', True),
                                               ('~1.2', '1.3.0', False), ('~1', '1.9.0', True), ('=1.2.3', '1.2.4', False), ('=1.2', '1.2.4', True),
                                               ('1.*', '1.9.0', True), ('1.*', '2.0.0', False), ('*', '7.0.0', True), ('^0.44.1', '0.44.0', False)]:
            with self.subTest(requirement=requirement, release=release):
                self.assertEqual(module.admits(requirement, release), expected)

    def test_a_library_pr_without_measured_builds_has_no_chain_to_follow(self):
        module = script('refresh_fixes')
        pr = {'url': 'https://github.com/alloy-rs/alloy/pull/1', 'client': 'reth', 'merged_at': '2026-09-24T00:00:00Z'}
        self.assertEqual(module.uptake(None, pr, 'm1', LIBRARIES, {}), {'releases': [], 'client': None, 'builds': {}})


class CaseSelectionTests(unittest.TestCase):
    def test_a_selected_case_brings_the_cases_it_is_compared_with(self):
        from trace_interop.cli import read, selected_cases
        for corpus, case, reference in [('probes-prague', 'field-gas-omitted', 'field-gas-omitted-eth-call'),
                                        ('h30', 'filter-blockhash', 'filter-block-2'),
                                        ('fee-compat', 'legacy-zero/trace/none', 'legacy-zero/eth')]:
            with self.subTest(case=case):
                names = [c['name'] for c in selected_cases(read(ROOT/f'fixtures/corpora/{corpus}.json'), f'^{case}$')]
                self.assertIn(reference, names)
                self.assertEqual(len(names), len(set(names)))


class ReplicaTranslationTests(unittest.TestCase):
    def test_translation_is_one_pass_on_byte_boundaries(self):
        from trace_interop.replica import translate
        a, b, c = ('0x' + n * 32 for n in ['11', '22', '33'])
        self.assertEqual(translate(json.dumps([a, b]), {a: b, b: c}), json.dumps([b, c]))
        misaligned = '0x0' + a[2:] + '0'
        self.assertEqual(translate(misaligned, {a: b}), misaligned)
        self.assertEqual(translate('0x00' + a[2:] + b[2:], {a: b, b: c}), '0x00' + b[2:] + c[2:])


class CompareResponsesTests(unittest.TestCase):
    def test_groups_reads_nested_runs_and_failed_exchanges(self):
        module = script('compare_responses')
        response = lambda value: {'status': 'result', 'raw_response': '', 'response': {'jsonrpc': '2.0', 'id': 1, 'result': {'stateDiff': value}}}
        observations = {'case': {'a': response({'x': 1}), 'b': response({'x': 2}),
                                 'c': {'status': 'transport_error', 'detail': '2 responses', 'raw_log': ''},
                                 'd': {'status': 'invalid_envelope', 'raw_response': '[]', 'response': []}}}
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp)/'2026-10-11/eval/a'
            run.mkdir(parents=True)
            (run/'observations.json').write_text(json.dumps(observations))
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                module.groups(type('Args', (), {'evidence': tmp, 'family': 'stateDiff'}))
        self.assertEqual(output.getvalue().split()[:2], ['2026-10-11/eval/a', 'case'])
        self.assertEqual(module.result(observations['case']['c']), {'transport_error': '2 responses'})


class TechTreeTests(unittest.TestCase):
    def test_anvil_node_matches_the_totals(self):
        import tomllib
        anvil = next(node for node in tomllib.loads((ROOT/'site/tech-tree/tree.toml').read_text())['node'] if node['id'] == 'anvil')
        self.assertNotIn('left out of the totals', anvil['text'])


if __name__ == '__main__':
    unittest.main()

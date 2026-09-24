"""Submitted fixes mark measured differences in the reports; they never replace the captured checks."""
from datetime import date, datetime
import importlib.util
import io
import contextlib
import json
from pathlib import Path
import tempfile
import unittest

from trace_interop.presentation import check_fixes, display_verdict, fixes_page, pending_fixes, save

ROOT = Path(__file__).resolve().parents[1]
DECISIONS = {d['id'] for d in json.loads((ROOT/'decisions/ledger.json').read_text())['items']}
FAMILIES = json.loads((ROOT/'decisions/impact.json').read_text())['clients']
BUILT = datetime.fromisoformat('2026-09-22T12:00:00+00:00')
DIFFERS = [{'status': 'change_needed'}, {'status': 'matches'}]


def catalog(*changes):
    prs = [dict(url=f'https://github.com/besu-eth/besu/pull/{number}', title='fix(rpc): report code', client='besu',
                decisions=['H10'], state='open', draft=False, merged_at=None) | change
           for number, change in enumerate(changes, 1)]
    return check_fixes({'checked_at': '2026-09-24', 'repositories': {'besu-eth/besu': 'Besu', 'ethereum/execution-apis': 'execution-apis'},
                        'prs': prs}, DECISIONS, FAMILIES)


class FixCatalogTests(unittest.TestCase):
    def test_catalog_matches_ledger_and_client_families(self):
        fixes = json.loads((ROOT/'decisions/fixes.json').read_text())
        date.fromisoformat(fixes['checked_at'])
        urls = [pr['url'] for pr in fixes['prs']]
        self.assertEqual(len(urls), len(set(urls)))
        for pr in fixes['prs']:
            with self.subTest(pr=pr['url']):
                self.assertLessEqual({'url', 'title', 'client', 'decisions', 'state', 'draft', 'merged_at'}, set(pr))
                self.assertIn(pr['client'], {*FAMILIES, None})
                self.assertLessEqual(set(pr['decisions']), DECISIONS)
                self.assertEqual(len(pr['decisions']), len(set(pr['decisions'])))
                self.assertIn(pr['state'], {'open', 'merged', 'closed'})
                self.assertIsInstance(pr['draft'], bool)
                self.assertEqual(pr['merged_at'] is not None, pr['state'] == 'merged')
                if pr['merged_at']:
                    datetime.fromisoformat(pr['merged_at'].replace('Z', '+00:00'))
                self.assertLessEqual(set(pr.get('partial', [])), set(pr['decisions']))
                self.assertIn(pr.get('awaiting_uptake', False), [True, False])
        check_fixes(fixes, DECISIONS, FAMILIES)

    def test_invalid_entries_are_rejected(self):
        for change in [{'client': 'parity'}, {'decisions': ['H99']}, {'state': 'draft'}, {'state': 'merged'},
                       {'merged_at': '2026-09-23T00:00:00Z'}, {'url': 'https://github.com/unknown/repo/pull/1'},
                       {'url': 'https://example.org/pull/1'}, {'partial': ['H09']}, {'awaiting_uptake': 'yes'}]:
            with self.subTest(change=change), self.assertRaises(ValueError):
                catalog(change)
        with self.assertRaises(ValueError):
            catalog({}, {'url': 'https://github.com/besu-eth/besu/pull/1'})


class FixSubmittedTests(unittest.TestCase):
    def verdict(self, checks, fixes, client='besu_release', topic='H10', built=BUILT):
        return display_verdict(checks, pending_fixes(fixes, client, topic, built))

    def test_open_pr_marks_a_difference_and_links_it(self):
        fixes = catalog({}, {'draft': True})
        self.assertEqual(self.verdict(DIFFERS, fixes), '🛠️ Fix submitted: [Besu #1](https://github.com/besu-eth/besu/pull/1)'
                         ' · [Besu #2](https://github.com/besu-eth/besu/pull/2)')
        self.assertTrue(self.verdict([{'status': 'matches'}, {'status': 'blocked'}], fixes).startswith('🛠️ Fix submitted'))

    def test_merged_pr_marks_only_builds_committed_before_the_merge(self):
        fixes = catalog({'state': 'merged', 'merged_at': '2026-09-22T12:00:01Z'})
        self.assertTrue(self.verdict(DIFFERS, fixes).startswith('🛠️'))
        self.assertEqual(self.verdict(DIFFERS, fixes, built=datetime.fromisoformat('2026-09-23T00:00:00+00:00')), '⚠️ Differs')
        self.assertEqual(self.verdict(DIFFERS, fixes, built=None), '⚠️ Differs')

    def test_other_outcomes_clients_decisions_and_closed_prs_are_unchanged(self):
        fixes = catalog({})
        self.assertEqual(self.verdict([{'status': 'matches'}], fixes), '✅ Checked cases agree')
        self.assertEqual(self.verdict([{'status': 'unsupported'}], fixes), '⛔ Method unavailable')
        self.assertEqual(self.verdict([{'status': 'observation'}], fixes), '❔ Policy open')
        self.assertEqual(self.verdict(DIFFERS, fixes, client='erigon_release'), '⚠️ Differs')
        self.assertEqual(self.verdict(DIFFERS, fixes, topic='H09'), '⚠️ Differs')
        self.assertEqual(self.verdict(DIFFERS, catalog({'state': 'closed'})), '⚠️ Differs')
        self.assertEqual(self.verdict(DIFFERS, catalog({'client': None})), '⚠️ Differs')
        self.assertEqual(pending_fixes(fixes, 'besu_development', 'H10', BUILT), [(fixes['prs'][0], False)])

    def test_partial_fixes_are_linked_without_hiding_the_difference(self):
        partial = {'decisions': ['H09', 'H10'], 'partial': ['H10']}
        link = '[Besu #1](https://github.com/besu-eth/besu/pull/1) (partial fix)'
        self.assertEqual(self.verdict(DIFFERS, catalog(partial)), f'⚠️ Differs · {link}')
        self.assertEqual(self.verdict([{'status': 'matches'}, {'status': 'unassessed'}], catalog(partial)), f'🟡 Partially assessed · {link}')
        self.assertTrue(self.verdict(DIFFERS, catalog(partial), topic='H09').startswith('🛠️ Fix submitted'))
        self.assertEqual(self.verdict(DIFFERS, catalog(partial, {})),
                         f'🛠️ Fix submitted: {link} · [Besu #2](https://github.com/besu-eth/besu/pull/2)')

    def test_merged_library_fix_awaiting_uptake_counts_as_submitted(self):
        merged = {'state': 'merged', 'merged_at': '2026-09-20T00:00:00Z'}
        self.assertEqual(self.verdict(DIFFERS, catalog(merged)), '⚠️ Differs')
        self.assertTrue(self.verdict(DIFFERS, catalog(merged | {'awaiting_uptake': True})).startswith('🛠️'))
        self.assertTrue(self.verdict(DIFFERS, catalog(merged | {'awaiting_uptake': True}), built=None).startswith('🛠️'))
        self.assertEqual(self.verdict(DIFFERS, catalog({'state': 'closed', 'awaiting_uptake': True})), '⚠️ Differs')


class FixesPageTests(unittest.TestCase):
    def test_page_groups_prs_by_state_with_decision_tags(self):
        fixes = catalog({'state': 'merged', 'merged_at': '2026-09-23T01:00:00Z', 'title': 'Serialize markers', 'decisions': ['H17', 'H26'], 'partial': ['H26']},
                        {'draft': True, 'note': 'verified locally'},
                        {'url': 'https://github.com/ethereum/execution-apis/pull/895', 'client': None, 'decisions': [], 'title': 'feat(trace): add schemas'})
        text = fixes_page(fixes, ROOT, ROOT/'docs')
        self.assertLess(text.index('## Open'), text.index('## Merged'))
        self.assertNotIn('## Closed', text)
        self.assertIn('| [Besu #2](https://github.com/besu-eth/besu/pull/2) (draft) | Report code; verified locally | [H10](../reports/decisions/H10.md) |', text)
        self.assertIn('| [execution-apis #895](https://github.com/ethereum/execution-apis/pull/895) | Add schemas | — |', text)
        self.assertIn('| [Besu #1](https://github.com/besu-eth/besu/pull/1) | Serialize markers | [H17](../reports/decisions/H17.md), [H26](../reports/decisions/H26.md) (partial) | 2026-09-23 |', text)
        self.assertLess(text.index('Besu #2'), text.index('execution-apis #895'))

    def test_published_page_is_generated_from_the_catalog(self):
        fixes = check_fixes(json.loads((ROOT/'decisions/fixes.json').read_text()), DECISIONS, FAMILIES)
        with tempfile.TemporaryDirectory() as tmp:
            save(Path(tmp)/'client-fixes.md', fixes_page(fixes, ROOT, ROOT/'docs'))
            expected = (Path(tmp)/'client-fixes.md').read_text()
        self.assertEqual((ROOT/'docs/client-fixes.md').read_text(), expected)
        for pr in fixes['prs']:
            self.assertEqual(expected.count(f']({pr["url"]})'), 1, pr['url'])


class RefreshFixesTests(unittest.TestCase):
    def test_refresh_updates_github_fields_and_keeps_editorial_ones(self):
        spec = importlib.util.spec_from_file_location('refresh_fixes', ROOT/'scripts/refresh_fixes.py')
        module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        pr = dict(url='https://github.com/paradigmxyz/revm-inspectors/pull/1', title='old', client='reth', decisions=['H20'],
                  partial=['H20'], state='open', draft=True, merged_at=None, awaiting_uptake=True, note='kept')
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'fixes.json'
            path.write_text(json.dumps({'checked_at': '2026-01-01', 'repositories': {}, 'prs': [pr]}))
            view = lambda url: {'title': 'new', 'state': 'MERGED', 'isDraft': False, 'mergedAt': '2026-09-24T00:00:00Z'}
            with contextlib.redirect_stdout(io.StringIO()):
                module.refresh(path, view)
            refreshed = json.loads(path.read_text())
        self.assertEqual(refreshed['prs'][0], pr | dict(title='new', state='merged', draft=False, merged_at='2026-09-24T00:00:00Z'))
        self.assertNotEqual(refreshed['checked_at'], '2026-01-01')


if __name__ == '__main__':
    unittest.main()


class FreshnessTests(unittest.TestCase):
    def test_stale_pin_and_old_catalog_warn(self):
        spec = importlib.util.spec_from_file_location('freshness', ROOT/'scripts/freshness.py')
        module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        lock = {'repository': 'https://github.com/banteg/execution-apis', 'branch': 'feat/trace', 'commit': 'a' * 40}
        today = date(2026, 9, 25)
        self.assertEqual(module.warnings(lock, 'a' * 40, '2026-09-18', today, 7), [])
        found = module.warnings(lock, 'b' * 40, '2026-09-17', today, 7)
        self.assertEqual(len(found), 2)
        self.assertIn('bbbbbbbbbbbb', found[0])
        self.assertIn('8 days ago', found[1])
        self.assertIn('no branch', module.warnings(lock, None, '2026-09-25', today, 7)[0])

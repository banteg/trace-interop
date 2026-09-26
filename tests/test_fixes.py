"""Submitted fixes mark measured differences in the reports; they never replace the captured checks."""
from collections import defaultdict
import contextlib
from datetime import date, datetime
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

from trace_interop.presentation import (check_fixes, display_verdict, fix_progress, fixes_page, measured_builds,
                                        pending_fixes, save)

ROOT = Path(__file__).resolve().parents[1]
DECISIONS = {d['id'] for d in json.loads((ROOT/'decisions/ledger.json').read_text())['items']}
FAMILIES = json.loads((ROOT/'decisions/impact.json').read_text())['clients']
DIFFERS = [{'status': 'change_needed', 'corpus': 'a', 'case': 'two'}, {'status': 'matches', 'corpus': 'a', 'case': 'one'}]
AGREES = [{'status': 'matches', 'corpus': 'a', 'case': 'one'}]
REPOSITORIES = {'alloy-rs/alloy': 'Alloy', 'besu-eth/besu': 'Besu', 'bluealloy/revm': 'revm', 'ethereum/execution-apis': 'execution-apis',
                'paradigmxyz/reth': 'Reth', 'paradigmxyz/revm-inspectors': 'revm-inspectors'}
LIBRARIES = {'alloy-rs/alloy': {'crates': ['alloy-rpc-types-trace'], 'consumers': ['paradigmxyz/reth']},
             'bluealloy/revm': {'crates': ['revm'], 'consumers': ['paradigmxyz/revm-inspectors']},
             'paradigmxyz/revm-inspectors': {'crates': ['revm-inspectors'], 'consumers': ['paradigmxyz/reth']}}
BUILDS = {f'{client}_{channel}': {'repository': f'https://github.com/{repo}', 'commit': commit * 40, 'committed_at': '2026-09-22T12:00:00Z'}
          for client, repo, commits in [('besu', 'besu-eth/besu', 'ab'), ('reth', 'paradigmxyz/reth', 'cd')]
          for channel, commit in zip(['release', 'development'], commits)}
BESU = 'https://github.com/besu-eth/besu/pull/'
INSPECTORS = 'https://github.com/paradigmxyz/revm-inspectors/pull/1'


def merged(*inside, **uptake):
    """A merged PR whose recorded uptake places it in the listed measured builds."""
    return {'state': 'merged', 'merged_at': '2026-09-23T00:00:00Z',
            'uptake': {'merge_commit': 'f' * 40, 'builds': {ref['commit']: client in inside for client, ref in BUILDS.items()}} | uptake}


def release(repo, tag):
    return {'repo': repo, 'tag': tag, 'date': '2026-09-24T00:00:00Z', 'crates': {}}


def catalog(*changes, by_client=None):
    prs = [dict(url=f'{BESU}{number}', title='fix(rpc): report code', client='besu', decisions=['H10'], state='open', draft=False, merged_at=None) | change
           for number, change in enumerate(changes, 1)]
    fixes = check_fixes({'checked_at': '2026-09-24', 'repositories': REPOSITORIES, 'libraries': LIBRARIES, 'prs': prs}, DECISIONS, FAMILIES)
    return fix_progress(fixes, BUILDS, by_client or {})


def library(url, **change):
    return {'url': url, 'client': 'reth'} | change


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
                self.assertEqual('uptake' in pr, pr['state'] == 'merged' and pr['client'] is not None)
        check_fixes(fixes, DECISIONS, FAMILIES)

    def test_invalid_entries_are_rejected(self):
        for change in [{'client': 'parity'}, {'decisions': ['H99']}, {'state': 'draft'}, {'state': 'merged'},
                       {'merged_at': '2026-09-23T00:00:00Z'}, {'url': 'https://github.com/unknown/repo/pull/1'},
                       {'url': 'https://example.org/pull/1'}, {'partial': ['H09']}, {'awaiting_uptake': True},
                       {'uptake': {'merge_commit': 'f' * 40}}, {'depends_on': [f'{BESU}9']}, {'depends_on': [f'{BESU}1']},
                       {'conflicts_with': [f'{BESU}1']}, {'depends_on': [f'{BESU}2', f'{BESU}2']}, {'verified_cases': ['one']}]:
            with self.subTest(change=change), self.assertRaises(ValueError):
                catalog(change, {})
        with self.assertRaises(ValueError):
            catalog({}, {'url': f'{BESU}1'})

    def test_edges_must_be_acyclic_and_conflicts_symmetric(self):
        with self.assertRaisesRegex(ValueError, 'dependency cycle'):
            catalog({'depends_on': [f'{BESU}3']}, {'depends_on': [f'{BESU}1']}, {'depends_on': [f'{BESU}2']})
        with self.assertRaisesRegex(ValueError, 'both PRs'):
            catalog({'conflicts_with': [f'{BESU}2']}, {})
        fixes = catalog({'depends_on': [f'{BESU}2'], 'conflicts_with': [f'{BESU}3']}, {}, {'conflicts_with': [f'{BESU}1']})
        self.assertEqual(fixes['prs'][0]['stage'], 'open')

    def test_libraries_name_known_repositories(self):
        for library_entry in [{'crates': [], 'consumers': ['paradigmxyz/reth']}, {'crates': ['x'], 'consumers': ['unknown/repo']},
                              {'crates': ['x'], 'consumers': ['alloy-rs/alloy']}]:
            with self.subTest(library=library_entry), self.assertRaises(ValueError):
                check_fixes({'repositories': REPOSITORIES, 'libraries': {'alloy-rs/alloy': library_entry}, 'prs': []}, DECISIONS, FAMILIES)


class FixStageTests(unittest.TestCase):
    def stages(self, fixes):
        return [pr['stage'] for pr in fixes['prs']]

    def test_native_pr_reaches_the_builds_its_merge_commit_is_in(self):
        fixes = catalog({}, merged(), merged('besu_development'), merged('besu_development', 'besu_release'), {'state': 'closed'})
        self.assertEqual(self.stages(fixes), ['open', 'merged', 'in measured build', 'in measured build', 'closed'])
        self.assertEqual([pr['builds'] for pr in fixes['prs']], [[], [], ['besu_development'], ['besu_development', 'besu_release'], []])
        self.assertEqual([pr['chain'] for pr in fixes['prs']], [[]] * 5)

    def test_merged_pr_without_facts_for_a_measured_build_fails(self):
        stale = merged() | {'uptake': {'merge_commit': 'f' * 40, 'builds': {BUILDS['besu_release']['commit']: True}}}
        with self.assertRaisesRegex(ValueError, 'besu_development; run scripts/refresh_fixes.py'):
            catalog(stale)

    def test_single_hop_library_pr_is_released_then_taken_up(self):
        adopted = {'releases': [release('paradigmxyz/revm-inspectors', 'v0.44.0')], 'client': {'commit': 'e' * 40, 'date': '2026-09-25T00:00:00Z'}}
        fixes = catalog(library(INSPECTORS, **merged('reth_development', **adopted)))
        pr = fixes['prs'][0]
        self.assertEqual(pr['chain'], ['paradigmxyz/revm-inspectors', 'paradigmxyz/reth'])
        self.assertEqual((pr['stage'], pr['builds']), ('in measured build', ['reth_development']))

    def test_multi_hop_library_pr_follows_its_consumers(self):
        hops = [release('bluealloy/revm', 'v121'), release('paradigmxyz/revm-inspectors', 'v0.45.0')]
        fixes = catalog(library('https://github.com/bluealloy/revm/pull/1', **merged(releases=hops[:1], client=None)),
                        library('https://github.com/bluealloy/revm/pull/2', **merged(releases=hops, client={'commit': 'e' * 40, 'date': '2026-09-26T00:00:00Z'})),
                        library('https://github.com/bluealloy/revm/pull/3'))
        self.assertEqual([pr['chain'] for pr in fixes['prs']], [['bluealloy/revm', 'paradigmxyz/revm-inspectors', 'paradigmxyz/reth']] * 3)
        self.assertEqual(self.stages(fixes), ['released', 'in client', 'open'])

    def test_unreleased_and_unadopted_library_prs_stop_short_of_the_client(self):
        fixes = catalog(library('https://github.com/alloy-rs/alloy/pull/1', **merged(releases=[], client=None)),
                        library('https://github.com/alloy-rs/alloy/pull/2', **merged(releases=[release('alloy-rs/alloy', 'v2.5.0')], client=None)))
        self.assertEqual(self.stages(fixes), ['merged', 'released'])
        self.assertEqual([pr['builds'] for pr in fixes['prs']], [[], []])


class FixVerifiedTests(unittest.TestCase):
    def verified(self, *changes):
        by_client = {'besu_development': {'H10': AGREES, 'H09': DIFFERS}, 'besu_release': {'H10': DIFFERS, 'H09': DIFFERS}}
        return [(pr['stage'], pr['verified']) for pr in catalog(*changes, by_client=by_client)['prs']]

    def test_complete_fix_is_verified_where_its_decisions_agree(self):
        both = merged('besu_development', 'besu_release')
        self.assertEqual(self.verified(both, both | {'decisions': ['H09', 'H10']}, merged('besu_release')),
                         [('verified', ['besu_development']), ('in measured build', []), ('in measured build', [])])

    def test_partial_fix_needs_verified_cases(self):
        both = merged('besu_development', 'besu_release') | {'partial': ['H10']}
        self.assertEqual(self.verified(both, both | {'verified_cases': ['a/one']}, both | {'verified_cases': ['a/one', 'a/two']},
                                       both | {'decisions': ['H09', 'H10'], 'verified_cases': ['a/two']}),
                         [('in measured build', []), ('verified', ['besu_development', 'besu_release']),
                          ('in measured build', []), ('in measured build', [])])
        # A PR with no decisions checks its cases on every topic.
        self.assertEqual(self.verified(both | {'decisions': [], 'partial': [], 'verified_cases': ['a/one']},
                                       both | {'decisions': [], 'partial': [], 'verified_cases': ['a/two']}),
                         [('verified', ['besu_development', 'besu_release']), ('in measured build', [])])
        with self.assertRaisesRegex(ValueError, 'unmeasured verified cases: a/three'):
            self.verified(both | {'verified_cases': ['a/three']})


class FixSubmittedTests(unittest.TestCase):
    def verdict(self, checks, fixes, client='besu_release', topic='H10'):
        return display_verdict(checks, pending_fixes(fixes, client, topic))

    def test_open_pr_marks_a_difference_and_links_it(self):
        fixes = catalog({}, {'draft': True})
        self.assertEqual(self.verdict(DIFFERS, fixes), '🛠️ Fix submitted: [Besu #1](https://github.com/besu-eth/besu/pull/1)'
                         ' · [Besu #2](https://github.com/besu-eth/besu/pull/2)')
        self.assertTrue(self.verdict([{'status': 'matches'}, {'status': 'blocked'}], fixes).startswith('🛠️ Fix submitted'))

    def test_merged_pr_marks_a_build_until_it_is_in_the_build(self):
        fixes = catalog(merged('besu_development'))
        self.assertTrue(self.verdict(DIFFERS, fixes).startswith('🛠️'))
        self.assertEqual(self.verdict(DIFFERS, fixes, client='besu_development'), '⚠️ Differs')
        self.assertTrue(self.verdict(DIFFERS, catalog(merged())).startswith('🛠️'))

    def test_library_fix_marks_builds_until_their_lockfile_takes_it(self):
        fixes = catalog(library(INSPECTORS, **merged('reth_development', releases=[release('paradigmxyz/revm-inspectors', 'v0.44.0')], client=None)))
        self.assertTrue(self.verdict(DIFFERS, fixes, client='reth_release').startswith('🛠️ Fix submitted: [revm-inspectors #1]'))
        self.assertEqual(self.verdict(DIFFERS, fixes, client='reth_development'), '⚠️ Differs')

    def test_other_outcomes_clients_decisions_and_closed_prs_are_unchanged(self):
        fixes = catalog({})
        self.assertEqual(self.verdict([{'status': 'matches'}], fixes), '✅ Checked cases agree')
        self.assertEqual(self.verdict([{'status': 'unsupported'}], fixes), '⛔ Method unavailable')
        self.assertEqual(self.verdict([{'status': 'observation'}], fixes), '❔ Policy open')
        self.assertEqual(self.verdict(DIFFERS, fixes, client='erigon_release'), '⚠️ Differs')
        self.assertEqual(self.verdict(DIFFERS, fixes, topic='H09'), '⚠️ Differs')
        self.assertEqual(self.verdict(DIFFERS, catalog({'state': 'closed'})), '⚠️ Differs')
        self.assertEqual(self.verdict(DIFFERS, catalog({'client': None})), '⚠️ Differs')
        self.assertEqual(pending_fixes(fixes, 'besu_development', 'H10'), [(fixes['prs'][0], False)])

    def test_partial_fixes_are_linked_without_hiding_the_difference(self):
        partial = {'decisions': ['H09', 'H10'], 'partial': ['H10']}
        link = '[Besu #1](https://github.com/besu-eth/besu/pull/1) (partial fix)'
        self.assertEqual(self.verdict(DIFFERS, catalog(partial)), f'⚠️ Differs · {link}')
        self.assertEqual(self.verdict([{'status': 'matches'}, {'status': 'unassessed'}], catalog(partial)), f'🟡 Partially assessed · {link}')
        self.assertTrue(self.verdict(DIFFERS, catalog(partial), topic='H09').startswith('🛠️ Fix submitted'))
        self.assertEqual(self.verdict(DIFFERS, catalog(partial, {})),
                         f'🛠️ Fix submitted: {link} · [Besu #2](https://github.com/besu-eth/besu/pull/2)')


RETH_SECTION = '''## Reth

```mermaid
flowchart LR
  Alloy_1["Alloy #1"]:::verified
  Alloy_v2_5_0(["Alloy v2.5.0"]):::done
  Reth_takes_Alloy_v2_5_0[["Reth takes Alloy v2.5.0"]]:::done
  Reth_3["Reth #3"]:::open
  revm_2["revm #2"]:::open
  next_revm_release(["next revm release"]):::pending
  next_revm_inspectors_release(["next revm-inspectors release"]):::pending
  Reth_takes_next_revm_inspectors_release[["Reth takes next revm-inspectors release"]]:::pending
  Alloy_1 --> Alloy_v2_5_0
  Alloy_v2_5_0 --> Reth_takes_Alloy_v2_5_0
  Alloy_1 --> Reth_3
  revm_2 -.-> next_revm_release
  next_revm_release -.-> next_revm_inspectors_release
  next_revm_inspectors_release -.-> Reth_takes_next_revm_inspectors_release
  classDef open fill:#f6f8fa,stroke:#8c959f,color:#1f2328
  classDef verified fill:#1a7f37,stroke:#116329,color:#ffffff
  classDef done fill:#ffffff,stroke:#1a7f37,color:#1f2328
  classDef pending fill:#ffffff,stroke:#8c959f,stroke-dasharray:4 3,color:#57606a
```

| PR | Change | Decisions | Merged | Released | In client | In measured build | Verified |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Alloy #1](https://github.com/alloy-rs/alloy/pull/1) | Default filters to intersection | [H03](../reports/decisions/H03.md) | 2026-09-23 | [Alloy v2.5.0](https://github.com/alloy-rs/alloy/tree/v2.5.0) | [2026-09-24](https://github.com/paradigmxyz/reth/commit/eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee) | dev | dev |
| [Reth #3](https://github.com/paradigmxyz/reth/pull/3) (draft) | Bump alloy · after Alloy #1 | — | — | — | — | — | — |
| [revm #2](https://github.com/bluealloy/revm/pull/2) | Preserve selfdestruct payload | [H26](../reports/decisions/H26.md) (partial) | — | — | — | — | — |

'''


class FixesPageTests(unittest.TestCase):
    def test_page_has_a_section_per_client_with_stages_and_order(self):
        adopted = merged('reth_development', releases=[release('alloy-rs/alloy', 'v2.5.0')], client={'commit': 'e' * 40, 'date': '2026-09-24T01:00:00Z'})
        fixes = catalog({'draft': True, 'note': 'verified locally'},
                        library('https://github.com/alloy-rs/alloy/pull/1', title='fix(rpc-types-trace): default filters to intersection', decisions=['H03'], **adopted),
                        library('https://github.com/bluealloy/revm/pull/2', title='fix(inspector): preserve selfdestruct payload', decisions=['H26'], partial=['H26']),
                        library('https://github.com/paradigmxyz/reth/pull/3', title='chore: bump alloy', decisions=[], draft=True,
                                depends_on=['https://github.com/alloy-rs/alloy/pull/1']),
                        {'url': 'https://github.com/ethereum/execution-apis/pull/895', 'client': None, 'decisions': [], 'title': 'feat(trace): add schemas'},
                        {'state': 'closed', 'title': 'fix: superseded'},
                        by_client={'reth_development': {'H03': AGREES}})
        text = fixes_page(fixes, ROOT, ROOT/'docs', FAMILIES)
        self.assertIn(RETH_SECTION, text)
        self.assertIn('## Besu\n\n| PR |', text)
        self.assertIn('| [Besu #1](https://github.com/besu-eth/besu/pull/1) (draft) | Report code; verified locally | [H10](../reports/decisions/H10.md) | — | — | — | — | — |', text)
        self.assertIn('## Specifications, tests and other repositories\n\nNo measured build consumes these repositories.\n\n| PR |', text)
        self.assertTrue(text.endswith('## Closed\n\n- [Besu #6](https://github.com/besu-eth/besu/pull/6): Superseded\n'))
        self.assertLess(text.index('## Besu'), text.index('## Reth'))

    def test_published_page_is_generated_from_the_catalog(self):
        revisions = json.loads((ROOT/'locks/source-revisions.json').read_text())
        records = json.loads((ROOT/'reports/checks.json').read_text())
        by_client = defaultdict(lambda: defaultdict(list))
        for r in records:
            for check in r['checks']:
                by_client[r['client']][check['topic']].append(check | {'corpus': r['corpus'], 'case': r['case']})
        fixes = check_fixes(json.loads((ROOT/'decisions/fixes.json').read_text()), DECISIONS, FAMILIES)
        fix_progress(fixes, measured_builds({(r['client'], r['version']) for r in records}, revisions), by_client)
        with tempfile.TemporaryDirectory() as tmp:
            save(Path(tmp)/'client-fixes.md', fixes_page(fixes, ROOT, ROOT/'docs', FAMILIES))
            expected = (Path(tmp)/'client-fixes.md').read_text()
        self.assertEqual((ROOT/'docs/client-fixes.md').read_text(), expected)
        for pr in fixes['prs']:
            self.assertEqual(expected.count(f']({pr["url"]})'), 1, pr['url'])


def lock(**crates):
    return ''.join(f'[[package]]\nname = "{name}"\nversion = "{v}"\nsource = "registry+https://github.com/rust-lang/crates.io-index"\n\n'
                   for name, v in crates.items())


class RefreshFixesTests(unittest.TestCase):
    """The refresh records network facts; a fake GitHub stands in for gh."""
    STABLE, DEV = BUILDS['reth_release']['commit'], BUILDS['reth_development']['commit']

    def module(self):
        spec = importlib.util.spec_from_file_location('refresh_fixes', ROOT/'scripts/refresh_fixes.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def fake(self, module):
        stable, dev = self.STABLE, self.DEV

        class FakeGitHub(module.GitHub):
            def __init__(self):
                super().__init__()
                self.infos = {
                    INSPECTORS: ('m1', 'main', 'fix/a'),
                    'https://github.com/alloy-rs/alloy/pull/2': ('m2', 'main', 'fix/b'),
                    'https://github.com/bluealloy/revm/pull/3': ('m3', 'main', 'fix/c'),
                    'https://github.com/paradigmxyz/reth/pull/4': ('m4', 'main', 'fix/d'),
                    'https://github.com/paradigmxyz/reth/pull/5': ('m5', 'fix/d', 'fix/e'),
                    'https://github.com/paradigmxyz/reth/pull/6': (None, 'main', 'fix/f'),
                }
                self.inside = {('paradigmxyz/revm-inspectors', 'm1', 'v0.45.0'), ('paradigmxyz/revm-inspectors', 'm1', 'v0.44.0'),
                               ('bluealloy/revm', 'm3', 'v121'), ('paradigmxyz/reth', 'm4', dev)}
                self.tagged = {'paradigmxyz/revm-inspectors': ['v0.43.0', 'v0.45.0', 'v0.44.0', 'nightly'], 'alloy-rs/alloy': ['v2.5.0'],
                               'bluealloy/revm': ['v120', 'v121']}
                inspectors = '[package]\nname = "revm-inspectors"\nversion = "{}"\n[dependencies]\nrevm = {{ version = "{}" }}\n'
                self.files = {('paradigmxyz/revm-inspectors', 'v0.44.0'): inspectors.format('0.44.0', '43.0.0'),
                              ('paradigmxyz/revm-inspectors', 'v0.45.0'): inspectors.format('0.45.0', '44.0.0'),
                              ('bluealloy/revm', 'v121'): '[workspace.dependencies]\nrevm = { path = "crates/revm", version = "44.0.1" }\n'}
                for ref, inspectors_version, alloy in [('h1', '0.43.0', '2.5.0'), ('h2', '0.44.0', '2.5.0'), ('h3', '0.44.0', '2.5.0'),
                                                       (stable, '0.43.0', '2.4.0'), (dev, '0.44.0', '2.5.0')]:
                    self.files['paradigmxyz/reth', ref] = lock(**{'revm-inspectors': inspectors_version, 'revm': '43.0.3', 'alloy-rpc-types-trace': alloy})

            def pr(self, url):
                commit, base, head = self.infos[url]
                return {'title': 'new', 'state': 'MERGED' if commit else 'OPEN', 'isDraft': False, 'mergedAt': commit and '2026-09-24T00:00:00Z',
                        'mergeCommit': commit and {'oid': commit}, 'baseRefName': base, 'headRefName': head}

            def contains(self, repo, commit, ref):
                return (repo, commit, ref) in self.inside

            def tags(self, repo):
                return self.tagged[repo]

            def commit(self, repo, ref):
                return {'sha': 'h3' if ref == 'HEAD' else ref, 'date': '2026-09-25T00:00:00Z'}

            def file(self, repo, path, ref):
                return self.files[repo, ref]

            def history(self, repo, path, since):
                return ['h1', 'h2', 'h3']

        return FakeGitHub()

    def test_refresh_records_states_and_uptake_and_keeps_editorial_fields(self):
        module = self.module()
        prs = [{'url': url, 'title': 'old', 'client': 'reth', 'decisions': ['H20'], 'partial': ['H20'], 'state': 'open', 'draft': True,
                'merged_at': None, 'note': 'kept'}
               for url in self.fake(module).infos]
        prs[0]['state'], prs[0]['merged_at'] = 'merged', '2026-09-24T00:00:00Z'
        prs[0]['uptake'] = {'client': {'commit': 'h0', 'date': '2026-09-20T00:00:00Z'}}
        prs[5]['uptake'] = {'merge_commit': 'stale'}
        builds = {client: ref for client, ref in BUILDS.items() if client.startswith('reth')}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'fixes.json'
            path.write_text(json.dumps({'checked_at': '2026-01-01', 'repositories': REPOSITORIES, 'libraries': LIBRARIES, 'prs': prs}))
            with contextlib.redirect_stdout(io.StringIO()):
                module.refresh(path, self.fake(module), builds)
            refreshed = json.loads(path.read_text())
        self.assertNotEqual(refreshed['checked_at'], '2026-01-01')
        first, alloy, revm, native, through, still_open = refreshed['prs']
        self.assertEqual({k: first[k] for k in ('title', 'state', 'draft', 'note', 'partial')},
                         {'title': 'new', 'state': 'merged', 'draft': False, 'note': 'kept', 'partial': ['H20']})
        # Single hop, released and adopted; a recorded first sighting is kept.
        self.assertEqual(first['uptake'], {'merge_commit': 'm1', 'releases': [
            {'repo': 'paradigmxyz/revm-inspectors', 'tag': 'v0.44.0', 'date': '2026-09-25T00:00:00Z', 'crates': {'revm-inspectors': '0.44.0'}}],
            'client': {'commit': 'h0', 'date': '2026-09-20T00:00:00Z'}, 'builds': {self.STABLE: False, self.DEV: True}})
        # Merged but in no release yet.
        self.assertEqual(alloy['uptake'], {'merge_commit': 'm2', 'releases': [], 'client': None, 'builds': {self.STABLE: False, self.DEV: False}})
        # Two hops: revm v121, then the first revm-inspectors tag admitting revm 44; Reth has not bumped.
        self.assertEqual([(r['repo'], r['tag'], r['crates']) for r in revm['uptake']['releases']],
                         [('bluealloy/revm', 'v121', {'revm': '44.0.1'}), ('paradigmxyz/revm-inspectors', 'v0.45.0', {'revm-inspectors': '0.45.0'})])
        self.assertEqual((revm['uptake']['client'], revm['uptake']['builds']), (None, {self.STABLE: False, self.DEV: False}))
        self.assertEqual(native['uptake'], {'merge_commit': 'm4', 'builds': {self.STABLE: False, self.DEV: True}})
        self.assertEqual(through['uptake'], {'merge_commit': 'm5', 'via': 'https://github.com/paradigmxyz/reth/pull/4',
                                             'builds': {self.STABLE: False, self.DEV: True}})
        self.assertNotIn('uptake', still_open)

    def test_first_pinning_commit_is_found_by_bisection(self):
        module = self.module()
        gh = self.fake(module)
        required = [('paradigmxyz/revm-inspectors', 'm1', {'revm-inspectors': '0.44.0'})]
        self.assertEqual(module.first_pinning(gh, 'paradigmxyz/reth', '2026-09-24T00:00:00Z', required),
                         {'commit': 'h2', 'date': '2026-09-25T00:00:00Z'})

    def test_caret_requirements(self):
        module = self.module()
        for requirement, release, expected in [('43.0.0', '43.2.1', True), ('43.0.0', '44.0.0', False), ('0.44', '0.44.3', True),
                                               ('0.44', '0.45.0', False), ('^1.4', '1.3.9', False), ('0.0.3', '0.0.4', False)]:
            with self.subTest(requirement=requirement, release=release):
                self.assertEqual(module.admits(requirement, release), expected)


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


if __name__ == '__main__':
    unittest.main()

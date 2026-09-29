"""Freshness is a live gate; failures never silently reuse historical builds."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from trace_interop.cli import HIVE
from trace_interop.versions import current_references, check_current, lagging_development, matrix_lock, NAMES


class VersionTests(unittest.TestCase):
    def release(self, path):
        return dict(tag_name='v2.0.0', published_at='2026-09-22T00:00:00Z',
                    html_url='https://github.com/example/releases/tag/v2.0.0')

    def test_discovers_stable_tags_and_moving_development_references(self):
        refs = current_references(NAMES, self.release)
        self.assertEqual(refs['nethermind_release']['requested'], 'nethermind/nethermind:2.0.0')
        self.assertEqual(refs['reth_release']['requested'], 'ghcr.io/paradigmxyz/reth:v2.0.0')
        self.assertEqual(refs['erigon_development']['requested'], 'erigontech/erigon:main-latest')
        self.assertEqual(refs['nethermind_release']['release']['published_at'], '2026-09-22T00:00:00Z')

    def test_discovery_fails_closed(self):
        for names in ([], ['unknown'], ['reth_release'] * 2):
            with self.assertRaises(ValueError):
                current_references(names, self.release)
        for field in ('prerelease', 'draft'):
            with self.assertRaisesRegex(ValueError, 'unexpected stable'):
                current_references(['reth_release'], lambda _: dict(self.release(''), **{field: True}))
        with self.assertRaises(OSError):
            current_references(['reth_release'], lambda _: (_ for _ in ()).throw(OSError('offline')))

    def lock(self):
        return dict(hive_commit=HIVE, clients={
            'reth_release': dict(requested='ghcr.io/paradigmxyz/reth:v2.0.0', image_id='sha256:one', digest='repo@sha256:one'),
            'go-ethereum_trace': dict(image_id='sha256:geth', source=dict(commit='a'*40, dirty=False))})

    def command(self, *args, **kwargs):
        if args[:3] == ('docker','image','inspect'):
            return json.dumps([dict(Id='sha256:one', RepoDigests=['repo@sha256:one'])])
        if args[:2] == ('git','ls-remote'):
            return 'a'*40+'\trefs/heads/feat/trace\n'
        return ''

    @patch('trace_interop.versions.github_json')
    @patch('trace_interop.cli.run')
    def test_preflight_contacts_registry_and_records_identity(self, run, fetch):
        fetch.side_effect = self.release
        run.side_effect = self.command
        result = check_current(self.lock())
        self.assertEqual(result['status'], 'current')
        self.assertIn('checked_at', result)
        self.assertEqual(result['clients']['go-ethereum_trace'], 'sha256:geth')
        run.assert_any_call('docker','pull','ghcr.io/paradigmxyz/reth:v2.0.0')

    @patch('trace_interop.versions.github_json')
    @patch('trace_interop.cli.run')
    def test_rejects_old_release_retagged_image_moved_or_dirty_geth(self, run, fetch):
        fetch.side_effect = self.release
        run.side_effect = self.command
        for client, key, value in [
            ('reth_release','requested','ghcr.io/paradigmxyz/reth:v1.0.0'),
            ('reth_release','image_id','sha256:old'),
            ('reth_release','digest','repo@sha256:old'),
            ('go-ethereum_trace','source',dict(commit='b'*40, dirty=False)),
            ('go-ethereum_trace','source',dict(commit='a'*40, dirty=True)),
        ]:
            lock = self.lock()
            lock['clients'][client][key] = value
            with self.subTest(client=client, key=key), self.assertRaisesRegex(ValueError, 'stale client lock'):
                check_current(lock)
        run.side_effect = OSError('registry offline')
        with self.assertRaises(OSError):
            check_current(self.lock())
        with self.assertRaisesRegex(ValueError, 'empty'):
            check_current({'clients':{}})

    def test_flags_development_builds_older_than_their_release_build(self):
        # 2026-09-29 matrix: the Reth nightly was built hours before the v2.7.0 release image.
        clients = {
            'reth_development': dict(created='2026-09-28T01:42:58.151009851Z'),
            'reth_release': dict(created='2026-09-28T11:08:00.92360729Z', release=dict(tag='v2.7.0')),
            'erigon_development': dict(created='2026-09-28T22:16:55Z'),
            'erigon_release': dict(created='2026-09-24T12:26:33Z', release=dict(tag='v3.7.0')),
            'besu_development': dict(created='2026-09-28T16:20:49Z'),
            'go-ethereum_trace': dict(image_id='sha256:geth')}
        self.assertEqual(lagging_development(clients), {'reth_development': dict(
            created='2026-09-28T01:42:58.151009851Z', release='v2.7.0', release_created='2026-09-28T11:08:00.92360729Z')})

    @patch('trace_interop.versions.github_json')
    @patch('trace_interop.cli.run')
    def test_preflight_records_lagging_development_builds_without_failing(self, run, fetch):
        fetch.side_effect = self.release
        run.side_effect = self.command
        lock = self.lock()
        lock['clients']['reth_release'].update(created='2026-09-22T00:00:00Z', release=dict(tag='v2.0.0'))
        lock['clients']['reth_development'] = dict(requested='ghcr.io/paradigmxyz/reth:nightly', image_id='sha256:one',
                                                   digest='repo@sha256:one', created='2026-09-21T01:00:00Z')
        result = check_current(lock)
        self.assertEqual(result['status'], 'current')
        self.assertEqual(list(result['lagging_development']), ['reth_development'])

    @patch('trace_interop.versions.resolve_geth')
    @patch('trace_interop.versions.resolve_native')
    def test_matrix_refreshes_by_default_and_reproduction_is_explicit(self, native, geth):
        native.return_value = dict(hive_commit=HIVE, clients={n:dict(image_id=n) for n in NAMES})
        geth.return_value = dict(hive_commit=HIVE, clients={'go-ethereum_trace':dict(image_id='geth')})
        with tempfile.TemporaryDirectory() as folder:
            first = Path(folder)/'clients.json'
            lock = matrix_lock(first)
            native.assert_called_once()
            geth.assert_called_once()
            native.reset_mock(); geth.reset_mock()
            second = Path(folder)/'reproduction.json'
            self.assertEqual(matrix_lock(second, first), lock)
            native.assert_not_called(); geth.assert_not_called()
            with self.assertRaisesRegex(ValueError, 'immutable'):
                matrix_lock(second, first)


class MatrixInventoryTests(unittest.TestCase):
    def test_current_reports_cannot_mix_builds_drop_failed_runs_or_claim_historical_freshness(self):
        from trace_interop.inventory import report_runs
        from trace_interop.cli import write
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            matrix = root/'evidence/current'
            clients = {n:dict(image_id=n, requested=n, client=n.rsplit('_',1)[0]) for n in NAMES+['go-ethereum_trace']}
            # A replica build captures only chains it can replay; forks activate after genesis.
            hosted = {n:v for n,v in clients.items() if v['client'] != 'anvil'}
            manifests = {c:dict(corpus=c, clients=copy.deepcopy(clients)) for c in ['initial','a']}
            manifests['forks'] = dict(corpus='forks', clients=copy.deepcopy(hosted))
            for c,manifest in manifests.items(): write(matrix/c/'manifest.json', manifest)
            write(matrix/'clients.lock.json',dict(clients=clients))
            preflight = dict(status='current', checked_at='2026-09-24T00:00:00Z',
                             clients={n:v['image_id'] for n,v in clients.items()})
            write(matrix/'preflight.json',preflight)
            write(matrix/'matrix.json',[dict(corpus='initial',complete=True),dict(corpus='a',complete=False),dict(corpus='forks',complete=True)])
            selection = dict(matrix='evidence/current',runs=['evidence/current/initial','evidence/current/a','evidence/current/forks'])
            write(root/'reports.lock.json',selection)
            self.assertEqual(len(report_runs(root)),3)
            for corpus, selected in [('forks', clients), ('initial', hosted)]:
                write(matrix/corpus/'manifest.json',dict(corpus=corpus,clients=selected))
                with self.assertRaisesRegex(ValueError, 'mixed or missing'): report_runs(root)
                write(matrix/corpus/'manifest.json',manifests[corpus])
            write(root/'reports.lock.json',dict(selection,runs=selection['runs'][:1]))
            with self.assertRaisesRegex(ValueError, 'entire current matrix'): report_runs(root)
            # A focused capture of a new corpus joins the matrix only with the matrix's own builds.
            focused = root/'evidence/focused'
            write(focused/'raw-selector/manifest.json', dict(corpus='raw-selector', clients=copy.deepcopy(clients)))
            write(root/'reports.lock.json',dict(selection,runs=selection['runs']+['evidence/focused/raw-selector']))
            self.assertEqual(len(report_runs(root)),4)
            write(focused/'raw-selector/manifest.json', dict(corpus='raw-selector', clients=dict(clients, reth_release=dict(clients['reth_release'], image_id='old'))))
            with self.assertRaisesRegex(ValueError, 'mixed or missing'): report_runs(root)
            write(focused/'a/manifest.json', dict(corpus='a', clients=copy.deepcopy(clients)))
            write(root/'reports.lock.json',dict(selection,runs=selection['runs']+['evidence/focused/a']))
            with self.assertRaisesRegex(ValueError, 'repeats a corpus'): report_runs(root)
            # A focused recapture replaces the matrix's run of a corpus when it resends every request that run sent.
            sent = [dict(name='filter', request=dict(method='trace_filter', params=[{}]))]
            added = [dict(name='filter-blockhash', request=dict(method='trace_filter', params=[{'blockHash': '0x02'}]))]
            write(matrix/'a/manifest.json', dict(manifests['a'], selected_cases=sent))
            write(focused/'a/manifest.json', dict(corpus='a', clients=copy.deepcopy(clients), selected_cases=sent+added))
            write(root/'reports.lock.json',dict(selection,runs=[r for r in selection['runs'] if r != 'evidence/current/a']+['evidence/focused/a']))
            self.assertEqual(len(report_runs(root)),3)
            write(focused/'a/manifest.json', dict(corpus='a', clients=copy.deepcopy(clients), selected_cases=added))
            with self.assertRaisesRegex(ValueError, 'resend every request'): report_runs(root)
            write(matrix/'a/manifest.json',manifests['a'])
            write(root/'reports.lock.json',selection)
            manifests['a']['clients']['reth_release']['image_id']='old'
            write(matrix/'a/manifest.json',manifests['a'])
            with self.assertRaisesRegex(ValueError, 'mixed or missing'): report_runs(root)
            manifests['a']['clients']=clients
            write(matrix/'a/manifest.json',manifests['a'])
            write(matrix/'preflight.json',dict(preflight,status='historical-reproduction'))
            with self.assertRaisesRegex(ValueError, 'freshness preflight'): report_runs(root)

    @patch('trace_interop.versions.matrix_lock', return_value={})
    @patch('trace_interop.versions.check_current', side_effect=ValueError('stale'))
    @patch('subprocess.run')
    def test_suite_stops_before_corpus_on_failed_preflight(self, run, check, resolve):
        import runpy
        with tempfile.TemporaryDirectory() as folder, patch('sys.argv', ['run_matrix.py','--output',folder+'/run']):
            with self.assertRaisesRegex(ValueError,'stale'):
                runpy.run_path(str(Path(__file__).resolve().parents[1]/'scripts/run_matrix.py'))
        run.assert_not_called()

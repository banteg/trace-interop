"""Freshness is a live gate; failures never silently reuse historical builds."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from trace_interop.cli import HIVE
from trace_interop.versions import current_references, check_current, matrix_lock, NAMES


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

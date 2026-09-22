"""Counterexamples to false-positive capture and conformance assessments."""
import copy
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from trace_interop.cli import ROOT, collect, parse_exchange, read, sha, write
from trace_interop.rules import evaluate
from trace_interop.scenarios import verify_state




class ReportingRegressions(unittest.TestCase):
    def test_missing_and_ineligible_observations_are_accounted(self):
        from trace_interop.report import generate
        source = ROOT/'evidence/2026-09-23/geth-40eecf3-initial'
        for eligible in [True, False]:
            with self.subTest(eligible=eligible), tempfile.TemporaryDirectory() as tmp:
                base = Path(tmp); folder = base/'partial'; folder.mkdir()
                for file in ['manifest.json', 'summary.json', 'observations.json']:
                    write(folder/file, read(source/file))
                obs = read(folder/'observations.json'); del obs['filter-both']['go-ethereum_trace']
                write(folder/'observations.json', obs)
                write(folder/'checksums.json', {file.name: sha(file) for file in folder.iterdir()})
                with patch('trace_interop.report.verify_setup', return_value=(eligible, 'setup test')), patch('trace_interop.presentation.render'), contextlib.redirect_stdout(io.StringIO()):
                    generate(ROOT, [folder], base/'report')
                row = next(r for r in read(base/'report/checks.json') if r['case'] == 'filter-both')
                self.assertEqual(row['assessment'], 'unassessed')
                self.assertEqual([c['status'] for c in row['checks'] if c['topic'] == 'H03'], ['unassessed'])
                self.assertEqual(row['eligible'], eligible)
                self.assertGreater(read(base/'report/assessment.json')['coverage']['unassessed'], 0)

    def test_mixed_builds_do_not_harmonize_and_new_complete_build_supersedes_old(self):
        from trace_interop.status import decision_status, NATIVE_CLIENTS
        decision = {'id': 'H03', 'cases': ['a/one', 'a/two']}
        position = {'policy': 'converged', 'note': 'Agreed', 'sources': [{'label':'Review','url':'https://example.org'}]}
        records = [dict(client=f'{family}_{channel}', corpus='a', case=case, eligible=True,
                        build_id=build, captured_at=date, checks=[{'topic':'H03','status':'matches'}])
                   for family in NATIVE_CLIENTS for channel in ['development','release']
                   for case,build,date in [('one','v1','2026-09-21T00:00:00+00:00'),('two','v2','2026-09-22T00:00:00+00:00')]]
        self.assertEqual(decision_status(decision, records, position), '🤝 Converged')
        for row in list(records):
            if row['build_id'] == 'v1': row['checks'][0]['status'] = 'change_needed'
            else: records.append(dict(row, case='one'))
        self.assertEqual(decision_status(decision, records, position), '✅ Harmonized · stable')
        # A newly observed build in a different corpus still prevents stale badges.
        records.append(dict(records[-1], corpus='new', case='unrelated', build_id='v3', captured_at='2026-09-23T00:00:00+00:00', checks=[]))
        self.assertEqual(decision_status(decision, records, position), '🧪 Harmonized · dev')

    def test_report_rechecks_control_status_instead_of_trusting_capture_eligibility(self):
        from trace_interop.report import generate
        source = ROOT/'evidence/2026-09-23/geth-40eecf3-initial'
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp); folder = base/'invalid-control'; folder.mkdir()
            manifest, summary, obs = [read(source/f) for f in ['manifest.json','summary.json','observations.json']]
            # All bytes/roots are correct but the numbered control had a bad envelope.
            obs['_control/head']['go-ethereum_trace']['status'] = 'invalid_envelope'
            obs['_control/latest'] = copy.deepcopy(obs['_control/head'])
            obs['_control/latest']['go-ethereum_trace']['status'] = 'result'
            manifest['selected_cases'].append({'name':'_control/latest','request':{'method':'eth_getBlockByNumber','params':['latest',False]}})
            for name, value in [('manifest',manifest),('summary',summary),('observations',obs)]: write(folder/(name+'.json'),value)
            write(folder/'checksums.json',{file.name:sha(file) for file in folder.iterdir()})
            with patch('trace_interop.presentation.render'), contextlib.redirect_stdout(io.StringIO()): generate(ROOT,[folder],base/'report')
            row=next(r for r in read(base/'report/checks.json') if r['case']=='filter-both')
            self.assertTrue(row['capture_eligible'])
            self.assertFalse(row['eligible'])
            self.assertEqual(row['assessment'],'unassessed')

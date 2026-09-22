"""Regression counterexamples from the second harness review."""
import contextlib
import copy
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from trace_interop.cli import ROOT, read, write, sha, parse_exchange
from trace_interop.rules import evaluate
from test_harness_regressions import captured


class SemanticChecks(unittest.TestCase):
    def check_status(self, c, o, p, topic, expected):
        checks = [x for x in evaluate(c, o, p) if x['topic'] == topic]
        self.assertTrue(checks)
        if expected == 'matches':
            self.assertTrue(all(x['status'] == expected for x in checks), checks)
        else:
            self.assertIn(expected, [x['status'] for x in checks], checks)

    def test_empty_selection_preserves_fixture_output(self):
        for corpus, name in [('initial', 'call-empty-types-priced'), ('a', 'empty-types')]:
            c,o,p = captured('2026-09-23/harness-audit-geth-'+corpus,name,'go-ethereum_trace')
            self.check_status(c,o,p,'H11','matches')
            for bad in ['0x','0xffff',None]:
                with self.subTest(corpus=corpus, bad=bad):
                    o['response']['result']['output']=bad
                    self.check_status(c,o,p,'H11','change_needed')

    def test_callmany_diffs_are_individual_transitions(self):
        for name in ['many-storage-write-read','many-storage-write-revert-read']:
            for mutation in ['repeat diff','repeat nonce','drop first write','commit reverted write','null diff']:
                with self.subTest(name=name, mutation=mutation):
                    c,o,p=captured('2026-09-23/harness-audit-geth-a',name,'go-ethereum_trace')
                    self.check_status(c,o,p,'H16','matches')
                    r=o['response']['result'];sender=c['context']['sender'];target=c['request']['params'][0][0][0]['to']
                    if mutation=='repeat diff': r[1]['stateDiff']=copy.deepcopy(r[0]['stateDiff'])
                    elif mutation=='repeat nonce': r[1]['stateDiff'][sender]['nonce']=copy.deepcopy(r[0]['stateDiff'][sender]['nonce'])
                    elif mutation=='drop first write': r[0]['stateDiff'][target]['storage']={}
                    elif mutation=='commit reverted write': r[1]['stateDiff'][target]=copy.deepcopy(r[0]['stateDiff'][target])
                    else: r[1]['stateDiff']=None
                    self.check_status(c,o,p,'H16','change_needed')

    def test_storage_add_and_zero_to_value_encodings_are_equivalent_for_h16(self):
        c,o,p=captured('2026-09-23/harness-audit-geth-a','many-storage-write-read','go-ethereum_trace')
        target=c['request']['params'][0][0][0]['to'];slot='0x'+'00'*32
        o['response']['result'][0]['stateDiff'][target]['storage'][slot]={'*':{'from':slot,'to':'0x'+f'{42:064x}'}}
        self.check_status(c,o,p,'H16','matches')

    def test_deletion_values_match_frozen_prestate(self):
        for field,bad in [('code',{'-':'0x'}),('nonce',{'-':'0xdead'}),('storage',{'0x'+'00'*32:{'-':'0x'+'01'*32}})]:
            with self.subTest(field=field):
                c,o,p=captured('2026-09-23/harness-audit-geth-fork-followup','destroy-trace-55','go-ethereum_trace')
                self.check_status(c,o,p,'H26','matches')
                o['response']['result']['stateDiff'][c['request']['params'][0]['to']][field]=bad
                self.check_status(c,o,p,'H26','change_needed')

    def test_deletion_oracle_matches_genesis(self):
        alloc=read(ROOT/'fixtures/chains/forks/genesis.json')['alloc']
        account=alloc['0000000000000000000000000000000000001007']
        self.assertEqual(account['code'],'0x611008ff')
        self.assertEqual(account.get('nonce','0x0'),'0x0')
        self.assertEqual(account.get('storage',{}),{})


class ReferenceErrors(unittest.TestCase):
    def test_malformed_reference_does_not_abort_report(self):
        from trace_interop.report import generate
        import json
        source=ROOT/'evidence/2026-09-23/harness-audit-geth-initial'
        for bad in [None,[],3,'bad']:
            with self.subTest(bad=bad), tempfile.TemporaryDirectory() as tmp:
                folder=Path(tmp)
                manifest,summary,observations=[read(source/f) for f in ['manifest.json','summary.json','observations.json']]
                request=next(c['request'] for c in manifest['selected_cases'] if c['name']=='block-tree')
                observations['block-tree']['go-ethereum_trace']=parse_exchange('>> '+json.dumps(request)+'\n<< '+json.dumps(bad),request)
                for name,value in [('manifest',manifest),('summary',summary),('observations',observations)]:write(folder/(name+'.json'),value)
                write(folder/'checksums.json',{f.name:sha(f) for f in folder.iterdir()})
                with patch('trace_interop.presentation.render'), contextlib.redirect_stdout(io.StringIO()):generate(ROOT,[folder],folder/'report')
                records=read(folder/'report/checks.json')
                control=next(r for r in records if r['case']=='block-tree')
                self.assertIn('change_needed',[c['status'] for c in control['checks'] if c['topic']=='H25'])
                dependent=next(r for r in records if r['case']=='filter-both')
                self.assertEqual([c['status'] for c in dependent['checks'] if c['topic']=='H03'],['unassessed'])


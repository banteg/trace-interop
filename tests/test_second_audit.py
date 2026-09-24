"""Regression counterexamples from the second harness review."""
import contextlib
import copy
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from trace_interop.cli import ROOT, read, write, sha, parse_exchange, load_observations
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
                    c,o,p=captured('2026-09-23/harness-audit-native-a',name,'erigon_development')
                    self.check_status(c,o,p,'H16','matches')
                    r=o['response']['result'];sender=c['context']['sender'];target=c['request']['params'][0][0][0]['to']
                    if mutation=='repeat diff': r[1]['stateDiff']=copy.deepcopy(r[0]['stateDiff'])
                    elif mutation=='repeat nonce': r[1]['stateDiff'][sender]['nonce']=copy.deepcopy(r[0]['stateDiff'][sender]['nonce'])
                    elif mutation=='drop first write': r[0]['stateDiff'][target]['storage']={}
                    elif mutation=='commit reverted write': r[1]['stateDiff'][target]=copy.deepcopy(r[0]['stateDiff'][target])
                    else: r[1]['stateDiff']=None
                    self.check_status(c,o,p,'H16','change_needed')

    def test_existing_account_slots_use_change_markers(self):
        c,o,p=captured('2026-09-23/harness-audit-native-a','many-storage-write-read','erigon_development')
        self.check_status(c,o,p,'H16','matches')
        target=c['request']['params'][0][0][0]['to'];slot='0x'+'00'*32
        for index,marker in [(0,{'+':'0x'+f'{42:064x}'}),(1,'=')]:
            with self.subTest(marker=marker):
                mutated=copy.deepcopy(o)
                mutated['response']['result'][index]['stateDiff'].setdefault(target,{})['storage']={slot:marker}
                self.check_status(c,mutated,p,'H16','change_needed')

    def test_deletion_values_match_frozen_prestate(self):
        for field,bad in [('code',{'-':'0x'}),('nonce',{'-':'0xdead'}),('storage',{'0x'+'00'*32:{'-':'0x'+'01'*32}})]:
            with self.subTest(field=field):
                c,o,p=captured('2026-09-23/harness-audit-geth-fork-followup','destroy-trace-55','go-ethereum_trace')
                self.check_status(c,o,p,'H26','matches')
                o['response']['result']['stateDiff'][c['request']['params'][0]['to']][field]=bad
                self.check_status(c,o,p,'H26','change_needed')

    def test_deleted_balance_matches_genesis_and_storage_is_empty(self):
        alloc=read(ROOT/'fixtures/chains/forks/genesis.json')['alloc']
        for field,bad in [('balance',{'*':{'from':'0x64','to':None}}),('balance',{'-':'0x0'})]:
            with self.subTest(field=field, bad=bad):
                c,o,p=captured('2026-09-23/harness-audit-geth-fork-followup','destroy-trace-55','go-ethereum_trace')
                c['context']['_alloc']={'0x'+a:v for a,v in alloc.items()}
                self.check_status(c,o,p,'H26','matches')
                o['response']['result']['stateDiff'][c['request']['params'][0]['to']][field]=bad
                self.check_status(c,o,p,'H26','change_needed')
        # Any deleted account, not only the fixture's, must report empty storage.
        c,o,p=captured('2026-09-23/harness-audit-geth-fork-followup','destroy-trace-55','go-ethereum_trace')
        other={'balance':{'-':'0x1'},'code':{'-':'0x00'},'nonce':{'-':'0x1'},'storage':{'0x'+'00'*32:{'*':{'from':'0x'+'01'*32,'to':'0x'+'00'*32}}}}
        o['response']['result']['stateDiff']['0x'+'22'*20]=other
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
                manifest,summary=[read(source/f) for f in ['manifest.json','summary.json']];observations=load_observations(source)
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


class IsolationScenario(unittest.TestCase):
    def test_case_selection_keeps_every_ordered_phase(self):
        from trace_interop.cli import selected_cases
        from trace_interop.scenarios import ordered_cases
        corpus=read(ROOT/'fixtures/corpora/callmany-isolation.json')
        self.assertEqual(selected_cases(corpus,'^after-write-read/storage$'),corpus['cases'])
        for bad in [['before'],['before','before'],['../escape']]:
            with self.subTest(phases=bad),self.assertRaises(ValueError):
                ordered_cases(dict(corpus,scenario_phases=bad))

    def test_capture_plan_is_required_for_eligibility(self):
        from trace_interop.scenarios import verify_setup
        corpus=read(ROOT/'fixtures/corpora/callmany-isolation.json')
        manifest=read(ROOT/'evidence/2026-09-23/harness-audit-geth-a/manifest.json')
        manifest['corpus']='callmany-isolation'
        manifest['selected_cases']=[c for c in manifest['selected_cases'] if c['name'].startswith('_control/')]+corpus['cases']
        self.assertIn('Ordered scenario',verify_setup(manifest,corpus,{},'c')[1])

    def test_isolation_requires_order_and_execution_and_checks_after_value(self):
        corpus=read(ROOT/'fixtures/corpora/callmany-isolation.json')
        corpus.update(_chain='callmany-isolation',_scenario_phases=corpus['scenario_phases'])
        zero='0x'+'00'*32
        for kind in ['write-read','write-revert-read']:
            c=next(c for c in corpus['cases'] if c['name']=='after-'+kind+'/storage')
            c=dict(c,context=corpus)
            _,simulation,_=captured('2026-09-23/harness-audit-geth-a','many-storage-'+kind,'go-ethereum_trace')
            obs={'status':'result','response':{'result':zero}}
            peers={c['isolation_before']:copy.deepcopy(obs),c['isolation_after']:simulation}
            checks=lambda: [x for x in evaluate(c,obs,peers) if x['topic']=='H16']
            self.assertEqual([x['status'] for x in checks()],['matches'])
            obs['response']['result']='0x'+f'{42:064x}'
            self.assertEqual([x['status'] for x in checks()],['change_needed'])
            obs['response']['result']=zero
            for bad in [None,list(reversed(corpus['scenario_phases']))]:
                corpus['_scenario_phases']=bad
                self.assertEqual([x['status'] for x in checks()],['unassessed'])
            corpus['_scenario_phases']=corpus['scenario_phases']
            peers[c['isolation_after']]={'status':'unsupported','response':{'error':{'code':-32601}}}
            self.assertEqual([x['status'] for x in checks()],['unassessed'])

    def test_ordered_adapter_uses_phase_plan_instead_of_global_lexical_order(self):
        from trace_interop.scenarios import prepare, ORDERED
        corpus=read(ROOT/'fixtures/corpora/callmany-isolation.json')
        with tempfile.TemporaryDirectory() as tmp:
            hive=Path(tmp);sim=hive/'simulators/ethereum/rpc-compat';(sim/'tests').mkdir(parents=True)
            for path in ['clients/reth','clients/go-ethereum']:(hive/path).mkdir(parents=True)
            def original(args,**kwargs):
                if args[-1].endswith('/main.go'):return b'sendForkchoiceUpdated(t, c)\nrunAllTests(t, c, c.Type)\n'
                return b''
            with patch('trace_interop.scenarios.subprocess.check_output',side_effect=original):
                prepare(hive,corpus,'callmany-isolation',{},'0xhead')
            self.assertEqual(read(sim/'tests/ordered.json'),['_control']+corpus['scenario_phases'])
            self.assertNotIn('runAllTests', (sim/'main.go').read_text())
            self.assertIn('runInteropOrdered(t, c)',(sim/'main.go').read_text())
            self.assertIn('for _,phase:=range phases',ORDERED)
            self.assertIn('t.Run(hivesim.TestSpec',ORDERED)

    def test_captured_requests_follow_the_declared_phase_order(self):
        import re
        for run in ['native-isolation-verified','geth-isolation']:
            folder=ROOT/'evidence/2026-09-23'/('harness-audit-2-'+run)
            manifest=read(folder/'manifest.json')
            observed={client:[] for client in manifest['clients']}
            for line in (folder/'runner.log').read_text().splitlines():
                if 'test started' not in line:continue
                match=re.search(r'name="interop/(.*?) \(([^)]+)\)"',line)
                if match:observed[match[2]].append(match[1])
            expected=[c['name'] for phase in ['_control']+manifest['scenario_phases']
                      for c in sorted(manifest['selected_cases'],key=lambda c:c['name'])
                      if c['name'].split('/')[0]==phase]
            for client,names in observed.items():
                with self.subTest(run=run,client=client):self.assertEqual(names,expected)

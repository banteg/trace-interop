"""Separate account-existence encoding from admission and environment failures."""
import copy
import unittest

from trace_interop.chain_model import load_chain
from trace_interop.cli import ROOT, read, CHAINS
from trace_interop.coverage import supplement
from trace_interop.execution_models import created_address, prestate


class H17CapturedRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.corpora = {}
        cls.observations = {}
        for name in ['initial', 'a', 'coverage']:
            context = read(ROOT/f'fixtures/corpora/{name}.json')
            chain = ROOT/'fixtures/chains'/CHAINS[name]
            genesis = read(chain/'genesis.json')
            header = read(chain/'headblock.json')
            context['_alloc'] = {'0x'+a.removeprefix('0x'): v for a,v in genesis['alloc'].items()}
            context['_codes'] = {a:v.get('code','0x') for a,v in context['_alloc'].items()}
            context['_blocks'] = load_chain(chain/'chain.rlp')
            context['_head'] = header
            context['_environment'] = {k:int(header[v],16) for k,v in
                [('BASEFEE','baseFeePerGas'),('NUMBER','number'),('TIMESTAMP','timestamp'),('GASLIMIT','gasLimit')]}
            cls.corpora[name] = context
            cls.observations[name] = read(ROOT/f'evidence/2026-09-24/current-matrix/{name}/observations.json')

    def case(self, corpus, name):
        context = self.corpora[corpus]
        return dict(next(c for c in context['cases'] if c['name']==name), context=context)

    def checks(self, corpus, name, client, observation=None):
        peers = {n:clients.get(client,{}) for n,clients in self.observations[corpus].items()}
        return supplement(self.case(corpus,name), observation or peers[name], peers, [], ['H17'])

    def test_environment_errors_do_not_become_creation_marker_errors(self):
        for family, name in [('erigon','model-environment'), ('reth','model-environment-free')]:
            for channel in ['release','development']:
                client = f'{family}_{channel}'
                with self.subTest(client=client,case=name):
                    checks = self.checks('coverage',name,client)
                    self.assertTrue(all(c['status']=='matches' for c in checks if c['topic']=='H17'))
                    self.assertIn('change_needed',[c['status'] for c in checks if c['topic']=='H15'])
                    self.assertIn('change_needed',[c['status'] for c in checks if c['topic']=='H08'])

    def test_marker_and_runtime_inconsistency_mutations_still_fail(self):
        name, client = 'model-environment', 'erigon_development'
        context = self.corpora['coverage']
        case = self.case('coverage',name)
        address = created_address(case['request']['params'][0]['from'],context['model_nonce'])
        for code in ['=', {'*':{'from':'0x','to':'0x'}}, {'+':'0xff'}]:
            obs = copy.deepcopy(self.observations['coverage'][name][client])
            obs['response']['result']['stateDiff'][address]['code'] = code
            checks = self.checks('coverage',name,client,obs)
            self.assertIn('change_needed',[c['status'] for c in checks if c['topic']=='H17'])

    def test_missing_diff_is_blocked_instead_of_a_marker_failure(self):
        for channel in ['release','development']:
            checks = self.checks('initial','raw-valid-default-block',f'besu_{channel}')
            self.assertEqual([c['status'] for c in checks if c['topic']=='H17'],['blocked'])
        for name in ['model-empty-runtime','model-transfer','model-many-transfers']:
            obs = copy.deepcopy(self.observations['coverage'][name]['besu_development'])
            result = obs['response']['result']
            for envelope in result if isinstance(result,list) else [result]:
                envelope['stateDiff'] = None
            checks = self.checks('coverage',name,'besu_development',obs)
            statuses = [c['status'] for c in checks if c['topic']=='H17']
            self.assertTrue(statuses)
            self.assertEqual(set(statuses),{'blocked'})

    def test_new_transfer_account_and_empty_contract_have_independent_prestate(self):
        context = self.corpora['coverage']
        block = context['_blocks'][context['_head']['number']]
        exists,_ = prestate(context,block,None)
        case = self.case('coverage','model-transfer')
        self.assertNotIn(case['transfer_model']['target'],exists)
        self.assertIn(case['transfer_model']['sender'],exists)
        self.assertNotIn(created_address(case['transfer_model']['sender'],context['model_nonce']),exists)
        for family, differs in [('besu',False),('erigon',False),('nethermind',True),('reth',True)]:
            for channel in ['release','development']:
                checks = self.checks('coverage','model-transfer',f'{family}_{channel}')
                self.assertEqual(any(c['status']=='change_needed' for c in checks if c['topic']=='H17'),differs)
        for family, differs in [('besu',False),('erigon',False),('nethermind',True),('reth',False)]:
            checks = self.checks('coverage','model-empty-runtime',f'{family}_development')
            self.assertEqual(any(c['status']=='change_needed' for c in checks if c['topic']=='H17'),differs)

    def test_prefunded_account_is_existing_on_every_build(self):
        from trace_interop.rules import evaluate
        case = self.case('a','prefunded-empty')
        for client, observation in self.observations['a']['prefunded-empty'].items():
            checks = evaluate(case, observation, {})
            self.assertEqual([c['status'] for c in checks if c['topic']=='H17'],['matches'],client)

    def test_nethermind_fix_preserves_birth_and_subsequent_update_markers(self):
        fresh = read(ROOT/'evidence/2026-09-24/h17-retest/coverage/observations.json')
        client = 'nethermind_development'
        for name in ['model-transfer', 'model-many-transfers', 'model-empty-runtime']:
            with self.subTest(case=name):
                old = self.checks('coverage', name, client)
                new = self.checks('coverage', name, client, fresh[name][client])
                self.assertIn('change_needed', [c['status'] for c in old if c['topic']=='H17'])
                self.assertEqual({c['status'] for c in new if c['topic']=='H17'}, {'matches'})
        envelopes = fresh['model-many-transfers'][client]['response']['result']
        target = self.case('coverage', 'model-many-transfers')['transfer_model']['target']
        self.assertEqual(envelopes[0]['stateDiff'][target]['code'], {'+':'0x'})
        self.assertEqual(envelopes[1]['stateDiff'][target]['code'], '=')

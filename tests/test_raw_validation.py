import copy
import json
import unittest
from pathlib import Path

from trace_interop.scenarios import verify_state

ROOT = Path(__file__).resolve().parents[1]


class RawValidationFixtures(unittest.TestCase):
    def setUp(self):
        self.corpus = json.loads((ROOT/'fixtures/corpora/raw-validation.json').read_text())

    def test_only_intended_signed_field_changes(self):
        cases = {c['name'].removeprefix('raw-validation-').removesuffix('-all'): c
                 for c in self.corpus['cases'] if c['name'].endswith('-all')}
        valid = cases['valid']
        for name, changed in [('nonce-low', 'signed_nonce'), ('nonce-high', 'signed_nonce'),
                              ('wrong-chain', 'chainId'), ('funds-value', 'value'),
                              ('funds-gas', 'value'), ('intrinsic-gas', 'gas'), ('below-basefee', 'gasPrice'),
                              ('code-sender', 'sender'), ('delegated-sender-valid', 'sender'),
                              ('execution-oog-valid', 'gas')]:
            a = dict(valid['signed_fields'], signed_nonce=valid['signed_nonce'], sender=valid['sender'])
            b = dict(cases[name]['signed_fields'], signed_nonce=cases[name]['signed_nonce'], sender=cases[name]['sender'])
            self.assertEqual({k for k in a if a[k] != b[k]}, {changed}, name)
        self.assertEqual(cases['intrinsic-gas']['signed_fields']['gas'], hex(20999))
        self.assertEqual(cases['execution-oog-valid']['signed_fields']['gas'], hex(21000))
        self.assertEqual(cases['execution-oog-valid']['validation'], 'execute')
        self.assertEqual(cases['delegated-sender-valid']['validation'], 'execute')
        for name in ['create-nonce-high', 'create-nonce-low']:
            self.assertNotEqual(cases[name]['signed_create_address'], cases[name]['state_create_address'])

    def test_setup_checks_every_independent_control(self):
        observations = {name: {'c': {'status':'result', 'response': {'result': expected}}}
                        for name, expected in self.corpus['controls'].items()}
        observations['_control/head'] = {'c': {'status':'result', 'response': {'result': {'baseFeePerGas': self.corpus['base_fee']}}}}
        self.assertTrue(verify_state('raw-validation', self.corpus, observations, 'c')[0])
        for name in observations:
            broken = copy.deepcopy(observations); broken.pop(name)
            self.assertFalse(verify_state('raw-validation', self.corpus, broken, 'c')[0], name)

    def test_all_probes_have_all_and_individual_trace_selections(self):
        probes = [c for c in self.corpus['cases'] if 'validation' in c]
        self.assertEqual(len(probes), 56)
        for base in {c['name'].rsplit('-', 1)[0] for c in probes}:
            variants = [c for c in probes if c['name'].rsplit('-', 1)[0] == base]
            self.assertEqual({tuple(c['request']['params'][1]) for c in variants},
                             {('trace', 'stateDiff', 'vmTrace'), ('trace',), ('stateDiff',), ('vmTrace',)})


class RawValidationEvidence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = ROOT/'evidence/2026-09-23/raw-validation-native'
        cls.observations = json.loads((base/'observations.json').read_text())
        cls.summary = json.loads((base/'summary.json').read_text())
        corpus = json.loads((ROOT/'fixtures/corpora/raw-validation.json').read_text())
        cls.cases = {c['name']: c for c in corpus['cases']}

    def result(self, probe, client):
        item = self.observations[f'raw-validation-{probe}-all'][client]
        self.assertEqual(item['status'], 'result')
        return item['response']['result']

    def test_execution_claims_require_output_storage_and_vm_evidence(self):
        self.assertTrue(self.summary['complete'])
        self.assertEqual(len(self.summary['eligible']), 8)
        self.assertTrue(all(self.summary['eligible'].values()))
        probes = {'besu': ['wrong-chain', 'code-sender'],
                  'erigon': ['nonce-low', 'nonce-high', 'funds-value', 'funds-gas', 'code-sender'],
                  'nethermind': ['nonce-low', 'nonce-high', 'code-sender'], 'reth': []}
        word = '0x'+f'{42:064x}'
        for client, invalid in probes.items():
            for channel in ['release', 'development']:
                for probe in ['valid', 'delegated-sender-valid']+invalid:
                    r = self.result(probe, f'{client}_{channel}')
                    self.assertEqual(r['output'], word)
                    self.assertEqual(r['stateDiff']['0x'+'0'*36+'1002']['storage']['0x'+'0'*64]['*']['to'], word)
                    self.assertTrue(r['vmTrace']['ops'])
                    self.assertNotIn('error', r['trace'][0])

    def test_create_uses_state_nonce_in_executed_code(self):
        for probe in ['create-nonce-low', 'create-nonce-high']:
            case = self.cases[f'raw-validation-{probe}-all']
            address = case['state_create_address'].lower()
            self.assertNotEqual(address, case['signed_create_address'].lower())
            for client in ['erigon', 'nethermind']:
                for channel in ['release', 'development']:
                    r = self.result(probe, f'{client}_{channel}')
                    self.assertEqual(r['output'], '0x'+'0'*24+address[2:])
                    self.assertEqual(r['trace'][0]['result']['address'].lower(), address)
                    self.assertEqual(r['stateDiff'][address]['code']['+'], r['output'])

    def test_empty_and_malformed_results_are_not_execution_evidence(self):
        for channel in ['release', 'development']:
            for probe in ['nonce-low', 'nonce-high', 'funds-value', 'funds-gas', 'intrinsic-gas', 'below-basefee']:
                r = self.result(probe, 'besu_'+channel)
                self.assertEqual(r['output'], '0x')
                self.assertIsNone(r['stateDiff'])
                self.assertFalse(r['vmTrace']['ops'])
                self.assertEqual(r['trace'][0]['result']['gasUsed'], '0x0')
            for probe in ['wrong-chain', 'funds-value', 'funds-gas', 'intrinsic-gas', 'below-basefee']:
                self.assertEqual(self.observations[f'raw-validation-{probe}-all']['nethermind_'+channel]['status'], 'malformed_json')
            for client in ['besu', 'erigon', 'nethermind', 'reth']:
                r = self.result('execution-oog-valid', f'{client}_{channel}')
                self.assertTrue(r['trace'][0]['error'])

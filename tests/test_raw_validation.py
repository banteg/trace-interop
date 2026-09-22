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
        observations = {name: {'c': {'response': {'result': expected}}}
                        for name, expected in self.corpus['controls'].items()}
        observations['_control/head'] = {'c': {'response': {'result': {'baseFeePerGas': self.corpus['base_fee']}}}}
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

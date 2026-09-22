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


def captured(run, name, client):
    folder = ROOT/'evidence'/run
    manifest = read(folder/'manifest.json')
    observations = read(folder/'observations.json')
    case = next(c for c in manifest['selected_cases'] if c['name'] == name)
    context = read(ROOT/'fixtures/corpora'/f"{manifest['corpus']}.json")
    context['_chain'] = manifest['corpus']
    return dict(case, context=context), observations[name][client], {
        n: clients.get(client, {}) for n, clients in observations.items()}


class SetupRegressions(unittest.TestCase):
    def test_non_json_numbers_are_malformed_and_preserved(self):
        request = {'jsonrpc': '2.0', 'id': 1, 'method': 'trace_call', 'params': []}
        for constant in ['NaN', 'Infinity', '-Infinity']:
            for field in ['"result":{"extra":%s}', '"error":{"code":-32003,"message":"rejected","data":%s}']:
                raw = '{"jsonrpc":"2.0","id":1,' + field % constant + '}'
                obs = parse_exchange('>> '+json.dumps(request)+'\n<< '+raw, request)
                self.assertEqual(obs['status'], 'malformed_json')
                self.assertEqual(obs['raw_response'], raw)

    def test_invalid_envelopes_cannot_establish_state(self):
        corpus = read(ROOT/'fixtures/corpora/raw-validation.json')
        observations = {n: {'c': {'status': 'invalid_envelope', 'response': {'result': v}}}
                        for n, v in corpus['controls'].items()}
        observations['_control/head'] = {'c': {'status': 'invalid_envelope', 'response': {'result': {'baseFeePerGas': corpus['base_fee']}}}}
        self.assertFalse(verify_state('raw-validation', corpus, observations, 'c')[0])

    def test_collector_requires_canonical_head_and_valid_controls(self):
        head = read(ROOT/'fixtures/chains/a/headblock.json')
        corpus = read(ROOT/'fixtures/corpora/a.json')
        control_cases = [c for c in corpus['cases'] if c.get('expected_control') is not None]
        for corruption in ['none', 'missing latest', 'wrong latest', 'wrong id', 'wrong height']:
            with self.subTest(corruption=corruption), tempfile.TemporaryDirectory() as tmp:
                folder = Path(tmp); (folder/'hive').mkdir()
                (folder/'hive/details.log').write_text('')
                cases = [{'name': '_control/head', 'request': {'jsonrpc': '2.0', 'id': 1, 'method': 'eth_getBlockByNumber', 'params': [head['number'], False]}},
                         {'name': '_control/latest', 'request': {'jsonrpc': '2.0', 'id': 1, 'method': 'eth_getBlockByNumber', 'params': ['latest', False]}}] + control_cases
                if corruption == 'missing latest': cases.pop(1)
                write(folder/'manifest.json', {'selected_cases': cases, 'clients': {'c': {}}, 'head': head, 'corpus': 'a'})
                tests = {}
                for i, case in enumerate(cases):
                    value = case.get('expected_control', head)
                    if corruption == 'wrong latest' and case['name'] == '_control/latest': value = dict(head, hash='wrong')
                    if corruption == 'wrong height' and case['name'] == 'control-height': value = '0x0'
                    reply = {'jsonrpc': '2.0', 'id': 999 if corruption == 'wrong id' else 1, 'result': value}
                    tests[str(i)] = {'name': f"interop/{case['name']} (c)", 'summaryResult': {'pass': False, 'details': '>> '+json.dumps(case['request'])+'\n<< '+json.dumps(reply)}}
                write(folder/'hive/suite.json', {'testDetailsLog': 'details.log', 'testCases': tests})
                self.assertEqual(collect(folder)['complete'], corruption == 'none')


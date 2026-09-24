"""Counterexamples to false-positive capture and conformance assessments."""
import copy
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from trace_interop.cli import ROOT, collect, load_observations, parse_exchange, read, sha, write
from trace_interop.rules import evaluate
from trace_interop.scenarios import verify_state


def captured(run, name, client):
    folder = ROOT/'evidence'/run
    manifest = read(folder/'manifest.json')
    observations = load_observations(folder)
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

    def test_case_selector_keeps_setup_controls(self):
        from trace_interop.cli import selected_cases
        for corpus_name, probe in [('a','call-mcopy'), ('raw-validation','raw-validation-valid-all'), ('precompile-values','nested-call-outer0-value1-success')]:
            corpus = read(ROOT/f'fixtures/corpora/{corpus_name}.json')
            names = {c['name'] for c in selected_cases(corpus,'^'+probe+'$')}
            controls = {c['name'] for c in corpus['cases'] if c['name'].startswith(('control-','_control/')) or c.get('expected_control') is not None}
            self.assertTrue(controls <= names)
            self.assertIn(probe,names)

    def test_non_object_control_envelopes_block_setup_without_crashing(self):
        from trace_interop.scenarios import verify_setup
        manifest = read(ROOT/'evidence/2026-09-23/geth-40eecf3-initial/manifest.json')
        corpus = read(ROOT/'fixtures/corpora/initial.json')
        request = next(c['request'] for c in manifest['selected_cases'] if c['name']=='_control/head')
        for response in [[], None, 3, 'bad']:
            observation = parse_exchange('>> '+json.dumps(request)+'\n<< '+json.dumps(response),request)
            self.assertFalse(verify_setup(manifest,corpus,{'_control/head':{'c':observation}},'c')[0])

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



class SemanticRegressions(unittest.TestCase):
    def assert_rejected(self, case, observation, peers, topic):
        checks = [c for c in evaluate(case, observation, peers) if c['topic'] == topic]
        self.assertTrue(checks)
        self.assertFalse(all(c['status'] == 'matches' for c in checks), checks)

    def test_joint_filter_and_reference_omission(self):
        c, o, p = captured('2026-09-23/geth-40eecf3-initial', 'filter-both', 'go-ethereum_trace')
        o['response']['result'] = []; p['block-tree']['response']['result'] = []
        self.assert_rejected(c, o, p, 'H03')

    def test_revert_payload_and_gas_are_measured(self):
        for key, value in [('output', '0xdeadbeef'), ('gasUsed', '0x0')]:
            c, o, p = captured('2026-09-23/geth-40eecf3-a', 'call-siblings-revert-ok', 'go-ethereum_trace')
            next(f for f in o['response']['result']['trace'] if f['traceAddress'] == [0])['result'][key] = value
            self.assert_rejected(c, o, p, 'H09')

    def test_requested_raw_products_cannot_disappear(self):
        for key in ['stateDiff', 'vmTrace']:
            c, o, p = captured('2026-09-23/raw-validation-native', 'raw-validation-valid-all', 'reth_release')
            o['response']['result'][key] = None
            self.assert_rejected(c, o, p, 'H13')

    def test_precompile_child_identity_is_checked(self):
        for key, value in [('to', '0x'+'12'*20), ('value', '0x0'), ('from', '0x'+'34'*20), ('callType', 'delegatecall')]:
            c, o, p = captured('2026-09-23/precompile-values-native', 'nested-call-outer0-value1-success', 'reth_release')
            execution = o['response']['result'][c['execution_index']]
            next(f for f in execution['trace'] if f['traceAddress'] == [0])['action'][key] = value
            self.assert_rejected(c, o, p, 'H29')

    def test_joint_tree_child_and_get_omission(self):
        c, o, p = captured('2026-09-23/geth-40eecf3-a', 'get-nested-positive', 'go-ethereum_trace')
        tree = p['transaction-tree']['response']['result']
        # Hide the constructor's SELFDESTRUCT on both sides and repair counts.
        tree[:] = [f for f in tree if f.get('type') != 'suicide']
        next(f for f in tree if f.get('type') == 'create')['subtraces'] = 0
        o['response']['result'] = None
        self.assert_rejected(c, o, p, 'H02')

    def test_joint_range_and_blocks_omission(self):
        c, o, p = captured('2026-09-23/geth-40eecf3-a', 'filter-two-blocks', 'go-ethereum_trace')
        for name in ['block-2', 'block-3']:
            p[name]['response']['result'] = []
        o['response']['result'] = []
        self.assert_rejected(c, o, p, 'H27')

    def test_marker_storage_and_vm_ops_cannot_be_empty(self):
        for key in ['stateDiff', 'vmTrace']:
            c, o, p = captured('2026-09-23/raw-validation-native', 'raw-validation-valid-all', 'reth_release')
            if key == 'stateDiff':
                o['response']['result'][key][c['marker']]['storage'] = {}
            else:
                o['response']['result'][key]['ops'] = []
            self.assert_rejected(c, o, p, 'H13')

    def test_out_of_gas_cannot_fabricate_marker_storage(self):
        c,o,p = captured('2026-09-23/raw-validation-native','raw-validation-execution-oog-valid-all','reth_release')
        o['response']['result']['stateDiff'][c['marker']] = {'storage':{'0x'+'0'*64:{'+':'0x'+f'{42:064x}'}}}
        self.assert_rejected(c,o,p,'H13')

    def test_original_positive_controls_still_match(self):
        for run,name,client,topic in [
            ('geth-40eecf3-a','call-siblings-revert-ok','go-ethereum_trace','H09'),
            ('geth-40eecf3-initial','transaction-revert','go-ethereum_trace','H09'),
            ('geth-40eecf3-initial','filter-both','go-ethereum_trace','H03'),
            ('raw-validation-native','raw-validation-valid-all','reth_release','H13'),
            ('precompile-values-native','nested-call-outer0-value1-success','reth_release','H29'),
        ]:
            c,o,p = captured('2026-09-23/'+run,name,client)
            checks=[x for x in evaluate(c,o,p) if x['topic']==topic]
            self.assertTrue(checks)
            self.assertTrue(all(x['status']=='matches' for x in checks), (name,checks))

    def test_failed_create_has_no_filter_recipient(self):
        c, o, p = captured('2026-09-23/geth-40eecf3-a', 'filter-created-to', 'go-ethereum_trace')
        # A reverted CREATE whose would-be address is still reported in both the
        # block trace and the filter result must not satisfy toAddress.
        for frames in [p['block-2']['response']['result'], o['response']['result']]:
            next(f for f in frames if f['type'] == 'create')['error'] = 'Reverted'
        self.assert_rejected(c, o, p, 'H23')

    def test_contradicted_reference_action_fails_naming_the_field(self):
        from trace_interop.oracles import TREE
        c, o, p = captured('2026-09-23/geth-40eecf3-initial', 'filter-both', 'go-ethereum_trace')
        tree = p['block-tree']['response']['result']
        # DELEGATECALL reported with the executing address as `to`.
        next(f for f in tree if f['action'].get('callType') == 'delegatecall')['action']['to'] = TREE
        checks = [x for x in evaluate(c, o, p) if x['topic'] == 'H03']
        self.assertEqual([x['status'] for x in checks], ['change_needed'])
        self.assertIn('delegatecall 4 action.to', checks[0]['detail'])

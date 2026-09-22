"""Regressions for independent setup, response shape and semantic assessment."""
import copy
import json
import unittest
from pathlib import Path

from trace_interop.rules import evaluate
from trace_interop.presentation import outcome

ROOT = Path(__file__).resolve().parents[1]


def assess(name, result, method='trace_call', params=None, peers=None):
    return evaluate({'name': name, 'request': {'method': method, 'params': params or [{}, ['trace']]}},
                    {'status': 'result', 'response': {'result': result}}, peers or {})


class RuleSafetyTests(unittest.TestCase):
    def test_malformed_trace_is_a_failure(self):
        for trace in [None, {}, 1, 'bad', [None], [1]]:
            checks = assess('call', {'trace': trace, 'output': '0x'})
            self.assertTrue(any(c['status'] == 'change_needed' for c in checks))

    def test_failed_frame_null_and_non_string_error(self):
        for error in [1, None, {}, []]:
            checks = assess('call', {'trace': [{'error': error, 'result': None}]})
            self.assertIn('change_needed', [c['status'] for c in checks if c['topic'] == 'H09'])
        checks = assess('call', {'trace': [{'error': 'Out of gas', 'result': None}]})
        self.assertEqual([c['status'] for c in checks if c['topic'] == 'H09'], ['matches'])

    def test_revert_bytes_do_not_depend_on_error_wording(self):
        frame = {'traceAddress': [0], 'error': 'client specific label', 'result': None}
        checks = assess('call-siblings-revert-ok', {'trace': [frame]})
        self.assertIn('change_needed', [c['status'] for c in checks if c['topic'] == 'H09'])
        frame['result'] = {'output': '0xdead', 'gasUsed': '0x1'}
        self.assertTrue(all(c['status'] == 'matches' for c in assess('call-siblings-revert-ok', {'trace': [frame]}) if c['topic'] == 'H09'))

    def test_revert_frame_is_only_required_when_trace_is_selected(self):
        for selection in [['stateDiff'], ['vmTrace'], []]:
            checks=assess('replay-revert-stateDiff', {'trace':[], 'output':'0x'},
                          'trace_replayTransaction', ['0x'+'11'*32, selection])
            self.assertFalse(any(c['topic']=='H09' and c['status']=='change_needed' for c in checks))
        checks=assess('replay-revert-trace', {'trace':[], 'output':'0x'},
                      'trace_replayTransaction', ['0x'+'11'*32, ['trace']])
        self.assertIn('change_needed', [c['status'] for c in checks if c['topic']=='H09'])

    def test_nested_error_is_never_a_success(self):
        result = {'jsonrpc': '2.0', 'id': 1, 'error': {'code': -32000, 'message': 'bad'}}
        checks = assess('call-many', result, 'trace_callMany', [[[]]])
        self.assertIn('change_needed', [c['status'] for c in checks if c['topic'] == 'H25'])
        entry = {'record': {'eligible': True, 'status': 'result'}, 'observation': {'response': {'result': result}}}
        self.assertEqual(outcome(entry), 'Error envelope nested inside result')

    def test_missing_transaction_has_one_h06_check(self):
        checks = assess('get-missing-tx', None, 'trace_get', ['0x'+'00'*32, []])
        self.assertEqual(len([c for c in checks if c['topic'] == 'H06']), 1)

    def test_frozen_requests_tolerate_malformed_response_shapes(self):
        # Exercise actual request/context combinations, without assuming clients honor their schemas.
        for path in (ROOT/'fixtures/corpora').glob('*.json'):
            context = json.loads(path.read_text()); context['_chain'] = path.stem
            for case in context['cases']:
                for result in [None, [], [None], 7, 'bad', {'trace': None},
                               {'trace': [{'error': 1, 'result': None}]},
                               {'vmTrace': {'ops': [None, {'ex': 4, 'sub': 7}]}}, {'stateDiff': []}]:
                    with self.subTest(corpus=path.stem, case=case['name'], result=result):
                        evaluate(dict(case, context=context), {'status': 'result', 'response': {'result': result}}, {})

class CoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from trace_interop.validation import request_errors
        cls.methods = {m['name']: m for m in json.loads((ROOT/'spec/trace-openrpc.json').read_text())['methods']}

    def test_validation_cases_use_the_pinned_request_schemas(self):
        from trace_interop.validation import request_errors
        cases = json.loads((ROOT/'fixtures/corpora/a.json').read_text())['cases']
        negative = {'filter-wrong-address-type', 'filter-negative-count', 'get-integer-path',
                    'filter-both-unknown-mode', 'call-null-mode', 'call-scalar-mode'}
        seen = set()
        for case in cases:
            errors = request_errors(case['request'], self.methods)
            if case['name'] in negative:
                seen.add(case['name']); self.assertTrue(errors, case['name'])
                for status, response, expected in [('result', {'result': []}, 'change_needed'),
                                                  ('rpc_error', {'error': {'code': -32602}}, 'matches')]:
                    checks = evaluate(case, {'status': status, 'response': response}, {}, errors)
                    self.assertEqual([c['status'] for c in checks if c['topic'] == 'H14'], [expected])
            if case['name'] in ['call-unknown-field', 'filter-from-null', 'filter-to-null', 'filter-both-null']:
                self.assertFalse(errors, (case['name'], errors))
        self.assertEqual(seen, negative)

    def test_missing_reference_and_unchecked_topic_are_partial(self):
        from trace_interop.inventory import cover_topics
        from trace_interop.presentation import verdict
        checks = assess('get-nested-positive', None, 'trace_get', ['0x'+'00'*32, ['0x6', '0x0']])
        self.assertEqual([c['status'] for c in checks], ['unassessed'])
        checks = cover_topics([{'topic': 'H02', 'status': 'matches'}], ['H02', 'H09'])
        self.assertEqual(verdict(checks), 'Partially assessed')
        self.assertEqual(verdict(cover_topics([], ['H09'])), 'Not assessed')

    def test_filter_addresses_compare_bytes(self):
        address = '0x'+'ab'*20
        frame = {'action': {'from': address, 'to': '0x'+'cd'*20}, 'type': 'call', 'traceAddress': []}
        peers = {'block-tree': {'response': {'result': [frame]}}}
        checks = assess('filter-from', [frame], 'trace_filter', [{'fromAddress': ['0x'+address[2:].upper()]}], peers)
        self.assertEqual([c['status'] for c in checks if c['topic'] == 'H03'], ['matches'])

    def test_zero_fee_many_errors_and_cardinality(self):
        params = [[ [{'gasPrice': '0x0'}, ['trace']] ], 'latest']
        for result in [None, {}, [], {'jsonrpc': '2.0', 'error': {'code': -32603}}]:
            checks = assess('call-many', result, 'trace_callMany', params)
            self.assertEqual([c['status'] for c in checks if c['topic'] in ['H15','H16']], ['change_needed']*2)

    def test_inventory_rejects_empty_and_stale_references(self):
        import tempfile
        from trace_interop.inventory import verify_inventory
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'evidence/run').mkdir(parents=True); (root/'decisions').mkdir()
            (root/'reports.lock.json').write_text(json.dumps({'runs':['evidence/run']}))
            (root/'evidence/run/manifest.json').write_text(json.dumps({'corpus':'precompiles', 'selected_cases':[{'name':'root-success'}]}))
            for references in [[], ['initial/old-case']]:
                (root/'decisions/ledger.json').write_text(json.dumps({'items':[{'id':'H29','cases':references}]}))
                with self.assertRaises(ValueError): verify_inventory(root)
            (root/'decisions/ledger.json').write_text(json.dumps({'items':[{'id':'H29','cases':['precompiles/root-success']}]}))
            self.assertEqual(verify_inventory(root), 1)

class PrecompileValueTests(unittest.TestCase):
    def test_child_value_not_outer_value_controls_inclusion(self):
        corpus = json.loads((ROOT/'fixtures/corpora/precompile-values.json').read_text())
        case = next(c for c in corpus['cases'] if c['name'] == 'nested-call-outer1-value0-success')
        root = {'traceAddress': [], 'subtraces': 0, 'type':'create', 'result': {'address':'0x'+'11'*20}}
        result = {'trace': [root], 'output': '0x'+f'{1:064x}'}
        obs = {'status':'result', 'response': {'result':result}}
        context = dict(corpus, _chain='precompile-values')
        checks = evaluate(dict(case, context=context), obs, {})
        self.assertTrue(all(c['status']=='matches' for c in checks if c['topic']=='H29'))
        root['subtraces']=1; result['trace'].append({'traceAddress':[0]})
        self.assertIn('change_needed', [c['status'] for c in evaluate(dict(case, context=context),obs,{}) if c['topic']=='H29'])

    def test_zero_outer_value_fixture_funds_before_creation(self):
        corpus = json.loads((ROOT/'fixtures/corpora/precompile-values.json').read_text())
        for case in corpus['cases']:
            if 'outer0' not in case['name']:continue
            funding, creation = case['request']['params'][0]
            self.assertEqual(funding[0]['value'],'0x1')
            self.assertEqual(funding[0]['to'], corpus['funded_creation_address'])
            self.assertEqual(creation[0]['value'],'0x0')
            self.assertEqual(int(creation[0]['nonce'],16),int(funding[0]['nonce'],16)+1)
            self.assertEqual(case['precompile_value'],1)

    def test_fixture_setup_uses_independent_state_controls(self):
        from trace_interop.scenarios import verify_state
        controls={'_control/create-nonce':'0x85','_control/target-balance':'0x0',
                  '_control/target-nonce':'0x0','_control/target-code':'0x'}
        observations={n:{'c':{'response':{'result':v}}} for n,v in controls.items()}
        self.assertTrue(verify_state('precompile-values',{'sender_nonce':133},observations,'c')[0])
        observations['_control/create-nonce']['c']['response']['result']='0x86'
        self.assertFalse(verify_state('precompile-values',{'sender_nonce':133},observations,'c')[0])

class PublishedAssessmentTests(unittest.TestCase):
    def test_frozen_counterexamples_are_present_in_reports(self):
        records=json.loads((ROOT/'reports/checks.json').read_text())
        for corpus, case, client, topic in [
            ('a','filter-wrong-address-type','besu_release','H14'),
            ('a','filter-negative-count','nethermind_release','H14'),
            ('a','get-integer-path','reth_release','H14'),
            ('initial','call-many','besu_release','H25'),
            ('initial','call-many','erigon_release','H15'),
            ('a','filter-both-unknown-mode','nethermind_release','H03'),
        ]:
            with self.subTest(case=case, client=client):
                matching=[r for r in records if r['corpus']==corpus and r['case']==case and r['client']==client and r['eligible']]
                self.assertTrue(matching)
                self.assertTrue(all(any(c['topic']==topic and c['status']=='change_needed' for c in r['checks']) for r in matching))

    def test_report_provenance_matches_current_assessment_sources(self):
        import hashlib
        assessment=json.loads((ROOT/'reports/assessment.json').read_text())
        for name,digest in assessment['sources'].items():
            with self.subTest(name=name):
                self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),digest)

    def test_new_value_capture_has_independent_setup_and_success_proof(self):
        records=[r for r in json.loads((ROOT/'reports/checks.json').read_text())
                 if r['corpus']=='precompile-values' and not r['case'].startswith('_control')]
        self.assertEqual(len(records), 72)  # Eight discriminators on nine pinned builds.
        self.assertEqual(len({r['client'] for r in records}), 9)
        for r in records:
            self.assertTrue(r['eligible'])
            success=[c for c in r['checks'] if 'success bit' in c['requirement']]
            self.assertEqual([c['status'] for c in success],['matches'])
            if r['client'].startswith(('reth_','erigon_','nethermind_')) or r['client']=='go-ethereum_trace':
                self.assertTrue(all(c['status']=='matches' for c in r['checks'] if c['topic']=='H29'))
            if r['client'].startswith('besu_') and r['case'].endswith('failed'):
                self.assertIn('change_needed',[c['status'] for c in r['checks'] if c['topic']=='H24'])

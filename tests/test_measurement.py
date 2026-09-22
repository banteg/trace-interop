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

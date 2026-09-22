import copy
import json
import tempfile
import unittest
from pathlib import Path

from trace_interop.cli import parse_exchange, selected_cases, collect, write
from trace_interop.rules import evaluate
from trace_interop.scenarios import verify_state


REQ={'jsonrpc':'2.0','id':1,'method':'trace_call','params':[]}


class CaptureTests(unittest.TestCase):
    def exchange(self, response):
        return parse_exchange('>> '+json.dumps(REQ)+'\n<< '+response, REQ)

    def test_keeps_truncated_json(self):
        raw='{"jsonrpc":"2.0","id":1,"result":'
        obs=self.exchange(raw)
        self.assertEqual(obs['status'],'malformed_json')
        self.assertEqual(obs['raw_response'],raw)

    def test_json_null_is_an_invalid_envelope_not_malformed_json(self):
        self.assertEqual(self.exchange('null')['status'],'invalid_envelope')

    def test_null_result_is_not_missing(self):
        self.assertEqual(self.exchange('{"jsonrpc":"2.0","id":1,"result":null}')['status'],'result')

    def test_wrong_id_or_ambiguous_envelope_is_invalid(self):
        for reply in [{'jsonrpc':'2.0','id':2,'result':None}, {'jsonrpc':'2.0','id':1,'result':None,'error':{'code':-1,'message':'x'}}]:
            self.assertEqual(self.exchange(json.dumps(reply))['status'],'invalid_envelope')

    def test_null_error_and_boolean_numbers_are_invalid(self):
        for reply in [
            {'jsonrpc':'2.0','id':1,'error':None},
            {'jsonrpc':'2.0','id':True,'result':None},
            {'jsonrpc':'2.0','id':1,'error':{'code':False,'message':'x'}},
        ]:
            self.assertEqual(self.exchange(json.dumps(reply))['status'],'invalid_envelope')

    def test_empty_manifest_cannot_make_green_run(self):
        for cases, clients in [([], {'reth_release':{}}), ([{'name':'_control/head','request':REQ}], {})]:
            with tempfile.TemporaryDirectory() as d:
                path=Path(d)
                write(path/'manifest.json',{'selected_cases':cases,'clients':clients})
                with self.assertRaises(ValueError):collect(path)

    def test_error_categories(self):
        for code,expected in [(-32601,'unsupported'),(-32000,'rpc_error')]:
            self.assertEqual(self.exchange(json.dumps({'jsonrpc':'2.0','id':1,'error':{'code':code,'message':'x'}}))['status'],expected)

    def test_empty_selection_fails(self):
        with self.assertRaises(ValueError):selected_cases({'cases':[{'name':'a'}]},'^missing$')

    def test_missing_client_cannot_make_green_run(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d);(path/'hive').mkdir()
            write(path/'manifest.json',{'selected_cases':[{'name':'_control/head','request':REQ}], 'clients':{'reth_release':{}},'head':{'hash':'0x1'}})
            result=collect(path)
            self.assertFalse(result['complete'])
            self.assertEqual(result['missing'],[['_control/head','reth_release']])


class ScenarioTests(unittest.TestCase):
    def test_pruning_requires_independent_state_failure_and_live_control(self):
        def result(value):return {'c':{'status':'result','response':{'result':value}}}
        def error(message):return {'c':{'status':'rpc_error','response':{'error':{'code':-32603,'message':message}}}}
        obs={'old-header':result({'number':'0x2'}),'old-receipt':result({}), 'latest-call':result({'output':'0x'+f'{42:064x}'})}
        for n in ['old-transaction','old-replay','old-block','old-filter','old-nonce']:
            obs[n]=error('insufficient changesets to revert to block #1')
        self.assertTrue(verify_state('pruned',{},obs,'c')[0])
        obs['old-nonce']=result('0x1')
        self.assertFalse(verify_state('pruned',{},obs,'c')[0])

    def test_pruning_eligibility_does_not_depend_on_trace_results(self):
        def response(value): return {'c': {'status': 'result' if 'result' in value else 'rpc_error', 'response': value}}
        controls = {
            'old-header': response({'result': {'number': '0x2'}}),
            'old-receipt': response({'result': {}}),
            'latest-call': response({'result': {'output': '0x'+f'{42:064x}'}}),
            'old-nonce': response({'error': {'code': 4444, 'message': 'History unavailable'}}),
        }
        for trace in [{'result': None}, {'result': []}, {'error': {'code': 4444, 'message': 'gone'}},
                      {'error': {'code': -32603, 'message': 'unexpected'}}]:
            with self.subTest(trace=trace):
                obs = dict(controls)
                for name in ['old-transaction', 'old-replay', 'old-block', 'old-filter']:
                    obs[name] = response(trace)
                self.assertTrue(verify_state('pruned', {}, obs, 'c')[0])
        for nonce in [{'result': '0x0'}, {'error': {'code': -32603, 'message': 'Internal error'}}]:
            self.assertFalse(verify_state('pruned', {}, dict(controls, **{'old-nonce': response(nonce)}), 'c')[0])

    def test_reorg_requires_restored_head_not_just_accepted_switch(self):
        corpus={'heads_a':[{'hash':'A'}],'heads_b':[{'hash':'B'}]}
        obs={phase+'/head':{'c':{'status':'result','response':{'result':{'hash':h}}}} for phase,h in [('before','A'),('after','B'),('restored','B')]}
        self.assertFalse(verify_state('reorg-safe',corpus,obs,'c')[0])
        obs['restored/head']['c']['response']['result']['hash']='A'
        self.assertTrue(verify_state('reorg-safe',corpus,obs,'c')[0])


class ProposalTests(unittest.TestCase):
    def test_raw_block_extension_is_an_observation_for_acceptance_and_rejection(self):
        case = {'name': 'raw-valid', 'request': {'method': 'trace_rawTransaction', 'params': ['0x', ['trace'], 'latest']}}
        for response in [{'result': {}}, {'error': {'code': -32602}}, {'error': {'code': -32000}}]:
            obs = {'status': 'result' if 'result' in response else 'rpc_error', 'response': response}
            checks = evaluate(case, obs, {})
            self.assertEqual({q['topic'] for q in checks}, {'H12', 'H25'})
            self.assertEqual(next(q['status'] for q in checks if q['topic'] == 'H12'), 'observation')
            self.assertFalse(any(q['status'] == 'change_needed' for q in checks))
        malformed = evaluate(case, {'status': 'malformed_json'}, {})
        self.assertEqual(malformed[0]['topic'], 'H25')
        self.assertEqual(malformed[0]['status'], 'change_needed')

    def test_tree_path_rejects_flat_root_selection(self):
        from test_harness_regressions import captured
        case, obs, peers = captured('2026-09-23/geth-40eecf3-initial','get-zero','go-ethereum_trace')
        obs['response']['result'] = peers['transaction-tree']['response']['result'][0]
        self.assertEqual(evaluate(case,obs,peers)[0]['status'], 'change_needed')

    def test_get_path_uses_same_transaction_tree_with_precompile_siblings(self):
        from test_harness_regressions import captured
        case, obs, peers = captured('2026-09-23/geth-40eecf3-a','get-nested-positive','go-ethereum_trace')
        tree = peers['transaction-tree']['response']['result']
        tree[0]['subtraces'] += 1
        for frame in tree:
            if frame['traceAddress'] and frame['traceAddress'][0] == 6:
                frame['traceAddress'][0] = 7
        precompile = copy.deepcopy(tree[1]); precompile['traceAddress'] = [6]
        precompile['action']['to'] = '0x'+'0'*39+'4'; tree.insert(-2,precompile)
        obs['response']['result'] = None
        self.assertEqual(evaluate(case,obs,peers)[0]['status'],'matches')
        obs['response']['result'] = tree[-1]
        self.assertEqual(evaluate(case,obs,peers)[0]['status'],'change_needed')
        case['request']['params'][1] = ['0x7','0x0']
        self.assertEqual(evaluate(case,obs,peers)[0]['status'],'matches')

    def test_unsupported_is_not_empty_success(self):
        checks=evaluate({'name':'replay','request':{'method':'trace_replayTransaction','params':[]}}, {'status':'unsupported','response':{'error':{'code':-32601}}},{})
        self.assertEqual([c['status'] for c in checks],['unsupported'])

    def test_stack_encoding_checked_inside_child(self):
        vm={'ops':[{'ex':{'push':['0x0']},'sub':{'ops':[{'ex':{'push':['0x00']}}]}}]}
        case={'name':'vm','request':{'method':'trace_call','params':[{},['vmTrace']]}}
        checks=evaluate(case,{'status':'result','response':{'result':{'output':'0x','trace':[],'stateDiff':None,'vmTrace':vm}}},{})
        self.assertEqual(next(c for c in checks if c['topic']=='H21')['status'],'change_needed')

    def test_filter_composition_does_not_reuse_other_client_as_oracle(self):
        from test_harness_regressions import captured
        case, obs, peers = captured('2026-09-23/geth-40eecf3-initial','filter-both','go-ethereum_trace')
        self.assertEqual(evaluate(case,obs,peers)[0]['status'],'matches')
        obs['response']['result'] = peers['block-tree']['response']['result']
        self.assertEqual(evaluate(case,obs,peers)[0]['status'],'change_needed')


if __name__=='__main__':unittest.main()

import copy
import json
import tempfile
import unittest
from pathlib import Path

from trace_interop.cli import parse_exchange, selected_cases, collect, write
from trace_interop.rules import evaluate


REQ={'jsonrpc':'2.0','id':1,'method':'trace_call','params':[]}


class CaptureTests(unittest.TestCase):
    def exchange(self, response):
        return parse_exchange('>> '+json.dumps(REQ)+'\n<< '+response, REQ)

    def test_keeps_truncated_json(self):
        raw='{"jsonrpc":"2.0","id":1,"result":'
        obs=self.exchange(raw)
        self.assertEqual(obs['status'],'malformed_json')
        self.assertEqual(obs['raw_response'],raw)

    def test_null_result_is_not_missing(self):
        self.assertEqual(self.exchange('{"jsonrpc":"2.0","id":1,"result":null}')['status'],'result')

    def test_wrong_id_or_ambiguous_envelope_is_invalid(self):
        for reply in [{'jsonrpc':'2.0','id':2,'result':None}, {'jsonrpc':'2.0','id':1,'result':None,'error':{'code':-1,'message':'x'}}]:
            self.assertEqual(self.exchange(json.dumps(reply))['status'],'invalid_envelope')

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


class ProposalTests(unittest.TestCase):
    def test_tree_path_rejects_flat_root_selection(self):
        case={'name':'get-zero','request':{'method':'trace_get','params':['0xhash',['0x0']]}}
        obs={'status':'result','response':{'result':{'traceAddress':[]}}}
        checks=evaluate(case,obs,{})
        self.assertEqual(checks[0]['topic'],'H02')
        self.assertEqual(checks[0]['status'],'change_needed')

    def test_unsupported_is_not_empty_success(self):
        checks=evaluate({'name':'replay','request':{'method':'trace_replayTransaction','params':[]}}, {'status':'unsupported','response':{'error':{'code':-32601}}},{})
        self.assertEqual([c['status'] for c in checks],['unsupported'])

    def test_stack_encoding_checked_inside_child(self):
        vm={'ops':[{'ex':{'push':['0x0']},'sub':{'ops':[{'ex':{'push':['0x00']}}]}}]}
        case={'name':'vm','request':{'method':'trace_call','params':[{},['vmTrace']]}}
        checks=evaluate(case,{'status':'result','response':{'result':{'output':'0x','trace':[],'stateDiff':None,'vmTrace':vm}}},{})
        self.assertEqual(next(c for c in checks if c['topic']=='H21')['status'],'change_needed')

    def test_filter_composition_does_not_reuse_other_client_as_oracle(self):
        def frame(sender,target,path):return {'type':'call','action':{'from':sender,'to':target},'traceAddress':path,'transactionHash':'tx'}
        a,b=frame('A','X',[]),frame('B','Y',[0])
        case={'name':'filter-both','request':{'method':'trace_filter','params':[{'fromAddress':['A'],'toAddress':['Y']}]}}
        peers={'transaction-tree':{'response':{'result':[a,b]}},'block-tree':{'response':{'result':[a,b]}}}
        obs={'status':'result','response':{'result':[a,b]}}
        self.assertEqual(evaluate(case,obs,peers)[0]['status'],'change_needed')
        obs['response']['result']=[]
        self.assertEqual(evaluate(case,obs,peers)[0]['status'],'matches')


if __name__=='__main__':unittest.main()

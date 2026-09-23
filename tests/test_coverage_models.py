"""Independent counterexamples for the additional property models."""
import copy
import unittest
from pathlib import Path

from trace_interop.cli import ROOT, read
from trace_interop.chain_model import load_chain, decode_transaction
from trace_interop.coverage import supplement
from trace_interop.execution_models import assess, balance_delta, created_address
from trace_interop.presentation import verdict
from trace_interop.vm_model import execute, differences, intrinsic, UnsupportedProgram, local_invariants


class VMModelTests(unittest.TestCase):
    def test_return42_hand_calculated_steps(self):
        vm,out,reverted=execute('0x602a60005260206000f3',100)
        self.assertEqual(out,'0x'+f'{42:064x}')
        self.assertFalse(reverted)
        self.assertEqual([o['ex']['used'] for o in vm['ops']],[97,94,88,85,82,82])
        self.assertEqual([o['cost'] for o in vm['ops']],[3,3,6,3,3,0])
        self.assertEqual(vm['ops'][2]['ex']['mem'],{'off':0,'data':out})
        self.assertTrue(all(o['ex']['mem'] is None for i,o in enumerate(vm['ops']) if i!=2))

    def test_memory_reads_expand_without_writing(self):
        vm,_,_=execute('0x60405100',100)
        self.assertEqual(vm['ops'][1]['cost'],12)  # 3 + three words of expansion.
        self.assertEqual(vm['ops'][1]['ex']['push'],['0x0'])
        self.assertIsNone(vm['ops'][1]['ex']['mem'])

    def test_overlap_and_zero_length_copy(self):
        vm,out,_=execute('0x602a6000526020600060015e60406000f3',1000)
        self.assertEqual(bytes.fromhex(out[2:])[31:33],b'\x00\x2a')
        self.assertEqual(vm['ops'][6]['ex']['mem']['off'],1)
        vm,_,_=execute('0x600060ff60ff5e00',100)
        self.assertEqual(vm['ops'][3]['cost'],3)
        self.assertIsNone(vm['ops'][3]['ex']['mem'])

    def test_reject_unsupported_instead_of_using_response_as_oracle(self):
        for code in ['0x600054','0xf1','0xfe']:
            with self.assertRaises(UnsupportedProgram):execute(code,100000)

    def test_mutations_of_all_step_properties_are_detected(self):
        expected,_,_=execute('0x602a60005260206000f3',100)
        for key,value in [('used',94),('push',['0x0']),('mem',{'off':1,'data':'0x2a'}),('store',{'key':'0x0','val':'0x1'})]:
            actual=copy.deepcopy(expected)
            actual['ops'][0]['ex'][key]=value
            self.assertTrue(differences(actual,expected),key)
        actual=copy.deepcopy(expected);actual['ops'].pop()
        self.assertTrue(differences(actual,expected))
        actual=copy.deepcopy(expected);actual['ops'][0]['op']='STOP'
        self.assertTrue(differences(actual,expected))

    def test_prague_intrinsic_is_not_the_calldata_floor(self):
        self.assertEqual(intrinsic('0x0001'),21020)
        self.assertEqual(intrinsic('0x0001',True),53022)

    def test_nested_trace_mutation_is_detected(self):
        vm,_,_=execute('0x600100',100)
        vm['ops'][0]['sub']=copy.deepcopy(vm)
        vm['ops'][0]['sub']['ops'][0]['ex']['push']=['0x2']
        self.assertTrue(local_invariants(vm))


class ChainModelTests(unittest.TestCase):
    def test_complete_replay_inventory_and_recovered_authorization(self):
        blocks=load_chain(ROOT/'fixtures/chains/initial/chain.rlp')
        self.assertEqual(blocks['0x30']['hash'],read(ROOT/'fixtures/chains/initial/headblock.json')['hash'])
        txs=blocks['0x2']['transactions']
        self.assertEqual(len(txs),5)  # The old txinfo index listed only two.
        auth=txs[3]['authorizations'][0]
        info=read(ROOT/'fixtures/corpora/initial.json')['txinfo']['tx-eip7702']
        self.assertEqual(txs[3]['hash'],info['authorizeTx'])
        self.assertEqual(auth['authority'],info['account'])
        self.assertEqual(auth['address'],info['proxyAddr'])

    def test_empty_or_truncated_block_replay_cannot_pass(self):
        blocks=load_chain(ROOT/'fixtures/chains/initial/chain.rlp')
        case={'name':'replay-block-tree','request':{'method':'trace_replayBlockTransactions','params':['0x2',['trace']]},
              'context':{'_blocks':blocks}}
        result=[{'transactionHash':t['hash']} for t in blocks['0x2']['transactions']]
        for corrupted in [[],result[:-1],list(reversed(result))]:
            checks=supplement(case,{'status':'result','response':{'result':corrupted}}, {}, [], ['H07'])
            self.assertIn('change_needed',[c['status'] for c in checks if c['topic']=='H07'])


class DispositionTests(unittest.TestCase):
    def test_control_and_blocked_are_never_agreement(self):
        self.assertEqual(verdict([{'status':'control'}]),'Control / not applicable')
        self.assertEqual(verdict([{'status':'not_applicable'}]),'Control / not applicable')
        self.assertEqual(verdict([{'status':'blocked'}]),'Blocked')
        self.assertEqual(verdict([{'status':'matches'},{'status':'blocked'}]),'Partially assessed')

    def test_broken_wire_blocks_semantics_but_keeps_actual_failure(self):
        case={'name':'raw','request':{'method':'trace_rawTransaction','params':['0x00',['trace']]}}
        checks=supplement(case,{'status':'malformed_json'}, {}, [{'topic':'H25','status':'change_needed'}],['H13'])
        self.assertEqual([(c['topic'],c['status']) for c in checks],[('H25','change_needed'),('H13','blocked')])

    def test_balance_delta_rejects_malformed_numbers(self):
        self.assertIsNone(balance_delta({'*':{'from':'oops','to':'0x1'}}))
        self.assertEqual(balance_delta({'*':{'from':'0x10','to':'0x5'}}),-11)
        self.assertEqual(balance_delta({'+':'0x7'}),7)

    def test_existing_account_cannot_be_reported_as_new(self):
        sender='0x'+'11'*20
        case={'name':'call','request':{'method':'trace_call','params':[{'from':sender,'to':sender},['stateDiff']]},
              'context':{'_alloc':{sender:{}},'_codes':{sender:'0x'}}}
        response={'stateDiff':{sender:{'balance':{'+':'0x1'},'nonce':{'+':'0x0'},'code':{'+':'0x'}}}}
        self.assertIn('change_needed',[c['status'] for c in assess(case,{'status':'result','response':{'result':response}},{},{'H17'})])

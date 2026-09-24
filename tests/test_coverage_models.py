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

    def test_memory_reads_report_the_loaded_range(self):
        vm,_,_=execute('0x60405100',100)
        self.assertEqual(vm['ops'][1]['cost'],12)  # 3 + three words of expansion.
        self.assertEqual(vm['ops'][1]['ex']['push'],['0x0'])
        self.assertEqual(vm['ops'][1]['ex']['mem'],{'off':0x40,'data':'0x'+'00'*32})
        self.assertFalse(local_invariants(vm))
        for mem in [None,{'off':0,'data':'0x'+'00'*32},{'off':0x40,'data':'0x'+'01'*32}]:
            bad=copy.deepcopy(vm);bad['ops'][1]['ex']['mem']=mem
            self.assertTrue(local_invariants(bad),mem)

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
        actual=copy.deepcopy(expected);actual['ops'][0]['ex']['push']=['0x002a']
        self.assertFalse(differences(actual,expected))  # H21 owns quantity encoding.

    def test_prague_intrinsic_is_not_the_calldata_floor(self):
        self.assertEqual(intrinsic('0x0001'),21020)
        self.assertEqual(intrinsic('0x0001',True),53022)

    def test_nested_trace_mutation_is_detected(self):
        vm,_,_=execute('0x600100',100)
        vm['ops'][0]['sub']=copy.deepcopy(vm)
        vm['ops'][0]['sub']['ops'][0]['ex']['push']=['0x2']
        self.assertTrue(local_invariants(vm))
        self.assertTrue(local_invariants({'code':'0x600100','ops':[]}))

    def test_dup_reports_affected_stack_and_no_synthetic_stop(self):
        vm,_,_=execute('0x60018000',100)
        self.assertEqual(vm['ops'][1]['ex']['push'],['0x1','0x1'])
        self.assertFalse(local_invariants(vm))
        vm['code']='0x600180'  # Running off the end is not an operation.
        self.assertTrue(local_invariants(vm))
        vm['ops'].pop()
        self.assertFalse(local_invariants(vm))

    def call_frame(self, child_ops, used, mem=None, retlen=0x20):
        # PUSH1 retlen PUSH1 0 PUSH1 0 PUSH1 0 PUSH1 0 PUSH1 0x44 GAS CALL STOP
        code='0x60'+f'{retlen:02x}'+'6000'*4+'6044'+'5af100'
        ex=lambda used,push,mem=None:{'used':used,'push':push,'mem':mem,'store':None}
        pushes=[hex(retlen),'0x0','0x0','0x0','0x0','0x44']
        ops=[{'pc':2*i,'cost':3,'ex':ex(10000-3*(i+1),[v]),'sub':None} for i,v in enumerate(pushes)]
        ops.append({'pc':12,'cost':2,'ex':ex(9980,['0x26fc']),'sub':None})
        child={'code':'0x60006000','ops':child_ops}
        ops.append({'pc':13,'cost':2600+900,'ex':ex(used,['0x1'],mem),'sub':child})
        return {'code':code,'ops':ops}

    def test_call_gas_returns_child_leftover_and_mem_is_the_output_window(self):
        window={'off':0,'data':'0x'+'00'*32}
        child=[{'pc':0,'cost':3,'ex':{'used':897,'push':['0x0'],'mem':None,'store':None},'sub':None},
               {'pc':2,'cost':3,'ex':{'used':894,'push':['0x0'],'mem':None,'store':None},'sub':None}]
        # The child falls off its code end normally and returns 894 unused gas.
        self.assertFalse(local_invariants(self.call_frame(child,9980-3500+894,window)))
        self.assertTrue(local_invariants(self.call_frame(child,9980-3500,window)))
        for mem in [None,{'off':0,'data':'0x'}]:
            self.assertTrue(local_invariants(self.call_frame(child,9980-3500+894,mem)))
        self.assertFalse(local_invariants(self.call_frame(child,9980-3500+894,None,retlen=0)))
        # A halted child returns nothing.
        halted=copy.deepcopy(child);halted[-1]['ex']=None
        self.assertFalse(local_invariants(self.call_frame(halted,9980-3500,window)))

    def test_subtraces_only_on_calls_and_creations(self):
        vm,_,_=execute('0x600100',100)
        vm['ops'][0]['sub']={'code':'0x','ops':[]}
        self.assertIn('operation 0 has a subtrace but entered no child frame',local_invariants(vm))

    def test_difficulty_mnemonic_alias_is_not_a_semantic_mismatch(self):
        vm,_,_=execute('0x4400',100,environment={'PREVRANDAO':0})
        vm['ops'][0]['op']='DIFFICULTY'
        self.assertFalse(local_invariants(vm))


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

    def test_authorization_replay_cannot_omit_or_change_delegation(self):
        blocks=load_chain(ROOT/'fixtures/chains/initial/chain.rlp')
        tx=blocks['0x2']['transactions'][3]
        authority=tx['authorizations'][0]['authority']
        target=tx['authorizations'][0]['address']
        corpus=read(ROOT/'fixtures/chains/initial/genesis.json')
        context={'_blocks':blocks,'_alloc':{'0x'+a:v for a,v in corpus['alloc'].items()},
                 '_codes':{'0x'+a:v.get('code','0x') for a,v in corpus['alloc'].items()},
                 '_chain_id':corpus['config']['chainId']}
        case={'name':'replay','context':context,'request':{'method':'trace_replayTransaction','params':[tx['hash'],['stateDiff']]}}
        nonce={'*':{'from':'0x0','to':'0x1'}}
        for change,expected in [({'*':{'from':'0x','to':'0xef0100'+target[2:]}},'matches'),('=','change_needed'),(None,'change_needed')]:
            result={'stateDiff':{authority:{'code':change,'nonce':nonce}}}
            checks=assess(case,{'status':'result','response':{'result':result}},{},{'H18'})
            self.assertEqual([c['status'] for c in checks],[expected])

    def test_authorizations_fold_per_authority_and_skip_invalid_tuples(self):
        blocks=load_chain(ROOT/'fixtures/chains/initial/chain.rlp')
        genesis=read(ROOT/'fixtures/chains/initial/genesis.json')
        original=blocks['0x2']['transactions'][3]
        auth=original['authorizations'][0]
        absent='0x'+'ab'*20
        def replay(authorizations, diff):
            tx=dict(original,authorizations=authorizations)
            chain=dict(blocks,**{'0x2':dict(blocks['0x2'],transactions=blocks['0x2']['transactions'][:3]+[tx])})
            context={'_blocks':chain,'_alloc':{'0x'+a:v for a,v in genesis['alloc'].items()},
                     '_codes':{'0x'+a:v.get('code','0x') for a,v in genesis['alloc'].items()},
                     '_chain_id':genesis['config']['chainId']}
            case={'name':'replay','context':context,'request':{'method':'trace_replayTransaction','params':[tx['hash'],['stateDiff']]}}
            return [c['status'] for c in assess(case,{'status':'result','response':{'result':{'stateDiff':diff}}},{},{'H18'})]
        second=dict(auth,address='0x'+'00'*19+'05',nonce=1)
        delegated=lambda a:'0xef0100'+a[2:]
        # Two tuples from one authority: the net diff ends at the second target, nonce +2.
        net={auth['authority']:{'code':{'*':{'from':'0x','to':delegated(second['address'])}},'nonce':{'*':{'from':'0x0','to':'0x2'}}}}
        self.assertEqual(replay([auth,second],net),['matches'])
        # A stale nonce or foreign chain id skips the tuple; the authority is unchanged.
        for invalid in [dict(auth,nonce=1),dict(auth,chain_id=1)]:
            self.assertEqual(replay([invalid],{}),['matches'])
            self.assertEqual(replay([invalid],{auth['authority']:{'code':{'*':{'from':'0x','to':delegated(auth['address'])}}}}),['change_needed'])
        # An absent authority is born with creation markers.
        born=dict(auth,authority=absent)
        self.assertEqual(replay([born],{absent:{'code':{'+':delegated(auth['address'])},'nonce':{'+':'0x1'}}}),['matches'])
        self.assertEqual(replay([born],{absent:{'code':{'*':{'from':'0x','to':delegated(auth['address'])}},'nonce':{'*':{'from':'0x0','to':'0x1'}}}}),['change_needed'])

    def test_known_empty_execution_requires_empty_vm_object(self):
        blocks=load_chain(ROOT/'fixtures/chains/initial/chain.rlp')
        tx=blocks['0x2']['transactions'][3]
        case={'name':'replay','context':{'_blocks':blocks},
              'request':{'method':'trace_replayTransaction','params':[tx['hash'],['vmTrace']]}}
        for vm,expected in [({'code':'0x','ops':[]},'matches'),(None,'change_needed')]:
            checks=assess(case,{'status':'result','response':{'result':{'vmTrace':vm}}},{},{'H19','H20'})
            self.assertEqual([c['status'] for c in checks],[expected])

    def test_empty_or_truncated_block_replay_cannot_pass(self):
        blocks=load_chain(ROOT/'fixtures/chains/initial/chain.rlp')
        case={'name':'replay-block-tree','request':{'method':'trace_replayBlockTransactions','params':['0x2',['trace']]},
              'context':{'_blocks':blocks}}
        result=[{'transactionHash':t['hash']} for t in blocks['0x2']['transactions']]
        for corrupted in [[],result[:-1],list(reversed(result))]:
            checks=supplement(case,{'status':'result','response':{'result':corrupted}}, {}, [], ['H07'])
            self.assertIn('change_needed',[c['status'] for c in checks if c['topic']=='H07'])

    def test_missing_transaction_is_not_an_empty_inventory_failure(self):
        blocks=load_chain(ROOT/'fixtures/chains/initial/chain.rlp')
        case={'name':'transaction-missing','context':{'_blocks':blocks},
              'request':{'method':'trace_transaction','params':['0x'+'00'*32]}}
        checks=supplement(case,{'status':'result','response':{'result':None}},{},[{'topic':'H06','status':'matches'}],['H06'])
        self.assertEqual([c['status'] for c in checks],['matches'])

    def test_empty_reference_needs_decoded_empty_pos_block(self):
        from trace_interop.oracles import anchored_reference
        context={'cases':[{'name':'block','request':{'method':'trace_block','params':['0x2']}}],
                 '_blocks':{'0x2':{'transactions':[],'difficulty':0}}}
        peers={'block':{'status':'result','response':{'result':[]}}}
        self.assertEqual(anchored_reference(context,peers,'block'),[])
        context['_blocks']['0x2']['transactions']=[{'hash':'required'}]
        self.assertIsNone(anchored_reference(context,peers,'block'))


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

    def test_earlier_bundle_items_create_accounts(self):
        sender='0x'+'11'*20
        created=created_address(sender,0)
        calls=[[{'from':sender,'data':'0x60016000f3'},['stateDiff']],[{'from':sender,'to':created},['stateDiff']]]
        case={'name':'call-many','context':{},'request':{'method':'trace_callMany','params':[calls,'latest']}}
        # The unfunded default sender and the created contract exist after the first item.
        second={sender:{'balance':'=','nonce':{'*':{'from':'0x1','to':'0x2'}},'code':'=','storage':{}}}
        first={sender:{'balance':{'+':'0x0'},'nonce':{'+':'0x1'},'code':{'+':'0x'},'storage':{}},
               created:{'balance':{'+':'0x0'},'nonce':{'+':'0x1'},'code':{'+':'0x00'},'storage':{}}}
        checks=assess(case,{'status':'result','response':{'result':[{'stateDiff':first},{'stateDiff':second}]}},{},{'H17'})
        self.assertEqual([c['status'] for c in checks],['matches','matches'])
        second[created]={'balance':{'+':'0x0'},'nonce':{'+':'0x1'},'code':{'+':'0x00'},'storage':{}}
        checks=assess(case,{'status':'result','response':{'result':[{'stateDiff':first},{'stateDiff':second}]}},{},{'H17'})
        self.assertEqual([c['status'] for c in checks],['matches','change_needed'])

    def test_trace_only_many_does_not_require_state_diff(self):
        call={'from':'0x'+'11'*20,'to':'0x'+'22'*20}
        case={'name':'call-many','context':{},'request':{'method':'trace_callMany','params':[[[call,['trace']]],'latest']}}
        self.assertEqual(assess(case,{'status':'result','response':{'result':[{'trace':[],'stateDiff':None}]}},{},{'H16'}),[])

    def test_missing_state_assertions_have_stable_topic_order(self):
        case={'name':'call','context':{},'request':{'method':'trace_call','params':[{},['stateDiff']]}}
        checks=assess(case,{'status':'result','response':{'result':{}}},{},{'H17','H16'})
        self.assertEqual([c['topic'] for c in checks],['H16','H17'])


class TransferModelTests(unittest.TestCase):
    def fixture(self):
        sender,target,miner=['0x'+byte*20 for byte in ['11','22','33']]
        model={'sender':sender,'target':target,'miner':miner,'balance':1_000_000,'nonce':7,'value':7,'price':2,'miner_absent':True}
        case={'name':'model-transfer','transfer_model':model,'context':{'_environment':{'BASEFEE':1}},
              'request':{'method':'trace_call','params':[{'from':sender,'to':target},['trace','stateDiff']]}}
        result={'output':'0x','trace':[],'stateDiff':{
            sender:{'balance':{'*':{'from':hex(1_000_000),'to':hex(957_993)}},'nonce':{'*':{'from':'0x7','to':'0x8'}},'code':'=','storage':{}},
            target:{'balance':{'+':'0x7'},'nonce':{'+':'0x0'},'code':{'+':'0x'},'storage':{}},
            miner:{'balance':{'+':hex(21000)},'nonce':{'+':'0x0'},'code':{'+':'0x'},'storage':{}}}}
        peers={'_control/miner-balance':{'status':'result','response':{'result':'0x0'}}}
        return case,result,peers

    def test_fee_nonce_and_existence_mutations(self):
        case,result,peers=self.fixture()
        def checks(value):return supplement(case,{'status':'result','response':{'result':value}},peers,[],[])
        self.assertTrue(all(c['status']=='matches' for c in checks(result)))
        model=case['transfer_model']
        for who,field in [('sender','balance'),('sender','nonce'),('target','balance'),('miner','balance'),('target','code'),('target','nonce')]:
            value=copy.deepcopy(result);value['stateDiff'][model[who]][field]='='
            self.assertIn('change_needed',[c['status'] for c in checks(value)],(who,field))

    def test_invalid_control_cannot_establish_accounting(self):
        case,result,peers=self.fixture()
        peers['_control/miner-balance']['status']='invalid_envelope'
        checks=supplement(case,{'status':'result','response':{'result':result}},peers,[],[])
        self.assertEqual([c['status'] for c in checks if c['topic']=='H16'],['blocked'])


class AccountingTests(unittest.TestCase):
    def replay(self, corpus, name, client):
        from trace_interop.cli import CHAINS
        folder = ROOT/'evidence/2026-09-24/h15-call-compat'/corpus
        manifest, observations = read(folder/'manifest.json'), read(folder/'observations.json')
        chain = ROOT/'fixtures/chains'/CHAINS[corpus]
        genesis = read(chain/'genesis.json')
        context = dict(read(ROOT/f'fixtures/corpora/{corpus}.json'), cases=manifest['selected_cases'],
                       _blocks=load_chain(chain/'chain.rlp'), _chain_id=genesis['config']['chainId'],
                       _alloc={'0x'+a.removeprefix('0x').lower(): v for a,v in genesis['alloc'].items()},
                       _codes={'0x'+a.removeprefix('0x').lower(): v.get('code','0x') for a,v in genesis['alloc'].items()})
        case = dict(next(c for c in manifest['selected_cases'] if c['name'] == name), context=context)
        peers = {n: clients.get(client, {}) for n, clients in observations.items()}
        return case, peers[name], peers

    def test_blob_fee_is_debited_and_burned(self):
        # Block 56 tx 0 carries one blob; every build debits 131072 wei of blob fee.
        case, observation, peers = self.replay('forks', 'replay-56', 'reth_release')
        statuses = [c['status'] for c in assess(case, observation, peers, {'H16'})]
        self.assertTrue(statuses and all(s == 'matches' for s in statuses), statuses)
        blob = observation['response']['result'][0]['stateDiff']
        sender = next(a for a in blob.values() if isinstance(a.get('nonce'), dict))
        pair = sender['balance']['*']
        pair['to'] = hex(int(pair['to'], 16)+131072)
        self.assertEqual(assess(case, observation, peers, {'H16'})[0]['status'], 'change_needed')

    def test_root_gas_fallback_allows_the_refund_bound(self):
        from trace_interop.execution_models import settled_gas
        # 100 spent gas may settle at 80..100 when a refund is possible, never below.
        self.assertEqual(settled_gas([-90*3, 90*1], 90, 80, 100, 1, 2, 0), 90)
        self.assertIsNone(settled_gas([-79*3, 79*1], 79, 80, 100, 1, 2, 0))
        self.assertIsNone(settled_gas([-90*3, 90*1], 90, 100, 100, 1, 2, 0))

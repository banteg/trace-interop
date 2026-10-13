"""Counterexamples from the 2026-10-14 harness audit of the VM and chain models."""
import copy
import unittest

from trace_interop.chain_model import resolve_block
from trace_interop.vm_model import execute, differences, local_invariants, OutOfGas, UnsupportedProgram


class LocalInvariantTests(unittest.TestCase):
    def test_step_effects_must_be_an_object_or_null(self):
        vm,_,_=execute('0x600100',100)
        for ex in ['bad',[],123,True]:
            bad=copy.deepcopy(vm);bad['ops'][1]['ex']=ex
            self.assertTrue(local_invariants(bad),ex)

    def test_halted_step_cost_is_a_nonnegative_integer(self):
        vm,_,_=execute('0x600100',100)
        vm['ops'][1]['ex']=None
        self.assertFalse(local_invariants(vm))
        for cost in [-999,None,'0x0',False,1.5]:
            bad=copy.deepcopy(vm);bad['ops'][1]['cost']=cost
            self.assertTrue(local_invariants(bad),cost)

    def test_only_a_completed_sstore_reports_its_operands_as_store(self):
        vm,_,_=execute('0x600160025500',30000,environment={'FRESH_ACCOUNT':True})
        self.assertEqual(vm['ops'][2]['ex']['store'],{'key':'0x2','val':'0x1'})
        self.assertFalse(local_invariants(vm))
        for store in [None,{'key':'0x1','val':'0x2'},{'key':'0x2','val':'0x0'},{'key':'0x2'},'0x2']:
            bad=copy.deepcopy(vm);bad['ops'][2]['ex']['store']=store
            self.assertTrue(local_invariants(bad),store)
        halted=copy.deepcopy(vm);halted['ops'][2]['ex']=None
        self.assertFalse(local_invariants(halted))  # A halted SSTORE reports no effects.
        for code,i in [('0x6001600255600254',4),('0x600160025d00',2),('0x600160025d60025c00',4),('0x600100',0)]:
            vm,_,_=execute(code,30000,environment={'FRESH_ACCOUNT':True})
            self.assertFalse(local_invariants(vm),code)
            bad=copy.deepcopy(vm);bad['ops'][i]['ex']['store']={'key':'0x2','val':'0x1'}
            self.assertTrue(local_invariants(bad),code)

    def test_store_without_known_operands_must_still_be_reported(self):
        vm,_,_=execute('0x600160025500',30000,environment={'FRESH_ACCOUNT':True})
        vm['ops'][0]['ex']['push']=['bad']  # The stack cannot be followed past this step.
        vm['ops'][2]['ex']['store']=None
        self.assertIn('operation 2 SSTORE store is not its key and value operands',local_invariants(vm))


class BooleanOffsetTests(unittest.TestCase):
    def test_boolean_memory_offset_is_not_zero(self):
        expected,_,_=execute('0x602a60005260206000f3',100)
        actual=copy.deepcopy(expected)
        actual['ops'][2]['ex']['mem']['off']=False
        self.assertTrue(differences(actual,expected))
        vm,_,_=execute('0x60005100',100)
        vm['ops'][1]['ex']['mem']['off']=False
        self.assertTrue(local_invariants(vm))

    def test_boolean_pc_and_gas_are_not_integers(self):
        expected,_,_=execute('0x600100',100)
        for i,key,value in [(0,'pc',False),(1,'cost',False),(0,'cost',3.0)]:
            actual=copy.deepcopy(expected);actual['ops'][i][key]=value
            self.assertTrue(differences(actual,expected),(key,value))


class ExecutionTests(unittest.TestCase):
    def test_out_of_range_data_reads_are_zero(self):
        big='7f'+'ff'*32
        vm,_,_=execute('0x'+big+'3500',100,'0x'+'11'*40)
        self.assertEqual(vm['ops'][1]['ex']['push'],['0x0'])
        for op in ['37','39']:
            vm,_,_=execute('0x6020'+big+'6000'+op+'00',100,'0x'+'11'*40)
            self.assertEqual(vm['ops'][3]['ex']['mem'],{'off':0,'data':'0x'+'00'*32})

    def test_unaffordable_storage_access_halts_before_reading_the_slot(self):
        with self.assertRaises(OutOfGas):execute('0x600054',2102)
        with self.assertRaises(OutOfGas):execute('0x6001600055',2306)  # Sentry: 2300 left at SSTORE.
        with self.assertRaisesRegex(UnsupportedProgram,'unanchored'):execute('0x600054',2103)
        with self.assertRaisesRegex(UnsupportedProgram,'unanchored'):execute('0x6001600055',2307)
        with self.assertRaisesRegex(UnsupportedProgram,'invalid model program'):execute('0x600055',3)  # Underflow first.


class BlockSelectorTests(unittest.TestCase):
    def test_selectors_outside_the_draft_are_not_anchored(self):
        context={'_blocks':{'0x1a':{'number':26,'hash':'0x'+'ab'*32}},'_head':{'number':'0x1a'}}
        self.assertIs(resolve_block(context,'0x1a'),context['_blocks']['0x1a'])
        self.assertIs(resolve_block(context,'0x'+'AB'*32),context['_blocks']['0x1a'])
        for selector in ['0x1A',{'blockNumber':'0x1a'},{'blockHash':'0x'+'ab'*32}]:
            self.assertIsNone(resolve_block(context,selector),selector)


if __name__ == '__main__':
    unittest.main()

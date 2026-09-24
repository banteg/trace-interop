"""H15 oracle counterexamples; fixtures never learn expected fees from clients."""
import copy
import unittest

from trace_interop.cli import ROOT, read
from trace_interop.coverage import supplement
from trace_interop.fee_policy import assess, expected_steps, gas_used, SENDER, MINER, BALANCE, GAS
from trace_interop.rules import evaluate
from scripts.build_fee_policy_fixtures import build


class FeePolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.corpus = build()
        cls.cases = {c['name']:c for c in cls.corpus['cases']}
        header = read(ROOT/'fixtures/chains/raw-validation/headblock.json')
        cls.environment = {k:int(header[v],16) for k,v in [('BASEFEE','baseFeePerGas'),('NUMBER','number'),('TIMESTAMP','timestamp'),('GASLIMIT','gasLimit')]}

    def case(self, name):
        return dict(copy.deepcopy(self.cases[name]), context={'_environment':self.environment})

    def response(self, result):
        return dict(status='result', response=dict(jsonrpc='2.0', id=1, result=result))

    def test_generated_corpus_is_current_and_covers_every_selection(self):
        self.assertEqual(self.corpus, read(ROOT/'fixtures/corpora/fee-policy.json'))
        families = {}
        for case in self.corpus['cases']:
            if 'fee_policy' not in case:
                continue
            family = case['name'].rsplit('/',1)[0]
            families.setdefault(family, set()).add(case['name'].rsplit('/',1)[1])
        self.assertTrue(families)
        self.assertTrue(all(len(modes)==8 for modes in families.values()))

    def test_hand_calculated_gas_constants(self):
        # initcode intrinsic + execution + code deposit, no trace-gas witness.
        self.assertEqual(gas_used('environment'), 53540+283+44800)
        self.assertEqual(gas_used('revert'), 53138+18)
        self.assertEqual(gas_used('refund'), (53182+22218)*4//5)
        self.assertEqual(gas_used('out-of-gas'), GAS)

    def test_admission_labels_have_exact_independent_fee_and_funding_boundaries(self):
        used = {'environment':98623, 'refund':60320, 'revert':53156, 'out-of-gas':200000, 'transfer':21000}
        for original in self.corpus['cases']:
            policy = original.get('fee_policy', {})
            if policy.get('admission') not in ['accept','reject']:
                continue
            params = original['request']['params']
            calls = [p[0] for p in params[0]] if original['request']['method']=='trace_callMany' else [params[0]]
            balances = {SENDER:BALANCE}
            invalid = False
            for call, program in zip(calls, policy['programs'], strict=True):
                cap = int(call.get('gasPrice',call.get('maxFeePerGas')),16)
                tip = int(call.get('gasPrice',call.get('maxPriorityFeePerGas')),16)
                value, gas = int(call['value'],16), int(call['gas'],16)
                balance = balances.get(call['from'],0)
                if tip>cap or 0<cap<765625000 or balance<value+gas*cap:
                    invalid = True
                    break
                spent = used[program]*min(cap,765625000+tip)
                balances[call['from']] = balance-spent-(0 if program in ['revert','out-of-gas'] else value)
            self.assertEqual(invalid,policy['admission']=='reject',original['name'])

    def test_upfront_and_final_accounting_have_different_gas_basis(self):
        case = self.case('typed-tip-limited/call/stateDiff')
        step = expected_steps(case)[0]
        price = 765625001
        output = '0x'+''.join(f'{word:064x}' for word in [price,765625000,2,20,100000000,BALANCE-200000*price-7,0])
        self.assertEqual(step['output'], output)
        sender_after = BALANCE-98623*price-7
        diff = {
            SENDER: {'balance':{'*':{'from':hex(BALANCE),'to':hex(sender_after)}}, 'nonce':{'*':{'from':'0xa','to':'0xb'}}},
            MINER: {'balance':{'+':hex(98623)}},
            step['recipient']: {'balance':{'+':'0x7'}},
        }
        result = dict(output=output, stateDiff=diff)
        self.assertTrue(all(c['status']=='matches' for c in assess(case,self.response(result))))
        for address, field, replacement in [(SENDER,'balance','='),(SENDER,'nonce','='),(MINER,'balance','='),
                                             (step['recipient'],'balance',{'+' : '0x8'})]:
            bad = copy.deepcopy(result)
            bad['stateDiff'][address][field] = replacement
            self.assertIn('change_needed', [c['status'] for c in assess(case,self.response(bad))])

    def test_opcode_witness_catches_environment_and_accounting_without_state_diff(self):
        case = self.case('mixed-typed-free-priced-free/many/none')
        steps = expected_steps(case)
        good = [{'output':s['output']} for s in steps]
        self.assertTrue(all(c['status']=='matches' for c in assess(case,self.response(good))))
        for index, word in [(0,1),(1,0),(1,5),(2,5),(2,6),(0,2),(0,3),(0,4)]:
            bad = copy.deepcopy(good)
            data = bytearray.fromhex(bad[index]['output'][2:])
            data[word*32+31] ^= 1
            bad[index]['output'] = '0x'+data.hex()
            self.assertIn('change_needed', [c['status'] for c in assess(case,self.response(bad))])
        self.assertIn('change_needed', [c['status'] for c in assess(case,self.response(good[:-1]))])

    def test_typed_price_is_minimum_and_zero_tip_still_pays_base_fee(self):
        for name, price in [('typed-zero',0),('typed-zero-tip',765625000),('typed-tip-limited',765625001),('typed-cap-limited',765625001)]:
            step = expected_steps(self.case(name+'/call/none'))[0]
            self.assertEqual(int(step['output'][2:66],16),price)
            self.assertEqual(step['before']-step['after'],98623*price+7)

    def test_free_funding_rejection_does_not_get_generic_acceptance_rule(self):
        case = self.case('funding-free-short/call/none')
        observation = dict(status='rpc_error',response={'error':{'code':-32000,'message':'insufficient funds'}})
        checks = supplement(case, observation, {}, evaluate(case,observation,{}), ['H15'])
        self.assertEqual([c['status'] for c in checks if c['topic']=='H15'], ['matches'])
        for code in [-32603,-32601,-32700]:
            observation['response']['error']['code']=code
            self.assertEqual(assess(case,observation)[0]['status'],'blocked')
        self.assertEqual(assess(case,self.response({'output':'0x'}))[0]['status'],'change_needed')

    def test_crashes_and_rejection_for_wrong_reason_never_prove_validation(self):
        case = self.case('funding-free-short/call/none')
        for message, expected in [('method handler crashed','blocked'),('backend unavailable','blocked'),
                                  ('fee cap less than block base fee','change_needed')]:
            obs=dict(status='rpc_error',response={'error':{'code':-32000,'message':message}})
            self.assertEqual(assess(case,obs)[0]['status'],expected)
        case = self.case('mixed-legacy-free-then-invalid/many/trace')
        for index, expected in [(0,'change_needed'),(1,'matches')]:
            obs=dict(status='rpc_error',response={'error':{'code':-32000,'message':f'first run for txIndex {index} error: fee cap less than block base fee'}})
            self.assertEqual(assess(case,obs)[0]['status'],expected)

    def test_unresolved_defaults_do_not_receive_policy_passes(self):
        case=self.case('defaults-omitted/call/none')
        self.assertEqual(assess(case,self.response({'output':'0x'}))[0]['status'],'unassessed')

    def test_rejected_batches_are_not_misclassified_as_missing_execution_envelopes(self):
        obs=dict(status='rpc_error',response={'error':{'code':-32003,'message':'max fee per gas less than block base fee'}})
        for name in ['typed-below-base/many/trace','defaults-tip-only-positive/many/none']:
            checks=evaluate(self.case(name),obs,{})
            self.assertFalse(any(c['topic']=='H16' for c in checks))

    def test_refund_revert_and_oog_settlement_reaches_next_call(self):
        for program, used, sent in [('refund',60320,7),('revert',53156,0),('out-of-gas',200000,0)]:
            steps=expected_steps(self.case('legacy-'+program+'-then-observe/many/none'))
            self.assertEqual(steps[1]['before'],BALANCE-used*765625001-sent)
            self.assertEqual(steps[1]['miner_before'],used)
            self.assertEqual(steps[1]['nonce'],11)
        self.assertEqual(expected_steps(self.case('empty-sender-free/call/none'))[0]['before'],0)


if __name__ == '__main__':
    unittest.main()

"""Independent policy checks and method compatibility must remain distinct."""
import copy
import unittest

from scripts.build_fee_compat_fixtures import build
from trace_interop.cli import ROOT, read
from trace_interop.fee_policy import assess, assess_compatibility, expected_steps, BALANCE, GAS


class FeeCompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.corpus = build()
        self.cases = {c['name']: c for c in self.corpus['cases']}
        self.env = dict(BASEFEE=765625000, NUMBER=2, TIMESTAMP=20, GASLIMIT=100000000)

    def case(self, name):
        return dict(copy.deepcopy(self.cases[name]), context={'_environment':self.env})

    def observation(self, output, eth=False):
        return dict(status='result', response={'result':output if eth else {'output':output}})

    def test_frozen_pairs_have_identical_arguments_and_all_selections(self):
        self.assertEqual(self.corpus, read(ROOT/'fixtures/corpora/fee-compat.json'))
        families = {}
        for case in self.corpus['cases']:
            if 'fee_reference' not in case:
                continue
            reference = self.cases[case['fee_reference']]
            call, modes, block = case['request']['params']
            self.assertEqual(reference['request']['method'], 'eth_call')
            self.assertEqual(reference['request']['params'], [call, block])
            families.setdefault(case['fee_reference'], set()).add(tuple(modes))
        self.assertEqual(len(families), 32)
        self.assertTrue(all(len(selections)==8 for selections in families.values()))

    def test_zero_fee_environment_and_priced_upfront_balance_are_independent(self):
        for family in ['legacy-zero', 'typed-zero']:
            words = expected_steps(self.case(family+'/trace/none'))[0]['output'][2:]
            self.assertEqual([int(words[i:i+64],16) for i in range(0,len(words),64)],
                             [0,0,2,20,100000000,BALANCE-7,0])
        words = expected_steps(self.case('legacy-above-base/trace/none'))[0]['output'][2:]
        self.assertEqual([int(words[i:i+64],16) for i in range(0,len(words),64)],
                         [765625001,765625000,2,20,100000000,BALANCE-GAS*765625001-7,0])

    def test_agreement_cannot_mask_a_shared_wrong_environment(self):
        case = self.case('legacy-zero/trace/none')
        output = expected_steps(case)[0]['output']
        wrong = output[:66]+f'{765625000:064x}'+output[130:]
        trace = self.observation(wrong)
        peers = {case['fee_reference']:self.observation(wrong,eth=True)}
        self.assertEqual(assess_compatibility(case,trace,peers)[0]['status'],'matches')
        self.assertIn('change_needed',[c['status'] for c in assess(case,trace)])
        peers[case['fee_reference']] = self.observation(output,eth=True)
        self.assertEqual(assess_compatibility(case,trace,peers)[0]['status'],'change_needed')

    def test_pair_checks_balance_words_even_without_state_diff(self):
        case = self.case('legacy-above-base/trace/none')
        output = expected_steps(case)[0]['output']
        peers = {case['fee_reference']:self.observation(output,eth=True)}
        self.assertEqual(assess_compatibility(case,self.observation(output),peers)[0]['status'],'matches')
        wrong = output[:2+5*64]+f'{BALANCE-7:064x}'+output[2+6*64:]
        self.assertEqual(assess_compatibility(case,self.observation(wrong),peers)[0]['status'],'change_needed')

    def test_only_identifiable_rejections_establish_consistency(self):
        case = self.case('legacy-below-base/trace/none')
        error = lambda message, code=-32000: dict(status='rpc_error', response={'error':{'code':code,'message':message}})
        peers = {case['fee_reference']:error('fee cap less than block base fee')}
        for obs, expected in [(error('max fee per gas less than basefee'),'matches'),
                              (error('insufficient funds'),'change_needed'),
                              (self.observation('0x'),'change_needed'),
                              (error('internal error',-32603),'blocked'),
                              ({'status':'malformed_json'},'blocked')]:
            self.assertEqual(assess_compatibility(case,obs,peers)[0]['status'],expected)
        self.assertEqual(assess_compatibility(case,error('base fee'),{})[0]['status'],'blocked')

    def test_default_families_compare_with_eth_call(self):
        for family in ['defaults-omitted', 'defaults-tip-only-positive']:
            case = self.case(family+'/trace/none')
            peers = {case['fee_reference']:self.observation('0x01',eth=True)}
            self.assertEqual(assess_compatibility(case,self.observation('0x02'),peers)[0]['status'],'change_needed')
            self.assertEqual(assess_compatibility(case,self.observation('0x01'),peers)[0]['status'],'matches')

    def test_eth_reference_codes_do_not_impose_trace_error_codes(self):
        case = self.case('legacy-below-base/trace/none')
        def error(code, message):
            return dict(status='rpc_error', response={'error':dict(code=code,message=message)})
        for code, message, trace_message in [(-32009, 'Gas price below current base fee', 'fee cap less than base fee'),
                                             (-32004, 'Upfront cost exceeds account balance', 'insufficient funds'),
                                             (-32004, 'Upfront gas cost exceeds account balance', 'insufficient funds')]:
            peers = {case['fee_reference']:error(code,message)}
            self.assertEqual(assess_compatibility(case,error(-32000,trace_message),peers)[0]['status'],'matches')

    def test_report_retains_blocked_pair_check_for_malformed_response(self):
        from trace_interop.coverage import supplement
        case = self.case('legacy-below-base/trace/none')
        checks = supplement(case, {'status':'malformed_json'}, {}, [], ['H15'])
        paired = [c for c in checks if 'identical eth_call' in c['requirement']]
        self.assertEqual(len(paired), 1)
        self.assertEqual(paired[0]['status'], 'blocked')

    def test_mixed_calls_reset_fee_environment_per_item(self):
        from scripts.build_fee_policy_fixtures import build as fee_cases
        case = next(c for c in fee_cases()['cases'] if c['name']=='mixed-legacy-free-priced-free/many/none')
        steps = expected_steps(dict(case,context={'_environment':self.env}))
        self.assertEqual([int(s['output'][66:130],16) for s in steps],[0,765625000,0])
        self.assertEqual(steps[2]['before'],BALANCE-14-98623*765625001)

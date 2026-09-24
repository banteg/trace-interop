"""Counterexamples for the mined-probes chain and its independently derived oracles."""
import copy
import importlib.util
import unittest

import rlp

from trace_interop.chain_model import load_chain
from trace_interop.cli import CHAINS, ROOT, read
from trace_interop.coverage import supplement
from trace_interop.execution_models import root_environment
from trace_interop.report import run_context
from trace_interop.scenarios import verify_state
from trace_interop.vm_model import UnsupportedProgram, execute, intrinsic

CORPUS = read(ROOT/'fixtures/corpora/mined-probes.json')
CHAIN = ROOT/'fixtures/chains/mined-probes'
CASES = {c['name']: c for c in CORPUS['cases']}
BASE = 10**20
SENDER = '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf'
NOMINAL = 50000  # receipt gas the tests assume where the corpus derives none


def builder():
    spec = importlib.util.spec_from_file_location('build_mined_probes', ROOT/'scripts/build_mined_probes_fixtures.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def receipts():
    """Receipt witnesses that satisfy the corpus's independent receipt controls."""
    return {c['name']: {'status': 'result', 'response': {'result': {'gasUsed': hex(NOMINAL), **c['expected_control_fields']}}}
            for c in CORPUS['cases'] if 'expected_control_fields' in c}


def ideal(context, txhash):
    """A replay envelope built only from the corpus expectations (and the VM model)."""
    probe = copy.deepcopy(CORPUS['probes'][txhash])
    tx = next(t for b in context['_blocks'].values() for t in b['transactions'] if t['hash'] == txhash)
    frames = {}
    for a in probe['assertions']:
        if a['kind'] == 'tree':
            for path, kind in a['frames']:
                frames[tuple(path)] = {'traceAddress': path, 'type': kind, 'action': {'from': tx['sender']} if not path else {}, 'subtraces': 0,
                                       'result': {'gasUsed': '0x0', 'output': '0x'} if kind != 'suicide' else None}
    diff, output, vm = {}, '0x', {'code': '0x', 'ops': []}
    for a in probe['assertions']:
        if a['kind'] == 'frame':
            frame = frames[tuple(a['traceAddress'])]
            frame['action'].update(a['action'])
            if a['error'] is not None:
                frame['error'] = a['error']
            if 'result' in a:
                frame['result'] = a['result']
            if 'output' in a:
                frame['result']['output'] = a['output']
        elif a['kind'] == 'delta':
            nonce = {'*': {'from': '0x1', 'to': '0x2'}} if a['nonce'] else '='
            diff[a['address']] = {'balance': {'*': {'from': hex(BASE), 'to': hex(BASE+a['balance'])}}, 'nonce': nonce, 'code': '=', 'storage': {}}
        elif a['kind'] == 'output':
            output = a['value']
    for a in probe['assertions']:
        if a['kind'] == 'account' and a['diff'] is not None:
            diff[a['address']] = a['diff']
        elif a['kind'] == 'store':
            code = context['_codes'][tx['to']]
            raw, pcs, pc = bytes.fromhex(code[2:]), [], 0
            while pc < len(raw):
                if raw[pc] == 0x55:
                    pcs.append(pc)
                pc += 1+(raw[pc]-0x5f if 0x60 <= raw[pc] <= 0x7f else 0)
            vm = {'code': code, 'ops': [{'pc': pc, 'cost': 1, 'sub': None, 'ex': {'used': 1, 'push': [], 'mem': None, 'store': {'key': k, 'val': v}}}
                                        for pc, (k, v) in zip(pcs, a['writes'])]}
    if txhash in CORPUS['storage_anchors']:
        block = next(b for b in context['_blocks'].values() for t in b['transactions'] if t['hash'] == txhash)
        code = context['_codes'][tx['to']]
        vm = execute(code, tx['gas']-intrinsic(tx['data']), '0x', root_environment(tx, block, context, 'trace_replayTransaction'))[0]
    if not any(a['kind'] == 'delta' for a in probe['assertions']):
        # No derived receipt gas: settle a nominal charge that receipts() reports.
        block = next(b for b in context['_blocks'].values() for t in b['transactions'] if t['hash'] == txhash)
        paid = min(tx['price_cap'], block['base_fee']+tx['tip_cap'])
        diff.setdefault(SENDER, {'balance': {'*': {'from': hex(BASE), 'to': hex(BASE-NOMINAL*paid)}}, 'nonce': {'*': {'from': '0x1', 'to': '0x2'}}, 'code': '=', 'storage': {}})
        diff[block['miner']] = {'balance': {'*': {'from': hex(BASE), 'to': hex(BASE+NOMINAL*(paid-block['base_fee']))}}, 'nonce': '=', 'code': '=', 'storage': {}}
    for frame in frames.values():
        frame['subtraces'] = sum(len(p) == len(frame['traceAddress'])+1 and list(p[:-1]) == frame['traceAddress'] for p in frames)
    return {'transactionHash': txhash, 'output': output, 'trace': list(frames.values()), 'stateDiff': diff, 'vmTrace': vm}


class MinedProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.context = run_context(ROOT, {'corpus': 'mined-probes'})
        cls.context['cases'] = CORPUS['cases']
        cls.roles = {p['role']: h for h, p in CORPUS['probes'].items()}

    def checks(self, name, result, peers=None):
        case = dict(CASES[name], context=self.context)
        observation = {'status': 'result', 'response': {'result': result}}
        return supplement(case, observation, dict(receipts(), **(peers or {})), [], case['topics'])

    def replay(self, role, mutate=None):
        result = ideal(self.context, self.roles[role])
        if mutate:
            mutate(result)
        return self.checks('replay-'+role, result)

    def statuses(self, checks, topic):
        return [c['status'] for c in checks if c['topic'] == topic]

    def assert_ideal(self, checks):
        self.assertNotIn('change_needed', {c['status'] for c in checks}, [c for c in checks if c['status'] == 'change_needed'])

    def assert_detects(self, role, topic, mutate):
        self.assertIn('change_needed', self.statuses(self.replay(role, mutate), topic))

    def test_chain_and_corpus_are_reproducible(self):
        self.assertEqual(CHAINS['mined-probes'], 'mined-probes')
        self.assertEqual(builder().corpus(), CORPUS)
        blocks = load_chain(CHAIN/'chain.rlp')
        self.assertEqual(blocks['0x6']['hash'], read(CHAIN/'headblock.json')['hash'])
        genesis = read(CHAIN/'genesis.json')['config']
        self.assertEqual(genesis, read(ROOT/'fixtures/chains/raw-validation/genesis.json')['config'])

    def test_derived_receipt_gas_matches_consensus_block_gas(self):
        # Header gasUsed is consensus data; the corpus derives each receipt by hand.
        raw, offset, used = (CHAIN/'chain.rlp').read_bytes(), 0, {}
        while offset < len(raw):
            block, _, offset = rlp.codec.consume_item(raw, offset)
            used[hex(int.from_bytes(block[0][8], 'big'))] = int.from_bytes(block[0][10], 'big')
        derived = {c['request']['params'][0]: int(c['expected_control_fields']['gasUsed'], 16)
                   for c in CORPUS['cases'] if 'gasUsed' in c.get('expected_control_fields', {})}
        complete = 0
        for number, block in load_chain(CHAIN/'chain.rlp').items():
            if all(t['hash'] in derived for t in block['transactions']):
                self.assertEqual(sum(derived[t['hash']] for t in block['transactions']), used[number], number)
                complete += 1
        self.assertEqual(complete, 4)

    def test_every_expectation_matches_its_ideal_response(self):
        for role in self.roles:
            with self.subTest(role=role):
                checks = self.replay(role)
                self.assert_ideal(checks)
                self.assertIn('matches', {c['status'] for c in checks})
        for block in self.context['_blocks'].values():
            envelopes = [ideal(self.context, t['hash']) for t in block['transactions']]
            for e in envelopes:
                e['vmTrace'] = None
            self.assert_ideal(self.checks('replay-block-'+str(block['number']), envelopes))
            if 'block-'+str(block['number']) in CASES:
                frames = [dict(f, transactionHash=e['transactionHash']) for e in envelopes for f in e['trace']]
                self.assert_ideal(self.checks('block-'+str(block['number']), frames))

    def test_stale_system_state_is_detected(self):
        # Besu #10953: replay without the block's own pre-transaction system calls.
        def stale(result):
            reader = result['trace'][0]['action']['to']
            result['stateDiff'][reader]['storage'] = {'0x'+'00'*31+'01': {'*': {'from': '0x'+'00'*32, 'to': '0x'+'00'*32}}}
            result['output'] = '0x'+'00'*32
        for role in ['beacon-root-read', 'history-read']:
            self.assert_detects(role, 'H28', stale)
        def system_write(result):
            result['stateDiff']['0x000f3df6d732807ef1319fb7b8bb8522d0beac02'] = {'balance': '=', 'nonce': '=', 'code': '=', 'storage': {'0x'+'00'*31+'14': {'*': {'from': '0x'+'00'*32, 'to': '0x'+'00'*31+'14'}}}}
        self.assert_detects('beacon-root-read', 'H28', system_write)
        self.assert_detects('beacon-root-read', 'H28', lambda r: r['vmTrace']['ops'][1]['ex'].update(store={'key': '0x0', 'val': '0x14'}))
        self.assert_detects('history-read', 'H28', lambda r: r['trace'][1]['result'].update(output='0x'+'00'*32))

    def test_failed_create_shape_is_exact(self):
        # Erigon and Reth report the would-be address and code on a failed CREATE.
        for role, path in [('create-revert', 0), ('factory-create-revert', 1)]:
            would_be = lambda r, p=path: r['trace'][p]['result'].update(address='0x'+'11'*20, code='0x')
            self.assert_detects(role, 'H09', would_be)
            self.assert_detects(role, 'H09', lambda r, p=path: r['trace'][p].update(error='execution reverted'))
            self.assert_detects(role, 'H09', lambda r, p=path: r['trace'][p].update(result=None))
        self.assert_detects('create-revert', 'H09', lambda r: r['trace'][0]['action'].update(gas=hex(200000)))
        self.assert_detects('factory-create-revert', 'H09', lambda r: r['trace'][0].update(error='Reverted'))
        address = next(a['address'] for a in CORPUS['probes'][self.roles['create-revert']]['assertions'] if a['topic'] == 'H17')
        self.assert_detects('create-revert', 'H17', lambda r: r['stateDiff'].update({address: {'balance': {'+': '0x0'}, 'nonce': {'+': '0x1'}, 'code': {'+': '0x'}, 'storage': {}}}))

    def test_failed_create_is_not_a_recipient(self):
        for name, extra in [('filter-failed-create-recipient', lambda h: [[h[0], [], 'create']]),
                            ('filter-failed-nested-create-recipient', lambda h: [[h[1], [0], 'create']]),
                            ('filter-failed-create-intersection', lambda h: [[h[1], [0], 'create']])]:
            hashes = [self.roles['create-revert'], self.roles['factory-create-revert']]
            frames = [{'transactionHash': t, 'traceAddress': p, 'type': k} for t, p, k in extra(hashes)]
            self.assertEqual(self.statuses(self.checks(name, []), 'H23'), ['matches'])
            self.assertEqual(self.statuses(self.checks(name, frames), 'H23'), ['change_needed'])
        creator = CASES['filter-failed-create-union']['expected_frames']
        frames = [{'transactionHash': t, 'traceAddress': p, 'type': k} for t, p, k in creator]
        self.assertEqual(self.statuses(self.checks('filter-failed-create-union', frames), 'H23'), ['matches'])
        self.assertEqual(self.statuses(self.checks('filter-failed-create-union', []), 'H23'), ['change_needed'])

    def test_selfdestruct_after_cancun(self):
        destruct = '0x'+'0'*36+'de57'
        # A surviving contract must not be reported as deleted or with storage wiped.
        self.assert_detects('selfdestruct-self', 'H26', lambda r: r['stateDiff'].update({destruct: {'balance': {'-': '0x3e8'}, 'nonce': {'-': '0x1'}, 'code': {'-': '0x30ff'}, 'storage': {}}}))
        self.assert_detects('selfdestruct-self', 'H26', lambda r: r['trace'][1]['action'].update(balance='0x0'))
        absent = CORPUS['probes'][self.roles['create-destroy-absent']]
        child = next(a['address'] for a in absent['assertions'] if a['topic'] == 'H26' and a['kind'] == 'account')
        self.assert_detects('create-destroy-absent', 'H26', lambda r: r['stateDiff'].update({child: {'balance': {'+': '0x0'}, 'nonce': {'+': '0x1'}, 'code': {'+': '0x'}, 'storage': {}}}))
        prefunded = CORPUS['probes'][self.roles['create-destroy-prefunded']]
        child = next(a['address'] for a in prefunded['assertions'] if a['topic'] == 'H26' and a['kind'] == 'account')
        self.assert_detects('create-destroy-prefunded', 'H26', lambda r: r['stateDiff'][child].update(storage={'0x'+'00'*32: {'-': '0x'+'00'*31+'01'}}))
        self.assert_detects('create-destroy-prefunded', 'H26', lambda r: r['stateDiff'][child].update(balance={'-': hex(5000+0x100)}))
        self.assert_detects('create-destroy-prefunded', 'H26', lambda r: r['trace'][2]['action'].update(balance='0x100'))

    def test_destroyed_wei_is_burned_not_lost(self):
        sender = '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf'
        for role in ['create-destroy-absent', 'create-destroy-prefunded']:
            self.assertEqual(self.statuses(self.replay(role), 'H16').count('change_needed'), 0)
            # A sender debit that omits the forwarded value no longer settles.
            def keep_value(result):
                pair = result['stateDiff'][sender]['balance']['*']
                pair['to'] = hex(int(pair['to'], 16)+0x100)
            self.assertIn('change_needed', self.statuses(self.replay(role, keep_value), 'H16'))

    def test_refund_accounting_is_exact(self):
        for role, spent, refund in [('refund-clear', 5004, 4800), ('refund-capped', 10009, 9600)]:
            tx = next(t for b in self.context['_blocks'].values() for t in b['transactions'] if t['hash'] == self.roles[role])
            steps, _, _ = execute(self.context['_codes'][tx['to']], 100000, environment={'STORAGE': {int(k, 16): int(v, 16) for k, v in CORPUS['storage_anchors'][tx['hash']].items()}})
            self.assertEqual((100000-steps['ops'][-1]['ex']['used'], steps['refund']), (spent, refund))
            # Root gasUsed precedes the refund; the post-refund receipt value is a change.
            receipt = int(next(c for c in CORPUS['cases'] if c['name'] == '_control/receipt-'+role)['expected_control_fields']['gasUsed'], 16)
            self.assertEqual(receipt, 21000+spent-min(refund, (21000+spent)//5))
            self.assert_detects(role, 'H09', lambda r, g=receipt: r['trace'][0]['result'].update(gasUsed=hex(g-21000)))
            self.assert_detects(role, 'H20', lambda r: r['vmTrace']['ops'][2].update(cost=5000-2100))
            self.assert_detects(role, 'H16', lambda r, target=tx['to']: r['stateDiff'][target]['storage'].clear())
        # Without a receipt witness, the modelled refund makes the root-gas path exact.
        case = dict(CASES['replay-refund-capped'], context=self.context)
        result = ideal(self.context, self.roles['refund-capped'])
        observation = {'status': 'result', 'response': {'result': result}}
        checks = [c for c in supplement(case, observation, {}, [], ['H16']) if c['topic'] == 'H16']
        self.assertEqual({c['status'] for c in checks}, {'matches'})
        self.assertIn('less the modelled refund 9600', ' '.join(c['detail'] for c in checks))
        uncapped = copy.deepcopy(result)
        sender = uncapped['stateDiff']['0x7e5f4552091a69125d5dfcb7b8c2659029395bdf']['balance']['*']
        miner = uncapped['stateDiff']['0x'+'00'*20]['balance']['*']
        block = self.context['_blocks']['0x5']
        paid = min(tx['price_cap'], block['base_fee']+tx['tip_cap'])
        extra = 9600-6201  # an uncapped refund charges this much less gas
        sender['to'] = hex(int(sender['to'], 16)+extra*paid)
        miner['to'] = hex(int(miner['to'], 16)-extra*(paid-block['base_fee']))
        checks = supplement(case, {'status': 'result', 'response': {'result': uncapped}}, {}, [], ['H16'])
        self.assertIn('change_needed', self.statuses(checks, 'H16'))

    def test_sstore_model_follows_eip_3529(self):
        def run(code, storage, gas=100000):
            steps, _, _ = execute(code, gas, environment={'STORAGE': storage})
            return gas-steps['ops'][-1]['ex']['used'], steps['refund']
        self.assertEqual(run('0x600160005500', {0: 0}), (3+3+22100, 0))  # zero to nonzero, cold
        # 1 -> 2 (cold reset), 2 -> 1 (restores the original: +2800), 1 -> 0 (reset again: +4800).
        self.assertEqual(run('0x600260005560016000555f60005500', {0: 1}), (6+5000+6+100+5+2900, 2800+4800))
        self.assertEqual(run('0x600160005560005f5500', {0: 0}), (3+3+22100+3+2+100, 19900))  # set then restore zero
        with self.assertRaises(UnsupportedProgram):
            run('0x600160005500', {})
        with self.assertRaises(UnsupportedProgram):
            run('0x5f5f5500', {0: 1}, gas=2304)  # EIP-2200 sentry

    def test_folded_authorizations(self):
        existing = '0x2b5ad5c4795c026514f8317c7a215e218dccd6cf'
        absent = '0x6813eb9362372eef6200f3b1dbc3f819671cba69'
        restoring = '0x1eff47bc3a10a45d4b230b5d10e37751fe6aa718'
        a, b = '0xef0100'+'0'*35+'7702a', '0xef0100'+'0'*35+'7702b'
        stale = lambda r: r['stateDiff'][existing].update(code={'*': {'from': '0x', 'to': a}}, nonce={'*': {'from': '0x5', 'to': '0x8'}})
        self.assert_detects('authorizations', 'H18', stale)
        self.assert_detects('authorizations', 'H18', lambda r: r['stateDiff'][absent].update(code={'*': {'from': '0x', 'to': a}}, nonce={'*': {'from': '0x0', 'to': '0x1'}}))
        self.assert_detects('authorizations', 'H18', lambda r: r['stateDiff'][restoring].update(code={'*': {'from': a, 'to': a}}))
        self.assert_detects('authorizations', 'H18', lambda r: r['stateDiff'][restoring].update(nonce='='))
        self.assertIn(b, str(ideal(self.context, self.roles['authorizations'])['stateDiff'][existing]))

    def test_receipt_controls_gate_eligibility(self):
        observations = {c['name']: {'c': {'status': 'result', 'response': {'result': c.get('expected_control', c.get('expected_control_fields'))}}}
                        for c in CORPUS['cases'] if c['name'].startswith('_control/')}
        self.assertTrue(verify_state('mined-probes', CORPUS, observations, 'c')[0])
        wrong = copy.deepcopy(observations)
        wrong['_control/receipt-refund-capped']['c']['response']['result']['gasUsed'] = hex(31009)  # refund ignored
        self.assertFalse(verify_state('mined-probes', CORPUS, wrong, 'c')[0])
        wrong = copy.deepcopy(observations)
        wrong['_control/beacon-reader-root']['c']['response']['result'] = '0x'+'00'*32
        self.assertFalse(verify_state('mined-probes', CORPUS, wrong, 'c')[0])

    def test_malformed_responses_do_not_crash(self):
        for case in CORPUS['cases']:
            for result in [None, [], [None], 7, 'bad', {'trace': None}, {'trace': [{'error': 1, 'result': None}]},
                           {'vmTrace': {'code': 7, 'ops': [None, {'ex': 4, 'sub': 7}]}}, {'stateDiff': []}, [{'trace': 3, 'stateDiff': 'x'}]]:
                with self.subTest(case=case['name'], result=result):
                    supplement(dict(case, context=self.context), {'status': 'result', 'response': {'result': result}},
                               receipts(), [], case.get('topics', []))


if __name__ == '__main__':
    unittest.main()

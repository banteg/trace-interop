"""Harness audit regressions; only temporary copies of retained evidence are mutated."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest

from trace_interop.cli import ROOT, classify, load_observations, read, sha, write
from trace_interop.chain_model import resolve_block
from trace_interop.coverage import supplement
from trace_interop.execution_models import assess, created_address, prestate
from trace_interop.oracles import anchor
from trace_interop.report import assess_runs, result_validator, run_context
from trace_interop.rules import evaluate
from trace_interop.scenarios import assessed_cases, verify_setup
from trace_interop.validation import request_errors
from trace_interop.vm_model import intrinsic


METHODS = {m['name']: m for m in read(ROOT / 'spec/trace-openrpc.json')['methods']}
DECISIONS = {d['id']: d for d in read(ROOT / 'decisions/ledger.json')['items']}


def capture(corpus, name, client):
    folder = ROOT / 'evidence/2026-09-29/refresh' / corpus
    manifest = read(folder / 'manifest.json')
    context = run_context(ROOT, manifest)
    cases = assessed_cases(manifest['selected_cases'], context['cases'])
    context['cases'] = cases
    case = dict(next(c for c in cases if c['name'] == name), context=context)
    observations = load_observations(folder)
    peers = {n: entries.get(client, {}) for n, entries in observations.items()}
    return folder, manifest, case, peers[name], peers, observations


def scored(case, observation, peers):
    expected = [t for t, d in DECISIONS.items()
                if case['context']['_chain'] + '/' + case['name'] in d['cases']]
    checks = evaluate(case, observation, peers,
                      invalid_params=request_errors(case['request'], METHODS))
    return supplement(case, observation, peers, checks, expected)


class AuditRegressions(unittest.TestCase):
    def test_zero_fee_accounting_does_not_require_an_exact_refund(self):
        _, _, case, observation, peers, _ = capture(
            'initial', 'call-tree-stateDiff', 'reth_release')
        accounting = lambda obs: [c for c in assess(case, obs, peers, {'H16'})
                                  if c['topic'] == 'H15']
        self.assertEqual([c['status'] for c in accounting(observation)], ['matches'])
        # Refund uncertainty must not hide an unexpected debit or beneficiary payment.
        miner = case['context']['_blocks']['0x30']['miner']
        for conserve in [False, True]:
            changed = deepcopy(observation)
            diff = changed['response']['result']['stateDiff']
            diff[miner] = {'balance': {'+': '0x1'}}
            if conserve:
                sender = case['request']['params'][0]['from']
                diff[sender]['balance'] = {'*': {'from': '0x2', 'to': '0x1'}}
            self.assertEqual([c['status'] for c in accounting(changed)], ['change_needed'])

    def test_priced_accounting_retains_unproved_refund_gap(self):
        _, _, case, observation, peers, _ = capture(
            'initial', 'call-tree-stateDiff-priced', 'anvil_release')
        checks = assess(case, observation, peers, {'H16'})
        self.assertEqual([c['status'] for c in checks], ['blocked'])
        self.assertIn('refund is not independently derived', checks[0]['detail'])

    def test_invalid_result_shape_is_reported_without_aborting_the_report(self):
        folder, manifest, case, observation, _, observations = capture(
            'coverage', 'model-transfer', 'besu_development')
        summary = read(folder / 'summary.json')
        validator = result_validator(METHODS['trace_call']['result']['schema'])
        self.assertFalse(list(validator.iter_errors(observation['response']['result'])))
        bad = deepcopy(observation['response'])
        bad['result']['trace'][0]['result']['output'] = 1
        observations[case['name']]['besu_development'] = classify(json.dumps(bad), case['request'])
        self.assertTrue(list(validator.iter_errors(bad['result'])))
        self.assertTrue(verify_setup(manifest, case['context'], observations,
                                     'besu_development', summary['launches'])[0])
        pinned = (read(ROOT / 'spec.lock.json'), METHODS,
                  {n: result_validator(m['result']['schema']) for n, m in METHODS.items()}, {})
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / 'coverage'
            for name, data in [('manifest', manifest), ('summary', summary),
                               ('observations', observations)]:
                write(run / (name + '.json'), data)
            write(run / 'checksums.json', {p.name: sha(p) for p in run.iterdir()})
            records = assess_runs(ROOT, [run], Path(tmp) / 'reports', DECISIONS, pinned)[0]
            record = next(r for r in records if r['case'] == case['name']
                          and r['client'] == 'besu_development')
            self.assertEqual(record['schema']['status'], 'invalid')

    def test_equivalent_null_and_hash_selectors_keep_the_selected_block_fee_model(self):
        for name, position, count in [('model-transfer', 2, 1), ('model-many-transfers', 1, 2)]:
            _, _, case, observation, peers, _ = capture('coverage', name, 'besu_development')
            original = [c for c in scored(case, observation, peers)
                        if c['requirement'].startswith('Account balance deltas')]
            self.assertEqual([c['status'] for c in original], ['matches'] * count)
            for selector in [None, case['context']['_head']['hash']]:
                with self.subTest(name=name, selector=selector):
                    changed = deepcopy(case)
                    changed['request']['params'][position] = selector
                    self.assertEqual(request_errors(changed['request'], METHODS), [])
                    checks = [c for c in scored(changed, observation, peers)
                              if c['requirement'].startswith('Account balance deltas')]
                    self.assertEqual([c['status'] for c in checks], ['matches'] * count, checks)

    def test_reverted_mined_creation_stays_absent_from_later_prestate(self):
        context = run_context(ROOT, {'corpus': 'mined-probes'})
        tx = context['_blocks']['0x3']['transactions'][0]
        address = created_address(tx['sender'], tx['nonce'])
        expectations = context['probes'][tx['hash']]['assertions']
        self.assertTrue(any(a['kind'] == 'account' and a['address'] == address
                            and a['diff'] is None for a in expectations))
        sender = tx['sender']
        case = {'name': 'fund-reverted-creation', 'context': context,
                'request': {'jsonrpc': '2.0', 'id': 1, 'method': 'trace_call',
                            'params': [{'from': sender, 'to': address, 'value': '0x1',
                                        'gas': '0x5208', 'gasPrice': '0x0'},
                                       ['stateDiff'], 'latest']}}
        _, _, nonces = prestate(context, context['_blocks']['0x6'], None)
        result = {'output': '0x', 'trace': [], 'vmTrace': None, 'stateDiff': {
            sender: {'balance': {'*': {'from': '0x1000000', 'to': '0xffffff'}},
                     'nonce': {'*': {'from': hex(nonces[sender]), 'to': hex(nonces[sender] + 1)}},
                     'code': '=', 'storage': {}},
            address: {'balance': {'+': '0x1'}, 'nonce': {'+': '0x0'},
                      'code': {'+': '0x'}, 'storage': {}}}}
        self.assertEqual(request_errors(case['request'], METHODS), [])
        checks = assess(case, {'status': 'result', 'response': {'result': result}}, {}, {'H17'})
        self.assertEqual([c['status'] for c in checks], ['matches'], checks)

    def test_unresolved_selectors_do_not_invent_a_zero_base_fee(self):
        _, _, case, observation, peers, _ = capture(
            'coverage', 'model-transfer', 'besu_development')
        for selector in ['pending', '0x' + 'ef' * 32]:
            with self.subTest(selector=selector):
                changed = deepcopy(case)
                changed['request']['params'][2] = selector
                self.assertEqual(request_errors(changed['request'], METHODS), [])
                checks = assess(changed, observation, peers, {'H16', 'H17'})
                self.assertEqual({c['status'] for c in checks}, {'blocked'}, checks)
                self.assertEqual({c['topic'] for c in checks}, {'H15', 'H17'})

    def test_finalized_selector_uses_frozen_forkchoice_instead_of_head(self):
        context = run_context(ROOT, {'corpus': 'a'})
        self.assertEqual(resolve_block(context, 'safe')['number'], 48)
        self.assertEqual(resolve_block(context, 'finalized')['number'], 28)

    def test_hash_selected_replay_still_requires_every_transaction_envelope(self):
        _, _, case, observation, peers, _ = capture('forks', 'replay-56', 'reth_release')
        block = case['context']['_blocks'][case['request']['params'][0]]
        case['request']['params'][0] = block['hash']
        self.assertEqual(request_errors(case['request'], METHODS), [])
        inventory = lambda obs: [c for c in scored(case, obs, peers)
                                 if c['requirement'].startswith('Block replay has exactly one envelope')]
        self.assertEqual([c['status'] for c in inventory(observation)], ['matches'])
        omitted = deepcopy(observation)
        omitted['response']['result'].pop()
        self.assertEqual([c['status'] for c in inventory(omitted)], ['change_needed'])

    def test_mined_creation_finalization_controls_later_existence(self):
        sender = '0x' + '11' * 20
        address = created_address(sender, 0)
        for code, gas, outcome in [
                ('0x60006000fd', 100, False),  # REVERT
                ('0x60016000f3', 1, False),  # Execution out of gas
                ('0x60016000f3', 199, False),  # Cannot pay for one runtime byte
                ('0x600160005500', 30000, True),  # Fresh constructor storage starts at zero
                ('0x00', 100, True),  # Empty code still leaves an account
                ('0x31', 100, None)]:  # Unsupported execution stays uncertain
            with self.subTest(code=code, gas=gas):
                tx = {'sender': sender, 'nonce': 0, 'to': None, 'value': 0,
                      'data': code, 'gas': intrinsic(code, True) + gas, 'authorizations': []}
                block = {'number': 1, 'transactions': [tx], 'miner': '0x' + '22' * 20}
                context = {'_blocks': {'0x1': block}, '_head': {'number': '0x1'},
                           '_alloc': {sender: {'balance': '0x1000000'}}, '_codes': {sender: '0x'}}
                exists, codes, nonces = prestate(context, block, None)
                self.assertEqual(address in exists, outcome is True)
                self.assertEqual(nonces[sender], 1)
                if outcome is False:
                    self.assertNotIn(address, codes)
                    self.assertNotIn(address, nonces)
                elif outcome is True:
                    self.assertEqual(codes[address], '0x')
                    self.assertEqual(nonces[address], 1)
                else:
                    self.assertIsNone(codes[address])
                    # Neither omitted nor present birth markers establish prior existence.
                    case = {'context': context, 'request': {'method': 'trace_call',
                            'params': [{'from': sender, 'to': address, 'value': '0x1'}, ['stateDiff'], 'latest']}}
                    for account in [None, {'balance': {'+': '0x1'}, 'nonce': {'+': '0x0'}, 'code': {'+': '0x'}}]:
                        diff = {sender: {'balance': '=', 'nonce': '=', 'code': '='}}
                        if account is not None:
                            diff[address] = account
                        checks = assess(case, {'status': 'result', 'response': {'result': {'stateDiff': diff}}}, {}, {'H17'})
                        self.assertEqual([c['status'] for c in checks], ['blocked'], checks)

    def test_joint_phantom_transaction_cannot_pass_filter_selection(self):
        _, _, case, observation, peers, _ = capture('a', 'filter-all', 'go-ethereum_trace')
        baseline = [c for c in scored(case, observation, peers) if c['topic'] == 'H03']
        self.assertTrue(baseline)
        self.assertEqual({c['status'] for c in baseline}, {'matches'})
        phantom = deepcopy(peers['block-2']['response']['result'][0])
        phantom.update(transactionHash='0x' + 'ef' * 32, subtraces=0,
                       traceAddress=[], transactionPosition=13)
        self.assertFalse(any(t['hash'] == phantom['transactionHash']
                             for t in case['context']['_blocks']['0x2']['transactions']))
        for name in ['block-2', 'filter-all']:
            peers[name]['response']['result'].append(deepcopy(phantom))
        validator = result_validator(METHODS['trace_filter']['result']['schema'])
        self.assertFalse(list(validator.iter_errors(peers['filter-all']['response']['result'])))
        anchored, mismatch = anchor(case['context'], peers, 'block-2')
        self.assertIsNone(anchored)
        self.assertIn('transaction root inventory', mismatch)
        checks = [c for c in scored(case, peers['filter-all'], peers) if c['topic'] == 'H03']
        self.assertTrue(checks)
        self.assertNotEqual({c['status'] for c in checks}, {'matches'}, checks)


if __name__ == '__main__':
    unittest.main()

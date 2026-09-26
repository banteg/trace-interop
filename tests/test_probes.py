"""Counterexamples for the probes on the existing chains: a correct response matches,
each plausible wrong response (named after the client behaviour it models) needs a change."""
import copy
import unittest

from trace_interop.cli import ROOT, load_observations, read
from trace_interop.coverage import supplement
from trace_interop.probes import assess, same
from trace_interop.scenarios import verify_setup
from trace_interop.vm_model import execute, intrinsic, local_invariants

PRAGUE = {c['name']: c for c in read(ROOT/'fixtures/corpora/probes-prague.json')['cases']}
FORKS = {c['name']: c for c in read(ROOT/'fixtures/corpora/probes-forks.json')['cases']}


def realize(spec, label='Reverted'):
    """A response frame satisfying an expected subset, with the extra fields clients add;
    `label` stands in for a wildcard error."""
    frame = {k: copy.deepcopy(v) for k, v in spec.items() if k != 'absent' and not (k in ['error', 'result'] and v is None)}
    if frame.get('error') == '*':
        frame['error'] = label
    frame.setdefault('transactionHash', None)
    return frame


def result(value):
    return {'status': 'result', 'response': {'jsonrpc': '2.0', 'id': 1, 'result': value}}


def error(code):
    return {'status': 'rpc_error', 'response': {'jsonrpc': '2.0', 'id': 1, 'error': {'code': code, 'message': 'invalid'}}}


def statuses(case, observation, peers=None):
    return [c['status'] for c in assess(case, observation, peers or {})]


class Probe(unittest.TestCase):
    def assertMatches(self, case, observation, peers=None):
        checks = assess(case, observation, peers or {})
        self.assertTrue(checks)
        self.assertEqual({c['status'] for c in checks}, {'matches'}, checks)

    def assertDiffers(self, case, observation, peers=None):
        self.assertIn('change_needed', statuses(case, observation, peers), case['name'])


class VMProbeTests(Probe):
    def vm(self, name):
        case = PRAGUE[name]
        call = case['request']['params'][0]
        steps, output, _ = execute(case['model']['code'], int(call['gas'], 16)-intrinsic(call['data'], True),
                                   environment={'FRESH_ACCOUNT': True})
        return case, {'output': output, 'trace': [], 'stateDiff': None, 'vmTrace': steps}

    def test_push_window_arity_and_order(self):
        case, envelope = self.vm('vm-push-order')
        self.assertMatches(case, result(envelope))
        pushes = [op['ex']['push'] for op in envelope['vmTrace']['ops']]
        self.assertEqual(pushes[3:7], [['0x1', '0x2', '0x3', '0x1'], ['0x1', '0x3', '0x2'], ['0x2', '0x3'], ['0x3', '0x3']])
        self.assertEqual(local_invariants(envelope['vmTrace']), [])
        for index in [3, 6, 13]:  # Nethermind: DUPn reports the n words before the copy.
            wrong = copy.deepcopy(envelope)
            wrong['vmTrace']['ops'][index]['ex']['push'].pop()
            self.assertDiffers(case, result(wrong))
            self.assertTrue(local_invariants(wrong['vmTrace']))
        for index in [3, 4]:  # Besu: multi-word push top first.
            wrong = copy.deepcopy(envelope)
            wrong['vmTrace']['ops'][index]['ex']['push'].reverse()
            self.assertDiffers(case, result(wrong))
            self.assertTrue(local_invariants(wrong['vmTrace']))

    def test_store_exactly_on_completed_sstore(self):
        for name in ['vm-store', 'vm-store-vm-only']:
            case, envelope = self.vm(name)
            self.assertMatches(case, result(envelope))
            ops = envelope['vmTrace']['ops']
            self.assertEqual([(op['pc'], op['ex']['store']) for op in ops if op['ex']['store']],
                             [(4, {'key': '0x1', 'val': '0x2a'}), (9, {'key': '0x1', 'val': '0x2a'})])
            self.assertEqual([op['cost'] for op in ops if op['op'] in ['SSTORE', 'SLOAD', 'TSTORE', 'TLOAD']], [22100, 100, 2100, 100, 100])
            padded = copy.deepcopy(envelope)
            padded['vmTrace']['ops'][2]['ex']['store'] = {'key': '0x'+'00'*31+'01', 'val': '0x2a'}
            self.assertMatches(case, result(padded))  # Quantity encoding belongs to H21.
            for mutate in [lambda o: o[5]['ex'].update(store=None),                            # revm main: warm unchanged write
                           lambda o: o[7]['ex'].update(store={'key': '0x2', 'val': '0x0'}),   # revm main: cold SLOAD
                           lambda o: o[10]['ex'].update(store={'key': '0x3', 'val': '0x7'}),  # TSTORE
                           lambda o: [op['ex'].update(store=None) for op in o]]:              # Reth 0.43 and Nethermind without stateDiff
                wrong = copy.deepcopy(envelope)
                mutate(wrong['vmTrace']['ops'])
                self.assertDiffers(case, result(wrong))

    def test_no_synthetic_stop_past_the_code_end(self):
        case, envelope = self.vm('vm-off-end')
        self.assertMatches(case, result(envelope))
        wrong = copy.deepcopy(envelope)
        last = wrong['vmTrace']['ops'][-1]
        wrong['vmTrace']['ops'].append({'pc': 6, 'cost': 0, 'op': 'STOP', 'sub': None,
                                        'ex': {'used': last['ex']['used'], 'push': [], 'mem': None, 'store': None}})
        self.assertDiffers(case, result(wrong))

    def test_model_supplement_executes_fresh_creation_storage(self):
        case, envelope = self.vm('vm-store')
        context = {'_environment': {'BASEFEE': 1}, 'cases': [], 'model_nonce': 10}
        checks = supplement(dict(case, context=context), result(envelope), {}, [], ['H20'])
        model = [c for c in checks if c['requirement'].startswith('Every modelled step')]
        self.assertEqual([c['status'] for c in model], ['matches'], checks)
        wrong = copy.deepcopy(envelope)
        wrong['vmTrace']['ops'][5]['ex']['store'] = None
        checks = supplement(dict(case, context=context), result(wrong), {}, [], ['H20'])
        self.assertIn('change_needed', [c['status'] for c in checks if c['topic'] == 'H20'])


class FrameProbeTests(Probe):
    def envelope(self, name, **extra):
        case = PRAGUE[name]
        frames = [realize(f) for f in next(p for p in case['probes'] if p['kind'] == 'frames')['expected']]
        for label in [p for p in case['probes'] if p['kind'] == 'frame']:
            next(f for f in frames if same(f, label['select'])).update(label['expected'])
        output = next(p for p in case['probes'] if p['kind'] == 'outputs')['expected'][0]
        return case, dict({'output': output, 'trace': frames, 'stateDiff': None, 'vmTrace': None}, **extra)

    def vm_with_subs(self, case, sub_at):
        subs = next(p for p in case['probes'] if p['kind'] == 'subs')
        ops = [{'pc': pc, 'cost': 0, 'ex': None, 'sub': {'code': '0x', 'ops': []} if pc in sub_at else None}
               for pc in sorted(subs['null']+subs['object'])]
        return {'code': case['request']['params'][0]['data'], 'ops': ops}

    def test_precheck_failures_keep_a_failed_frame_without_sub(self):
        by_topic = lambda case, wrong: {t: {c['status'] for c in assess(case, result(wrong), {}) if c['topic'] == t} for t in ['H09', 'H29']}
        for name in ['precheck-call-value', 'precheck-create-value']:
            case = PRAGUE[name]
            subs = next(p for p in case['probes'] if p['kind'] == 'subs')
            _, envelope = self.envelope(name, vmTrace=self.vm_with_subs(case, subs['object']))
            self.assertMatches(case, result(envelope))
            # Reth: the same frame and the listed label.
            self.assertEqual(envelope['trace'][1]['error'], 'Insufficient balance for transfer')
            # Erigon: the frame is right; only H09 names the lowercase label.
            wrong = copy.deepcopy(envelope)
            wrong['trace'][1]['error'] = 'insufficient balance for transfer'
            self.assertEqual(by_topic(case, wrong), {'H09': {'change_needed'}, 'H29': {'matches'}})
            # Parity, Nethermind, Besu CALL: no frame, so the sibling moves to [0]; H09 has no frame to judge.
            wrong = copy.deepcopy(envelope)
            del wrong['trace'][1]
            wrong['trace'][1]['traceAddress'] = [0]
            wrong['trace'][0]['subtraces'] = 1
            topics = by_topic(case, wrong)
            self.assertEqual(topics['H09'], {'blocked'})
            self.assertIn('change_needed', topics['H29'])
            # A sub on the failed call or create.
            wrong = dict(envelope, vmTrace=self.vm_with_subs(case, subs['null']+subs['object']))
            self.assertDiffers(case, result(wrong))
            # Besu (C3): the dangling create context swallows the later sibling.
            wrong = copy.deepcopy(envelope)
            wrong['trace'][0]['subtraces'] = 0
            del wrong['trace'][1:]
            self.assertDiffers(case, result(wrong))

    def test_collision_frame_label_and_continuation(self):
        case, envelope = self.envelope('create2-collision')
        self.assertMatches(case, result(envelope))
        by_topic = lambda wrong: {t: {c['status'] for c in assess(case, result(wrong), {}) if c['topic'] == t} for t in ['H09', 'H29']}
        # A frame with another label has the right H29 shape; only H09 names the label.
        for label in ['Out of gas', 'contract address collision', 'CreateCollision', 'Illegal state change']:  # Parity, Erigon, Reth, Besu
            wrong = copy.deepcopy(envelope)
            wrong['trace'][2]['error'] = label
            self.assertEqual(by_topic(wrong), {'H09': {'change_needed'}, 'H29': {'matches'}}, label)
        for mutate in [lambda t: t[2].update(error=''), lambda t: t[2].pop('error'),
                       lambda t: t[2].update(result={'gasUsed': '0x0', 'output': '0x'})]:
            wrong = copy.deepcopy(envelope)
            mutate(wrong['trace'])
            self.assertIn('change_needed', by_topic(wrong)['H29'])
        # Nethermind: no frame. H29 differs; the label cannot be judged.
        wrong = copy.deepcopy(envelope)
        wrong['trace'].pop(2)
        wrong['trace'][0]['subtraces'] = 2
        wrong['trace'][2]['traceAddress'] = [1]
        self.assertEqual(by_topic(wrong), {'H09': {'blocked'}, 'H29': {'change_needed', 'matches'}})
        wrong = dict(envelope, output=envelope['output'][:-64]+'0'*64)
        self.assertDiffers(case, result(wrong))

    def test_reverted_create_has_gas_and_output_only(self):
        case, envelope = self.envelope('create-reverted')
        self.assertMatches(case, result(envelope))
        self.assertEqual(envelope['trace'][1]['result'], {'gasUsed': '0x12', 'output': '0xdeadbeef'})
        for mutate in [lambda f: f['result'].update(address='0x'+'11'*20, code='0xdeadbeef'),  # Erigon, Reth
                       lambda f: f.pop('result'),                                              # Besu, Nethermind
                       lambda f: f['result'].update(gasUsed='0x0'),
                       lambda f: f.update(error='Out of gas')]:
            wrong = copy.deepcopy(envelope)
            mutate(wrong['trace'][1])
            self.assertDiffers(case, result(wrong))


class CallManyProbeTests(Probe):
    def outputs(self, name):
        case = PRAGUE[name]
        return case, next(p for p in case['probes'] if p['kind'] == 'outputs')['expected']

    def test_item_isolation(self):
        wrong_outputs = {'many-transient': {2: 42}, 'many-warm': {1: (107, 107, 107, 107)},
                         'many-selfdestruct': {2: (0, 5)}, 'many-original-value': {1: (2208,)}}
        for name, wrong in wrong_outputs.items():
            case, outputs = self.outputs(name)
            correct = [{'output': o, 'trace': [], 'stateDiff': None, 'vmTrace': None} for o in outputs]
            self.assertMatches(case, result(correct))
            for index, values in wrong.items():
                mutated = copy.deepcopy(correct)
                values = values if isinstance(values, tuple) else (values,)
                mutated[index]['output'] = '0x'+''.join(f'{v:064x}' for v in values)
                self.assertDiffers(case, result(mutated))
            self.assertDiffers(case, result(correct[:-1]))

    def test_expected_gas_is_hand_derived(self):
        self.assertEqual(self.outputs('many-warm')[1][1], '0x'+''.join(f'{v:064x}' for v in [3+2600+2+2, 3+100+2+2, 3+2100+2+2, 3+100+2+2]))
        self.assertEqual(self.outputs('many-original-value')[1][1], '0x'+f'{3+3+2100+2900+2:064x}')

    def test_selfdestruct_of_earlier_item_is_not_a_deletion(self):
        case = PRAGUE['many-selfdestruct-diff']
        address = case['probes'][0]['address']
        account = {'balance': {'*': {'from': '0x5', 'to': '0x0'}}, 'code': '=', 'nonce': '=', 'storage': {}}
        envelopes = [{'output': '0x', 'trace': [], 'stateDiff': None}, {'output': '0x', 'trace': [], 'stateDiff': {address: account}},
                     {'output': '0x', 'trace': [], 'stateDiff': None}]
        self.assertMatches(case, result(envelopes))
        deleted = copy.deepcopy(envelopes)
        deleted[1]['stateDiff'][address] = {'balance': {'-': '0x5'}, 'code': {'-': '0x61beefff'}, 'nonce': {'-': '0x1'}, 'storage': {}}
        self.assertDiffers(case, result(deleted))


class FieldProbeTests(Probe):
    def test_fields_take_effect_or_reject(self):
        for name, case in PRAGUE.items():
            if not name.startswith('field-') or 'probes' not in case:
                continue
            kinds = {p['kind'] for p in case['probes']}
            if any('observe' in p for p in case['probes']):
                for observation in [result({'output': '0x', 'trace': []}), error(-32602), error(-32603)]:
                    self.assertEqual(set(statuses(case, observation)), {'observation'}, name)
            elif kinds == {'error'}:
                self.assertMatches(case, error(-32602))
                self.assertDiffers(case, result({'output': '0x'+f'{42:064x}', 'trace': []}))
                if any('code' in p for p in case['probes']):
                    self.assertDiffers(case, error(-32000))
            elif kinds == {'outputs'}:
                want = case['probes'][0]['expected'][0]
                self.assertMatches(case, result({'output': want, 'trace': []}))
                # Erigon drops input and authorizationList; an ignored access list reads cold.
                self.assertDiffers(case, result({'output': '0x' if want != '0x' else '0x'+f'{42:064x}', 'trace': []}))
                # Besu: an unfunded zero-address sender under a base-fee default fails on H15, not the field.
                self.assertEqual(statuses(case, error(-32603)), ['blocked' if 'depends' in case['probes'][0] else 'change_needed'], name)

    def test_omitted_gas_is_the_eth_call_cap(self):
        case = PRAGUE['field-gas-omitted']
        peers = {'field-gas-omitted-eth-call': result('0x'+f'{49_978_000:064x}')}
        self.assertMatches(case, result({'output': '0x'+f'{49_978_000:064x}', 'trace': []}), peers)
        self.assertDiffers(case, result({'output': '0x'+f'{99_978_000:064x}', 'trace': []}), peers)
        self.assertEqual(statuses(case, result({'output': '0x', 'trace': []}), {}), ['blocked'])

    def test_authorization_tuple_recovers_key_one(self):
        import rlp

        from trace_interop.chain_model import decode_transaction
        auth = PRAGUE['field-authorization']['request']['params'][0]['authorizationList'][0]
        fields = [int(auth['chainId'], 16), bytes.fromhex(auth['address'][2:]), int(auth['nonce'], 16),
                  int(auth['yParity'], 16), int(auth['r'], 16), int(auth['s'], 16)]
        # Recover through the chain decoder's EIP-7702 path, wrapped in a minimal type-4 envelope.
        from eth_keys import keys
        key = keys.PrivateKey((1).to_bytes(32, 'big'))
        body = [fields[0], 0, 0, 1, 21000, b'\x11'*20, 0, b'', [], [fields]]
        signature = key.sign_msg_hash(__import__('eth_hash.auto', fromlist=['keccak']).keccak(b'\x04'+rlp.encode(body)))
        tx = decode_transaction(b'\x04'+rlp.encode(body+[signature.v, signature.r, signature.s]))
        self.assertEqual(tx['authorizations'][0]['authority'], PRAGUE['field-authorization']['request']['params'][0]['to'])


class ForksProbeTests(Probe):
    def records(self, name):
        return [realize(r) for r in FORKS[name]['probes'][0]['expected']]

    def test_reward_matching_and_modes(self):
        rewards = self.records('rewards-to')
        self.assertEqual([(r['blockNumber'], r['action']['rewardType'], int(r['action']['value'], 16)) for r in rewards],
                         [(2, 'block', 5*10**18), (3, 'block', 5*10**18+2*5*10**18//32), (3, 'uncle', 7*5*10**18//8), (3, 'uncle', 7*5*10**18//8),
                          (4, 'block', 5*10**18+5*10**18//32), (4, 'uncle', 7*5*10**18//8), (5, 'block', 5*10**18+5*10**18//32), (5, 'uncle', 7*5*10**18//8)])
        self.assertMatches(FORKS['rewards-to'], result(rewards))
        self.assertDiffers(FORKS['rewards-to'], result([]))  # Besu, Nethermind: rewards matched by from/to only.
        self.assertDiffers(FORKS['rewards-to'], result([rewards[i] for i in [0, 2, 1, 3, 4, 5, 6, 7]]))
        self.assertMatches(FORKS['rewards-intersection'], result([]))
        self.assertDiffers(FORKS['rewards-intersection'], result(rewards))  # Erigon: rewards ignore mode and fromAddress.
        union = self.records('rewards-union')
        self.assertEqual([r['type'] for r in union], ['call']*3+['reward']+['call']+['reward']*3)
        self.assertMatches(FORKS['rewards-union'], result(union))
        self.assertDiffers(FORKS['rewards-union'], result([r for r in union if r['type'] == 'call']))

    def test_pagination_filters_before_skipping(self):
        page = self.records('sender-skip')
        self.assertEqual([(r['blockNumber'], r['transactionPosition']) for r in page], [(2, 2), (3, 0), (4, 0)])
        self.assertMatches(FORKS['sender-skip'], result(page))
        window = self.records('rewards-window')
        self.assertEqual([(r['blockNumber'], r['type'], r['action'].get('rewardType')) for r in window],
                         [(2, 'reward', 'block'), (3, 'call', None), (3, 'reward', 'block'), (3, 'reward', 'uncle'), (3, 'reward', 'uncle')])
        self.assertMatches(FORKS['rewards-window'], result(window))
        self.assertDiffers(FORKS['rewards-window'], result(window[1:]+window[:1]))
        # Skipping unfiltered records first returns a different page.
        union = self.records('rewards-union')
        self.assertDiffers(FORKS['sender-skip'], result([r for r in union if r['type'] == 'call'][2:5]))

    def test_genesis_has_no_records(self):
        for name in ['genesis-block', 'genesis-replay', 'genesis-filter']:
            self.assertMatches(FORKS[name], result([]))
            self.assertDiffers(FORKS[name], error(-32000))  # Nethermind: no parent for block 0.
        reward = {'type': 'reward', 'blockNumber': 0, 'traceAddress': [], 'subtraces': 0,
                  'action': {'author': '0x'+'00'*20, 'rewardType': 'block', 'value': hex(5*10**18)}}
        self.assertDiffers(FORKS['genesis-block'], result([reward]))  # Reth: fabricated genesis reward.
        rewards = self.records('genesis-range-rewards')
        self.assertEqual([r['blockNumber'] for r in rewards], [1, 2])
        self.assertMatches(FORKS['genesis-range-rewards'], result(rewards))
        self.assertDiffers(FORKS['genesis-range-rewards'], result([reward]+rewards))
        self.assertDiffers(FORKS['genesis-range-rewards'], result([]))  # Nethermind: truncated at genesis.

    def test_reversed_range_is_invalid_params(self):
        self.assertMatches(FORKS['range-reversed'], error(-32602))
        self.assertDiffers(FORKS['range-reversed'], error(-32000))  # Erigon, Nethermind
        self.assertDiffers(FORKS['range-reversed'], result([]))     # Parity

    def test_rewards_intersection_mode_dependency(self):
        for name in ['rewards-intersection', 'rewards-intersection-default']:
            self.assertMatches(FORKS[name], result([]))
            self.assertDiffers(FORKS[name], result(self.records('rewards-to')))
        # Besu rejects the explicit mode field (H03), which says nothing about reward matching.
        self.assertEqual(statuses(FORKS['rewards-intersection'], error(-32602)), ['blocked'])
        self.assertNotIn('mode', FORKS['rewards-intersection-default']['request']['params'][0])
        self.assertDiffers(FORKS['rewards-intersection-default'], error(-32602))

    def test_block_55_reads_are_h28_probes_not_setup(self):
        folder = ROOT/'evidence/2026-09-25/fixture-wave/probes-forks'
        manifest, observations = read(folder/'manifest.json'), load_observations(folder)
        corpus = read(ROOT/'fixtures/corpora/probes-forks.json')
        zero = '0x'+'00'*32
        for name in ['_control/beacon-timestamp-55', '_control/beacon-root-55']:
            case = FORKS[name]
            self.assertNotIn('expected_control', case)
            checks = supplement(dict(case, context={}), result(zero), {}, [], ['H28'])
            self.assertEqual([(c['topic'], c['status']) for c in checks], [('H28', 'matches')])
            # Erigon 3.6.1 reads block 56's write at block 55: an H28 difference, not a setup failure.
            erigon = observations[name]['erigon_release']
            self.assertNotEqual(erigon['response']['result'], zero)
            self.assertEqual(statuses(case, erigon), ['change_needed'])
        self.assertTrue(verify_setup(manifest, corpus, observations, 'erigon_release')[0])
        # The captured definitions still made the block-55 reads setup controls.
        self.assertFalse(verify_setup(manifest, dict(corpus, cases=manifest['selected_cases']), observations, 'erigon_release')[0])

    def test_setup_controls_follow_the_assessed_definitions(self):
        folder = ROOT/'evidence/2026-09-25/fixture-wave/probes-forks'
        manifest, observations = read(folder/'manifest.json'), load_observations(folder)
        corpus = read(ROOT/'fixtures/corpora/probes-forks.json')
        self.assertTrue(verify_setup(manifest, corpus, observations, 'reth_release')[0])
        # A current control on an unchanged request applies to the old evidence.
        wrong = copy.deepcopy(corpus)
        next(c for c in wrong['cases'] if c['name'] == '_control/beacon-root-56')['expected_control'] = '0x'+'00'*32
        self.assertFalse(verify_setup(manifest, wrong, observations, 'reth_release')[0])
        # A control whose request has changed since, or that was never captured, keeps or needs nothing new.
        changed = copy.deepcopy(corpus)
        control = next(c for c in changed['cases'] if c['name'] == '_control/beacon-root-56')
        control['request'] = dict(control['request'], params=control['request']['params'][:2]+['latest'])
        control['expected_control'] = '0x'+'00'*32
        changed['cases'].append({'name': '_control/uncaptured', 'request': {'jsonrpc': '2.0', 'id': 1, 'method': 'eth_chainId', 'params': []},
                                 'expected_control': '0x1'})
        self.assertTrue(verify_setup(manifest, changed, observations, 'reth_release')[0])

    def test_beacon_call_many_twin(self):
        for number in [55, 56]:
            output = FORKS[f'beacon-trace-{number}']['probes'][0]['expected'][0]
            peers = {f'beacon-trace-{number}': result({'output': output, 'trace': []})}
            case = FORKS[f'beacon-many-{number}']
            self.assertMatches(case, result([{'output': output, 'trace': []}]), peers)
        root = FORKS['beacon-trace-56']['probes'][0]['expected'][0]
        # Erigon: callMany at historical 55 sees block 56's system write.
        self.assertDiffers(FORKS['beacon-many-55'], result([{'output': root, 'trace': []}]),
                           {'beacon-trace-55': result({'output': '0x', 'trace': []})})
        self.assertEqual(FORKS['beacon-trace-55']['probes'][0]['expected'], ['0x'])


if __name__ == '__main__':
    unittest.main()


class DepthProbeTests(Probe):
    """The depth-limit probe: a chain of 1025 executed frames, then the failed attempts beyond it."""

    def trace(self, attempts=(('call', 'Max call depth exceeded'), ('create', 'Max call depth exceeded')), phantom=False):
        frames = [{'type': 'create', 'traceAddress': [], 'subtraces': 2, 'action': {}, 'result': {}},
                  {'type': 'create', 'traceAddress': [0], 'subtraces': 0, 'action': {}, 'result': {}}]
        frames += [{'type': 'call', 'traceAddress': [1]+[0]*(d-1), 'subtraces': 1, 'action': {}, 'result': {}} for d in range(1, 1025)]
        deepest = frames[-1]
        deepest['subtraces'] = len(attempts) + phantom
        for i, (kind, label) in enumerate(attempts):
            frames.append({'type': kind, 'traceAddress': deepest['traceAddress']+[i], 'subtraces': 0, 'action': {}, 'error': label})
        if phantom:  # Besu: the failed CREATE as a successful frame
            frames.append({'type': 'create', 'traceAddress': deepest['traceAddress']+[0], 'subtraces': 0, 'action': {}, 'result': {'address': '0x1'}})
        return {'output': '0x', 'trace': frames, 'stateDiff': None, 'vmTrace': None}

    def statuses(self, envelope):
        case = FORKS['depth-limit']
        return {t: {c['status'] for c in assess(case, result(envelope), {}) if c['topic'] == t} for t in ['H09', 'H29']}

    def test_attempts_beyond_the_limit(self):
        self.assertEqual(self.statuses(self.trace()), {'H09': {'matches'}, 'H29': {'matches'}})
        # Erigon and Reth: the right frames, other labels.
        for label in ['max call depth exceeded', 'CallTooDeep']:
            wrong = self.trace(attempts=(('call', label), ('create', label)))
            self.assertEqual(self.statuses(wrong), {'H09': {'change_needed'}, 'H29': {'matches'}}, label)
        # Nethermind and the previous rule: no attempts, so H09 has nothing to judge.
        self.assertEqual(self.statuses(self.trace(attempts=())), {'H09': {'blocked'}, 'H29': {'change_needed'}})
        # Besu: the failed CREATE reported as a successful frame one level deeper.
        self.assertEqual(self.statuses(self.trace(attempts=(), phantom=True))['H29'], {'change_needed'})


class NullMemberTests(Probe):
    """An explicit null for an optional member is the same as omitting it (H14)."""

    def test_null_bound_matches_its_omitted_twin(self):
        case = FORKS['filter-null-toBlock']
        records = [{'type': 'reward', 'blockNumber': 2}]
        same = assess(case, result(records), {'filter-omitted-toBlock': result(records)})
        self.assertEqual({c['status'] for c in same}, {'matches'})
        # A client that rejects the null differs; one whose reference failed is blocked.
        rejected = assess(case, error(-32602), {'filter-omitted-toBlock': result(records)})
        self.assertEqual({c['status'] for c in rejected}, {'change_needed'})
        blocked = assess(case, result(records), {'filter-omitted-toBlock': error(-32602)})
        self.assertEqual({c['status'] for c in blocked}, {'blocked'})

    def test_null_input_does_not_conflict_with_data(self):
        from trace_interop.validation import request_errors
        methods = {m['name']: m for m in read(ROOT/'spec/trace-openrpc.json')['methods']}
        self.assertEqual(request_errors(PRAGUE['field-null-members']['request'], methods), [])
        self.assertEqual(request_errors(PRAGUE['field-data-input-differ']['request'], methods), ['data and input must agree'])

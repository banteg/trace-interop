"""Counterexamples for the consistency laws: each models a defect a matrix build showed,
and the matching consistent response holds the law."""
import copy
import unittest

from trace_interop.laws import evaluate, first_difference, tree_violations
from trace_interop.presentation import laws_page

SENDER = '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f'
TX = '0x' + '11' * 32
CALL = {'from': SENDER, 'to': '0x' + '22' * 20, 'gas': '0x927c0', 'gasPrice': '0x0', 'data': '0x'}


def frame(path, subtraces=0, gas='0x100', used='0x10', **extra):
    return {'type': 'call', 'action': {'callType': 'call', 'from': SENDER, 'gas': gas}, 'result': {'gasUsed': used, 'output': '0x'},
            'subtraces': subtraces, 'traceAddress': path, **extra}


def located(path, subtraces=0, **extra):
    return frame(path, subtraces, blockHash='0x' + 'aa' * 32, blockNumber=2, transactionHash=TX, transactionPosition=0, **extra)


def case(name, method, params):
    return {'name': name, 'request': {'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}}


def ok(value):
    return {'status': 'result', 'response': {'jsonrpc': '2.0', 'id': 1, 'result': value}}


CONTEXT = {'_blocks': {'0x2': {'number': 2, 'hash': '0x' + 'aa' * 32}}, '_head': {'number': '0x2'},
           'txinfo': {'_decoded': [{'txhash': TX, 'sender': SENDER, 'block': '0x2', 'indexInBlock': 0}]}}


def laws(cases, responses, context=CONTEXT, profile=True):
    return {(f['law'], f['holds']) for f in evaluate(context, cases, {c['name']: responses[c['name']] for c in cases}, profile=profile)}


class Laws(unittest.TestCase):
    def test_get_selects_requested_path(self):
        stored = [located([], 1), located([0], 1), located([0, 0])]
        tree = case('tree', 'trace_transaction', [TX])
        for selector, expected in [([], stored[0]), (['0x0'], stored[1]), (['0x0', '0x0'], stored[2]), (['0x1'], None)]:
            with self.subTest(selector=selector):
                get = case('get', 'trace_get', [TX, selector])
                self.assertIn(('L05', True), laws([tree, get], {'tree': ok(stored), 'get': ok(expected)}))
                wrong = stored[1] if not selector else stored[0]
                self.assertIn(('L05', False), laws([tree, get], {'tree': ok(stored), 'get': ok(wrong)}))
        get = case('get', 'trace_get', [TX, ['0x0']])
        self.assertIn(('L05', False), laws([tree, get], {'tree': ok(stored), 'get': ok(None)}))
        self.assertIn(('L05', False), laws([tree, get], {'tree': ok(stored), 'get': ok(dict(stored[1], subtraces=2))}))
        self.assertIn(('L05', True), laws([tree, get], {'tree': ok(stored), 'get': ok(stored[0])}, profile=False))
        self.assertNotIn('L05', {law for law, _ in laws([tree, get], {'tree': ok([]), 'get': ok(None)})})
        invalid = case('get', 'trace_get', [TX, [0]])
        self.assertIn(('L05', True), laws([tree, invalid], {'tree': ok(stored), 'get': ok(stored[0])}))

    def test_block_replay_preserves_transaction_identity(self):
        replay = case('replay', 'trace_replayTransaction', [TX, ['trace']])
        block = case('block', 'trace_replayBlockTransactions', ['0x2', ['trace']])
        envelope = {'output': '0x', 'trace': [frame([])], 'stateDiff': None, 'vmTrace': None}
        good = dict(envelope, transactionHash=TX)
        self.assertIn(('L08', True), laws([replay, block], {'replay': ok(envelope), 'block': ok([good])}))
        for bad in [[], [dict(good, transactionHash='0x' + '33' * 32)], [envelope], [dict(good, output='0x01')]]:
            with self.subTest(bad=bad):
                self.assertIn(('L08', False), laws([replay, block], {'replay': ok(envelope), 'block': ok(bad)}))
        self.assertIn(('L08', True), laws([replay, block], {'replay': ok(envelope), 'block': ok([envelope])}, profile=False))
        self.assertNotIn('L08', {law for law, _ in laws([replay, block], {'replay': ok(envelope), 'block': ok([])}, profile=False)})
        # Identity comes from the request, even when the single replay is also mislabeled.
        wrong = dict(good, transactionHash='0x' + '33' * 32)
        self.assertIn(('L08', False), laws([replay, block], {'replay': ok(wrong), 'block': ok([wrong])}))
        disjoint = case('block', 'trace_replayBlockTransactions', ['0x2', ['stateDiff']])
        unknown = case('block', 'trace_replayBlockTransactions', ['0x3', ['trace']])
        self.assertIn(('L08', False), laws([replay, disjoint], {'replay': ok(envelope), 'block': ok([])}))
        self.assertNotIn('L08', {law for law, _ in laws([replay, unknown], {'replay': ok(envelope), 'block': ok([])})})
        # A later transaction must occur at its own index, even if another envelope matches.
        later = copy.deepcopy(CONTEXT)
        later['txinfo']['_decoded'][0]['indexInBlock'] = 1
        self.assertIn(('L08', False), laws([replay, block], {'replay': ok(envelope), 'block': ok([good])}, later))
        self.assertIn(('L08', True), laws([replay, block], {'replay': ok(envelope), 'block': ok([wrong, good])}, later))

    def test_selector_and_identity_pairs_require_success_and_frozen_chain(self):
        tree, get = case('tree', 'trace_transaction', [TX]), case('get', 'trace_get', [TX, ['0x0']])
        replay, block = case('replay', 'trace_replayTransaction', [TX, ['trace']]), case('block', 'trace_replayBlockTransactions', ['0x2', ['trace']])
        envelope = {'output': '0x', 'trace': [frame([])]}
        error = {'status': 'rpc_error', 'response': {'error': {'code': -32000, 'message': 'unavailable'}}}
        wrapped = ok({'jsonrpc': '2.0', 'id': 1, 'error': {'code': -32000, 'message': 'unavailable'}})
        for cases, responses, code in [([tree, get], {'tree': ok([located([], 1), located([0])]), 'get': ok(located([]))}, 'L05'),
                                        ([replay, block], {'replay': ok(envelope), 'block': ok([])}, 'L08')]:
            for name in responses:
                for failure in [error, wrapped]:
                    self.assertNotIn(code, {law for law, _ in laws(cases, responses | {name: failure})})
            moving = dict(CONTEXT, _scenario_phases=['before', 'after'])
            self.assertNotIn(code, {law for law, _ in laws(cases, responses, moving)})

    def test_tree_shape(self):
        tree = [frame([], 1), frame([0])]
        self.assertEqual(tree_violations(tree), [])
        self.assertIn('[] reports 2 subtraces for 1 children', tree_violations([frame([], 2), frame([0])]))
        self.assertIn('records are not in preorder', tree_violations([frame([], 2), frame([1]), frame([0])]))
        # Besu's depth-limit CREATE: negative gas wrapped to an unsigned 64-bit value.
        wrapped = [frame([], 0, gas='0x1e2ad6', used='0xffffffffffff9cf3')]
        self.assertTrue(any('reports gasUsed' in p for p in tree_violations(wrapped)))

    def test_selection_is_a_projection(self):
        cases = [case('trace', 'trace_call', [CALL, ['trace'], 'latest']), case('state', 'trace_call', [CALL, ['stateDiff'], 'latest'])]
        trace = {'output': '0x2a', 'trace': [frame([])], 'stateDiff': None, 'vmTrace': None}
        state = {'output': '0x2a', 'trace': [], 'stateDiff': {}, 'vmTrace': None}
        self.assertIn(('L04', True), laws(cases, {'trace': ok(trace), 'state': ok(state)}))
        # Nethermind 2.0.0 loses the output when only stateDiff is selected.
        self.assertIn(('L04', False), laws(cases, {'trace': ok(trace), 'state': ok(dict(state, output=None))}))

    def test_error_leaves_pair_unevaluated(self):
        cases = [case('trace', 'trace_call', [CALL, ['trace'], 'latest']), case('state', 'trace_call', [CALL, ['stateDiff'], 'latest'])]
        trace = {'output': '0x2a', 'trace': [frame([])], 'stateDiff': None, 'vmTrace': None}
        # Besu wraps an error envelope in a successful result; it is not a result to compare.
        wrapped = ok({'jsonrpc': '2.0', 'id': 1, 'error': {'code': -32603, 'message': 'Internal error'}})
        self.assertNotIn('L04', {law for law, _ in laws(cases, {'trace': ok(trace), 'state': wrapped})})

    def test_stored_and_replayed_frames(self):
        cases = [case('stored', 'trace_transaction', [TX]), case('replay', 'trace_replayTransaction', [TX, ['trace']])]
        stored = [located([], 1), located([0])]
        replay = {'output': '0x', 'trace': [frame([], 1), frame([0])], 'stateDiff': None, 'vmTrace': None}
        self.assertIn(('L07', True), laws(cases, {'stored': ok(stored), 'replay': ok(replay)}))
        # Anvil's stored records keep a zero-value precompile frame its replay omits.
        extra = [located([], 2), located([0]), located([1])]
        self.assertIn(('L07', False), laws(cases, {'stored': ok(extra), 'replay': ok(replay)}))

    def test_bundle_item_is_a_call(self):
        call, many = case('call', 'trace_call', [CALL, ['trace'], '0x2']), case('many', 'trace_callMany', [[[CALL, ['trace']]], '0x2'])
        envelope = {'output': '0x', 'trace': [frame([])], 'stateDiff': None, 'vmTrace': None}
        self.assertIn(('L09', True), laws([call, many], {'call': ok(envelope), 'many': ok([envelope])}))
        self.assertIn(('L09', False), laws([call, many], {'call': ok(envelope), 'many': ok([dict(envelope, output='0x01')])}))
        # An omitted block defaults by policy (H31), so it pairs with nothing.
        omitted = case('many', 'trace_callMany', [[[CALL, ['trace']]]])
        self.assertNotIn('L09', {law for law, _ in laws([call, omitted], {'call': ok(envelope), 'many': ok([dict(envelope, output='0x01')])})})

    def test_filter_selects_block_records(self):
        block = case('block', 'trace_block', ['0x2'])
        records = [located([])]
        whole = case('filter', 'trace_filter', [{'fromBlock': '0x2', 'toBlock': '0x2'}])
        self.assertIn(('L10', True), laws([block, whole], {'block': ok(records), 'filter': ok(records)}))
        # Erigon 3.7.0 fabricates a reward the block trace does not have.
        reward = {'type': 'reward', 'action': {'author': SENDER, 'rewardType': 'block', 'value': '0x1'}, 'traceAddress': [], 'subtraces': 0}
        self.assertIn(('L10', False), laws([block, whole], {'block': ok(records), 'filter': ok(records + [reward])}))
        addressed = case('filter', 'trace_filter', [{'fromBlock': '0x2', 'toBlock': '0x2', 'fromAddress': [SENDER]}])
        self.assertIn(('L10', True), laws([block, addressed], {'block': ok(records), 'filter': ok([])}))

    def test_paging_slices_the_filter(self):
        spec = {'fromBlock': '0x2', 'toBlock': '0x2'}
        whole, page = case('whole', 'trace_filter', [spec]), case('page', 'trace_filter', [dict(spec, after=1, count=1)])
        records = [located([], 1), located([0])]
        self.assertIn(('L11', True), laws([whole, page], {'whole': ok(records), 'page': ok(records[1:])}))
        self.assertIn(('L11', False), laws([whole, page], {'whole': ok(records), 'page': ok(records[:1])}))
        # A negative count is invalid input, not a slice.
        negative = case('page', 'trace_filter', [dict(spec, count=-1)])
        self.assertNotIn('L11', {law for law, _ in laws([whole, negative], {'whole': ok(records), 'page': ok([])})})

    def test_equivalent_spellings(self):
        by_number, by_hash = case('number', 'trace_block', ['0x2']), case('hash', 'trace_block', ['0x' + 'aa' * 32])
        records = [located([])]
        self.assertIn(('L12', True), laws([by_number, by_hash], {'number': ok(records), 'hash': ok(records)}))
        self.assertIn(('L12', False), laws([by_number, by_hash], {'number': ok(records), 'hash': ok([])}))
        # A reorganizing scenario moves the chain between requests, so nothing pairs.
        moving = dict(CONTEXT, _scenario_phases=['before', 'after'])
        self.assertNotIn('L12', {law for law, _ in laws([by_number, by_hash], {'number': ok(records), 'hash': ok([])}, moving)})

    def test_vmtrace_idx_is_not_compared(self):
        vm = {'code': '0x00', 'ops': [{'idx': '0-0', 'pc': 0}]}
        self.assertIsNone(first_difference({'vmTrace': vm}, {'vmTrace': copy.deepcopy(vm) | {'ops': [{'idx': 0, 'pc': 0}]}}))
        self.assertIsNotNone(first_difference({'vmTrace': vm}, {'vmTrace': {'code': '0x00', 'ops': [{'idx': 0, 'pc': 1}]}}))

    def test_stale_note_fails(self):
        summary = {'laws': [{'id': 'L01', 'title': 'Tree shape', 'statement': ''}], 'counts': {}, 'violations': []}
        with self.assertRaises(ValueError):
            laws_page(summary, {'L01': {'besu_release': 'fixed'}}, str)


if __name__ == '__main__':
    unittest.main()

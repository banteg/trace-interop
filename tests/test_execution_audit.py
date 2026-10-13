"""Counterexamples from the 2026-10-14 harness audit of the execution models."""
import unittest
from copy import deepcopy

from eth_hash.auto import keccak
from test_execution_anchor_regressions import capture

from trace_interop.chain_model import load_chain
from trace_interop.cli import ROOT, read
from trace_interop.execution_models import assess, traced_refund, transactions


def checksum(address):
    digest = keccak(address[2:].encode()).hex()
    return '0x'+''.join(c.upper() if int(d, 16) >= 8 else c for c, d in zip(address[2:], digest))


def statuses(case, result, topics, topic=None):
    return [c['status'] for c in assess(case, {'status': 'result', 'response': {'result': result}}, {}, topics)
            if topic is None or c['topic'] == topic]


class Accounts:
    sender, target, miner = '0x'+'11'*20, '0x'+'ab'*20, '0x'+'cd'*20


class ValueTransferTests(Accounts, unittest.TestCase):
    """#4: settlement checks each account a plain transfer touches, not only the balance sum."""

    def transfer(self):
        case = {'name': 'transfer', 'context': {
                    '_head': {'number': '0x1'}, '_blocks': {'0x1': {'number': 1, 'base_fee': 1, 'miner': self.miner, 'transactions': []}},
                    '_alloc': {self.sender: {'balance': '0x1000000'}}, '_codes': {self.sender: '0x'}},
                'request': {'method': 'trace_call', 'params': [{'from': self.sender, 'to': self.target, 'gas': '0x5208', 'gasPrice': '0x2', 'value': '0x7'}, ['stateDiff'], 'latest']}}
        # 21000 gas at price 2 over base fee 1: tip 1/gas to the miner, 1/gas burned.
        diff = {self.sender: {'balance': {'*': {'from': hex(0x1000000), 'to': hex(0x1000000-7-2*21000)}}, 'nonce': {'*': {'from': '0x0', 'to': '0x1'}}, 'code': '=', 'storage': {}},
                self.target: {'balance': {'+': '0x7'}, 'nonce': {'+': '0x0'}, 'code': {'+': '0x'}, 'storage': {}},
                self.miner: {'balance': {'+': hex(21000)}, 'nonce': {'+': '0x0'}, 'code': {'+': '0x'}, 'storage': {}}}
        return case, {'stateDiff': diff}

    def test_plain_transfer_settles_per_account(self):
        case, result = self.transfer()
        self.assertEqual(statuses(case, result, {'H16'}), ['matches'])
        # The recipient credit moved back to the sender keeps the sum but not the transfer.
        moved = deepcopy(result)
        moved['stateDiff'][self.target]['balance'] = {'+': '0x0'}
        moved['stateDiff'][self.sender]['balance']['*']['to'] = hex(0x1000000-2*21000)
        self.assertEqual(statuses(case, moved, {'H16'}), ['change_needed'])
        # A fabricated offsetting change on an untouched account.
        other = deepcopy(result)
        other['stateDiff'][self.sender]['balance']['*']['to'] = hex(0x1000000-7-2*21000+5)
        other['stateDiff']['0x'+'22'*20] = {'balance': {'*': {'from': '0x10', 'to': '0xb'}}, 'nonce': '=', 'code': '=', 'storage': {}}
        self.assertEqual(statuses(case, other, {'H16'}), ['change_needed'])

    def test_replayed_transfer_cannot_move_the_credit_to_the_sender(self):
        _, _, case, observation, peers, _ = capture('initial', 'replay-transfer-stateDiff', 'reth_release')
        h16 = lambda obs: [c['status'] for c in assess(case, obs, peers, {'H16'})]
        self.assertEqual(h16(observation), ['matches'])
        tx, _, _ = transactions(case)[0]
        changed = deepcopy(observation)
        diff = changed['response']['result']['stateDiff']
        diff[tx['to']]['balance'] = '='
        pair = diff[tx['sender']]['balance']['*']
        pair['to'] = hex(int(pair['to'], 16)+tx['value'])
        self.assertEqual(h16(changed), ['change_needed'])


class EndpointExistenceTests(Accounts, unittest.TestCase):
    """#5: birth, survival and deletion markers on every field and slot."""
    dying = '0x'+'dd'*20

    def call(self):
        case = {'name': 'transfer', 'context': {'_alloc': {self.sender: {'balance': '0x100'}, self.dying: {'code': '0x6000ff'}},
                                                '_codes': {self.sender: '0x', self.dying: '0x6000ff'}},
                'request': {'method': 'trace_call', 'params': [{'from': self.sender, 'to': self.target, 'value': '0x1'}, ['stateDiff']]}}
        diff = {self.sender: {'balance': {'*': {'from': '0x100', 'to': '0xff'}}, 'nonce': {'*': {'from': '0x0', 'to': '0x1'}}, 'code': '=', 'storage': {}},
                self.target: {'balance': {'+': '0x1'}, 'nonce': {'+': '0x0'}, 'code': {'+': '0x'}, 'storage': {}}}
        return case, diff

    def h17(self, case, diff):
        return statuses(case, {'stateDiff': diff}, {'H17'})

    def test_markers(self):
        case, diff = self.call()
        self.assertEqual(self.h17(case, diff), ['matches'])
        word = lambda n: '0x'+f'{n:064x}'
        mutations = {
            'born null value': (self.target, 'balance', {'+': None}),
            'born non-hex value': (self.target, 'nonce', {'+': 123}),
            'born changed slot': (self.target, 'storage', {word(0): {'*': {'from': word(0), 'to': word(1)}}}),
            'born zero slot': (self.target, 'storage', {word(0): {'+': word(0)}}),
            'surviving sender deleted': (self.sender, None, {'balance': {'-': '0x100'}, 'nonce': {'-': '0x0'}, 'code': {'-': '0x'}, 'storage': {}}),
            'partial deletion': (self.sender, 'balance', {'-': '0x100'}),
            'missing field': (self.sender, 'code', None),
            'malformed change': (self.sender, 'nonce', {'*': {'from': '0x0'}}),
            'created slot on existing account': (self.sender, 'storage', {word(0): {'+': word(1)}}),
        }
        for label, (address, field, value) in mutations.items():
            with self.subTest(label):
                changed = deepcopy(diff)
                if field is None:
                    changed[address] = value
                elif value is None:
                    del changed[address][field]
                else:
                    changed[address][field] = value
                self.assertEqual(self.h17(case, changed), ['change_needed'])
        # A born account's nonzero slots are created; an account with code may still die (H26 judges it).
        born = deepcopy(diff)
        born[self.target]['storage'] = {word(0): {'+': word(1)}}
        born[self.dying] = {'balance': {'-': '0x0'}, 'nonce': {'-': '0x0'}, 'code': {'-': '0x6000ff'}, 'storage': {}}
        self.assertEqual(self.h17(case, born), ['matches'])
        # An omitted storage member lists no slots; the schema judges the member.
        del born[self.target]['storage']
        self.assertEqual(self.h17(case, born), ['matches'])


class NullMemberTests(Accounts, unittest.TestCase):
    """#14: an explicit null call member is omitted (H14)."""
    null = dict.fromkeys(['from', 'value', 'data', 'gasPrice', 'maxFeePerGas', 'maxPriorityFeePerGas', 'nonce', 'gas'])

    def case(self, method, call):
        params = [call, ['stateDiff', 'vmTrace']] if method == 'trace_call' else [[[call, ['stateDiff', 'vmTrace']]], 'latest']
        return {'name': 'null', 'context': {'_alloc': {self.target: {'code': '0x00'}}, '_codes': {self.target: '0x00'}},
                'request': {'method': method, 'params': params}}

    def test_null_members_model_like_omitted_ones(self):
        for method in ['trace_call', 'trace_callMany']:
            with self.subTest(method):
                omitted = transactions(self.case(method, {'to': self.target, 'input': '0x01'}))
                self.assertEqual(transactions(self.case(method, dict(self.null, to=self.target, input='0x01'))), omitted)
                self.assertEqual(omitted[0][0]['data'], '0x01')
                result = {'stateDiff': {}, 'vmTrace': {'code': '0x00', 'ops': []}}
                checks = assess(self.case(method, dict(self.null, to=self.target)), {'status': 'result', 'response': {'result': result if method == 'trace_call' else [result]}},
                                {}, {'H16', 'H17', 'H19', 'H20'})
                self.assertEqual({c['topic']: c['status'] for c in checks}.get('H19'), 'matches')

    def test_unmodelled_call_members_leave_the_bundle_unmodelled(self):
        for call in [{'from': 7, 'to': self.target}, {'to': self.target, 'value': 'oops'}, {'to': self.target, 'data': 5}]:
            with self.subTest(call):
                self.assertEqual(transactions(self.case('trace_call', call)), [])
                self.assertEqual(transactions(self.case('trace_callMany', call)), [])


class TracedRefundTests(unittest.TestCase):
    """#15: a malformed state diff or call frame leaves the traced refund unknown."""
    root, child = '0x'+'aa'*20, '0x'+'bb'*20

    def tree(self):
        clear = {'code': '0x600060055500', 'ops': [{'pc': 4, 'cost': 2900, 'ex': {'used': 0, 'push': [], 'mem': None,
                                                                                   'store': {'key': '0x5', 'val': '0x0'}}, 'sub': None}]}
        vm = {'code': '0x6000600060006000600073'+self.child[2:]+'5af1', 'ops': [{'pc': 32, 'cost': 100, 'ex': {'used': 0, 'push': ['0x1'], 'mem': None, 'store': None}, 'sub': clear}]}
        frames = [{'type': 'call', 'traceAddress': [], 'action': {'callType': 'call', 'to': self.root}},
                  {'type': 'call', 'traceAddress': [0], 'action': {'callType': 'call', 'to': self.child}}]
        return vm, frames, {self.child: clear['code']}

    def test_malformed_inputs_are_unknown(self):
        vm, frames, codes = self.tree()
        slot = '0x'+'05'.rjust(64, '0')
        self.assertEqual(traced_refund(vm, frames, {self.child: {'storage': {slot: {'*': {'from': '0x5', 'to': '0x0'}}}}}, codes), 4800)
        for storage in [{'0xzz': {'*': {'from': '0x5', 'to': '0x0'}}}, {slot: {'-': 'not_hex'}}, {slot: {'*': {'from': 123}}}, {slot: {'*': 'x'}}]:
            with self.subTest(storage):
                self.assertIsNone(traced_refund(vm, frames, {self.child: {'storage': storage}}, codes))
        nested = deepcopy(frames)+[{'type': 'call', 'traceAddress': [[0], 0], 'action': {'callType': 'call', 'to': self.child}}]
        self.assertIsNone(traced_refund(vm, nested, {}, codes))


class ChecksumAddressTests(Accounts, unittest.TestCase):
    """#19: state-diff and request addresses match case-insensitively."""

    def test_checksummed_miner_settles(self):
        case, result = ValueTransferTests.transfer(self)
        diff = result['stateDiff']
        diff[checksum(self.miner)] = diff.pop(self.miner)
        self.assertEqual(statuses(case, result, {'H16'}), ['matches'])

    def test_checksummed_authority_delegates(self):
        blocks = load_chain(ROOT/'fixtures/chains/initial/chain.rlp')
        genesis = read(ROOT/'fixtures/chains/initial/genesis.json')
        tx = blocks['0x2']['transactions'][3]
        auth = tx['authorizations'][0]
        case = {'name': 'replay', 'request': {'method': 'trace_replayTransaction', 'params': [tx['hash'], ['stateDiff']]},
                'context': {'_blocks': blocks, '_chain_id': genesis['config']['chainId'],
                            '_alloc': {'0x'+a: v for a, v in genesis['alloc'].items()},
                            '_codes': {'0x'+a: v.get('code', '0x') for a, v in genesis['alloc'].items()}}}
        self.assertNotEqual(checksum(auth['authority']), auth['authority'])
        diff = {checksum(auth['authority']): {'code': {'*': {'from': '0x', 'to': '0xef0100'+auth['address'][2:]}}, 'nonce': {'*': {'from': '0x0', 'to': '0x1'}}}}
        self.assertEqual(statuses(case, {'stateDiff': diff}, {'H18'}), ['matches'])

    def test_checksummed_call_target_runs_its_code(self):
        case = {'name': 'call', 'context': {'_alloc': {self.target: {'code': '0x00'}}, '_codes': {self.target: '0x00'}},
                'request': {'method': 'trace_call', 'params': [{'to': checksum(self.target)}, ['vmTrace']]}}
        self.assertEqual(statuses(case, {'vmTrace': {'code': '0x00', 'ops': []}}, {'H19'}), ['matches'])


if __name__ == '__main__':
    unittest.main()

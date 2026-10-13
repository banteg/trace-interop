"""Counterexamples from the 2026-10-14 harness audit (docs/reviews/2026-10-14-harness-bugs.md)
for the corpus probes and the mined-probes assertions: each wrong response needs a change, never passes or crashes."""
import copy
import unittest

import test_probes
from test_mined_probes import CASES as MINED
from test_mined_probes import CORPUS, ideal, receipts
from test_probes import FORKS, H30, result

from trace_interop.cli import ROOT
from trace_interop.coverage import supplement
from trace_interop.probes import assess
from trace_interop.report import run_context


def topic_statuses(case, observation, topic, peers=None):
    return {c['status'] for c in assess(case, observation, peers or {}) if c['topic'] == topic}


class VMTrailingOpTests(unittest.TestCase):
    """#6: push and store judge the whole root operation list, not its modelled prefix."""
    def vm(self, name):
        return test_probes.VMProbeTests.vm(self, name)

    def test_extra_operations_after_the_modelled_program_differ(self):
        case, envelope = self.vm('vm-push-order')
        dup = next(op for op in envelope['vmTrace']['ops'] if len(op['ex']['push']) > 1)
        wrong = copy.deepcopy(envelope)
        wrong['vmTrace']['ops'].append(dict(copy.deepcopy(dup), ex=dict(dup['ex'], push=['0xbad'])))
        self.assertEqual(topic_statuses(case, result(wrong), 'H20'), {'change_needed'})
        for name in ['vm-store', 'vm-store-vm-only']:
            case, envelope = self.vm(name)
            store = next(op for op in envelope['vmTrace']['ops'] if op['ex']['store'])
            wrong = copy.deepcopy(envelope)
            wrong['vmTrace']['ops'].append(dict(copy.deepcopy(store), ex=dict(store['ex'], store={'key': '0x9', 'val': '0x9'})))
            self.assertEqual(topic_statuses(case, result(wrong), 'H20'), {'change_needed'}, name)


class DeletedStorageTests(unittest.TestCase):
    """#7 is not a bug: deletion wipes all storage and listed - entries are no enumeration (spec, H26 ledger)."""

    def test_a_partial_accurate_listing_matches(self):
        case = FORKS['many-write-delete-storage']
        account = dict(copy.deepcopy(case['probes'][0]['expected']), storage={'0x'+f'{1:064x}': {'-': '0x'+'00'*32}})
        self.assertEqual(topic_statuses(case, result([{}, {}, {'stateDiff': {case['probes'][0]['address']: account}}]), 'H26'), {'matches'})


class DepthParentTests(unittest.TestCase):
    """#8: the failed attempts must be children of the deepest executed frame."""

    def test_attempts_elsewhere_at_the_attempt_depth_differ(self):
        envelope = test_probes.DepthProbeTests.trace(None)
        for frame, prefix in zip(envelope['trace'][-2:], [999, 888]):
            frame['traceAddress'] = [prefix]*len(frame['traceAddress'])
        case = FORKS['depth-limit']
        self.assertEqual(topic_statuses(case, result(envelope), 'H29'), {'change_needed'})
        self.assertEqual(topic_statuses(case, result(envelope), 'H09'), {'blocked'})


class BlockHashMalformedTests(unittest.TestCase):
    """#16: unhashable record locations are a difference, not a TypeError."""

    def test_unhashable_block_fields_differ(self):
        case = dict(H30['filter-blockhash'], context={'_head': {'number': '0x30'}})
        digest = case['request']['params'][0]['blockHash']
        twin = {'filter-block-2': result([{'type': 'call', 'blockNumber': 2, 'blockHash': digest, 'traceAddress': []}])}
        for number, block in [([], digest), (2, {}), ({}, [])]:
            with self.subTest(number=number, block=block):
                records = [{'type': 'call', 'blockNumber': number, 'blockHash': block, 'traceAddress': []}]
                self.assertEqual(topic_statuses(case, result(records), 'H33', twin), {'change_needed'})


class MinedBlockLayoutTests(unittest.TestCase):
    """#9: trace_block is each transaction's frames, contiguous and in block order, then any reward records."""

    @classmethod
    def setUpClass(cls):
        cls.context = run_context(ROOT, {'corpus': 'mined-probes'})
        cls.context['cases'] = list(MINED.values())

    def statuses(self, name, frames):
        case = dict(MINED[name], context=self.context)
        checks = supplement(case, {'status': 'result', 'response': {'result': frames}}, receipts(), [], case['topics'])
        return {c['status'] for c in checks if c['topic'] in case['topics']}

    def frames(self, number):
        block = self.context['_blocks'][hex(number)]
        return [dict(f, transactionHash=t['hash']) for t in block['transactions'] for f in ideal(self.context, t['hash'])['trace']]

    def test_order_extras_and_non_objects_differ(self):
        for number in [3, 4, 5]:
            name, frames = f'block-{number}', self.frames(number)
            self.assertEqual(self.statuses(name, frames), {'matches'}, name)
            reward = {'type': 'reward', 'transactionHash': None, 'traceAddress': [], 'subtraces': 0,
                      'action': {'author': '0x'+'00'*20, 'rewardType': 'block', 'value': '0x0'}}
            self.assertEqual(self.statuses(name, frames+[reward]), {'matches'}, name)  # H05 judges rewards
            hashes = [t['hash'] for t in self.context['_blocks'][hex(number)]['transactions']]
            for wrong in [[f for h in reversed(hashes) for f in frames if f['transactionHash'] == h],
                          frames+[dict(frames[0], transactionHash='0x'+'ab'*32)],
                          frames+[dict(frames[0])],
                          frames+[None], [None]+frames, frames[:1]+[None]+frames[1:],
                          frames+[dict(reward, transactionHash=hashes[0])], [reward]+frames]:
                with self.subTest(name=name, wrong=[f and f['transactionHash'] for f in wrong]):
                    self.assertIn('change_needed', self.statuses(name, wrong))

    def test_replay_frames_are_objects(self):
        txhash = MINED['transaction-create-revert']['request']['params'][0]
        role = CORPUS['probes'][txhash]['role']
        envelope = ideal(self.context, txhash)
        self.assertEqual(self.statuses('replay-'+role, envelope), {'matches'})
        envelope['trace'].append(None)
        self.assertIn('change_needed', self.statuses('replay-'+role, envelope))

    def test_trace_transaction_frames_all_belong_to_it(self):
        name = 'transaction-create-revert'
        txhash = MINED[name]['request']['params'][0]
        frames = [dict(f, transactionHash=txhash) for f in ideal(self.context, txhash)['trace']]
        self.assertEqual(self.statuses(name, frames), {'matches'})
        for wrong in [frames+[None], frames+[dict(frames[0], transactionHash='0x'+'ab'*32)]]:
            self.assertIn('change_needed', self.statuses(name, wrong))


if __name__ == '__main__':
    unittest.main()

"""Check hand-derived oracle constants against the frozen fixture programs."""
import unittest

from trace_interop.cli import ROOT, read
from trace_interop.oracles import CHILD_INIT, REVERT, REVERT_GAS, REVERT_OUTPUT, TREE


class FixtureOracles(unittest.TestCase):
    def test_revert_branch_bytes_and_gas(self):
        # A bounded interpreter for this one straight-line/JUMPI fixture. Any
        # new opcode fails closed instead of silently accepting a new program.
        genesis = read(ROOT/'fixtures/chains/initial/genesis.json')
        code = bytes.fromhex(genesis['alloc'][REVERT[2:]]['code'][2:])
        stack, memory, pc, gas = [], bytearray(), 0, 0
        for _ in range(100):
            op = code[pc]; pc += 1
            if 0x60 <= op <= 0x7f:
                size = op-0x5f; stack.append(int.from_bytes(code[pc:pc+size], 'big')); pc += size; gas += 3
            elif op == 0x35:  # CALLDATALOAD with the frozen tx input 0x01
                offset = stack.pop(); stack.append(int.from_bytes((b'\x01'[offset:offset+32]).ljust(32,b'\0'),'big')); gas += 3
            elif op == 0x54:  # The only storage access is cold and its value is discarded.
                self.assertEqual(stack.pop(), 0x42ff); stack.append(0); gas += 2100
            elif op == 0x50:
                stack.pop(); gas += 2
            elif op == 0x15:
                stack.append(int(stack.pop() == 0)); gas += 3
            elif op == 0x57:
                target, condition = stack.pop(), stack.pop()
                if condition: pc = target
                gas += 10
            elif op == 0x5b:
                gas += 1
            elif op == 0x52:
                offset, value = stack.pop(), stack.pop()
                old = len(memory)//32; new = max(old,(offset+32+31)//32)
                gas += 3 + 3*(new-old) + new*new//512 - old*old//512
                memory.extend(b'\0'*(32*new-len(memory)))
                memory[offset:offset+32] = value.to_bytes(32,'big')
            elif op == 0xfd:
                offset, size = stack.pop(), stack.pop()
                self.assertEqual('0x'+memory[offset:offset+size].hex(), REVERT_OUTPUT)
                self.assertEqual(hex(gas), REVERT_GAS)
                return
            else:
                self.fail(f'Unexpected fixture opcode {op:#x}')
        self.fail('Fixture did not revert within the bounded program')

    def test_tree_child_program_and_sibling_revert_fixture(self):
        for chain in ['initial','a','forks']:
            alloc = read(ROOT/f'fixtures/chains/{chain}/genesis.json')['alloc']
            self.assertTrue(alloc[TREE[2:]]['code'].endswith(CHILD_INIT[2:]))
        corpus = read(ROOT/'fixtures/corpora/a.json')
        self.assertEqual(corpus['contracts']['revert']['code'], '60006000fd')
        # PUSH1 0, PUSH1 0, REVERT: empty bytes, six gas, no memory expansion.

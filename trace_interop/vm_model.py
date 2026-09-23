"""Bounded, independent straight-line Prague EVM model for trace discriminators.

No client response is an input. Unsupported programs fail closed. This is not a
general EVM: calls, jumps, storage and exceptional halts need separate fixtures.
"""

NAMES = {0: 'STOP', 1: 'ADD', 0x30: 'ADDRESS', 0x34: 'CALLVALUE',
         0x35: 'CALLDATALOAD', 0x36: 'CALLDATASIZE', 0x37: 'CALLDATACOPY',
         0x38: 'CODESIZE', 0x39: 'CODECOPY', 0x3a: 'GASPRICE',
         0x41: 'COINBASE', 0x42: 'TIMESTAMP', 0x43: 'NUMBER', 0x45: 'GASLIMIT',
         0x48: 'BASEFEE', 0x50: 'POP', 0x51: 'MLOAD', 0x52: 'MSTORE',
         0x53: 'MSTORE8', 0x58: 'PC', 0x59: 'MSIZE', 0x5a: 'GAS',
         0x5e: 'MCOPY', 0x5f: 'PUSH0', 0xf3: 'RETURN', 0xfd: 'REVERT'}
NAMES.update({i: 'PUSH'+str(i-0x5f) for i in range(0x60, 0x80)})
NAMES.update({i: 'DUP'+str(i-0x7f) for i in range(0x80, 0x90)})
NAMES.update({i: 'SWAP'+str(i-0x8f) for i in range(0x90, 0xa0)})
NAMES.update({0x14:'EQ',0x15:'ISZERO',0x1c:'SHR',0x33:'CALLER',0x32:'ORIGIN',
              0x44:'PREVRANDAO',0x46:'CHAINID',0x54:'SLOAD',0x55:'SSTORE',
              0x56:'JUMP',0x57:'JUMPI',0x5b:'JUMPDEST',0xa0:'LOG0',0xa1:'LOG1',
              0xf0:'CREATE',0xf1:'CALL',0xf2:'CALLCODE',0xf4:'DELEGATECALL',0xf5:'CREATE2',0xfa:'STATICCALL',0xff:'SELFDESTRUCT',3:'SUB'})


class UnsupportedProgram(ValueError):
    pass


def intrinsic(data, creation=False):
    raw = bytes.fromhex(data.removeprefix('0x'))
    return 21000 + sum(4 if b == 0 else 16 for b in raw) + (32000 + 2*((len(raw)+31)//32) if creation else 0)


def execute(code, gas, calldata='0x', environment=None):
    raw = bytes.fromhex(code.removeprefix('0x'))
    data = bytes.fromhex(calldata.removeprefix('0x'))
    env = dict(environment or {})
    stack, memory, steps = [], bytearray(), []
    pc, output, reverted = 0, '0x', False
    jumpdests=set()
    cursor=0
    while cursor<len(raw):
        op=raw[cursor]
        if op==0x5b:jumpdests.add(cursor)
        cursor+=1+(op-0x5f if 0x60<=op<=0x7f else 0)

    def expand(offset, size):
        if not size:
            return 0
        end = offset + size
        if end > 65536:
            raise UnsupportedProgram('model memory bound exceeded')
        old, new = len(memory)//32, max(len(memory)//32, (end+31)//32)
        memory.extend(bytes(32*new-len(memory)))
        return 3*(new-old) + new*new//512 - old*old//512

    try:
        while pc < len(raw):
            if len(steps) >= 1024:
                raise UnsupportedProgram('model step bound exceeded')
            at, op = pc, raw[pc]
            pc += 1
            cost, push, mem = 0, [], None
            if 0x60 <= op <= 0x7f:
                size = op-0x5f
                value = int.from_bytes(raw[pc:pc+size].ljust(size, b'\0'), 'big')
                pc += size
                cost, push = 3, [value]
                stack.append(value)
            elif op == 0x5f:
                cost, push = 2, [0]
                stack.append(0)
            elif 0x80 <= op <= 0x8f:
                value = stack[-(op-0x7f)]
                stack.append(value)
                cost, push = 3, stack[-(op-0x7f+1):]
            elif 0x90 <= op <= 0x9f:
                depth = op-0x8f
                stack[-1], stack[-1-depth] = stack[-1-depth], stack[-1]
                cost, push = 3, stack[-1-depth:]
            elif op == 1:
                value = (stack.pop()+stack.pop()) % (1 << 256)
                stack.append(value)
                cost, push = 3, [value]
            elif op in [0x14,0x15,0x1c,3]:
                a=stack.pop()
                value=int(a==0) if op==0x15 else int(a==stack.pop()) if op==0x14 else stack.pop()>>a if op==0x1c else (a-stack.pop())%(1<<256)
                stack.append(value)
                cost,push=3,[value]
            elif op in [0x56,0x57]:
                target=stack.pop()
                condition=stack.pop() if op==0x57 else 1
                cost=10 if op==0x57 else 8
                if condition:
                    if target not in jumpdests:
                        raise UnsupportedProgram('invalid jump destination')
                    pc=target
            elif op==0x5b:
                cost=1
            elif op==0x54:
                slot=stack.pop()
                storage=env.get('STORAGE',{})
                if slot not in storage:
                    raise UnsupportedProgram('unanchored storage read')
                warm=env.setdefault('_warm_slots',set())
                cost=100 if slot in warm else 2100
                warm.add(slot)
                stack.append(storage[slot]);push=[storage[slot]]
            elif op == 0x50:
                stack.pop()
                cost = 2
            elif op in [0x51, 0x52, 0x53]:
                offset = stack.pop()
                size = 1 if op == 0x53 else 32
                cost = 3 + expand(offset, size)
                if op == 0x51:
                    value = int.from_bytes(memory[offset:offset+size], 'big')
                    stack.append(value)
                    push = [value]
                else:
                    value = stack.pop() % (1 << (size*8))
                    memory[offset:offset+size] = value.to_bytes(size, 'big')
                    mem = {'off': offset, 'data': '0x'+memory[offset:offset+size].hex()}
            elif op in [0x37, 0x39, 0x5e]:
                dest, source, size = stack.pop(), stack.pop(), stack.pop()
                cost = 3 + 3*((size+31)//32) + expand(dest, size)
                if op == 0x5e:
                    cost += expand(source, size)
                origin = memory if op == 0x5e else raw if op == 0x39 else data
                value = bytes(origin[source:source+size]).ljust(size, b'\0')
                if size:
                    memory[dest:dest+size] = value
                    mem = {'off': dest, 'data': '0x'+value.hex()}
            elif op == 0x35:
                offset = stack.pop()
                value = int.from_bytes(data[offset:offset+32].ljust(32, b'\0'), 'big')
                stack.append(value)
                cost, push = 3, [value]
            elif op in [0x36, 0x38, 0x58, 0x59, 0x5a]:
                cost = 2
                value = {0x36: len(data), 0x38: len(raw), 0x58: at, 0x59: len(memory), 0x5a: gas-cost}[op]
                stack.append(value)
                push = [value]
            elif op in [0x30, 0x32, 0x33, 0x34, 0x3a, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x48]:
                key = NAMES[op]
                if key not in env:
                    raise UnsupportedProgram('unanchored environment: '+key)
                cost, push = 2, [env[key]]
                stack.append(env[key])
            elif op in [0xf3, 0xfd]:
                offset, size = stack.pop(), stack.pop()
                cost = expand(offset, size)
                output = '0x'+memory[offset:offset+size].hex()
                reverted = op == 0xfd
            elif op != 0:
                raise UnsupportedProgram(f'unmodelled opcode {op:#x}')
            if gas < cost:
                raise UnsupportedProgram('exceptional halt requires an OOG model')
            gas -= cost
            steps.append({'pc': at, 'cost': cost, 'op': NAMES[op], 'sub': None,
                          'ex': {'used': gas, 'push': [hex(v) for v in push], 'mem': mem, 'store': None}})
            if op in [0, 0xf3, 0xfd]:
                break
    except (IndexError, OverflowError) as exc:
        raise UnsupportedProgram('invalid model program') from exc
    return {'code': code, 'ops': steps}, output, reverted


def differences(actual, expected):
    """Compare mandatory semantics and optional mnemonics, never optional idx."""
    if not isinstance(actual, dict) or not isinstance(actual.get('ops'), list):
        return ['missing VM execution']
    errors = []
    if len(actual['ops']) != len(expected['ops']):
        errors.append(f'operation count {len(actual["ops"])} != {len(expected["ops"])}')
    for i, (got, want) in enumerate(zip(actual['ops'], expected['ops'])):
        if not isinstance(got, dict):
            errors.append(f'step {i} is not an object')
            continue
        for key in ['pc', 'cost', 'sub']:
            if got.get(key) != want[key] or key in ['pc','cost'] and type(got.get(key)) is not int:
                errors.append(f'step {i} ({want["op"]}) {key}: expected {want[key]}, got {got.get(key)}')
        ex=got.get('ex')
        if not isinstance(ex,dict):
            errors.append(f'step {i} execution effects missing')
        else:
            for key in ['used','mem','store']:
                if ex.get(key)!=want['ex'][key] or key=='used' and type(ex.get(key)) is not int:
                    errors.append(f'step {i} ({want["op"]}) {key}: expected {want["ex"][key]}, got {ex.get(key)}')
            # Numeric equality belongs to execution semantics; minimal wire
            # encoding is independently checked by H21.
            try:
                valid=isinstance(ex.get('push'),list) and [int(v,16) for v in ex['push']]==[int(v,16) for v in want['ex']['push']]
            except (ValueError,TypeError):
                valid=False
            if not valid:errors.append(f'step {i} pushed stack values disagree with the model')
        if 'op' in got and got['op'] != want['op'] and {got['op'],want['op']} != {'DIFFICULTY','PREVRANDAO'}:
            errors.append(f'step {i} mnemonic disagrees with executing bytecode')
    return errors


def local_invariants(vm):
    """Check mandatory local step relations even in programs containing calls.

Nested CALL/CREATE gas accounting remains explicitly outside this relation;
every other consecutive step must deduct its recorded operation cost. Dedicated
models additionally derive costs and effects independently of recorded values.
"""
    errors=[]
    if not isinstance(vm,dict) or not isinstance(vm.get('ops'),list):
        return ['VM operations missing']
    try:
        code=bytes.fromhex(vm.get('code','0x')[2:])
    except (ValueError,TypeError):
        return ['VM bytecode malformed']
    if code and not vm['ops']:
        return ['nonempty executing bytecode has no operations']
    previous=None
    fallthrough=0
    for i,op in enumerate(vm['ops']):
        if not isinstance(op,dict):
            errors.append(f'operation {i} malformed');continue
        pc=op.get('pc');ex=op.get('ex')
        if type(pc) is not int or pc<0 or pc>=len(code) and pc!=fallthrough:
            errors.append(f'operation {i} pc outside executing bytecode');continue
        opcode=code[pc] if pc<len(code) else 0  # EVM's implicit STOP past code end.
        fallthrough=pc+1+(opcode-0x5f if 0x60<=opcode<=0x7f else 0)
        if 'op' in op and opcode in NAMES and op['op']!=NAMES[opcode] and not (opcode==0x44 and op['op']=='DIFFICULTY'):
            errors.append(f'operation {i} mnemonic disagrees with bytecode')
        if isinstance(ex,dict):
            used,cost=ex.get('used'),op.get('cost')
            if type(used) is not int or type(cost) is not int or used<0 or cost<0:
                errors.append(f'operation {i} gas is not a nonnegative integer')
            elif previous is not None and opcode not in [0xf0,0xf1,0xf2,0xf4,0xf5,0xfa] and used!=previous-cost:
                errors.append(f'operation {i} post-step gas does not deduct this operation cost')
            if 0x60<=opcode<=0x7f:
                size=opcode-0x5f
                want=int.from_bytes(code[pc+1:pc+1+size].ljust(size,b'\0'),'big')
                push=ex.get('push')
                try: valid=isinstance(push,list) and len(push)==1 and int(push[0],16)==want
                except (ValueError,TypeError):valid=False
                if not valid:errors.append(f'operation {i} PUSH value disagrees with bytecode')
            # Memory reads/RETURN are not writes, irrespective of expansion.
            if opcode in [0x51,0xf3,0xfd] and ex.get('mem') is not None:
                errors.append(f'operation {i} reports a memory write for a read/return')
            previous=used if type(used) is int else None
        else:
            previous=None
        if op.get('sub') is not None:
            errors.extend(f'subtrace {i}: '+e for e in local_invariants(op['sub']))
    return errors

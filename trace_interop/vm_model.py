"""Bounded, independent straight-line Prague EVM model for trace discriminators.

No client response is an input. Unsupported programs fail closed. This is not a
general EVM: calls, creations and exceptional halts need separate fixtures, and
storage is modelled only for anchored slots or a fresh (just-created) account.
"""
import re


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
              0x44:'PREVRANDAO',0x46:'CHAINID',0x54:'SLOAD',0x55:'SSTORE',0x5c:'TLOAD',0x5d:'TSTORE',
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

    # STORAGE anchors known slots; a fresh account (a creation's own address)
    # has only zero slots. Writes are tracked on top of the original values.
    written, transient = {}, {}

    def original_value(slot):
        storage=env.get('STORAGE',{})
        if slot in storage:
            return storage[slot]
        if env.get('FRESH_ACCOUNT'):
            return 0
        raise UnsupportedProgram('unanchored storage read')

    def slot_value(slot):
        return written[slot] if slot in written else original_value(slot)

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
            cost, push, mem, store = 0, [], None, None
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
            elif op in [0x54,0x55]:
                slot=stack.pop()
                current=slot_value(slot)
                warm=env.setdefault('_warm_slots',set())
                cold=0 if slot in warm else 2100
                warm.add(slot)
                if op==0x54:
                    cost=cold or 100
                    stack.append(current);push=[current]
                else:
                    value=stack.pop()
                    if gas<=2300:
                        raise UnsupportedProgram('exceptional halt requires an OOG model')
                    original=original_value(slot)
                    # EIP-2200 with EIP-2929 cold surcharges; refunds do not change cost.
                    cost=cold+(100 if current==value or original!=current else 20000 if original==0 else 2900)
                    written[slot]=value
                    store={'key':hex(slot),'val':hex(value)}
            elif op in [0x5c,0x5d]:
                slot=stack.pop()
                cost=100
                if op==0x5c:
                    value=transient.get(slot,0)
                    stack.append(value);push=[value]
                else:
                    transient[slot]=stack.pop()
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
                # Post-operation contents of the operand range, for reads too.
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
                          'ex': {'used': gas, 'push': [hex(v) for v in push], 'mem': mem, 'store': store}})
            if op in [0, 0xf3, 0xfd]:
                break
    except (IndexError, OverflowError) as exc:
        raise UnsupportedProgram('invalid model program') from exc
    return {'code': code, 'ops': steps}, output, reverted


def store_words(store):
    """Numeric (key, val) of a store delta; None when absent or malformed. H21 owns its encoding."""
    try:
        return (int(store['key'],16),int(store['val'],16)) if isinstance(store,dict) else None
    except (KeyError,ValueError,TypeError):
        return None


def stack_window(opcode, stack):
    """Expected push of DUPn/SWAPn from the stack before it: the top n+1 words after execution, deepest first."""
    n=opcode-0x7f if opcode<0x90 else opcode-0x8f
    if len(stack)<n+(opcode>=0x90):
        return None
    if opcode<0x90:
        return stack[len(stack)-n:]+[stack[-n]]
    window=stack[len(stack)-n-1:]
    return [window[-1]]+window[1:-1]+[window[0]]


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
            for key in ['used','mem']:
                if ex.get(key)!=want['ex'][key] or key=='used' and type(ex.get(key)) is not int:
                    errors.append(f'step {i} ({want["op"]}) {key}: expected {want["ex"][key]}, got {ex.get(key)}')
            if store_words(ex.get('store'))!=store_words(want['ex']['store']) or ex.get('store') is not None and store_words(ex['store']) is None:
                errors.append(f'step {i} ({want["op"]}) store: expected {want["ex"]["store"]}, got {ex.get("store")}')
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


CALLS = [0xf1, 0xf2, 0xf4, 0xfa]
CREATES = [0xf0, 0xf5]
TERMINAL = [0x00, 0xf3, 0xfd, 0xff]
# Stack words each opcode consumes; its ex.push replaces them (DUPn: n in, n+1 out).
INPUTS = {**dict.fromkeys([0x00, 0x30, 0x32, 0x33, 0x34, 0x36, 0x38, 0x3a, 0x3d, *range(0x41, 0x49), 0x4a,
                           0x58, 0x59, 0x5a, 0x5b, *range(0x5f, 0x80), 0xfe], 0),
          **dict.fromkeys([0x15, 0x19, 0x31, 0x35, 0x3b, 0x3f, 0x40, 0x49, 0x50, 0x51, 0x54, 0x56, 0x5c, 0xff], 1),
          **dict.fromkeys([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x0a, 0x0b, 0x10, 0x11, 0x12, 0x13, 0x14, 0x16,
                           0x17, 0x18, 0x1a, 0x1b, 0x1c, 0x1d, 0x20, 0x52, 0x53, 0x55, 0x57, 0x5d, 0xf3, 0xfd], 2),
          **dict.fromkeys([0x08, 0x09, 0x37, 0x39, 0x3e, 0x5e, 0xf0], 3),
          0x3c: 4, 0xf5: 4, 0xf1: 7, 0xf2: 7, 0xf4: 6, 0xfa: 6,
          **{op: op-0x7f for op in range(0x80, 0x90)}, **{op: op-0x8e for op in range(0x90, 0xa0)},
          **{op: op-0x9e for op in range(0xa0, 0xa5)}}


def words(push):
    try:
        return [int(v, 16) for v in push] if isinstance(push, list) else None
    except (ValueError, TypeError):
        return None


def returned(sub):
    """Whether a child frame's last operation is RETURN."""
    last = sub['ops'][-1]
    try:
        return isinstance(last, dict) and bytes.fromhex(sub['code'][2:])[last['pc']] == 0xf3
    except (ValueError, TypeError, KeyError, IndexError):
        return False


def leftover(sub):
    """Gas a child returns: its last operation's used if it ended normally, else 0."""
    last = sub['ops'][-1]
    ex = last.get('ex') if isinstance(last, dict) else None
    try:
        code = bytes.fromhex(sub['code'][2:])
        pc = last['pc']
    except (ValueError, TypeError, KeyError):
        return 0
    # Running off the code end stops normally; a synthetic STOP there is reported
    # separately by the child's own pc check.
    opcode = code[pc] if type(pc) is int and 0 <= pc < len(code) else 0
    size = 1+(opcode-0x5f if 0x60 <= opcode <= 0x7f else 0)
    ended = opcode in TERMINAL or pc+size >= len(code)
    return ex['used'] if isinstance(ex, dict) and ended and type(ex.get('used')) is int else 0


def local_invariants(vm):
    """Check mandatory local step relations even in programs containing calls.

Every step deducts its recorded cost; a call or creation that entered a child
frame also receives the child's unused gas. DUPn and SWAPn push the top n+1 words,
deepest first, of the stack reconstructed from earlier pushes (arity only once it is lost). Operand ranges come from the stack
reconstructed from reported push words. Dedicated models additionally derive
costs and effects independently of recorded values.
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
    stack=[]  # None once the reported stack effects cannot be followed.
    for i,op in enumerate(vm['ops']):
        if not isinstance(op,dict):
            errors.append(f'operation {i} malformed');continue
        pc=op.get('pc');ex=op.get('ex');sub=op.get('sub')
        if type(pc) is not int or pc<0 or pc>=len(code):
            errors.append(f'operation {i} pc outside executing bytecode');continue
        opcode=code[pc]
        if 'op' in op and opcode in NAMES and op['op']!=NAMES[opcode] and not (opcode==0x44 and op['op']=='DIFFICULTY'):
            errors.append(f'operation {i} mnemonic disagrees with bytecode')
        if sub is not None and (opcode not in CALLS+CREATES or not isinstance(ex,dict)):
            errors.append(f'operation {i} has a subtrace but entered no child frame')
        pushed=words(ex.get('push')) if isinstance(ex,dict) else None
        if 0x80<=opcode<=0x9f and pushed is not None:
            want=stack_window(opcode,stack) if stack is not None else None
            arity=opcode-0x7e if opcode<0x90 else opcode-0x8e
            if len(pushed)!=(len(want) if want is not None else arity) or want is not None and pushed!=want:
                errors.append(f'operation {i} {NAMES[opcode]} push is not the top {arity} words after execution, deepest first')
                pushed=None
        if stack is not None and pushed is not None and opcode in INPUTS and len(stack)>=INPUTS[opcode]:
            operands=stack[len(stack)-INPUTS[opcode]:][::-1]
            stack=stack[:len(stack)-INPUTS[opcode]]+pushed
        else:
            stack=None
        if isinstance(ex,dict):
            used,cost=ex.get('used'),op.get('cost')
            if type(used) is not int or type(cost) is not int or used<0 or cost<0:
                errors.append(f'operation {i} gas is not a nonnegative integer')
            elif previous is not None and opcode in CALLS+CREATES:
                # A creation that RETURNs still pays the code deposit and exit checks,
                # which the child's steps do not show, so its returned gas is unknown here.
                if isinstance(sub,dict) and isinstance(sub.get('ops'),list) and sub['ops'] and not (opcode in CREATES and returned(sub)) and used!=previous-cost+leftover(sub):
                    errors.append(f'operation {i} post-step gas does not deduct its cost and return the child leftover')
            elif previous is not None and used!=previous-cost:
                errors.append(f'operation {i} post-step gas does not deduct this operation cost')
            if 0x60<=opcode<=0x7f:
                size=opcode-0x5f
                want=int.from_bytes(code[pc+1:pc+1+size].ljust(size,b'\0'),'big')
                if pushed is None or len(pushed)!=1 or pushed[0]!=want:
                    errors.append(f'operation {i} PUSH value disagrees with bytecode')
            mem=ex.get('mem')
            if opcode in [0xf3,0xfd] and mem is not None:
                errors.append(f'operation {i} reports memory for RETURN/REVERT')
            if opcode==0x51:
                word=f'0x{pushed[0]:064x}' if pushed and len(pushed)==1 else None
                if not isinstance(mem,dict) or mem.get('data')!=word or operands and mem.get('off')!=operands[0]:
                    errors.append(f'operation {i} MLOAD mem is not the loaded word at its offset')
            if opcode in CALLS and operands:
                offset,size=operands[-2],operands[-1]
                if not (mem is None if size==0 else isinstance(mem,dict) and mem.get('off')==offset
                        and isinstance(mem.get('data'),str) and len(mem['data'])==2+2*size):
                    errors.append(f'operation {i} call mem is not the full output window')
            previous=used if type(used) is int else None
        else:
            previous=None
        if sub is not None:
            errors.extend(f'subtrace {i}: '+e for e in local_invariants(sub))
    return errors


QUANTITY = re.compile(r'0x(?:0|[1-9a-f][0-9a-f]*)')
DATA = re.compile(r'0x(?:[0-9a-f]{2})*')


def encoding_valid(ex):
    """Check a VM step's ex encoding: minimal quantities for push and store, integer offsets and even data for mem."""
    if ex is None:
        return True
    if not isinstance(ex, dict):
        return False
    push, store, mem = ex.get('push'), ex.get('store'), ex.get('mem')
    return (isinstance(push, list) and all(isinstance(v, str) and QUANTITY.fullmatch(v) for v in push)
            and (store is None or isinstance(store, dict) and all(
                isinstance(store.get(k), str) and QUANTITY.fullmatch(store[k]) for k in ['key', 'val']))
            and (mem is None or isinstance(mem, dict) and type(mem.get('off')) is int and mem['off'] >= 0
                 and isinstance(mem.get('data'), str) and DATA.fullmatch(mem['data']) is not None))

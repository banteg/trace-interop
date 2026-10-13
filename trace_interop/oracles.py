"""Independent anchors for the frozen Hive fixtures, never client-majority output."""

TREE = '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'
REVERT = TREE[:-1]+'3'
CHILD_INIT = '0x5b646368696c6460006000a133ff'
REVERT_OUTPUT = ('0x08c379a0' + f'{32:064x}' + f'{10:064x}' + b'user error'.hex())
# Between CALLCODE and CREATE the calltree program runs PUSH1 0 PUSH1 0 PUSH1 4 PUSH1 0
# PUSH1 0 PUSH1 4 PUSH2 0xea60 CALL: a nested zero-value call to the identity precompile,
# which H29 omits from every emitted tree.
IDENTITY = '0x' + '0'*39 + '4'
# The selected branch of the genesis REVERT program performs one cold SLOAD
# (2100) and 85 gas of stack/control/memory operations, including 4 memory words.
REVERT_GAS = hex(2100 + 85)


def anchored_reference(context, peers, name):
    return anchor(context, peers, name)[0]


def malformed(tree):
    """Why one transaction's records are not a single-rooted tree with dense children, or None."""
    paths = [f.get('traceAddress') for f in tree]
    if paths.count([]) != 1:
        return f'has {paths.count([])} root records'
    if any(not isinstance(p, list) or any(type(i) is not int or i < 0 for i in p) for p in paths):
        return 'has a traceAddress that is not a list of non-negative integers'
    if len({tuple(p) for p in paths}) != len(paths):
        return 'has duplicate traceAddress values'
    for frame, path in zip(tree, paths):
        children = sorted(p[-1] for p in paths if len(p) == len(path)+1 and p[:-1] == path)
        if frame.get('subtraces') != len(children) or children != list(range(len(children))):
            return f'reports {frame.get("subtraces")} subtraces at {path} for children {children}'
        if path and path[:-1] not in paths:
            return f'has no parent for {path}'
    return None


def anchor(context, peers, name):
    """Return (reference, mismatch) after checking the independent fixture inventory.

    This anchors the complete decoded root inventory when available and the calltree's
    non-precompile children. It is not a general EVM or full child-trace oracle.
    Optional precompile frames may shift paths; emitted paths must form a tree.
    An unestablished inventory gives (None, None); a response that contradicts the
    inventory, its tree shape or an anchored action field gives (None, description).
    """
    obs = peers.get(name, {})
    if not isinstance(obs, dict) or obs.get('status') != 'result' or not isinstance(obs.get('response'), dict):
        return None, None
    frames = obs['response'].get('result')
    request = next((c['request'] for c in context.get('cases', []) if c['name'] == name), {})
    params = request.get('params', [])
    if not params:
        return None, None
    transactions = [(kind, tx) for kind, entries in context.get('txinfo', {}).items() if isinstance(entries, list)
                    for tx in entries if isinstance(tx, dict) and 'txhash' in tx
                    and (tx.get('txhash') == params[0] if request.get('method') == 'trace_transaction'
                         else tx.get('block') == params[0])]
    block = context.get('_blocks', {}).get(params[0]) if request.get('method') == 'trace_block' else None
    if not transactions:
        if isinstance(block, dict) and block.get('transactions') == [] and block.get('difficulty') == 0:
            # Independently decoded empty PoS block. Reward records are H05's to judge, here as below.
            if frames == []:
                return [], None
            rewards = isinstance(frames, list) and all(isinstance(f, dict) and f.get('type') == 'reward' for f in frames)
            return None, None if rewards else 'records for an empty proof-of-stake block: '+str(frames)[:200]
        return None, None  # No independent inventory, including purported empty blocks.
    if not isinstance(frames, list) or any(not isinstance(f, dict) or not isinstance(f.get('action'), dict) for f in frames):
        return None, 'not a list of records with actions: '+str(frames)[:200]
    mismatches = []
    def expect(label, got, want):
        if got != want:
            mismatches.append(f'{label}: expected {want}, got {got}')
    # An extra transaction cannot become a filter expectation just because both
    # methods report it. Legacy indexed txinfo alone is not a complete block inventory.
    inventory = None
    if request.get('method') == 'trace_transaction':
        inventory = [params[0]]
    elif isinstance(block, dict) and isinstance(block.get('transactions'), list):
        inventory = [tx['hash'] for tx in block['transactions']]
    elif request.get('method') == 'trace_block' and '_decoded' in context.get('txinfo', {}):
        inventory = [tx['txhash'] for tx in context['txinfo']['_decoded'] if tx['block'] == params[0]]
    if inventory is not None:
        roots = [f.get('transactionHash') for f in frames
                 if f.get('traceAddress') == [] and f.get('type') in ['call','create']]
        expect('transaction root inventory', roots, inventory)
        extra = [f.get('transactionHash') for f in frames
                 if f.get('type') != 'reward' and f.get('transactionHash') not in inventory]
        if extra:
            mismatches.append('records for transactions outside the frozen inventory: '+str(extra[:4]))
    for kind, tx in transactions:
        tree = [f for f in frames if f.get('transactionHash') == tx['txhash']]
        if (problem := malformed(tree)):
            mismatches.append(f'{tx["txhash"]} {problem}')
            continue
        root = next(f for f in tree if f['traceAddress'] == [])
        expect(f'{tx["txhash"]} root action.from', root['action'].get('from'), tx.get('sender'))
        if kind != 'tx-calltree':
            continue
        expect('calltree root action.to', root['action'].get('to'), TREE)
        # Six ordinary calls followed by CREATE. The inventory tolerates the identity
        # precompile between CALLCODE and CREATE; H29 asserts its omission separately.
        ordinary = [f for f in tree if len(f['traceAddress']) == 1 and f['action'].get('to') != IDENTITY]
        calls = [('call', TREE[:-1]+'1', '0x1'), ('call', REVERT, '0x0'),
                 ('staticcall', TREE[:-1]+'2', '0x0'),
                 ('staticcall', '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', '0x0'),
                 ('delegatecall', '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', '0x0'),
                 ('callcode', TREE[:-1]+'1', '0x0')]
        if len(ordinary) != 7:
            mismatches.append(f'calltree has {len(ordinary)} non-precompile depth-1 records, expected 7')
            continue
        for i, (frame, (call_type, target, value)) in enumerate(zip(ordinary, calls)):
            expect(f'calltree call {i} type', frame.get('type'), 'call')
            for key, want in [('from', TREE), ('to', target), ('callType', call_type), ('value', value)]:
                expect(f'calltree {call_type} {i} action.{key}', frame['action'].get(key), want)
        creation = ordinary[-1]
        expect('calltree creation type', creation.get('type'), 'create')
        expect('calltree creation action.init', creation['action'].get('init'), CHILD_INIT)
        suicides = [f for f in tree if f.get('type') == 'suicide' and f['traceAddress'] == creation['traceAddress']+[0]]
        expect('calltree creation suicide records', len(suicides), 1)
        if suicides:
            expect('calltree suicide action.refundAddress', suicides[0]['action'].get('refundAddress'), TREE)
    # A transaction listed under several fixture kinds is checked once per kind.
    return (None, '; '.join(dict.fromkeys(mismatches))) if mismatches else (frames, None)

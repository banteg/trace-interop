"""Independent anchors for the frozen Hive fixtures, never client-majority output."""

TREE = '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'
REVERT = TREE[:-1]+'3'
CHILD_INIT = '0x5b646368696c6460006000a133ff'
REVERT_OUTPUT = ('0x08c379a0' + f'{32:064x}' + f'{10:064x}' + b'user error'.hex())
# The selected branch of the genesis REVERT program performs one cold SLOAD
# (2100) and 85 gas of stack/control/memory operations, including 4 memory words.
REVERT_GAS = hex(2100 + 85)


def anchored_reference(context, peers, name):
    """Return a reference only after checking its independent fixture inventory.

    This anchors required roots and the calltree's non-precompile children. It is
    deliberately a minimum inventory, not a general EVM or full trace oracle.
    Optional precompile frames may shift paths; emitted paths must form a tree.
    """
    obs = peers.get(name, {})
    if not isinstance(obs, dict) or obs.get('status') != 'result' or not isinstance(obs.get('response'), dict):
        return None
    frames = obs['response'].get('result')
    if not isinstance(frames, list) or any(not isinstance(f, dict) or not isinstance(f.get('action'), dict) for f in frames):
        return None
    request = next((c['request'] for c in context.get('cases', []) if c['name'] == name), {})
    params = request.get('params', [])
    if not params:
        return None
    transactions = [(kind, tx) for kind, entries in context.get('txinfo', {}).items() if isinstance(entries, list)
                    for tx in entries if isinstance(tx, dict) and 'txhash' in tx
                    and (tx.get('txhash') == params[0] if request.get('method') == 'trace_transaction'
                         else tx.get('block') == params[0])]
    if not transactions:
        block=context.get('_blocks',{}).get(params[0])
        if (request.get('method')=='trace_block' and isinstance(block,dict)
                and block.get('transactions')==[] and block.get('difficulty')==0):
            return [] if frames==[] else None  # Independently decoded empty PoS block.
        return None  # No independent inventory, including purported empty blocks.
    for kind, tx in transactions:
        tree = [f for f in frames if f.get('transactionHash') == tx['txhash']]
        roots = [f for f in tree if f.get('traceAddress') == []]
        if len(roots) != 1 or roots[0].get('action', {}).get('from') != tx.get('sender'):
            return None
        paths = [f.get('traceAddress') for f in tree]
        if any(not isinstance(p, list) or any(type(i) is not int or i < 0 for i in p) for p in paths):
            return None
        if len({tuple(p) for p in paths}) != len(paths):
            return None
        for frame, path in zip(tree, paths):
            children = [p for p in paths if len(p) == len(path)+1 and p[:-1] == path]
            if frame.get('subtraces') != len(children) or sorted(p[-1] for p in children) != list(range(len(children))):
                return None
            if path and path[:-1] not in paths:
                return None
        if kind != 'tx-calltree':
            continue
        if roots[0].get('action', {}).get('to') != TREE:
            return None
        # Six ordinary calls followed by CREATE. The identity precompile between
        # CALLCODE and CREATE may be omitted by the client's emission policy.
        ordinary = [f for f in tree if len(f['traceAddress']) == 1
                    and f.get('action', {}).get('to') != '0x'+'0'*39+'4']
        calls = [('call', TREE[:-1]+'1', '0x1'), ('call', REVERT, '0x0'),
                 ('staticcall', TREE[:-1]+'2', '0x0'),
                 ('staticcall', '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', '0x0'),
                 ('delegatecall', '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', '0x0'),
                 ('callcode', TREE[:-1]+'1', '0x0')]
        if len(ordinary) != 7:
            return None
        for frame, (call_type, target, value) in zip(ordinary, calls):
            action = frame.get('action', {})
            if frame.get('type') != 'call' or any(action.get(k) != v for k, v in
                    [('from', TREE), ('to', target), ('callType', call_type), ('value', value)]):
                return None
        creation = ordinary[-1]
        if creation.get('type') != 'create' or creation.get('action', {}).get('init') != CHILD_INIT:
            return None
        suicides = [f for f in tree if f.get('type') == 'suicide' and f['traceAddress'] == creation['traceAddress']+[0]]
        if len(suicides) != 1 or suicides[0].get('action', {}).get('refundAddress') != TREE:
            return None
    return frames

"""Consistency laws: two successful responses from the same client that must agree.

Every trace method projects one execution. A law pairs two captured requests that
denote the same execution, or the same records, and compares what one client
returned for both. It needs no expected value and no other client, and it holds
under every policy the decision ledger is still weighing: a law never asks which
precompile frames exist, how a record is encoded or which errors a request earns,
only that a client answers the same question the same way. An error on either
side is not a violation; it leaves the pair unevaluated.
"""
from __future__ import annotations

import json
import re

from .rules import embedded_error

LOCALIZATION = ('blockHash', 'blockNumber', 'transactionHash', 'transactionPosition')
COMPONENTS = ('trace', 'stateDiff', 'vmTrace')
# Replayed and simulated envelopes; each selected component is a projection of one execution.
ENVELOPES = {'trace_call', 'trace_callMany', 'trace_rawTransaction', 'trace_replayTransaction', 'trace_replayBlockTransactions'}

LAWS = {
    'L01': ('Tree shape', 'Every frame list is a preorder tree: one root, unique dense paths, subtraces equal to the number of children, and no frame using more gas than it was given.'),
    'L02': ('Changed values', 'A stateDiff `*` entry changes its value: `from` differs from `to`.'),
    'L03': ('Root output', 'A successful root call frame reports the envelope output.'),
    'L04': ('Selection is a projection', 'Requests that differ only in their trace types return the same output and the same value for every component both select.'),
    'L05': ('trace_get selects from trace_transaction', 'A record trace_get returns is one of the trace_transaction records, unchanged.'),
    'L06': ('trace_transaction is a slice of trace_block', 'trace_transaction(tx) equals the trace_block records carrying its hash, in order.'),
    'L07': ('Stored and replayed frames agree', 'The frames of trace_transaction and trace_block equal the replayed trace of the same transaction, apart from localization fields.'),
    'L08': ('Single and block replay agree', 'trace_replayTransaction(tx) equals the block replay envelope of that transaction for every selected component.'),
    'L09': ('A bundle item is a call', 'trace_callMany items equal the same items replayed as a shorter bundle, and a first item equals trace_call on the same block.'),
    'L10': ('Filters select block records', 'trace_filter over an explicit range returns block records, unchanged and in block order; without addresses or paging it returns all of them.'),
    'L11': ('Paging slices the filter', 'trace_filter with after and count returns that slice of the same filter without them.'),
    'L12': ('Equivalent block and address spellings', 'The same request, or one that differs only in address letter case or in naming one block by number, hash or head tag, returns the same result.'),
}


def mapping(value):
    return value if isinstance(value, dict) else {}


def sequence(value):
    return value if isinstance(value, list) else []


def canonical(value):
    return json.dumps(value, sort_keys=True)


def core(frame):
    return {k: v for k, v in mapping(frame).items() if k not in LOCALIZATION}


def quantity(value):
    return int(value, 16) if isinstance(value, str) and re.fullmatch(r'0x[0-9a-fA-F]+', value) else None


class Run:
    """One client's successful results in one captured run, with the frozen chain that resolves blocks."""

    def __init__(self, context, cases, peers):
        self.cases = [c for c in cases if c['request']['method'].startswith('trace_')]
        self.results = {c['name']: peers[c['name']]['response']['result'] for c in self.cases
                        if mapping(peers.get(c['name'])).get('status') == 'result' and isinstance(peers[c['name']].get('response'), dict)
                        and not embedded_error(peers[c['name']]['response'])}
        blocks = context.get('_blocks', {})
        self.numbers = {b['hash']: b['number'] for b in blocks.values()}
        self.block_of = {t['txhash']: (quantity(t['block']), t['indexInBlock']) for t in context.get('txinfo', {}).get('_decoded', [])}
        # Scenario phases reorganize or prune the chain between requests, so only a frozen chain pairs them.
        self.frozen = not context.get('_scenario_phases') and not context.get('_alternate_blocks')
        self.head = quantity(mapping(context.get('_head')).get('number'))
        self.hashes_by_block = {}
        for tx, (number, index) in self.block_of.items():
            self.hashes_by_block.setdefault(number, {})[index] = tx

    def block(self, value):
        """The block number a selector names, or None when it depends on policy or state."""
        if value == 'latest':
            return self.head
        if isinstance(value, str) and len(value) == 66:
            return self.numbers.get(value.lower())
        return quantity(value)

    def of(self, *methods):
        return [c for c in self.cases if c['request']['method'] in methods and c['name'] in self.results]


def tree_violations(frames):
    """Structural defects of one transaction's frame list; empty when it is a well-formed preorder tree."""
    paths = [f.get('traceAddress') for f in frames]
    if any(not isinstance(p, list) or any(type(i) is not int or i < 0 for i in p) for p in paths):
        return ['a traceAddress is not a list of non-negative integers']
    keys = [tuple(p) for p in paths]
    problems = []
    if keys.count(()) != 1 or keys[0] != ():
        problems.append('the list does not start with its single root')
    if len(set(keys)) != len(keys):
        problems.append('duplicate traceAddress')
    if keys != sorted(keys):
        problems.append('records are not in preorder')
    for frame, key in zip(frames, keys):
        children = sorted(k[-1] for k in keys if len(k) == len(key)+1 and k[:-1] == key)
        if children != list(range(len(children))):
            problems.append(f'{where(key)} has non-dense children {children}')
        if frame.get('subtraces') != len(children):
            problems.append(f'{where(key)} reports {frame.get("subtraces")} subtraces for {len(children)} children')
        if key and key[:-1] not in keys:
            problems.append(f'{where(key)} has no parent')
        gas, used = quantity(mapping(frame.get('action')).get('gas')), quantity(mapping(frame.get('result')).get('gasUsed'))
        if gas is not None and used is not None and used > gas:
            problems.append(f'{where(key)} ({frame.get("type")}) reports gasUsed {used} of {gas} gas')
    return problems


def transactions(frames):
    """Group localized records by transaction, dropping block-level reward records."""
    groups = {}
    for frame in frames:
        if mapping(frame).get('type') != 'reward':
            groups.setdefault(mapping(frame).get('transactionHash'), []).append(frame)
    return groups


def envelopes(case, result):
    """(label, types, envelope) for each envelope a replay or simulation returned."""
    method, params = case['request']['method'], case['request']['params']
    if method == 'trace_callMany':
        items = sequence(params[0]) if params else []
        return [(f'[{i}]', item[1] if len(item) > 1 else None, e) for i, (item, e) in enumerate(zip(items, sequence(result)))
                if isinstance(item, list) and isinstance(e, dict)]
    if method == 'trace_replayBlockTransactions':
        return [(f'[{i}]', params[1] if len(params) > 1 else None, e) for i, e in enumerate(sequence(result)) if isinstance(e, dict)]
    return [('', params[1] if len(params) > 1 else None, result)] if isinstance(result, dict) else []


def where(path):
    """A traceAddress short enough to read in a detail line."""
    return str(list(path)) if len(path) <= 6 else f'[{path[0]}, … {len(path)} deep]'


def shown(value):
    return json.dumps(value)[:80]


def first_difference(a, b, path=''):
    """The first differing location of two JSON values, or None when they are equal.

    vmTrace `idx` is skipped: its numbering is an unmodeled optional convention that may
    legitimately encode an envelope's position in a bundle or block.
    """
    if type(a) is not type(b):
        return f'{path or "value"}: {shown(a)} vs {shown(b)}'
    if isinstance(a, str) and a != b:
        at = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
        start = max(0, at - 8)
        return f'{path or "value"}: differs at character {at}: …{a[start:at+40]} vs …{b[start:at+40]}'
    if isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            if k == 'idx' and 'vmTrace' in path:
                continue
            if k not in a or k not in b:
                return f'{path}.{k} present on one side only'
            if (d := first_difference(a[k], b[k], f'{path}.{k}')):
                return d
        return None
    if isinstance(a, list):
        if len(a) != len(b):
            return f'{path or "list"} has {len(a)} vs {len(b)} entries'
        return next((d for i, (x, y) in enumerate(zip(a, b)) if (d := first_difference(x, y, f'{path}[{i}]'))), None)
    return None if a == b else f'{path or "value"}: {shown(a)} vs {shown(b)}'


def evaluate(context, cases, peers):
    """Every law instance this run supports for one client, as {law, cases, holds, detail} dicts."""
    run = Run(context, cases, peers)
    found = []

    def law(code, names, difference):
        found.append({'law': code, 'cases': list(names), 'holds': not difference, 'detail': difference or ''})

    def compare(code, names, a, b):
        law(code, names, first_difference(a, b))

    # L01-L03: one response at a time.
    for case in run.of(*ENVELOPES, 'trace_transaction', 'trace_block'):
        result = run.results[case['name']]
        if case['request']['method'] in ('trace_transaction', 'trace_block'):
            lists = [(tx or '', frames) for tx, frames in transactions(sequence(result)).items()]
        else:
            lists = [(label, sequence(e.get('trace'))) for label, _, e in envelopes(case, result)]
        for label, frames in lists:
            if frames and all(isinstance(f, dict) for f in frames):
                problems = tree_violations(frames)
                law('L01', [case['name']], f'{label} {"; ".join(problems[:3])}'.strip() if problems else None)
        for label, _, e in envelopes(case, result):
            for address, account in mapping(e.get('stateDiff')).items():
                for field, change in mapping(account).items():
                    for key, marker in (mapping(change).items() if field == 'storage' else [(None, change)]):
                        star = mapping(marker).get('*')
                        if isinstance(star, dict):
                            same = star.get('from') == star.get('to')
                            law('L02', [case['name']], f'{label} {address} {field}{" "+key if key else ""} "*" from equals to {star.get("to")}'.strip() if same else None)
            root = next((f for f in sequence(e.get('trace')) if mapping(f).get('traceAddress') == []), None)
            output = mapping(mapping(root).get('result')).get('output')
            if mapping(root).get('type') == 'call' and 'error' not in root and output is not None:
                law('L03', [case['name']], None if output == e.get('output') else f'{label} root output {output[:74]} vs envelope {shown(e.get("output"))}'.strip())

    if not run.frozen:
        return found

    # L04: requests identical apart from their trace types.
    def untyped(case):
        method, params = case['request']['method'], list(case['request']['params'])
        if method == 'trace_callMany':
            params[0] = [item[:1] for item in sequence(params[0])]
        elif len(params) > 1:
            params[1] = None
        return canonical([method, params])
    selections = {}
    for case in run.of(*ENVELOPES):
        selections.setdefault(untyped(case), []).append(case)
    for group in selections.values():
        for i, a in enumerate(group):
            for b in group[i+1:]:
                ea, eb = envelopes(a, run.results[a['name']]), envelopes(b, run.results[b['name']])
                diff = None if len(ea) == len(eb) else f'{len(ea)} vs {len(eb)} envelopes'
                for (label, ta, x), (_, tb, y) in zip(ea, eb) if not diff else []:
                    shared = [k for k in COMPONENTS if k in sequence(ta) and k in sequence(tb)]
                    if (diff := next((label+d for k in ['output', *shared] if (d := first_difference(x.get(k), y.get(k), '.'+k))), None)):
                        break
                law('L04', [a['name'], b['name']], diff)

    # L05: trace_get against trace_transaction.
    trees = {c['request']['params'][0]: c for c in run.of('trace_transaction') if c['request']['params']}
    for case in run.of('trace_get'):
        params = case['request']['params']
        tree = trees.get(params[0]) if params else None
        if tree is None:
            continue
        # Which record a selector names, and whether a miss is null, belong to H02 and H06.
        record = run.results[case['name']]
        if isinstance(record, dict):
            law('L05', [case['name'], tree['name']], None if record in sequence(run.results[tree['name']]) else
                f'{record.get("type")} record at {record.get("traceAddress")} is not in the transaction trace')

    # L06, L07: stored records against block records and replays.
    blocks = {}
    for case in run.of('trace_block'):
        number = run.block(case['request']['params'][0]) if case['request']['params'] else None
        if number is not None and isinstance(run.results[case['name']], list):
            blocks.setdefault(number, case)
    for tx, case in trees.items():
        located = run.block_of.get(tx)
        block = blocks.get(located[0]) if located else None
        if block and isinstance(run.results[case['name']], list):
            compare('L06', [case['name'], block['name']], run.results[case['name']],
                    [f for f in sequence(run.results[block['name']]) if mapping(f).get('transactionHash') == tx])
    replays = {}
    for case in run.of('trace_replayTransaction'):
        params = case['request']['params']
        if len(params) > 1 and 'trace' in sequence(params[1]) and isinstance(run.results[case['name']], dict):
            replays.setdefault(params[0], case)
    for case in run.of('trace_replayBlockTransactions'):
        params = case['request']['params']
        number = run.block(params[0]) if params else None
        if number is None or len(params) < 2 or 'trace' not in sequence(params[1]):
            continue
        for index, e in enumerate(sequence(run.results[case['name']])):
            tx = run.hashes_by_block.get(number, {}).get(index)
            if tx and isinstance(e, dict):
                replays.setdefault(tx, dict(case, _index=index))
    stored = [(tx, c, run.results[c['name']]) for tx, c in trees.items()]
    stored += [(tx, c, frames) for c in blocks.values() for tx, frames in transactions(sequence(run.results[c['name']])).items()]
    for tx, case, frames in stored:
        replay = replays.get(tx)
        if replay is None or not isinstance(frames, list):
            continue
        result = run.results[replay['name']]
        envelope = result[replay['_index']] if '_index' in replay else result
        compare('L07', [case['name'], replay['name']], [core(f) for f in frames], sequence(envelope.get('trace')))

    # L08: a single replay against its block replay envelope.
    for case in run.of('trace_replayTransaction'):
        params = case['request']['params']
        located = run.block_of.get(params[0]) if params else None
        result = run.results[case['name']]
        if not located or not isinstance(result, dict) or len(params) < 2:
            continue
        for other in run.of('trace_replayBlockTransactions'):
            other_params = other['request']['params']
            envelope = sequence(run.results[other['name']])
            if len(other_params) < 2 or run.block(other_params[0]) != located[0] or located[1] >= len(envelope):
                continue
            shared = [k for k in COMPONENTS if k in sequence(params[1]) and k in sequence(other_params[1])]
            if shared:
                other_env = mapping(envelope[located[1]])
                law('L08', [case['name'], other['name']],
                    next((d for k in ['output', *shared] if (d := first_difference(result.get(k), other_env.get(k), '.'+k))), None))

    # L09: bundle prefixes and first items.
    bundles = run.of('trace_callMany')
    for case in bundles:
        params = case['request']['params']
        items, selector = sequence(params[0]) if params else [], params[1:]
        result = sequence(run.results[case['name']])
        for other in bundles:
            other_params = other['request']['params']
            shorter = sequence(other_params[0]) if other_params else []
            if (other is not case and 0 < len(shorter) < len(items) and shorter == items[:len(shorter)] and other_params[1:] == selector):
                law('L09', [other['name'], case['name']], first_difference(sequence(run.results[other['name']]), result[:len(shorter)]))
        # Omitted blocks default by policy (H31), so both sides name theirs.
        if not items or not isinstance(items[0], list) or len(items[0]) < 2 or len(selector) != 1 or not result:
            continue
        for call in run.of('trace_call'):
            call_params = call['request']['params']
            if call_params[:2] == items[0][:2] and len(call_params) == 3 and run.block(call_params[2]) == run.block(selector[0]) is not None:
                compare('L09', [call['name'], case['name']], run.results[call['name']], result[0])

    # L10, L11: filters against block records and against their own unpaged form.
    filters = [c for c in run.of('trace_filter') if c['request']['params'] and isinstance(c['request']['params'][0], dict)]
    for case in filters:
        spec = case['request']['params'][0]
        start, end = run.block(spec.get('fromBlock')), run.block(spec.get('toBlock'))
        result = run.results[case['name']]
        if start is None or end is None or not isinstance(result, list) or any(n not in blocks for n in range(start, end+1)):
            continue
        records = [f for n in range(start, end+1) for f in sequence(run.results[blocks[n]['name']])]
        names = [case['name']] + [blocks[n]['name'] for n in range(start, end+1)]
        if not any(k in spec for k in ('fromAddress', 'toAddress', 'after', 'count', 'mode')):
            compare('L10', names, result, records)
            continue
        position, missing = 0, None
        for frame in result:
            while position < len(records) and records[position] != frame:
                position += 1
            if position == len(records):
                missing = f'record {result.index(frame)}, {frame.get("type")} at {frame.get("transactionHash")} {frame.get("traceAddress")}, is not the next block record'
                break
            position += 1
        law('L10', names, missing)
    for case in filters:
        spec = case['request']['params'][0]
        if 'after' not in spec and 'count' not in spec:
            continue
        unpaged = {k: v for k, v in spec.items() if k not in ('after', 'count')}
        for other in filters:
            if other['request']['params'][0] == unpaged:
                after, count = spec.get('after', 0), spec.get('count')
                if all(type(v) is int and v >= 0 for v in (after, 0 if count is None else count)):
                    whole = sequence(run.results[other['name']])
                    compare('L11', [case['name'], other['name']], run.results[case['name']], whole[after:None if count is None else after+count])

    # L12: equivalent spellings of the same request.
    def spelled(value, key=None):
        if isinstance(value, dict):
            return {k: spelled(v, k) for k, v in value.items()}
        if isinstance(value, list):
            return [spelled(v, key) for v in value]
        if isinstance(value, str) and re.fullmatch(r'0x[0-9a-fA-F]{40}', value):
            return value.lower()
        return value
    def normal(case):
        method, params = case['request']['method'], spelled(case['request']['params'])
        index = {'trace_call': 2, 'trace_callMany': 1, 'trace_block': 0, 'trace_replayBlockTransactions': 0}.get(method)
        if index is not None and len(params) > index:
            number = run.block(params[index])
            if number is None:
                return None
            params[index] = number
        if method == 'trace_filter' and params and isinstance(params[0], dict):
            for bound in ('fromBlock', 'toBlock'):
                if bound in params[0]:
                    if (number := run.block(params[0][bound])) is None:
                        return None
                    params[0][bound] = number
        return canonical([method, params])
    spellings = {}
    for case in run.of(*{c['request']['method'] for c in run.cases}):
        if (key := normal(case)) is not None:
            spellings.setdefault(key, []).append(case)
    for group in spellings.values():
        for a, b in zip(group, group[1:]):
            compare('L12', [a['name'], b['name']], run.results[a['name']], run.results[b['name']])
    return found


def summarize(instances):
    """Counts of held and violated instances per law and client, with every violation kept for the report."""
    counts = {}
    for i in instances:
        tally = counts.setdefault(i['law'], {}).setdefault(i['client'], {'held': 0, 'violated': 0})
        tally['held' if i['holds'] else 'violated'] += 1
    return {'laws': [{'id': code, 'title': title, 'statement': statement} for code, (title, statement) in LAWS.items()],
            'counts': {law: dict(sorted(by_client.items())) for law, by_client in sorted(counts.items())},
            'violations': sorted(({k: i[k] for k in ('law', 'client', 'version', 'run', 'corpus', 'cases', 'detail')} for i in instances if not i['holds']),
                                 key=lambda v: (v['law'], v['client'], v['corpus'], v['cases']))}

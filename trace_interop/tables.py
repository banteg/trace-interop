"""Decision tables: the pinned draft's prose rules, enumerated over every input they govern.

A table names the dimensions of one question and the outcome attributes every valid cell
must determine. Each clause quotes the pinned draft and says, as predicates, which cells
it governs and which attribute values it requires there. Enumerating every cell finds
what reading the prose misses: a cell whose attribute no clause determines is a **gap**,
and a cell whose clauses require different values is a **conflict**. Clauses that agree
on a cell are an **overlap**, which is harmless but shows where a sentence is implied by
others. A clause marked general states a principle, such as error alone deciding failure, that
specific clauses are expected to restate, so agreeing with it is not reported as an overlap.

The encoding is a reading of the text and is reviewed like any other assertion. Every
quote must occur verbatim in the pinned draft, so a repinned draft that rewords a clause
fails verification until its table follows.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from itertools import product
import json
from typing import Callable


@dataclass(frozen=True)
class Clause:
    id: str
    quote: str
    applies: Callable[[dict], bool]
    requires: Callable[[dict], dict]
    general: bool = False  # a principle other clauses restate; agreeing with it is not an overlap


@dataclass(frozen=True)
class Table:
    id: str
    title: str
    question: str
    topics: tuple
    dimensions: dict
    valid: Callable[[dict], bool]
    attributes: Callable[[dict, dict], tuple]
    clauses: tuple
    notes: tuple = field(default=())  # (quote, reading) pairs that shape the dimensions rather than decide outcomes


def cells(table):
    names = list(table.dimensions)
    for values in product(*table.dimensions.values()):
        cell = dict(zip(names, values))
        if table.valid(cell):
            yield cell


def evaluate(table):
    """Each valid cell with the values its clauses require, as {cell, values, gaps, conflicts, overlaps}.

    `attributes(cell, values)` names the attributes the cell must determine given what is already
    decided, so an omitted frame needs no result shape. values maps attribute -> {value: [clause ids]}.
    """
    general = {c.id for c in table.clauses if c.general}
    for cell in cells(table):
        values = {}
        for clause in table.clauses:
            if clause.applies(cell):
                for attribute, value in clause.requires(cell).items():
                    values.setdefault(attribute, {}).setdefault(value, []).append(clause.id)
        decided = {a: next(iter(v)) for a, v in values.items() if len(v) == 1}
        needed = table.attributes(cell, decided)
        agreeing = {a: [i for i in next(iter(v.values())) if i not in general] for a, v in values.items() if a in needed and len(v) == 1}
        yield {'cell': cell, 'values': values,
               'gaps': [a for a in needed if a not in values],
               'conflicts': {a: v for a, v in values.items() if a in needed and len(v) > 1},
               'overlaps': {a: ids for a, ids in agreeing.items() if len(ids) > 1}}


def summarize(table):
    """Group gap, conflict and overlap cells by what they share, projecting the cells onto their dimensions."""
    groups = {}
    for result in evaluate(table):
        findings = [('gap', a, ()) for a in result['gaps']]
        findings += [('conflict', a, tuple(sorted((str(value), tuple(ids)) for value, ids in v.items()))) for a, v in result['conflicts'].items()]
        findings += [('overlap', a, tuple(ids)) for a, ids in result['overlaps'].items()]
        for finding in findings:
            groups.setdefault(finding, []).append(result['cell'])
    return [{'kind': kind, 'attribute': attribute, 'detail': detail, 'cells': len(members), 'span': span(table, members),
             'members': members if len(members) <= LISTED else None}
            for (kind, attribute, detail), members in sorted(groups.items(), key=lambda g: (['conflict', 'gap', 'overlap'].index(g[0][0]), g[0][1], str(g[0][2])))]


LISTED = 12  # groups this small list their cells rather than a projection


def span(table, members):
    """Each dimension's values among the cells, or * when the cells take every value the table
    allows for that dimension alongside their other coordinates."""
    shown = {}
    for name, domain in table.dimensions.items():
        present = [v for v in domain if any(c[name] == v for c in members)]
        possible = [v for v in domain if any(table.valid(dict(c, **{name: v})) for c in members)]
        shown[name] = '*' if present == possible else ', '.join(map(str, present))
    return shown


def strings(value):
    if isinstance(value, dict):
        for v in value.values():
            yield from strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from strings(v)
    elif isinstance(value, str):
        yield value


def verify(spec, tables):
    """Raise unless every quoted clause and note occurs verbatim in the pinned draft."""
    text = list(strings(spec))
    missing = [(t.id, q) for t in tables for q in [c.quote for c in t.clauses] + [q for q, _ in t.notes]
               if not any(q in s for s in text)]
    if missing:
        raise ValueError('decision-table quotes missing from the pinned draft: ' + '; '.join(f'{t}: {q!r}' for t, q in missing))


# Frame emission (H09, H29): which call and create attempts produce a record, and in what shape.
CALLS = ('CALL', 'CALLCODE', 'DELEGATECALL', 'STATICCALL')
CREATES = ('CREATE', 'CREATE2')
PRECHECKS = ('precheck depth', 'precheck balance', 'precheck nonce')


def frame_valid(c):
    create = c['opcode'] in CREATES
    values = {'CALL': ('zero', 'transferred'), 'CALLCODE': ('zero', 'transferred'), 'DELEGATECALL': ('zero', 'inherited'),
              'STATICCALL': ('zero',), 'CREATE': ('zero', 'transferred'), 'CREATE2': ('zero', 'transferred')}[c['opcode']]
    return (c['value'] in values
            and (c['position'] == 'nested' or c['opcode'] in ('CALL', 'CREATE') and c['outcome'] not in PRECHECKS)
            and (not create or c['target'] == 'account')
            and (create or c['outcome'] not in ('precheck nonce', 'collision'))
            and (c['outcome'] != 'precheck balance' or c['value'] == 'transferred')
            and (c['target'] == 'account' or c['outcome'] != 'revert')
            # Only CREATE prechecks change at Amsterdam; every other cell holds for any fork.
            and (c['fork'] != 'any fork') == (create and c['outcome'] in PRECHECKS))


def frame_attributes(cell, decided):
    return ('emitted',) + (('error', 'result') if decided.get('emitted') is not False else ())


FRAMES = Table(
    id='frames', title='Frame emission', topics=('H09', 'H29'),
    question='Does a call or create attempt produce a record, and does that record carry an error and a result?',
    dimensions={'position': ('root', 'nested'), 'opcode': CALLS + CREATES, 'target': ('account', 'precompile'),
                'value': ('zero', 'transferred', 'inherited'),
                'outcome': ('success', 'revert', 'halt', 'collision') + PRECHECKS,
                'fork': ('any fork', 'before Amsterdam', 'from Amsterdam')},
    valid=frame_valid, attributes=frame_attributes,
    notes=(('A precompile is an address in the precompile set active at the executing block\'s fork.',
            'target is precompile exactly when the callee is in that set; a precompile cannot REVERT, so its failures are halts.'),
           ('Retain root precompile calls regardless of value.',
            'A root is the transaction itself: CALL or CREATE, whose prechecks are transaction validation, not frames.')),
    clauses=(
        Clause('root-precompile', 'Retain root precompile calls regardless of value.',
               lambda c: c['position'] == 'root' and c['target'] == 'precompile', lambda c: {'emitted': True}),
        Clause('nested-zero-precompile', 'Omit nested precompile frames with zero value',
               lambda c: c['position'] == 'nested' and c['target'] == 'precompile' and c['value'] == 'zero', lambda c: {'emitted': False}),
        Clause('nested-value-precompile', 'retain nested frames with nonzero transferred or inherited value, whether successful or failed',
               lambda c: c['position'] == 'nested' and c['target'] == 'precompile' and c['value'] != 'zero', lambda c: {'emitted': True}),
        Clause('call-precheck', 'A CALL-family call that fails its precheck (call depth limit or insufficient balance) emits a frame with its action and error, no result and no subtraces',
               lambda c: c['opcode'] in CALLS and c['outcome'] in PRECHECKS,
               lambda c: {'emitted': True, 'error': 'present', 'result': 'absent'}),
        Clause('create-precheck', 'A CREATE or CREATE2 that fails its precheck (call depth limit, insufficient balance or nonce overflow) emits the same kind of frame before Amsterdam',
               lambda c: c['opcode'] in CREATES and c['outcome'] in PRECHECKS and c['fork'] == 'before Amsterdam',
               lambda c: {'emitted': True, 'error': 'present', 'result': 'absent'}),
        Clause('create-precheck-amsterdam', 'from Amsterdam the check runs in the creating opcode and no frame is emitted',
               lambda c: c['opcode'] in CREATES and c['outcome'] in PRECHECKS and c['fork'] == 'from Amsterdam', lambda c: {'emitted': False}),
        Clause('collision', 'A CREATE whose address collides emits a create frame with error "Contract address collision" that consumes its gas.',
               lambda c: c['outcome'] == 'collision', lambda c: {'emitted': True, 'error': 'present'}),
        Clause('halt-result', 'Exceptional halt, including an address collision; result is omitted or null.',
               lambda c: c['outcome'] in ('halt', 'collision'), lambda c: {'result': 'optional'}),
        Clause('halt', "An exceptional halt consumes the frame's action gas; its result may be omitted or null.",
               lambda c: c['outcome'] == 'halt', lambda c: {'result': 'optional'}),
        Clause('revert', 'A REVERT frame has error "Reverted" and a required result {gasUsed, output} carrying its revert bytes',
               lambda c: c['outcome'] == 'revert', lambda c: {'error': 'present', 'result': 'required'}),
        Clause('success', 'Successful frame; result is required and error must be absent.',
               lambda c: c['outcome'] == 'success', lambda c: {'error': 'absent', 'result': 'required'}),
        Clause('error-alone', 'error alone determines failure.',
               lambda c: True, lambda c: {'error': 'absent' if c['outcome'] == 'success' else 'present'}, general=True),
    ))


# Address filtering (H03, H04, H23): whether trace_filter selects a record.
def filter_valid(c):
    # A reward has no from side and a failed CREATE no created-address side, so neither list can match there.
    return not (c['record'] == 'reward' and c['from'] == 'match') and not (c['record'] == 'failed create' and c['to'] == 'match')


def populated(c):
    return [c[side] for side in ('from', 'to') if c[side] != 'unrestricted']


FILTERS = Table(
    id='filters', title='Address filtering', topics=('H03', 'H04', 'H23'),
    question='Does trace_filter select a record, given how each address list relates to the record’s sides and the mode?',
    dimensions={'record': ('call', 'failed call', 'create', 'failed create', 'suicide', 'reward'),
                'from': ('unrestricted', 'match', 'miss'), 'to': ('unrestricted', 'match', 'miss'),
                'mode': ('omitted', 'intersection', 'union')},
    valid=filter_valid, attributes=lambda cell, decided: ('selected',),
    notes=(('Match CALL sender/recipient, CREATE creator/created address and SELFDESTRUCT executing (self-destructing) account/beneficiary',
            'from and to describe the list against the record’s side: unrestricted, containing that side’s address (match) or not (miss).'),
           ('Failed CREATE has no created-address match.', 'A failed create’s to side never matches.'),
           ('A reward matches toAddress by author and has no from side', 'A reward’s from side never matches.'),
           ('omitted/null/empty lists are unrestricted', 'unrestricted covers an omitted, null or empty list.')),
    clauses=(
        Clause('intersection', 'Apply OR within each address list and AND between the lists by default',
               lambda c: c['mode'] != 'union' and populated(c), lambda c: {'selected': all(s == 'match' for s in populated(c))}),
        Clause('union', 'mode union matches either populated list',
               lambda c: c['mode'] == 'union' and populated(c), lambda c: {'selected': any(s == 'match' for s in populated(c))}),
        Clause('unrestricted', 'omitted/null/empty lists are unrestricted',
               lambda c: not populated(c), lambda c: {'selected': True}, general=True),
        Clause('reward-intersection', 'in intersection mode it is excluded whenever fromAddress is populated',
               lambda c: c['record'] == 'reward' and c['mode'] != 'union' and c['from'] != 'unrestricted', lambda c: {'selected': False}),
        Clause('reward-union', 'while in union mode a toAddress match suffices',
               lambda c: c['record'] == 'reward' and c['mode'] == 'union' and c['to'] == 'match', lambda c: {'selected': True}),
    ))


# Block selection (H06, H30, H31, H32): what a block selector resolves to, method by method.
SELECTORS = ('omitted', 'number', 'number beyond head', 'hash', 'unknown hash', 'non-canonical hash',
             'latest', 'earliest', 'safe', 'finalized', 'unresolvable safe', 'pending')
TAGGED = {'latest', 'earliest', 'safe', 'finalized', 'unresolvable safe', 'pending'}
# Selectors naming a canonical block; whether a non-canonical hash selects its block is left to the clauses.
KNOWN = ('number', 'hash', 'latest', 'earliest', 'safe', 'finalized')


def schema_forms(spec, method):
    """The selector forms the pinned schema admits for a method's block parameter."""
    methods = {m['name']: m for m in spec['methods']}
    if method == 'trace_filter':
        param = methods[method]['params'][0]['schema']['properties']['fromBlock']
        required = False
    else:
        param = next(p for p in methods[method]['params'] if p['name'] == 'Block')
        required, param = param.get('required', False), param['schema']
    tags, titles = set(), set()
    def walk(node):
        if isinstance(node, dict):
            tags.update(node.get('enum', []))
            titles.add(node.get('title'))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
    walk(param)
    forms = {'number', 'number beyond head'} if 'Block number' in titles else set()
    forms |= {'hash', 'unknown hash', 'non-canonical hash'} if 'Block hash' in titles else set()
    forms |= {s for s in TAGGED if s.split()[-1] in tags}
    return forms | ({'omitted'} if not required else set())


def blocks(spec):
    methods = ('trace_call', 'trace_callMany', 'trace_block', 'trace_replayBlockTransactions', 'trace_filter')
    forms = {m: schema_forms(spec, m) for m in methods}
    call_like = ('trace_call', 'trace_callMany')
    replayed = ('trace_block', 'trace_replayBlockTransactions')

    def names(c, selectors):
        return c['selector'] in selectors and c['selector'] in forms[c['method']]
    return Table(
        id='blocks', title='Block selection', topics=('H06', 'H30', 'H31', 'H32'),
        question='What does a request return for each way of naming its block, when the block’s state is available or pruned?',
        dimensions={'method': methods, 'selector': SELECTORS, 'history': ('available', 'pruned')},
        valid=lambda c: c['history'] == 'available' or c['selector'] in ('number', 'hash'),
        attributes=lambda cell, decided: ('response',),
        notes=(('Resolve tags once per request.', 'trace_filter is read with both bounds naming the same block.'),
               ('If the `safe` or `finalized` tag cannot be resolved to a block, the method responds as it does for an unknown block.',
                'unresolvable safe stands for either tag before the chain has one.'),
               ('Bounds exclude pending.', 'This names no response; the schema, which omits pending from trace_filter bounds, decides it.')),
        clauses=(
            Clause('schema', 'Invalid params',
                   lambda c: c['selector'] not in forms[c['method']], lambda c: {'response': '-32602'}, general=True),
            Clause('call-default', 'Optional block, latest when omitted or null',
                   lambda c: c['method'] in call_like and c['selector'] == 'omitted', lambda c: {'response': 'latest state'}),
            Clause('call-state', 'Execute against the state at the end of the selected block, default latest, under its fork rules and block environment.',
                   lambda c: c['method'] == 'trace_call' and names(c, KNOWN) and c['history'] == 'available', lambda c: {'response': 'selected state'}),
            Clause('many-state', 'The first item runs against the same state and environment as trace_call at the selected block.',
                   lambda c: c['method'] == 'trace_callMany' and names(c, KNOWN) and c['history'] == 'available', lambda c: {'response': 'selected state'}),
            Clause('call-unknown', 'an unknown selected block returns -32001 (Resource not found), and a known block whose required state is pruned returns 4444',
                   lambda c: c['method'] == 'trace_call' and names(c, ('number', 'hash', 'number beyond head', 'unknown hash', 'unresolvable safe'))
                   and (c['selector'] not in ('number', 'hash') or c['history'] == 'pruned'),
                   lambda c: {'response': '4444' if c['history'] == 'pruned' else '-32001'}),
            Clause('call-pending', 'pending has no agreed semantics yet; a client that does not implement it must reject it explicitly rather than substitute another block',
                   lambda c: c['method'] == 'trace_call' and c['selector'] == 'pending', lambda c: {'response': 'open: reject or pending state'}),
            Clause('block-state', 'Trace the block from its parent\'s post-block state with its own pre-transaction system operations applied, under its own fork rules.',
                   lambda c: c['method'] in replayed and names(c, KNOWN) and c['history'] == 'available', lambda c: {'response': 'selected block'}),
            Clause('block-unknown', 'An unknown selected block returns -32001 (Resource not found); a known block whose required state is pruned returns 4444',
                   lambda c: c['method'] in replayed and names(c, ('number', 'hash', 'number beyond head', 'unknown hash', 'unresolvable safe'))
                   and (c['selector'] not in ('number', 'hash') or c['history'] == 'pruned'),
                   lambda c: {'response': '4444' if c['history'] == 'pruned' else '-32001'}),
            Clause('block-pending', 'Block does not accept pending (-32602)',
                   lambda c: c['method'] in replayed and c['selector'] == 'pending', lambda c: {'response': '-32602'}),
            Clause('filter-default', 'defaults omitted fromBlock and toBlock to the same latest head',
                   lambda c: c['method'] == 'trace_filter' and c['selector'] == 'omitted', lambda c: {'response': 'latest block'}),
            Clause('filter-range', 'If either bound resolves beyond the current head block, or fromBlock resolves above toBlock, return -32602',
                   lambda c: c['method'] == 'trace_filter' and c['selector'] == 'number beyond head', lambda c: {'response': '-32602'}),
            Clause('filter-records', 'Indexed retrieval and replay must yield the same fork-correct per-block records, each block traced from its parent\'s post-block state.',
                   lambda c: c['method'] == 'trace_filter' and names(c, KNOWN) and c['history'] == 'available', lambda c: {'response': 'selected block'}),
            Clause('filter-pruned', 'return 4444 if required history is unavailable',
                   lambda c: c['method'] == 'trace_filter' and names(c, KNOWN) and c['history'] == 'pruned', lambda c: {'response': '4444'}),
        ))


def tables(spec):
    return [FRAMES, FILTERS, blocks(spec)]


def report(spec):
    found = tables(spec)
    verify(spec, found)
    return [{'id': t.id, 'title': t.title, 'question': t.question, 'topics': list(t.topics),
             'dimensions': {k: list(v) for k, v in t.dimensions.items()}, 'cells': sum(1 for _ in cells(t)),
             'clauses': [{'id': c.id, 'quote': c.quote} for c in t.clauses],
             'notes': [{'quote': q, 'reading': r} for q, r in t.notes],
             'findings': json.loads(json.dumps(summarize(t)))} for t in found]

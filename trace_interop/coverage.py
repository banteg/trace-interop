"""Additional property checks and explicit reasons for unevaluated obligations.

Ledger references are not all executable assertions. Controls, inapplicable
properties and blocked checks are retained, without turning them into passes.
"""
import re

from .oracles import anchor
from .vm_model import execute, intrinsic, differences, local_invariants, encoding_valid, UnsupportedProgram, NAMES
from .chain_model import decode_transaction
import rlp
from eth_hash.auto import keccak
from .execution_models import assess as assess_execution
from .fee_policy import assess as assess_fee_policy, assess_compatibility


def obj(value):
    return value if isinstance(value, dict) else {}


def seq(value):
    return value if isinstance(value, list) else []


def integer(value):
    try:
        return int(value, 16) if isinstance(value, str) else None
    except ValueError:
        return None


def supplement(case, observation, peers, checks, expected):
    checks = list(checks)
    context = case.get('context', {})
    name, request = case['name'], case['request']
    method, params = request['method'], request.get('params', [])
    status = observation.get('status', 'not_observed')
    result = obj(observation.get('response')).get('result')
    declared = set(expected)
    if not method.startswith('trace_'):
        return checks + [dict(topic=t,status='control',requirement='Retain independent reference evidence.',
                              detail='Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.')
                         for t in sorted(declared - {c['topic'] for c in checks})]
    blocks = context.get('_blocks', {})

    def add(topic, ok, requirement, detail=''):
        checks.append({'topic': topic, 'status': 'matches' if ok else 'change_needed',
                       'requirement': requirement, 'detail': detail})

    def explain(topic, kind, detail):
        checks.append({'topic': topic, 'status': kind,
                       'requirement': 'Assess the declared property.', 'detail': detail})

    def covered(topic):
        return any(c['topic'] == topic for c in checks)

    if case.get('role')=='reference':
        explain('H27','control' if status=='result' else 'blocked',
                'Per-block reference response for the filter comparison.' if status=='result' else 'Per-block reference unavailable: '+status)

    def other(n):
        observation = obj(peers.get(n))
        return obj(observation.get('response')).get('result') if observation.get('status') == 'result' else None

    # Availability is distinct from request success and from execution semantics.
    if 'H01' in declared and not covered('H01') and status in ['result', 'rpc_error']:
        add('H01', True, 'The method responds without Method not found (-32601).')
    checks.extend(assess_compatibility(case, observation, peers))
    if status in ['unsupported', 'malformed_json', 'invalid_envelope', 'harness_error', 'transport_error', 'not_observed']:
        for topic in sorted(declared - {c['topic'] for c in checks}):
            explain(topic, 'blocked', f'Cannot inspect this property: {status}.')
        return checks
    checks.extend(assess_fee_policy(case, observation))
    if method == 'trace_rawTransaction' and len(params)>2:
        for topic in sorted(declared - {c['topic'] for c in checks}):
            explain(topic, 'not_applicable', 'The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.')
        return checks
    if status == 'rpc_error' and any(c['topic']=='H13' and c['status']=='matches' for c in checks):
        for topic in sorted(declared - {c['topic'] for c in checks}):
            explain(topic, 'not_applicable', 'The signed transaction was correctly rejected before execution; execution-result properties do not apply.')
        return checks
    if case.get('expected_control') is not None and method.startswith('trace_'):
        add('H27', result == case['expected_control'], 'The explicit trace control matches its fixture expectation.')

    if method == 'trace_get' and name in ['get-missing', 'get-missing-tx']:
        add('H02', status == 'result' and result is None, 'A missing selected frame is null, not an empty collection.')
    if 'H06' in declared and not covered('H06'):
        if name == 'latest-call':
            explain('H06', 'control', 'Latest execution is the successful control for the unavailable-history probe.')
        elif name == 'get-nested':
            reference = next((c for c in checks if c['topic'] == 'H02'), None)
            if reference:
                checks.append(dict(reference, topic='H06', requirement='The nested path returns its independently anchored frame or null when absent.'))

    if method in ['trace_replayTransaction', 'trace_replayBlockTransactions']:
        if method == 'trace_replayBlockTransactions':
            transactions = obj(blocks.get(params[0])).get('transactions')
            if transactions is not None:
                add('H07', isinstance(result, list) and [obj(e).get('transactionHash') for e in result] == [t['hash'] for t in transactions],
                    'Block replay has exactly one envelope per frozen transaction, with hashes in transaction order.')
        elif 'H07' in declared and result is None and name == 'replay-missing':
            explain('H07', 'not_applicable', 'A missing transaction has no replay envelope or transactionHash; H06 checks null.')

    envelopes = ([result] if isinstance(result, dict) else seq(result)
                 if method in ['trace_callMany', 'trace_replayBlockTransactions'] else [])
    frames = [f for e in envelopes for f in seq(obj(e).get('trace')) if isinstance(f, dict)]
    if method in ['trace_block', 'trace_transaction', 'trace_filter']:
        frames = [f for f in seq(result) if isinstance(f, dict)]
    elif method == 'trace_get' and isinstance(result, dict):
        frames = [result]

    if 'H09' in declared and not covered('H09') and status == 'result':
        # A no-failure control is meaningful only for a fixture known to transfer
        # without executing code. Absence of an error alone is not proof.
        if name == 'call-many-transfers':
            add('H09', len(envelopes) == len(params[0]) and all(len(seq(obj(e).get('trace'))) == 1
                and 'error' not in obj(e['trace'][0]) for e in envelopes),
                'Each transfer has one successful root, with no fabricated failure.')
        else:
            if method == 'trace_filter':
                if any(c['topic'] in ['H03','H04','H23'] and c['status']=='change_needed' for c in checks):
                    explain('H09', 'blocked', 'Address selection differs from its reference; failure-bearing frame selection is not established.')
                else:
                    explain('H09', 'not_applicable', 'No failed frame is selected; the address-filter assertion independently checks the selected inventory.')
            else:
                add('H09', False, 'The declared failing execution contains its failed frame.',
                    'No failed frame was returned for this failure-bearing fixture.')

    if 'H10' in declared and status == 'result' and not covered('H10'):
        creations = [f for f in frames if f.get('type') == 'create']
        add('H10', bool(creations) and all('error' in f or all(k in obj(f.get('result')) for k in ['address','code','gasUsed']) for f in creations),
            'The creation fixture contains its CREATE frame and successful creations include address, code and gasUsed.')

    if 'H14' in declared and not covered('H14') and name in ['filter-from-only-intersection', 'filter-to-only-intersection']:
        explain('H14', 'not_applicable', 'A one-sided intersection filter is valid input; H03 checks its result. Invalid-input codes do not apply.')

    if method == 'trace_filter' and params and isinstance(params[0], dict) and status == 'result':
        filt = params[0]
        if 'H04' in declared and not covered('H04'):
            baseline, mismatch = anchor(context, peers, 'block-tree')
            if baseline is not None or mismatch:
                add('H04', result == baseline, 'Omitted address lists impose no address restriction.',
                    'Reference frames contradict the fixture: '+mismatch if mismatch else '')
        if 'after' in filt or 'count' in filt or name in ['filter-transfer', 'withdrawal-filter-51', 'withdrawal-filter-52', 'withdrawal-filter-53']:
            baseline, mismatch = None, None
            for c in context.get('cases', []):
                req = c['request']
                if req['method'] == 'trace_block' and req['params'][0] == filt.get('fromBlock') == filt.get('toBlock'):
                    baseline, mismatch = anchor(context, peers, c['name'])
                    break
            if mismatch:
                add('H03', False, 'Filter the anchored canonical inventory before applying after/count.',
                    'Reference frames contradict the fixture: '+mismatch)
            elif baseline is not None:
                senders=[s.lower() for s in filt.get('fromAddress') or [] if isinstance(s,str)]
                recipients=[s.lower() for s in filt.get('toAddress') or [] if isinstance(s,str)]
                def selected(frame):
                    action=obj(frame.get('action'));kind=frame.get('type')
                    sender,target=action.get('from'),action.get('to')
                    if kind=='create':target=None if 'error' in frame else obj(frame.get('result')).get('address')
                    elif kind=='suicide':sender,target=action.get('address'),action.get('refundAddress')
                    elif kind=='reward':sender,target=None,action.get('author')
                    sides=[]
                    if senders:sides.append(str(sender).lower() in senders)
                    if recipients:sides.append(str(target).lower() in recipients)
                    return any(sides) if filt.get('mode')=='union' and sides else all(sides)
                baseline=[f for f in baseline if selected(f)]
                after, count = filt.get('after', 0), filt.get('count', len(baseline))
                if type(after) is int and type(count) is int and after >= 0 and count >= 0:
                    add('H03', result == baseline[after:after+count], 'Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.')
            elif name in ['filter-transfer','withdrawal-filter-51','withdrawal-filter-52','withdrawal-filter-53'] or any(t in name for t in ['page','filter-zero']):
                explain('H03', 'blocked', 'The per-block reference lacks an independent transaction inventory.')
    if 'H05' in declared and not covered('H05') and status == 'result':
        add('H05', isinstance(result, list) and all(obj(f).get('type') != 'reward' for f in result),
            'The declared PoS range contains no synthetic PoW reward records, including withdrawal blocks.')
    if 'H23' in declared and name == 'transaction-tree':
        explain('H23', 'control', 'This transaction trace anchors CREATE/SELFDESTRUCT identities for the address-filter probes.')
    if 'H27' in declared and name in ['block-35', 'block-36']:
        explain('H27', 'control', 'Per-block reference for the independently anchored fork-crossing filter comparison.')
    if context.get('_chain')=='h30' and name in ['filter-0-to-2','filter-head-only']:
        explain('H32' if name=='filter-0-to-2' else 'H30', 'control',
                'Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.')

    if 'H15' in declared and not covered('H15') and method in ['trace_call','trace_callMany']:
        calls = [params[0]] if method=='trace_call' else [c[0] for c in params[0]]
        add('H15', status=='result' and len(envelopes)==len(calls),
            'Unsigned execution accepts the supplied nonzero fee and returns one envelope per call; exact environment values are checked by coverage/model-environment.')

    if status=='result':
        checks.extend(assess_execution(case,observation,peers,declared & {'H16','H17','H18','H19','H20'}))

    # Independently decoded transaction roots make reference-only pages useful
    # without adopting the client's own list as its inventory.
    if method in ['trace_transaction','trace_block'] and status=='result' and blocks:
        if method=='trace_transaction':
            wanted=[t for b in blocks.values() for t in b['transactions'] if t['hash']==params[0]]
        else:
            selected_blocks=context.get('_alternate_blocks',{}) if name.startswith('after/') else blocks
            wanted=selected_blocks.get(params[0],{}).get('transactions')
        if wanted is not None and (method=='trace_block' or wanted):
            roots=[f for f in frames if f.get('traceAddress')==[] and f.get('type') in ['call','create']]
            add('H02',isinstance(result,list) and [f.get('transactionHash') for f in roots]==[t['hash'] for t in wanted]
                and all(obj(f.get('action')).get('from')==t['sender'] for f,t in zip(roots,wanted)),
                'Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.')
    if method=='trace_filter' and name.startswith(('before/','after/','restored/')) and blocks:
        selected_blocks=context.get('_alternate_blocks',{}) if name.startswith('after/') else blocks
        filt=params[0]
        selected=[b for b in selected_blocks.values() if int(filt['fromBlock'],16)<=b['number']<=int(filt['toBlock'],16)]
        wanted=[(t['hash'],b['hash']) for b in selected for t in b['transactions']]
        roots=[f for f in frames if f.get('traceAddress')==[] and f.get('type') in ['call','create']]
        add('H27',status=='result' and isinstance(result,list) and [(f.get('transactionHash'),f.get('blockHash')) for f in roots]==wanted,
            'Every phase range has exactly the frozen canonical roots and block hashes; restoration returns the original inventory.')

    # Replay arrays need the same numeric/metadata walk as individual envelopes.
    if 'H21' in declared and not covered('H21') and status == 'result':
        vms = [obj(e).get('vmTrace') for e in envelopes]
        valid = bool(vms)
        while vms:
            vm = vms.pop()
            valid &= isinstance(vm, dict) and isinstance(obj(vm).get('ops'), list)
            for op in seq(obj(vm).get('ops')):
                ex = obj(obj(op).get('ex'))
                valid &= all(type(obj(op).get(k)) is int and obj(op)[k] >= 0 for k in ['pc','cost'])
                if ex:
                    valid &= type(ex.get('used')) is int and ex['used'] >= 0
                    valid &= encoding_valid(ex)
                if obj(op).get('sub') is not None:
                    vms.append(op['sub'])
        add('H21', bool(valid), 'Replay VM numeric fields use nonnegative integers; stack words and storage operands use minimal quantities at every depth.')

    if 'H20' in declared and status=='result':
        vms=[obj(e).get('vmTrace') for e in envelopes]
        errors=[error for vm in vms for error in local_invariants(vm)]
        add('H20',bool(vms) and not errors,
            'At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem.',
            '; '.join(errors[:4]))

    # Execute independently supplied straight-line fixtures, including their exact
    # output, opcode gas, same-step writes and stack changes.
    if method == 'trace_call' and params and isinstance(params[0], dict):
        call = params[0]
        model = case.get('model')
        code = model.get('code') if isinstance(model, dict) else None
        if code is None and ('H19' in declared or 'H20' in declared):
            if 'to' not in call:
                code = call.get('data', call.get('input', '0x'))
            else:
                code = context.get('_codes', {}).get(call['to'].lower())
        modes = params[1] if len(params) > 1 else []
        if code is not None and 'vmTrace' in modes and status == 'result':
            env = dict(context.get('_environment', {}), GASPRICE=integer(call.get('gasPrice','0x0')) or 0,
                       CALLVALUE=integer(call.get('value','0x0')) or 0)
            if env['GASPRICE'] == 0:
                env['BASEFEE'] = 0
            vm = obj(result).get('vmTrace')
            add('H19', status == 'result' and obj(vm).get('code') == code,
                'Root VM bytecode equals the independently frozen execution source.')
            try:
                data = call.get('data', call.get('input','0x'))
                gas = int(call['gas'],16)-intrinsic(data, 'to' not in call)
                want, output, reverted = execute(code, gas, '0x' if 'to' not in call else data, env)
            except (UnsupportedProgram, KeyError, ValueError) as exc:
                if 'H20' in declared and not covered('H20'):
                    explain('H20', 'unassessed', 'The bounded VM model cannot establish this program: '+str(exc))
            else:
                errors = differences(vm, want)
                add('H20', status == 'result' and not errors, 'Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects.', '; '.join(errors[:4]))
                add('H08', obj(result).get('output') == output, 'Modelled execution returns exactly the independently computed bytes.')
                if reverted:
                    root=next((f for f in frames if f.get('traceAddress')==[]),{})
                    used=gas-want['ops'][-1]['ex']['used']
                    add('H09',bool(root.get('error')) and obj(root.get('result')).get('output')==output
                        and integer(obj(root.get('result')).get('gasUsed'))==used,
                        'The modelled REVERT root retains its exact return bytes and independently calculated execution gas.')
                if model and model.get('environment'):
                    add('H15', obj(result).get('output') == output,
                        'GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved.')
                if model and model.get('creation') and not reverted and isinstance(obj(result).get('stateDiff'), dict):
                    creations = [f for f in frames if f.get('type') == 'create' and f.get('traceAddress') == []]
                    nonce = context.get('model_nonce')
                    address = ('0x'+keccak(rlp.encode([bytes.fromhex(call['from'][2:]),nonce]))[-20:].hex()
                               if nonce is not None else obj(obj(creations[0]).get('result')).get('address') if creations else None)
                    account = obj(obj(result).get('stateDiff')).get(address)
                    # H08/H15 compare runtime bytes against the independent EVM
                    # model. H17 checks their account-existence encoding: a wrong
                    # BASEFEE/GASLIMIT must not become a second marker failure.
                    runtime = obj(result).get('output')
                    add('H17', isinstance(account, dict) and account.get('nonce') == {'+':'0x1'}
                        and isinstance(runtime, str) and re.fullmatch(r'0x(?:[0-9a-fA-F]{2})*', runtime) is not None
                        and account.get('code') == {'+':runtime} and account.get('balance') == {'+':call.get('value','0x0')},
                        'A new contract has creation markers for nonce one, returned runtime and balance, including empty values.')

    model = case.get('transfer_model')
    if model:
        count = 2 if method == 'trace_callMany' else 1
        add('H08',len(envelopes)==count and all(obj(e).get('output')=='0x' for e in envelopes),
            'Every transfer to the independently empty-code recipient returns empty bytes.')
        base = context['_environment']['BASEFEE']
        before_miner = integer(other('_control/miner-balance'))
        if before_miner is None:
            explain('H16', 'blocked', 'Independent fee-recipient balance unavailable.')
        else:
            add('H16', len(envelopes) == count, 'Return one execution envelope per modelled transfer.')
            for i in range(count):
                envelope = obj(envelopes[i]) if i < len(envelopes) else {}
                diff = obj(envelope.get('stateDiff'))
                sender = obj(diff.get(model['sender']))
                recipient = obj(diff.get(model['target']))
                fee_recipient = obj(diff.get(model['miner']))
                paid, tip = 21000*model['price'], 21000*(model['price']-base)
                before = model['balance']-i*(paid+model['value'])
                changed = lambda a,b: {'*':{'from':hex(a),'to':hex(b)}}
                add('H16', sender.get('balance') == changed(before,before-paid-model['value'])
                    and sender.get('nonce') == changed(model['nonce']+i,model['nonce']+i+1)
                    and fee_recipient.get('balance') == ({'+':hex(tip)} if i==0 and model.get('miner_absent') else changed(before_miner+i*tip,before_miner+(i+1)*tip))
                    and recipient.get('balance') == ({'+':hex(model['value'])} if i==0 else changed(i*model['value'],(i+1)*model['value'])),
                    f'Transfer {i}: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression.',
                    f'Price={model["price"]}, baseFee={base}, gas=21000; expected debit={paid+model["value"]}, tip={tip}.')
                if isinstance(envelope.get('stateDiff'), dict):
                    add('H17', recipient.get('nonce') == ({'+':'0x0'} if i==0 else '=')
                        and recipient.get('code') == ({'+':'0x'} if i==0 else '=')
                        and recipient.get('storage') == {},
                        f'Transfer {i}: new-account markers include zero nonce and empty code; the next call treats the account as existing.')

    # For old broad examples without independently pinned pre/post state, retain
    # specific model gaps. Dedicated coverage fixtures carry exact state anchors.
    for topic in sorted(declared - {c['topic'] for c in checks}):
        if status == 'rpc_error':
            explain(topic, 'blocked', 'The RPC returned an error, so there is no execution result to inspect.')
        else:
            details = {
                'H15': 'No independent block-environment/output model is attached to this legacy execution.',
                'H16': 'This legacy execution lacks independently pinned balance, fee and per-transaction state expectations.',
                'H17': 'This legacy execution lacks an independent pre-state existence and post-state model.',
                'H18': 'This legacy replay lacks per-transaction authorization-state expectations.',
                'H19': 'This legacy replay lacks an independently resolved execution-code model.',
                'H20': 'Nested calls, refunds and exceptional gas boundaries require a separate VM model.',
            }
            explain(topic, 'unassessed', details.get(topic, 'No property-specific model is registered for this declared case.'))
    return checks

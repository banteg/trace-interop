"""Transaction identity, state-existence and accounting models for frozen cases."""
import rlp
from eth_hash.auto import keccak

from .chain_model import decode_transaction
from .vm_model import intrinsic, execute, differences, UnsupportedProgram
from functools import lru_cache


def mapping(value):
    return value if isinstance(value, dict) else {}


def quantity(value):
    try:
        return int(value,16) if isinstance(value,str) else None
    except ValueError:
        return None


def created_address(sender, nonce):
    return '0x'+keccak(rlp.encode([bytes.fromhex(sender[2:]),nonce]))[-20:].hex()


@lru_cache(maxsize=64)
def deployed_code(initcode):
    try:
        _,output,reverted=execute(initcode,10_000_000)
        return None if reverted else output
    except UnsupportedProgram:
        return None


def transactions(case):
    context = case['context']
    blocks = context.get('_blocks', {})
    request = case['request']
    method, params = request['method'], request.get('params', [])
    head = context.get('_head', {}).get('number')
    position=1 if method=='trace_callMany' else 2
    selected = params[position] if method in ['trace_call','trace_callMany'] and len(params)>position else head
    block = blocks.get(selected if selected not in ['latest','pending'] else head, {})
    if method == 'trace_replayBlockTransactions':
        block = blocks.get(params[0], {})
        return [(tx,block,i) for i,tx in enumerate(block.get('transactions',[]))]
    if method in ['trace_replayTransaction','trace_transaction']:
        return [(tx,b,i) for b in blocks.values() for i,tx in enumerate(b['transactions']) if tx['hash']==params[0]]
    if method == 'trace_rawTransaction':
        if len(params)>2:
            return []  # Explicit block extension has its own unresolved contract.
        try:
            return [(decode_transaction(bytes.fromhex(params[0][2:])),block,None)]
        except (ValueError,IndexError,rlp.exceptions.RLPException):
            return []
    if method in ['trace_call','trace_callMany']:
        calls = [params[0]] if method=='trace_call' else [c[0] for c in params[0]]
        return [({'sender':c.get('from','0x'+'00'*20).lower(), 'to':c.get('to'),
                  'value':quantity(c.get('value','0x0')), 'data':c.get('data',c.get('input','0x')),
                  'gas':quantity(c.get('gas','0x0')), 'price_cap':quantity(c.get('gasPrice',c.get('maxFeePerGas','0x0'))),
                  'tip_cap':quantity(c.get('gasPrice',c.get('maxPriorityFeePerGas','0x0'))),
                  'authorizations':[], 'nonce':quantity(c.get('nonce','0x0'))},block,None) for c in calls if isinstance(c,dict)]
    return []


def delegation(address):
    return '0x' if int(address,16)==0 else '0xef0100'+address[2:]


def authorize(tx, exists, codes, nonces, chain_id):
    """Apply valid EIP-7702 tuples in order, after the sender nonce increment; return the applied tuples."""
    applied=[]
    for auth in tx['authorizations']:
        authority=auth['authority']
        code=codes.get(authority,'0x')
        if (auth['chain_id'] not in [0,chain_id] or auth['nonce']!=nonces.get(authority,0)
                or code not in ['0x',None] and not code.startswith('0xef0100')):
            continue
        exists.add(authority)
        codes[authority]=delegation(auth['address'])
        nonces[authority]=auth['nonce']+1
        applied.append(auth)
    return applied


def prestate(context, block, index):
    """Known endpoint existence/code/nonce from genesis and preceding signed fixtures.

The retained chains only create persistent contracts at top level. The calltree's
internal constructor self-destructs within the same transaction.
"""
    codes = dict(context.get('_codes', {}))
    exists = set(context.get('_alloc', {}))
    nonces = {a:int(v.get('nonce','0x0'),16) for a,v in context.get('_alloc', {}).items()}
    for b in context.get('_blocks', {}).values():
        if b['number'] > block.get('number',-1):
            continue
        for i,tx in enumerate(b['transactions']):
            if b['number']==block.get('number') and index is not None and i>=index:
                break
            exists.add(tx['sender'])
            codes.setdefault(tx['sender'],'0x')
            nonces[tx['sender']]=tx['nonce']+1
            if tx['to'] is None:
                address=created_address(tx['sender'],tx['nonce'])
                exists.add(address)
                runtime=deployed_code(tx['data'])
                codes[address]=runtime
                nonces[address]=1
            elif tx['value']:
                exists.add(tx['to'])
                codes.setdefault(tx['to'],'0x')
            authorize(tx,exists,codes,nonces,context.get('_chain_id'))
        # Fees create the recipient if nonzero. Every nonempty fixture block has
        # positive tips; the dedicated model chain has empty blocks and no miner.
        if b['transactions'] and (b['number'] < block.get('number',-1) or index is None or index>0):
            exists.add(b['miner'])
            codes.setdefault(b['miner'],'0x')
    return exists,codes,nonces


def execution_code(tx,codes,exists,nonces,chain_id):
    codes,exists,nonces=dict(codes),set(exists),dict(nonces)
    nonces[tx['sender']]=nonces.get(tx['sender'],0)+1
    authorize(tx,exists,codes,nonces,chain_id)
    code=tx['data'] if tx['to'] is None else codes.get(tx['to'],'0x' if tx['to'] not in exists else None)
    if isinstance(code,str) and code.startswith('0xef0100'):
        target='0x'+code[8:]
        code=codes.get(target,'0x' if target not in exists else None)
    return code


def opcodes(code):
    raw=bytes.fromhex(code[2:])
    i=0
    while i<len(raw):
        yield raw[i]
        i+=1+(raw[i]-0x5f if 0x60<=raw[i]<=0x7f else 0)


def settled_gas(deltas, miner, low, high, tip_price, burn_price, blob):
    """Return the charged gas in [low, high] that settles every observed balance exactly, if any."""
    if any(v is None for v in deltas) or miner is None:
        return None
    total=sum(deltas)
    gas=miner//tip_price if tip_price else -(total+blob)//burn_price if burn_price else low
    return gas if low<=gas<=high and miner==tip_price*gas and total==-(burn_price*gas+blob) else None


def balance_delta(change):
    if change == '=':
        return 0
    if not isinstance(change,dict) or len(change)!=1:
        return None
    if '+' in change:
        return quantity(change['+'])
    if '-' in change:
        n=quantity(change['-'])
        return -n if n is not None else None
    pair=change.get('*')
    if isinstance(pair,dict):
        before,after=quantity(pair.get('from')),quantity(pair.get('to'))
        return after-before if before is not None and after is not None else None
    return None


def assess(case, observation, peers, topics):
    if not topics:
        return []
    context=case['context']
    method=case['request']['method']
    result=mapping(observation.get('response')).get('result')
    if observation.get('status')!='result':
        return []
    models=transactions(case)
    envelopes=result if method in ['trace_replayBlockTransactions','trace_callMany'] and isinstance(result,list) else [result]
    checks=[]
    def observed(name):
        value=mapping(peers.get(name))
        return mapping(value.get('response')).get('result') if value.get('status')=='result' else None
    def add(topic,ok,requirement,detail=''):
        checks.append(dict(topic=topic,status='matches' if ok else 'change_needed',requirement=requirement,detail=detail))
    for i,(tx,block,index) in enumerate(models):
        e=mapping(envelopes[i]) if i<len(envelopes) else {}
        diff=e.get('stateDiff')
        params=case['request']['params']
        modes=params[0][i][1] if method=='trace_callMany' else params[1] if len(params)>1 else []
        state_requested=isinstance(modes,list) and 'stateDiff' in modes
        for topic in sorted(topics & {'H16','H17'}) if state_requested else []:
            if not isinstance(diff,dict):
                if topic == 'H17':
                    checks.append(dict(topic=topic,status='blocked',
                        requirement='Inspect account-existence markers in the requested state diff.',
                        detail='No state-diff object was returned; account markers cannot be assessed.'))
                else:
                    add(topic,False,'The declared state-diff fixture returns the requested account changes.')
        exists,codes,nonces=prestate(context,block,index)
        # Earlier bundle items persist: the sender's nonce, a modelled creation and
        # a funded recipient. Internal value recipients are not modelled, and an
        # unmodelled creation leaves its address undetermined.
        unknown=set()
        for prior,_,_ in models[:i] if method=='trace_callMany' else []:
            exists.add(prior['sender'])
            codes.setdefault(prior['sender'],'0x')
            nonce=nonces.get(prior['sender'],0)
            nonces[prior['sender']]=nonce+1
            if prior['to'] is None:
                address=created_address(prior['sender'],nonce)
                runtime=deployed_code(prior['data'])
                if runtime is None:
                    unknown.add(address)
                else:
                    exists.add(address);codes[address]=runtime;nonces[address]=1
            elif prior['value']:
                exists.add(prior['to'])
                codes.setdefault(prior['to'],'0x')
            if prior['price_cap']>block.get('base_fee',0) and block.get('miner'):
                exists.add(block['miner'])
        if 'H18' in topics and tx['authorizations']:
            after_exists,after_codes,after_nonces=set(exists),dict(codes),dict(nonces)
            after_nonces[tx['sender']]=nonces.get(tx['sender'],0)+1
            applied=authorize(tx,after_exists,after_codes,after_nonces,context.get('_chain_id'))
            for authority in dict.fromkeys(a['authority'] for a in tx['authorizations']):
                born=authority not in exists and authority in after_exists
                def change(before,after):
                    return {'+':after} if born else '=' if before==after else {'*':{'from':before,'to':after}}
                want={'code':change(codes.get(authority,'0x'),after_codes.get(authority,'0x')),
                      'nonce':change(hex(nonces.get(authority,0)),hex(after_nonces.get(authority,0)))}
                account=mapping(mapping(diff).get(authority))
                count=sum(a['authority']==authority for a in applied)
                add('H18',isinstance(diff,dict) and all(account.get(k,'=')==v for k,v in want.items()),
                    'Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing.',
                    f'Authority {authority}; {count} of {sum(a["authority"]==authority for a in tx["authorizations"])} tuples valid; expected {want}.')
        if 'H17' in topics and state_requested and isinstance(diff,dict):
            bad=[]
            for address,account in diff.items():
                account=mapping(account)
                if address.lower() in unknown:
                    continue
                if address.lower() in exists:
                    if any(isinstance(account.get(k),dict) and '+' in account[k] for k in ['balance','nonce','code']):
                        bad.append(address+': existing account has creation markers')
                elif any(account.get(k) != {'+':mapping(account.get(k)).get('+')} for k in ['balance','nonce','code']):
                    bad.append(address+': new account lacks creation markers for all fields')
            add('H17',bool(diff) and not bad,'State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields.', '; '.join(bad[:4]))
        if topics & {'H19','H20'}:
            code=execution_code(tx,codes,exists,nonces,context.get('_chain_id'))
            if code is not None:
                vm=e.get('vmTrace')
                if 'H19' in topics:
                    add('H19',isinstance(vm,dict) and vm.get('code')==code,
                        'The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs.',
                        f'Expected source {code[:100]}.')
                if 'H20' in topics and code not in ['0x','']:
                    env={'GASPRICE':min(tx['price_cap'],block.get('base_fee',0)+tx['tip_cap']),
                         'BASEFEE':block.get('base_fee',0),'NUMBER':block.get('number',0),
                         'TIMESTAMP':block.get('timestamp',0),'GASLIMIT':block.get('gas_limit',0),
                         'CALLVALUE':tx['value'] or 0,'ORIGIN':int(tx['sender'],16),
                         'COINBASE':int(block.get('miner','0x0'),16),'CHAINID':context.get('_chain_id',0),
                         'PREVRANDAO':block.get('prev_randao',0)}
                    # The frozen revert contract only reads this slot; no fixture
                    # transaction can change it. Its expected zero is independent.
                    if tx['to']=='0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3':env['STORAGE']={0x42ff:0}
                    try:
                        gas=tx['gas']-intrinsic(tx['data'],tx['to'] is None)-tx.get('intrinsic_extra',0)
                        want,output,reverted=execute(code,gas,'0x' if tx['to'] is None else tx['data'],env)
                    except (UnsupportedProgram,ValueError,KeyError):
                        pass  # The separately reported local relation still applies.
                    else:
                        errors=differences(vm,want)
                        add('H20',not errors,'The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects.', '; '.join(errors[:4]))
        if 'H16' not in topics or not state_requested or not isinstance(diff,dict):
            continue
        trace=e.get('trace')
        if not isinstance(trace,list) or not trace:
            # Same execution under another trace selection is a relational input,
            # not an independent gas oracle. Mined accounting uses receipt gas below.
            for c in context.get('cases',[]):
                req=c['request']
                original=case['request']
                if req['method']==method and req['params'][0]==original['params'][0] and req['params'][2:]==original['params'][2:]:
                    candidate=observed(c['name'])
                    if isinstance(candidate,dict) and candidate.get('trace'):
                        trace=candidate['trace'];break
        roots=[f for f in trace or [] if isinstance(f,dict) and f.get('traceAddress')==[]]
        def receipt_gas(receipt):
            receipt=mapping(receipt)
            gas=quantity(receipt.get('gasUsed'))
            if (receipt.get('transactionHash')!=tx.get('hash') or receipt.get('blockHash')!=block.get('hash')
                    or gas is None or not 0<=gas<=tx['gas']):
                return None
            return gas
        receipt=observed('_control/receipt/'+tx.get('hash',''))
        gas=receipt_gas(receipt)
        if gas is None and tx.get('hash'):
            for c in context.get('cases',[]):
                if c['request']['method']=='eth_getTransactionReceipt' and c['request']['params']==[tx['hash']]:
                    receipt=observed(c['name'])
                    gas=receipt_gas(receipt)
        source='independent receipt'
        low=gas
        if gas is None and roots:
            used=quantity(mapping(roots[0].get('result')).get('gasUsed'))
            if used is not None:
                data=bytes.fromhex(tx['data'][2:])
                floor=21000+10*sum(1 if b==0 else 4 for b in data)
                spent=intrinsic(tx['data'],tx['to'] is None)+tx.get('intrinsic_extra',0)+used
                # Root gasUsed precedes the EIP-3529 refund of at most a fifth of the
                # spent gas. Only root code without SSTORE and without nested frames
                # is known not to refund.
                code=execution_code(tx,codes,exists,nonces,context.get('_chain_id'))
                refundable=code is None or len(trace)>1 or 0x55 in opcodes(code)
                gas,low=max(spent,floor),max(spent-spent//5 if refundable else spent,floor)
                source='root execution gas plus independently calculated Prague intrinsic/floor cost'+(', less any refund' if refundable else '')
        if gas is None and tx['to'] and tx['data']=='0x' and codes.get(tx['to'],'0x')=='0x':
            gas,low,source=21000,21000,'independent simple-transfer model'
        if gas is None:
            checks.append(dict(topic='H16',status='blocked',requirement='Check accounting against independent gas.',detail='No receipt gas or execution-gas witness was captured.'))
            continue
        blob=0
        if tx.get('type')==3:
            blob_gas,blob_price=quantity(mapping(receipt).get('blobGasUsed')),quantity(mapping(receipt).get('blobGasPrice'))
            if blob_gas is None or blob_price is None:
                checks.append(dict(topic='H16',status='blocked',requirement='Check accounting against independent gas.',detail='The receipt lacks blob gas used or blob gas price.'))
                continue
            blob=blob_gas*blob_price
        base=block.get('base_fee',0)
        price=min(tx['price_cap'],base+tx['tip_cap'])
        # Fee-free calls explicitly bypass admission, but do not pay negative tips.
        tip_price,burn_price=max(price-base,0),min(price,base)
        deltas=[balance_delta(mapping(a).get('balance')) for a in diff.values()]
        miner=balance_delta(mapping(diff.get(block.get('miner'))).get('balance','='))
        settled=settled_gas(deltas,miner,low,gas,tip_price,burn_price,blob)
        add('H16',settled is not None,
            'Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee and blob fee.',
            f'Gas={gas if low==gas else f"{low}..{gas}"} ({source}), price={price}, expected tip={tip_price}/gas, burn={burn_price}/gas, blob fee={blob}.')
    return checks

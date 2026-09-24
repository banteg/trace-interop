"""Decode immutable chain bytes into independent transaction/header anchors."""
from functools import lru_cache

import rlp
from eth_hash.auto import keccak
from eth_keys.datatypes import Signature


def number(raw):
    return int.from_bytes(raw, 'big')


def decode_transaction(raw):
    wire = rlp.encode(raw) if isinstance(raw, list) else raw
    return _decode_transaction(wire)


@lru_cache(maxsize=4096)
def _decode_transaction(raw):
    wire = raw
    typed = raw[0] < 0x80
    kind = raw[0] if typed else 0
    fields = rlp.decode(raw[1:]) if typed else raw if isinstance(raw, list) else rlp.decode(raw)
    if kind == 0:
        nonce, price, gas, to, value, data, v, r, s = fields
        v = number(v)
        parity = (v-35) % 2 if v >= 35 else v-27
        signing = fields[:6]+[(v-35)//2,0,0] if v >= 35 else fields[:6]
        digest = keccak(rlp.encode(signing))
        tip = number(price)
    else:
        if kind not in [1,2,3,4]:
            raise ValueError(f'Unsupported frozen transaction type {kind}')
        nonce = fields[1]
        if kind == 1:
            price, gas, to, value, data = fields[2:7]
            tip = number(price)
        else:
            tip, price, gas, to, value, data = fields[2:8]
            tip = number(tip)
        parity, r, s = number(fields[-3]), fields[-2], fields[-1]
        digest = keccak(bytes([kind])+rlp.encode(fields[:-3]))
    sender = Signature(vrs=(parity,number(r),number(s))).recover_public_key_from_msg_hash(digest).to_address()
    authorizations = []
    access_list=fields[7] if kind==1 else fields[8] if kind else []
    if kind == 4:
        for auth in fields[9]:
            authority = Signature(vrs=(number(auth[3]),number(auth[4]),number(auth[5]))).recover_public_key_from_msg_hash(
                keccak(b'\x05'+rlp.encode(auth[:3]))).to_address()
            authorizations.append({'authority':authority,'address':'0x'+auth[1].hex(),'nonce':number(auth[2]),'chain_id':number(auth[0])})
    return {'hash':'0x'+keccak(wire).hex(), 'sender':sender, 'nonce':number(nonce),
            'gas':number(gas),'price_cap':number(price),'tip_cap':tip,'type':kind,
            'intrinsic_extra':2400*len(access_list)+1900*sum(len(a[1]) for a in access_list)+25000*len(authorizations),
            'to':'0x'+to.hex() if to else None,'value':number(value),'data':'0x'+data.hex(),
            'authorizations':authorizations}


@lru_cache(maxsize=8)
def load_chain(path):
    raw = path.read_bytes()
    blocks, offset = {}, 0
    while offset < len(raw):
        block, _, offset = rlp.codec.consume_item(raw, offset)
        header, transactions, uncles = block[:3]
        n = number(header[8])
        blocks[hex(n)] = {'number':n,'hash':'0x'+keccak(rlp.encode(header)).hex(),
                         'difficulty':number(header[7]),
                         'miner':'0x'+header[2].hex(),'timestamp':number(header[11]),
                         'gas_limit':number(header[9]),'base_fee':number(header[15]) if len(header)>15 else 0,
                         'prev_randao':number(header[13]),'parent_hash':'0x'+header[0].hex(),
                         'excess_blob_gas':number(header[18]) if len(header)>18 else None,
                         'parent_beacon_root':'0x'+header[19].hex() if len(header)>19 else None,
                         'uncles':[{'number':number(u[8]),'miner':'0x'+u[2].hex()} for u in uncles],
                         'transactions':[decode_transaction(t) for t in transactions]}
    return blocks

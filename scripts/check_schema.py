"""Check the pinned generated schema, positive vectors and nested negative vectors."""
import copy
import hashlib
import json
from pathlib import Path

from jsonschema import Draft201909Validator

root=Path(__file__).resolve().parents[1]
file=root/'spec/trace-openrpc.json'
lock=json.loads((root/'spec.lock.json').read_text())
assert hashlib.sha256(file.read_bytes()).hexdigest()==lock['generated_sha256']
doc=json.loads(file.read_text())
methods={m['name']:m for m in doc['methods']}
assert set(methods)=={'trace_call','trace_callMany','trace_rawTransaction','trace_replayTransaction','trace_replayBlockTransactions','trace_block','trace_transaction','trace_get','trace_filter'}
for m in methods.values():
    Draft201909Validator.check_schema(m['result']['schema'])
    for p in m['params']:Draft201909Validator.check_schema(p['schema'])

empty={'output':'0x','trace':[],'stateDiff':None,'vmTrace':None}
frame={'type':'call','action':{'callType':'call','from':'0x'+'11'*20,'to':'0x'+'22'*20,'gas':'0x100','input':'0x','value':'0x0'},'result':{'gasUsed':'0x0','output':'0x'},'subtraces':0,'traceAddress':[], 'blockHash':'0x'+'11'*32,'blockNumber':1,'transactionHash':'0x'+'22'*32,'transactionPosition':0}
examples={'trace_call':empty,'trace_rawTransaction':empty,'trace_callMany':[empty], 'trace_replayTransaction':dict(empty,transactionHash='0x'+'22'*32),'trace_replayBlockTransactions':[dict(empty,transactionHash='0x'+'22'*32)], 'trace_get':frame,'trace_transaction':[frame],'trace_block':[frame],'trace_filter':[frame]}
for name,value in examples.items():Draft201909Validator(methods[name]['result']['schema']).validate(value)
for name in ['trace_get','trace_transaction','trace_replayTransaction']:
    Draft201909Validator(methods[name]['result']['schema']).validate(None)

validator=Draft201909Validator(methods['trace_call']['result']['schema'])
vm={'code':'0x00','ops':[]}
for _ in range(5):
    vm={'code':'0x00','ops':[{'pc':0,'cost':0,'ex':{'used':1,'push':['0x0'],'mem':None,'store':None},'sub':vm}]}
value=dict(empty,vmTrace=vm)
validator.validate(value)
bad=copy.deepcopy(value);node=bad['vmTrace']
for _ in range(5):node=node['ops'][0]['sub']
node['code']='0x0'
assert list(validator.iter_errors(bad)), 'nested odd-length code escaped validation'
bad=copy.deepcopy(value);bad['vmTrace']['ops'][0]['ex']['push']=['0x00']
assert list(validator.iter_errors(bad)), 'padded quantity escaped validation'
bad=copy.deepcopy(empty);bad['output']=None
assert list(validator.iter_errors(bad)), 'null output escaped validation'
print('Validated nine method schemas, positive examples and recursive negative vectors.')

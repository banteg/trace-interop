"""Generate small independently modelled probes on the frozen Prague chain."""
from pathlib import Path
from trace_interop.cli import read, write, sha

root = Path(__file__).resolve().parents[1]
sender = '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf'
target = '0x0000000000000000000000000000000000004444'
miner = '0x0000000000000000000000000000000000000000'
cases = []


def case(name, method, params, **extra):
    cases.append(dict(name=name, request=dict(jsonrpc='2.0', id=1, method=method, params=params), **extra))


for label, address, nonce, balance in [('sender',sender,'0xa',hex(10**18)), ('target',target,'0x0','0x0')]:
    for field, method, expected in [('nonce','eth_getTransactionCount',nonce), ('balance','eth_getBalance',balance), ('code','eth_getCode','0x')]:
        case('_control/'+label+'-'+field, method, [address,'latest'], expected_control=expected)
case('_control/miner-balance', 'eth_getBalance', [miner,'latest'])
case('_control/miner-nonce', 'eth_getTransactionCount', [miner,'latest'], expected_control='0x0')
case('_control/miner-code', 'eth_getCode', [miner,'latest'], expected_control='0x')

programs = {
    'return42': '602a60005260206000f3',
    'mload-expansion': '6040515060006000f3',
    'mload-existing': '602a6000526000515060006000f3',
    'mcopy': '602a6000526020600060205e60406000f3',
    'mcopy-overlap': '602a6000526020600060015e60406000f3',
    'mcopy-zero': '600060ff60ff5e60006000f3',
    'empty-runtime': '60006000f3',
    'revert': '602a60005260206000fd',
    'environment': '3a6000524860205243604052426060524560805260a06000f3',
}
for name, code in programs.items():
    for fee in (['0x0','0x77359400'] if name == 'environment' else ['0x77359400']):
        call = {'from':sender, 'gas':'0x493e0', 'gasPrice':fee, 'data':'0x'+code}
        case('model-'+name+('-free' if fee=='0x0' else ''), 'trace_call', [call,['trace','stateDiff','vmTrace'],'latest'],
             model={'code':'0x'+code,'creation':True,'environment':name=='environment'})
transfer = {'from':sender,'to':target,'gas':'0x186a0','gasPrice':'0x77359400','value':'0x7','data':'0x'}
model = {'sender':sender,'target':target,'miner':miner,'balance':10**18,'nonce':10,'value':7,'price':2_000_000_000,'miner_absent':True}
case('model-transfer', 'trace_call', [transfer,['trace','stateDiff','vmTrace'],'latest'], transfer_model=model)
case('model-many-transfers', 'trace_callMany', [[[transfer,['trace','stateDiff']],[transfer,['trace','stateDiff']]],'latest'], transfer_model=model)
write(root/'fixtures/corpora/coverage.json', {'cases':cases,'model_nonce':10,'description':'Bounded Prague VM, environment, creation markers and exact sequential transfer accounting.'})
checksums=read(root/'fixtures/checksums.json')
checksums['corpora/coverage.json']=sha(root/'fixtures/corpora/coverage.json')
write(root/'fixtures/checksums.json', checksums)

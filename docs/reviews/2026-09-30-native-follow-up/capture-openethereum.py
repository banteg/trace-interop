import argparse
import json
import urllib.request
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument('--endpoint',default='http://127.0.0.1:18745')
parser.add_argument('--output',type=Path,default=Path('openethereum-h26.json'))
args=parser.parse_args()
sender='0x7e5f4552091a69125d5dfcb7b8c2659029395bdf'
target='0xf2e246bb76df876cef8b38ae84130f4f55de395b'
runtime='36156008576000ff5b602a60005500'
init='600f80600b6000396000f3'+runtime
def call(method,params):
    req={'jsonrpc':'2.0','id':1,'method':method,'params':params}
    resp=json.loads(urllib.request.urlopen(urllib.request.Request(args.endpoint, json.dumps(req).encode(),{'Content-Type':'application/json'}),timeout=30).read())
    captures.append({'request':req,'response':resp})
    return resp
captures=[]
print(call('web3_clientVersion',[]))
print(call('eth_getTransactionCount',[sender,'latest']))
print(call('eth_blockNumber',[]))
base={'from':sender,'gas':'0x493e0','gasPrice':'0x0'}
items=[[dict(base,data='0x'+init),['trace','stateDiff']],
       [dict(base,to=target,data='0x'),['trace','stateDiff']],
       [dict(base,to=target,data='0x01'),['trace','stateDiff']]]
response=call('trace_callMany',[items,'latest'])
print(json.dumps(response,indent=2))
print(call('eth_getCode',[target,'latest']))
args.output.write_text(json.dumps({'captures':captures,'runtime':runtime,'initcode':init},indent=2)+'\n')

import json,urllib.request,pathlib
endpoint='http://127.0.0.1:8545';i=0
rows=[]
def rpc(method,params):
 global i;i+=1;q={'jsonrpc':'2.0','id':i,'method':method,'params':params}
 req=urllib.request.Request(endpoint,data=json.dumps(q).encode(),headers={'Content-Type':'application/json'})
 try:r=json.load(urllib.request.urlopen(req,timeout=15))
 except Exception as e:r={'transport_error':str(e)}
 rows.append({'request':q,'response':r});return r
version=rpc('web3_clientVersion',[]);block=rpc('eth_getBlockByNumber',['latest',False]).get('result')
if block is None:raise SystemExit(json.dumps(rows))
selector={'blockHash':block['hash'],'requireCanonical':True};base=int(block['baseFeePerGas'],16)
target='0x0000000000000000000000000000000000001002';sender='0x0000000000000000000000000000000000001001'
overrides={target:{'code':'0x3a600052486020524a6040524360605260806000f3'},sender:{'balance':hex(10**25)}}
blobhash='0x01'+'00'*31
families={'plain-free':{},'blob-omitted-free':{'blobVersionedHashes':[blobhash]},'blob-zero-free':{'blobVersionedHashes':[blobhash],'maxFeePerBlobGas':'0x0'},'blob-omitted-priced':{'blobVersionedHashes':[blobhash],'maxFeePerGas':hex(2*base),'maxPriorityFeePerGas':hex(base)},'blob-zero-priced':{'blobVersionedHashes':[blobhash],'maxFeePerBlobGas':'0x0','maxFeePerGas':hex(2*base),'maxPriorityFeePerGas':hex(base)},'blob-positive-priced':{'blobVersionedHashes':[blobhash],'maxFeePerBlobGas':hex(10**18),'maxFeePerGas':hex(2*base),'maxPriorityFeePerGas':hex(base)}}
summary=[]
for name,fields in families.items():
 call={'from':sender,'to':target,'gas':'0x493e0',**fields}
 for method,params in [('eth_call',[call,selector,overrides]),('trace_call',[call,['trace','stateDiff'],selector,overrides])]:
  r=rpc(method,params);out=r.get('result');out=out.get('output') if isinstance(out,dict) else out
  words=[int(out[n:n+64],16) for n in range(2,len(out),64)] if isinstance(out,str) and out.startswith('0x') else None
  summary.append({'family':name,'method':method,'words':words,'error':r.get('error') or r.get('transport_error')})
for method,params in [('eth_call',[{'from':sender,'to':target,'gas':'0x493e0'},'pending',overrides]),('trace_call',[{'from':sender,'to':target,'gas':'0x493e0'},['trace'],'pending',overrides])]:
 r=rpc(method,params);out=r.get('result');out=out.get('output') if isinstance(out,dict) else out;summary.append({'family':'pending','method':method,'output':out,'error':r.get('error')})
path=pathlib.Path('/tmp/trace-grandfathering-src/reth-probes.json');path.write_text(json.dumps({'version':version,'block':block,'observations':rows,'summary':summary},indent=2)+'\n');print(json.dumps({'version':version,'number':block['number'],'hash':block['hash'],'basefee':base,'summary':summary},indent=2))

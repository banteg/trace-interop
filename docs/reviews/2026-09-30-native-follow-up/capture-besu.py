import argparse, json, os, subprocess, time, urllib.request
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument('--besu', required=True, type=Path)
parser.add_argument('--jdk', required=True, type=Path)
parser.add_argument('--work-dir', required=True, type=Path)
args=parser.parse_args()
root=args.work_dir.resolve(); root.mkdir(parents=True,exist_ok=True)
fixtures=Path(__file__).resolve().parent
env=dict(os.environ,JAVA_HOME=str(args.jdk.resolve()))
binary=args.besu.resolve()
for cap in [30000,100000,50000000]:
    label=f'besu-fixed-cap{cap}'
    args=[str(binary),f'--genesis-file={fixtures}/besu-genesis.json',f'--data-path={root}/{label}-data',
          '--rpc-http-enabled','--rpc-http-host=127.0.0.1','--rpc-http-port=18645',
          '--rpc-http-api=ETH,TRACE,WEB3,NET','--host-allowlist=localhost,127.0.0.1',
          '--engine-rpc-port=18651','--p2p-enabled=false','--discovery-enabled=false',
          '--sync-mode=FULL','--data-storage-format=BONSAI',f'--rpc-gas-cap={cap}']
    captures=[]
    def rpc(method,params):
        req={'jsonrpc':'2.0','id':1,'method':method,'params':params}
        resp=json.loads(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:18645',json.dumps(req).encode(),{'Content-Type':'application/json'}),timeout=30).read())
        captures.append({'request':req,'response':resp})
        return resp
    with (root/(label+'-node.log')).open('w') as log:
        proc=subprocess.Popen(args,stdout=log,stderr=subprocess.STDOUT,env=env)
        try:
            for _ in range(60):
                if proc.poll() is not None: raise RuntimeError('node exited: '+label)
                try: rpc('web3_clientVersion',[]); break
                except OSError: time.sleep(0.5)
            else: raise RuntimeError('node not ready')
            rpc('eth_chainId',[]); rpc('eth_getBlockByNumber',['latest',False])
            for vector in json.loads((fixtures/'transactions.json').read_text()):
                response=rpc('trace_rawTransaction',[vector['raw'],['trace','stateDiff','vmTrace']])
                captures[-1]['name']=vector['name']
                print(cap,vector['name'],response.get('error') or response['result'].get('output'),flush=True)
            rpc('eth_getTransactionCount',['0x7e5f4552091a69125d5dfcb7b8c2659029395bdf','latest'])
            rpc('eth_getStorageAt',['0x0000000000000000000000000000000000001002','0x0','latest'])
            (root/(label+'.json')).write_text(json.dumps({'configuration':label,'rpc_gas_cap':cap,'command':args,'captures':captures},indent=2)+'\n')
        finally:
            proc.terminate()
            try: proc.wait(timeout=15)
            except subprocess.TimeoutExpired: proc.kill();proc.wait()

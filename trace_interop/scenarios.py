"""Small scenario overlays on the pinned Hive simulator; no production node access."""
import json
from pathlib import Path
import subprocess

READINESS = r'''package main
import (
 "context"
 "fmt"
 "net"
 "time"
 "github.com/ethereum/hive/hivesim"
)
// Hive observes port 8545; the authenticated Engine endpoint may open later.
func waitInteropEngine(t *hivesim.T, c *hivesim.Client) {
 for deadline:=time.Now().Add(30*time.Second); time.Now().Before(deadline); {
  conn,err:=net.DialTimeout("tcp",net.JoinHostPort(c.IP.String(),"8551"),time.Second)
  if err==nil {conn.Close();return}
  time.Sleep(100*time.Millisecond)
 }
 t.Fatal("Engine endpoint did not become ready")
}
// An accepted forkchoice can precede publication to the ordinary RPC cache.
func waitInteropHead(t *hivesim.T,c *hivesim.Client,want string) {
 for deadline:=time.Now().Add(30*time.Second);time.Now().Before(deadline); {
  ctx,cancel:=context.WithTimeout(context.Background(),2*time.Second)
  var head struct { Hash string `json:"hash"` }
  err:=c.RPC().CallContext(ctx,&head,"eth_getBlockByNumber","latest",false)
  cancel()
  if err==nil && head.Hash==want {return}
  time.Sleep(100*time.Millisecond)
 }
 t.Fatal(fmt.Sprintf("canonical RPC head did not become %s",want))
}
'''

REORG = r'''package main
import (
 "encoding/json"
 "fmt"
 "os"
 "regexp"
 "time"
 "github.com/ethereum/hive/hivesim"
)
type interopRequest struct { Method string `json:"method"`; Params []any `json:"params"` }
func runInteropScenario(t *hivesim.T, c *hivesim.Client) bool {
 data,err:=os.ReadFile("tests/reorg.json")
 if os.IsNotExist(err) { return false }; if err!=nil { t.Fatal(err) }
 var plan struct { Payloads []interopRequest `json:"payloads"`; Switch interopRequest `json:"switch"`; Restore interopRequest `json:"restore"` }
 if err:=json.Unmarshal(data,&plan);err!=nil { t.Fatal(err) }
 phase:=func(name string) {
  for _,test:=range loadTests(t,"tests/interop/"+name,regexp.MustCompile(".*")) {
   test:=test
   t.Run(hivesim.TestSpec{Name:fmt.Sprintf("interop/%s/%s (%s)",name,test.name,c.Type),Run:func(t *hivesim.T){if err:=runTest(t,c,&test);err!=nil {t.Fatal(err)}}})
  }
 }
 phase("_control"); phase("before")
 for _,req:=range plan.Payloads {
  var reply map[string]any
  err:=c.EngineAPI().Call(&reply,req.Method,req.Params...)
  t.Logf("interop Engine %s: reply=%v error=%v",req.Method,reply,err)
  if err!=nil || reply["status"]=="INVALID" { t.Fatal("alternate payload rejected",err,reply) }
 }
 move:=func(req interopRequest) {
  for i:=0;i<150;i++ {
   var reply struct { PayloadStatus struct { Status string `json:"status"` } `json:"payloadStatus"` }
   err:=c.EngineAPI().Call(&reply,req.Method,req.Params...)
   if err!=nil { t.Fatal(err) }
   if reply.PayloadStatus.Status=="VALID" { t.Logf("interop forkchoice accepted: %v",req.Params); waitInteropHead(t,c,req.Params[0].(map[string]any)["headBlockHash"].(string)); return }
   if reply.PayloadStatus.Status=="INVALID" {t.Fatal("forkchoice invalid")}
   time.Sleep(200*time.Millisecond)
  }
  t.Fatal("forkchoice timed out")
 }
 move(plan.Switch); phase("after"); move(plan.Restore); phase("restored")
 return true
}
'''

ORDERED = r'''package main
import (
 "encoding/json"
 "fmt"
 "os"
 "regexp"
 "github.com/ethereum/hive/hivesim"
)
func runInteropOrdered(t *hivesim.T, c *hivesim.Client) {
 data,err:=os.ReadFile("tests/ordered.json"); if err!=nil {t.Fatal(err)}
 var phases []string
 if err:=json.Unmarshal(data,&phases);err!=nil {t.Fatal(err)}
 // Each Run completes before the next request starts, even when the deliberate
 // capture placeholder fails. Never schedule these phases with RunParallel.
 for _,phase:=range phases {
  for _,test:=range loadTests(t,"tests/interop/"+phase,regexp.MustCompile(".*")) {
   test:=test
   t.Run(hivesim.TestSpec{Name:fmt.Sprintf("interop/%s/%s (%s)",phase,test.name,c.Type),Run:func(t *hivesim.T){if err:=runTest(t,c,&test);err!=nil {t.Fatal(err)}}})
  }
 }
}
'''


def ordered_cases(corpus):
    """Validate phase coverage before selecting an indivisible ordered scenario."""
    phases = corpus['scenario_phases']
    if (not phases or len(set(phases)) != len(phases)
            or any(not isinstance(p,str) or not p or '/' in p or p in ['.','..','_control'] for p in phases)):
        raise ValueError('invalid ordered scenario phases')
    used = {c['name'].split('/')[0] for c in corpus['cases'] if '/' in c['name']}
    if used != set(phases) or any('/' not in c['name'] for c in corpus['cases']):
        raise ValueError('ordered scenario phases must cover every case')
    return corpus['cases']


PRUNE = '''# Prune only the disposable imported test database, retaining headers/receipts.
cat > /trace-prune.toml <<'CONFIG'
[prune]
block_interval = 1
minimum_pruning_distance = 0
[prune.segments]
account_history = { before = 44 }
storage_history = { before = 44 }
CONFIG
$reth prune --datadir "$DATADIR" --chain /genesis.json --config /trace-prune.toml || exit 1
FLAGS="$FLAGS --config /trace-prune.toml"

'''


def prepare(hive, corpus, name, clients, head_hash):
    sim=hive/'simulators/ethereum/rpc-compat'
    # Only restore files this adapter owns inside our dedicated dependency checkout.
    for relative in ['simulators/ethereum/rpc-compat/main.go','clients/reth/reth.sh','clients/go-ethereum/geth.sh']:
        original=subprocess.check_output(['git','show','HEAD:'+relative],cwd=hive)
        (hive/relative).write_bytes(original)
    if any(c['client']=='go-ethereum' for c in clients.values()):
        p=hive/'clients/go-ethereum/geth.sh';text=p.read_text()
        needle='admin,debug,eth,miner'
        if text.count(needle)!=2:raise ValueError('pinned Geth API flags changed')
        p.write_text(text.replace(needle,'admin,debug,trace,eth,miner'))
    (sim/'interop_scenario.go').unlink(missing_ok=True)
    (sim/'interop_readiness.go').write_text(READINESS)
    p=sim/'main.go';text=p.read_text();needle='sendForkchoiceUpdated(t, c)'
    if text.count(needle)!=1:raise ValueError('pinned Hive readiness insertion point changed')
    p.write_text(text.replace(needle,'waitInteropEngine(t, c)\n\t\t\t'+needle))
    if name in ['reorg','reorg-safe']:
        # A complete scenario is small; case-level selection still needs all phase controls.
        (sim/'tests/reorg.json').write_text(json.dumps(corpus['plan'])+'\n')
        if 'initial_fcu' in corpus:
            (sim/'tests/headfcu.json').write_text(json.dumps(corpus['initial_fcu'])+'\n')
        p=sim/'main.go';text=p.read_text();needle='sendForkchoiceUpdated(t, c)'
        if text.count(needle)!=1:raise ValueError('pinned Hive scenario insertion point changed')
        p.write_text(text.replace(needle,needle+'\n\t\t\tif runInteropScenario(t, c) { return }'))
        (sim/'interop_scenario.go').write_text(REORG)
    else:
        p=sim/'main.go';text=p.read_text()
        p.write_text(text.replace(needle, needle+'\n\t\t\twaitInteropHead(t, c, '+json.dumps(head_hash)+')'))
        if corpus.get('scenario_phases'):
            ordered_cases(corpus)
            (sim/'tests/ordered.json').write_text(json.dumps(['_control']+corpus['scenario_phases'])+'\n')
            (sim/'interop_scenario.go').write_text(ORDERED)
            text=p.read_text();needle='runAllTests(t, c, c.Type)'
            if text.count(needle)!=1:raise ValueError('pinned Hive ordered insertion point changed')
            p.write_text(text.replace(needle,'runInteropOrdered(t, c)'))
    if name=='pruned':
        if any(c['client']!='reth' for c in clients.values()):
            raise ValueError('pruned scenario has a verified Reth adapter only; select Reth clients')
        p=hive/'clients/reth/reth.sh';text=p.read_text();needle='# Launch the main client.'
        if text.count(needle)!=1:raise ValueError('pinned Reth pruning insertion point changed')
        p.write_text(text.replace(needle,PRUNE+needle))


def assessed_cases(captured, corpus):
    """Captured requests with the current corpus expectations for the identical request.

    Observations stay immutable; expectation fields (fee policy, models, references)
    follow the checksummed corpus, so a corrected expectation reassesses old evidence.
    A request that has since changed keeps the expectations it was captured with.
    """
    current = {c['name']: c for c in corpus}
    return [current[c['name']] if c['name'] in current and current[c['name']]['request'] == c['request'] else c
            for c in captured]


def verify_state(corpus_name, corpus, observations, client):
    def result(name):
        observation = observations.get(name, {}).get(client, {})
        return observation.get('response', {}).get('result') if observation.get('status') == 'result' else None
    for case in corpus.get('cases', []):
        if case.get('expected_control') is not None and result(case['name']) != case['expected_control']:
            return False, 'Independent setup control failed or unavailable: '+case['name']
        # A control may pin only the fields it derives independently, such as receipt gas.
        fields = case.get('expected_control_fields')
        value = result(case['name']) if fields is not None else None
        if fields is not None and (not isinstance(value, dict) or any(value.get(k) != v for k, v in fields.items())):
            return False, 'Independent setup control failed or unavailable: '+case['name']
    if corpus_name == 'raw-validation':
        controls = corpus.get('controls', {})
        head = result('_control/head')
        ok = bool(controls) and all(result(name) == expected for name, expected in controls.items())
        ok = ok and isinstance(head, dict) and head.get('baseFeePerGas') == corpus['base_fee']
        return ok, 'requires independently verified nonce, balance, sender code, chain ID, base fee and marker code/storage'
    if corpus_name in ['reorg','reorg-safe']:
        for phase,key in [('before','heads_a'),('after','heads_b'),('restored','heads_a')]:
            header=result(phase+'/head')
            if not isinstance(header,dict) or header.get('hash')!=corpus[key][-1]['hash']:
                return False, 'canonical '+phase+' head not established'
        return True, 'canonical switch and restoration verified'
    if corpus_name=='precompile-values':
        ok=(result('_control/create-nonce') == hex(corpus['sender_nonce'])
            and result('_control/target-balance') == '0x0'
            and result('_control/target-nonce') == '0x0'
            and result('_control/target-code') == '0x')
        return ok, 'requires sender nonce 133 and an empty, unfunded future creation address'
    if corpus_name=='pruned':
        header,receipt,latest=result('old-header'),result('old-receipt'),result('latest-call')
        valid=isinstance(header,dict) and header.get('number')=='0x2' and isinstance(receipt,dict) and isinstance(latest,dict) and latest.get('output')=='0x'+f'{42:064x}'
        nonce_observation=observations.get('old-nonce',{}).get(client,{})
        nonce_error=nonce_observation.get('response',{}).get('error') if nonce_observation.get('status') == 'rpc_error' else None
        def unavailable(error):
            message=error.get('message','') if isinstance(error,dict) else ''
            message=message.lower() if isinstance(message,str) else ''
            return isinstance(error,dict) and (error.get('code') in (4444, -32002) or 'prun' in message or 'insufficient changesets to revert' in message)
        valid=valid and unavailable(nonce_error)
        return bool(valid), 'requires retained old header/receipt, successful latest call, and independently unavailable old state'
    return True, 'ordinary imported-chain scenario'


def verify_setup(manifest, corpus, observations, client, launches=()):
    """Require correlated controls for both imported identity and canonical RPC head."""
    # A scenario that stopped at an Engine API step reports that step's error, not the
    # first control it never reached.
    for launch in launches:
        if launch.get('name') == f'client launch ({client})' and not launch.get('pass'):
            lines = [line for line in str(launch.get('log', '')).splitlines() if line.strip()]
            return False, 'Scenario setup stopped: '+(lines[-1] if lines else 'client launch failed')
    requests = {c['name']: c['request'] for c in manifest['selected_cases']}
    if corpus.get('scenario_phases'):
        ordered_cases(corpus)
        if (manifest.get('scenario_phases') != corpus['scenario_phases']
                or any(requests.get(c['name']) != c['request'] for c in corpus['cases'])):
            return False, 'Ordered scenario plan or requests not established by the capture'
    head = manifest['head']
    for name, block in [('_control/head', head.get('number')), ('_control/latest', 'latest')]:
        request = requests.get(name, {})
        observation = observations.get(name, {}).get(client, {})
        response = observation.get('response')
        actual = response.get('result') if isinstance(response, dict) else None
        if (request.get('method') != 'eth_getBlockByNumber' or request.get('params') != [block, False]
                or observation.get('status') != 'result' or not isinstance(actual, dict)
                or not all(key in head and actual.get(key) == head[key]
                           for key in ['number', 'hash', 'stateRoot', 'transactionsRoot', 'receiptsRoot'])):
            return False, 'Valid '+name+' does not establish the frozen canonical head'
    # Legacy controls without an expected_control field still have a known height.
    for case in manifest['selected_cases']:
        if case['request']['method'] == 'eth_blockNumber':
            obs = observations.get(case['name'], {}).get(client, {})
            if obs.get('status') != 'result' or obs.get('response', {}).get('result') != head['number']:
                return False, 'Canonical height control failed: '+case['name']
    # Controls are the captured cases, judged by their current definition when the request is unchanged.
    cases = assessed_cases(manifest['selected_cases'], corpus.get('cases', []))
    return verify_state(manifest.get('corpus', ''), dict(corpus, cases=cases), observations, client)

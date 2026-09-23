"""Fresh sequential captures against immutable builds; retain incomplete runs."""
import argparse
from pathlib import Path
import subprocess
import sys

from trace_interop.cli import read, write

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--native-lock',default='locks/clients-2026-09-21.json')
p.add_argument('--geth-lock',default='locks/geth-trace.json')
p.add_argument('--output',required=True)
p.add_argument('--corpora',default='initial,a,repeat,forks,fork-followup,precompiles,precompile-values,raw-validation,coverage,callmany-isolation,h30,reorg-safe,pruned')
args=p.parse_args()
out=Path(args.output).resolve()
out.mkdir(parents=True,exist_ok=False)
lock=read(args.native_lock)
geth=read(args.geth_lock)
if lock['hive_commit']!=geth['hive_commit']:
    raise ValueError('incompatible Hive revisions')
lock['clients'].update(geth['clients'])
write(out/'clients.lock.json',lock)
results=[]
for corpus in args.corpora.split(','):
    command=[sys.executable,'-m','trace_interop','run','--lock',str(out/'clients.lock.json'),
             '--corpus',corpus,'--output',str(out/corpus)]
    if corpus=='pruned':command+=['--clients','reth_release,reth_development']
    print('Capturing '+corpus,flush=True)
    with (out/(corpus+'.log')).open('w') as log:
        process=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT)
    summary=read(out/corpus/'summary.json') if (out/corpus/'summary.json').exists() else {}
    results.append(dict(corpus=corpus,exit_code=process.returncode,complete=summary.get('complete',False),
                        exchanges=summary.get('exchange_count',0),eligible=summary.get('eligible',{})))
    write(out/'matrix.json',results)
    print(results[-1],flush=True)
sys.exit(int(any(r['exit_code'] for r in results)))

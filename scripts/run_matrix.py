"""Resolve latest releases/development builds, then capture one immutable matrix."""
import argparse
from pathlib import Path
import subprocess
import sys

from trace_interop.cli import read, write
from trace_interop.versions import matrix_lock, check_current

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--reproduce-lock',help='explicitly reproduce a historical combined nine-build lock instead of refreshing')
p.add_argument('--output',required=True)
p.add_argument('--corpora',default='initial,a,repeat,forks,fork-followup,precompiles,precompile-values,raw-validation,coverage,fee-policy,fee-compat,callmany-isolation,h30,probes-prague,probes-forks,reorg-safe,pruned')
args=p.parse_args()
out=Path(args.output).resolve()
out.mkdir(parents=True,exist_ok=False)
lock=matrix_lock(out/'clients.lock.json',args.reproduce_lock)
write(out/'preflight.json', check_current(lock) if not args.reproduce_lock else
      {'status':'historical-reproduction','lock':str(Path(args.reproduce_lock).resolve())})
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

"""Pin a clean, built execution-apis checkout without copying editable YAML."""
import hashlib,json,os,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
checkout=Path(sys.argv[1]).resolve()
def git(*args):return subprocess.check_output(['git',*args],cwd=checkout,text=True).strip()
if git('status','--porcelain'):raise SystemExit('spec checkout is dirty; commit it before pinning')
env=dict(os.environ,GOTOOLCHAIN='go1.26.1')
subprocess.run(['make','build'],cwd=checkout,env=env,check=True)
if git('status','--porcelain'):raise SystemExit('build changed tracked spec files')
doc=json.loads((checkout/'openrpc.json').read_text())
doc['methods']=[m for m in doc['methods'] if m['name'].startswith('trace_')]
if len(doc['methods'])!=9:raise SystemExit('expected nine trace methods')
file=root/'spec/trace-openrpc.json';file.parent.mkdir(exist_ok=True)
file.write_text(json.dumps(doc,indent=2)+'\n')
lock={'repository':'https://github.com/banteg/execution-apis','branch':'feat/trace','commit':git('rev-parse','HEAD'),'generated_sha256':hashlib.sha256(file.read_bytes()).hexdigest()}
(root/'spec.lock.json').write_text(json.dumps(lock,indent=2)+'\n')
print('Pinned',lock['commit'])

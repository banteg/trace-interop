"""Build an isolated Geth source snapshot and lock its local Docker image."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def output(*args, cwd=None):
    return subprocess.check_output(args, cwd=cwd, text=True).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--reference', type=Path, help='rebuild the source and base image pinned by an existing Geth lock')
    parser.add_argument('--allow-dirty', action='store_true', help='label a development build explicitly')
    args = parser.parse_args()
    source = args.source.resolve()
    if args.output.exists():
        parser.error('choose a new lock path')
    if os.uname().sysname != 'Linux':
        parser.error('build on Linux for the Hive runtime')
    dirty = bool(output('git', 'status', '--porcelain', cwd=source))
    if dirty and not args.allow_dirty:
        parser.error('commit the source first, or use --allow-dirty for a development capture')
    commit = output('git', 'rev-parse', 'HEAD', cwd=source)
    date = output('git', 'show', '-s', '--format=%cs', 'HEAD', cwd=source)
    reference = json.loads(args.reference.read_text())['clients']['go-ethereum_trace'] if args.reference else None
    if reference and (dirty or commit != reference['source']['commit']):
        parser.error('reference rebuild requires the exact clean source commit')
    tree = hashlib.sha256()
    files = subprocess.check_output(['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], cwd=source).split(b'\0')
    with tempfile.TemporaryDirectory(prefix='trace-geth-') as folder:
        work = Path(folder)
        snapshot = work/'source'
        snapshot.mkdir()
        for name in sorted(set(files)):
            if not name:
                continue
            relative = Path(os.fsdecode(name))
            original = source/relative
            if not original.is_file():  # Omit submodule gitlinks and deleted files.
                continue
            data = original.read_bytes()
            tree.update(name+b'\0'+hashlib.sha256(data).digest())
            target = snapshot/relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(original, target)
        if reference and tree.hexdigest() != reference['source']['tree_sha256']:
            parser.error('source snapshot differs from reference')
        version = commit + ('-dirty' if dirty else '')
        env = dict(os.environ, CGO_ENABLED='0', GOTOOLCHAIN='go1.26.1', GOMAXPROCS='16')
        command = ['go','build','-trimpath','-buildvcs=false','-ldflags',
                   f'-X github.com/ethereum/go-ethereum/internal/version.gitCommit={version} -X github.com/ethereum/go-ethereum/internal/version.gitDate={date}',
                   '-o',str(work/'geth'),'./cmd/geth']
        subprocess.run(command,cwd=snapshot,env=env,check=True)
        binary_sha = hashlib.sha256((work/'geth').read_bytes()).hexdigest()
        if reference and binary_sha != reference['build']['binary_sha256']:
            parser.error('rebuilt binary differs from reference')
        requested_base = reference['build']['base_image'] if reference else 'alpine:3.23'
        subprocess.run(['docker','pull',requested_base],check=True)
        base = json.loads(output('docker','image','inspect',requested_base))[0]['RepoDigests'][0]
        recipe = f'FROM {base}\nCOPY geth /usr/local/bin/geth\nENTRYPOINT ["/usr/local/bin/geth"]\n'
        (work/'Dockerfile').write_text(recipe)
        # Keep the build context to the binary and recipe, excluding the source snapshot.
        (work/'.dockerignore').write_text('source\n')
        tag = 'trace-interop/geth-source:'+binary_sha
        subprocess.run(['docker','build','-t',tag,str(work)],check=True)
        meta = json.loads(output('docker','image','inspect',tag))[0]
    root = Path(__file__).resolve().parents[1]
    hive = json.loads((root/'locks/clients-2026-09-21.json').read_text())['hive_commit']
    lock = {'hive_commit':hive,'resolved_at':dt.datetime.now(dt.timezone.utc).isoformat(),
            'clients':{'go-ethereum_trace':{'client':'go-ethereum','requested':'banteg/go-ethereum:feat/trace',
                'local_image':tag,'image_id':meta['Id'],'architecture':meta['Architecture'],
                'source':{'repository':'https://github.com/banteg/go-ethereum','commit':commit,'dirty':dirty,'tree_sha256':tree.hexdigest()},
                'build':{'toolchain':'go1.26.1','cgo':False,'binary_sha256':binary_sha,'base_image':base,'dockerfile':recipe,
                         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}}}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(lock,indent=2,sort_keys=True)+'\n')
    print(args.output)


if __name__=='__main__':
    main()

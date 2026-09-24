"""Portable Hive execution and immutable evidence collection."""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HIVE = '43ea47bef5761351e3da7b726050ea80ab362c52'
CHAINS = {'initial': 'initial', 'a': 'a', 'repeat': 'a', 'fixed': 'a',
          'forks': 'forks', 'fork-followup': 'forks', 'boundary-repeat': 'forks',
          'reorg': 'a', 'reorg-safe': 'a', 'pruned': 'a', 'precompiles': 'a', 'precompile-values': 'a', 'raw-validation': 'raw-validation', 'coverage': 'raw-validation', 'fee-policy': 'raw-validation', 'fee-compat': 'raw-validation', 'callmany-isolation': 'a', 'h30': 'a',
          'probes-prague': 'raw-validation', 'probes-forks': 'forks'}
from .versions import NAMES


def read(path):
    return json.loads(Path(path).read_text())


def serialize(value):
    return json.dumps(value, indent=2, sort_keys=True) + '\n'


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(serialize(value))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


# A run keeps its observations as observations.json (the original, indented form) or as
# observations.json.gz: compact JSON that omits each parsed response decode_response
# re-derives from the retained wire string. Both load to the same mapping.
OBSERVATIONS = 'observations.json'
COMPACT_OBSERVATIONS = 'observations.json.gz'


def reject_constant(value):
    raise ValueError(f'Not a JSON number: {value}')


def sorted_object(pairs):
    return dict(sorted(dict(pairs).items()))


def decode_response(raw):
    """Parse one wire response strictly (ValueError for anything but JSON).

    Objects come back with sorted keys, as a written observations file reads back, so a
    response derived at load time is indistinguishable from one read from the original file.
    """
    return json.loads(raw, parse_constant=reject_constant, object_pairs_hook=sorted_object)


NOT_DERIVED = object()


def derived_response(entry):
    """The response decode_response derives from an entry's wire string, or NOT_DERIVED."""
    if 'raw_response' not in entry:
        return NOT_DERIVED
    try:
        return decode_response(entry['raw_response'])
    except ValueError:
        return NOT_DERIVED


def compact_observations(observations):
    """Omit every parsed response that decode_response derives exactly from raw_response."""
    def canonical(value):
        return json.dumps(value, sort_keys=True)
    compact = {}
    for case, clients in observations.items():
        compact[case] = {}
        for client, entry in clients.items():
            derived = derived_response(entry)
            if 'response' not in entry and derived is not NOT_DERIVED:
                raise ValueError(f'{case}/{client}: a decodable response without a parsed form is not representable')
            if 'response' in entry and derived is not NOT_DERIVED and canonical(derived) == canonical(entry['response']):
                entry = {k: v for k, v in entry.items() if k != 'response'}
            compact[case][client] = entry
    return compact


def expand_observations(compact):
    """Restore each omitted response; entries whose wire string does not decode stay as stored."""
    for clients in compact.values():
        for client, entry in clients.items():
            if 'response' not in entry and (derived := derived_response(entry)) is not NOT_DERIVED:
                clients[client] = dict(sorted({**entry, 'response': derived}.items()))
    return compact


def compact_bytes(observations):
    """Deterministic gzip of the compact form: identical observations give identical bytes."""
    text = json.dumps(compact_observations(observations), sort_keys=True, separators=(',', ':'))
    return gzip_bytes(text.encode())


def write_observations(folder, observations):
    (Path(folder) / COMPACT_OBSERVATIONS).write_bytes(compact_bytes(observations))


def observations_file(folder):
    compact = Path(folder) / COMPACT_OBSERVATIONS
    return compact if compact.exists() else Path(folder) / OBSERVATIONS


def load_observations(folder):
    path = observations_file(folder)
    if path.name == COMPACT_OBSERVATIONS:
        return expand_observations(json.loads(gzip.decompress(path.read_bytes())))
    return read(path)


def gzip_bytes(data):
    """Deterministic gzip: identical bytes give identical archives."""
    return gzip.compress(data, compresslevel=9, mtime=0)


def log_bytes(path):
    """A capture log's original bytes, whether stored plainly or as path + '.gz'."""
    path = Path(path)
    return path.read_bytes() if path.exists() else gzip.decompress(Path(str(path) + '.gz').read_bytes())


def compress_logs(folder):
    """Replace each .log file under a run with its deterministic gzip; bytes are unchanged."""
    for path in sorted(Path(folder).rglob('*.log')):
        Path(str(path) + '.gz').write_bytes(gzip_bytes(path.read_bytes()))
        path.unlink()


def evidence_bytes(folder, name):
    """The bytes a run's checksums.json entry covers. A run converted to the compact form keeps
    its original observations.json checksum; that entry is checked against the original
    writer's serialization of the reconstructed observations. A compressed log keeps its
    original checksum, checked against the decompressed bytes."""
    path = Path(folder) / name
    if name == OBSERVATIONS and not path.exists() and (Path(folder) / COMPACT_OBSERVATIONS).exists():
        return serialize(load_observations(folder)).encode()
    if name.endswith('.log'):
        return log_bytes(path)
    return path.read_bytes()


def verify_evidence(folder):
    for name, digest in read(Path(folder) / 'checksums.json').items():
        if hashlib.sha256(evidence_bytes(folder, name)).hexdigest() != digest:
            raise ValueError(f'evidence modified: {Path(folder).name}/{name}')


def run(*args, cwd=None, capture=False):
    env = dict(os.environ)
    if args and args[0] == "go":
        env["GOTOOLCHAIN"] = "go1.26.1"
    return subprocess.run(args, cwd=cwd, check=True, text=True, env=env,
                          stdout=subprocess.PIPE if capture else None).stdout


def docker_state():
    """Dangling volumes and tagged Hive image IDs, to find what one capture leaves behind."""
    volumes = set(run('docker', 'volume', 'ls', '-q', '--filter', 'dangling=true', capture=True).split())
    images = set(run('docker', 'images', '-q', '--no-trunc', '--filter', 'reference=hive/*/*', capture=True).split())
    return volumes, images


def remove_capture_leftovers(before, created_tags=()):
    """Remove what one capture left: Hive removes client containers but not their anonymous
    volumes, and it untags the previous hive/* image when it rebuilds one; the capture's own
    base tags follow. Everything else, including images still tagged elsewhere and their
    layers, stays for the next capture."""
    volumes, images = before
    left = set(run('docker', 'volume', 'ls', '-q', '--filter', 'dangling=true',
                   '--filter', 'label=com.docker.volume.anonymous', capture=True).split()) - volumes
    untagged = images - set(run('docker', 'images', '-q', '--no-trunc', '--filter', 'reference=hive/*/*', capture=True).split())
    dangling = set(run('docker', 'images', '-q', '--no-trunc', '--filter', 'dangling=true', capture=True).split())
    for kind, names in [('volume', sorted(left)), ('image', sorted(untagged & dangling)), ('image', list(created_tags))]:
        if names:
            subprocess.run(['docker', kind, 'rm', *names], stdout=subprocess.DEVNULL, check=False)


def verify():
    manifest = read(ROOT / 'fixtures/checksums.json')
    for name, expected in manifest.items():
        if sha(ROOT / 'fixtures' / name) != expected:
            raise ValueError(f'fixture changed: {name}')
    for corpus in (ROOT / 'fixtures/corpora').glob('*.json'):
        cases = read(corpus)['cases']
        names = [c['name'] for c in cases]
        if not names or len(set(names)) != len(names):
            raise ValueError(f'empty or duplicate cases: {corpus.name}')
    from .inventory import verify_inventory
    decisions = verify_inventory(ROOT)
    print(f'Verified {len(manifest)} frozen inputs and {decisions} decisions against the report inventory.')



def resolve(args):
    from .versions import resolve_native
    resolve_native(args.output, args.clients.split(','))


DOCKERFILE = '''FROM golang:1.26.1-alpine AS builder
RUN apk add --no-cache gcc musl-dev linux-headers
WORKDIR /source
COPY go.mod go.sum ./
RUN go mod download
COPY *.go ./
ENV GOMAXPROCS=6
RUN go build -p 6 -o rpc-compat .
FROM alpine:latest
WORKDIR /source
COPY --from=builder /source/rpc-compat .
COPY tests ./tests
COPY openrpc.json ./openrpc.json
ENTRYPOINT ["./rpc-compat"]
'''


def checkout():
    path = ROOT / '.cache/hive'
    if not path.exists():
        path.mkdir(parents=True)
        run('git', 'init', '-q', str(path))
        run('git', 'remote', 'add', 'origin', 'https://github.com/ethereum/hive.git', cwd=path)
        run('git', 'fetch', '--depth=1', 'origin', HIVE, cwd=path)
        run('git', 'checkout', '--detach', 'FETCH_HEAD', cwd=path)
    if run('git', 'rev-parse', 'HEAD', cwd=path, capture=True).strip() != HIVE:
        raise ValueError('Hive cache is at an unexpected revision')
    if not (path / 'hive').exists():
        run('go', 'build', '-o', 'hive', '.', cwd=path)
    return path


def selected_cases(corpus, pattern):
    cases = [c for c in corpus['cases'] if re.search(pattern, c['name'])]
    if not cases:
        raise ValueError('case selector matched zero cases')
    if corpus.get('scenario_phases'):
        from .scenarios import ordered_cases
        return ordered_cases(corpus)
    selected = {c['name'] for c in cases}
    # Setup controls remain mandatory even for a single selected probe.
    cases += [c for c in corpus['cases'] if c['name'] not in selected
              and (c['name'].startswith(('control-', '_control/'))
                   or c.get('expected_control') is not None)]
    return cases


def execute(args):
    # Capture source state before creating the run's own untracked artifacts.
    source_commit = run('git', 'rev-parse', 'HEAD', cwd=ROOT, capture=True).strip()
    source_dirty = bool(run('git', 'status', '--porcelain', cwd=ROOT, capture=True))
    verify()
    out = Path(args.output).resolve()
    if out.exists():
        raise ValueError('use a new run directory; observations are immutable')
    if args.corpus not in CHAINS:
        raise ValueError('this corpus requires a scenario adapter; see docs/scenarios.md')
    lock = read(args.lock)
    if lock['hive_commit'] != HIVE:
        raise ValueError('lock and runner Hive revisions differ')
    names = args.clients.split(',') if args.clients else list(lock['clients'])
    if not names or len(names) != len(set(names)) or any(n not in lock['clients'] for n in names):
        raise ValueError('client selection must contain distinct locked clients')
    corpus = read(ROOT / 'fixtures/corpora' / (args.corpus + '.json'))
    cases = selected_cases(corpus, args.case)
    if args.corpus in ['reorg', 'reorg-safe']:
        cases = corpus['cases']  # Canonical transitions require all three phases.
    elif any(c['request']['method'] in ['trace_filter', 'trace_get'] for c in cases):
        names_selected = {c['name'] for c in cases}
        cases += [c for c in corpus['cases'] if c['name'] not in names_selected and (c['request']['method'] == 'trace_transaction' or c['name'] == 'block-tree' or c['name'].startswith('block-'))]
    chain = ROOT / 'fixtures/chains' / CHAINS[args.corpus]
    head = read(chain / 'headblock.json')
    cases = [{'name': '_control/head', 'request': {'jsonrpc': '2.0', 'id': 1,
              'method': 'eth_getBlockByNumber', 'params': [head['number'], False]}},
             {'name': '_control/latest', 'request': {'jsonrpc': '2.0', 'id': 1,
              'method': 'eth_getBlockByNumber', 'params': ['latest', False]}},
             {'name': '_control/version', 'request': {'jsonrpc': '2.0', 'id': 1,
              'method': 'web3_clientVersion', 'params': []}}] + cases
    # Receipt gas is independent of the trace under assessment. Retain one control
    # per mined replay so accounting does not adopt a client's trace gas as truth.
    from .chain_model import load_chain
    blocks = load_chain(chain/'chain.rlp')
    txhashes = set()
    for case in list(cases):
        request = case['request']
        if request['method'] == 'trace_replayTransaction':
            if any(t['hash']==request['params'][0] for b in blocks.values() for t in b['transactions']):
                txhashes.add(request['params'][0])
        elif request['method'] == 'trace_replayBlockTransactions':
            txhashes.update(t['hash'] for t in blocks.get(request['params'][0],{}).get('transactions',[]))
    cases += [{'name':'_control/receipt/'+h, 'request':{'jsonrpc':'2.0','id':1,'method':'eth_getTransactionReceipt','params':[h]}} for h in sorted(txhashes)]
    if args.corpus not in ['reorg','reorg-safe'] and not corpus.get('scenario_phases'):
        needed = set()
        for case in cases:
            request=case['request']
            if request['method']!='trace_filter' or not request.get('params') or not isinstance(request['params'][0],dict):
                continue
            filt=request['params'][0]
            def bound(value):
                if value in ['latest','safe','finalized',None]:return int(head['number'],16)
                if value=='earliest':return 0
                try:return int(value,16)
                except (ValueError,TypeError):return None
            start,end=bound(filt.get('fromBlock')),bound(filt.get('toBlock'))
            if start is not None and end is not None and 0<=end-start<=64:
                needed.update(hex(n) for n in range(start,end+1) if hex(n) in blocks)
        present={c['request']['params'][0] for c in cases if c['request']['method']=='trace_block'}
        cases += [{'name':'_reference/block/'+n, 'request':{'jsonrpc':'2.0','id':1,'method':'trace_block','params':[n]},'role':'reference'} for n in sorted(needed-present,key=lambda n:int(n,16))]
    hive = checkout()
    sim = hive / 'simulators/ethereum/rpc-compat'
    tests = sim / 'tests'
    if tests.exists():
        shutil.rmtree(tests)
    tests.mkdir()
    for name in ['genesis.json', 'chain.rlp', 'forkenv.json', 'headfcu.json']:
        shutil.copy2(chain / name, tests / name)
    for case in cases:
        p = tests / 'interop' / (case['name'] + '.io')
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text('// Observation only. Placeholder mismatches are not conformance failures.\n'
                     '>> ' + json.dumps(case['request']) + '\n<< ' + json.dumps(
                         {'jsonrpc': '2.0', 'id': 1, 'result': {'capture_only': True}}) + '\n')
    write(sim / 'openrpc.json', {'openrpc': '1.2.6', 'info': {'title': 'Observations', 'version': '0'}, 'methods': []})
    (sim / 'Dockerfile').write_text(DOCKERFILE)
    from .scenarios import prepare
    prepare(hive, corpus, args.corpus, {n: lock['clients'][n] for n in names}, head['hash'])
    out.mkdir(parents=True)
    entries = []
    created_tags = []
    for name in names:
        info = lock['clients'][name]
        image = info.get('local_image') or info['digest']
        if 'local_image' not in info:
            run('docker', 'pull', image)
        meta = json.loads(run('docker', 'image', 'inspect', image, capture=True))[0]
        if meta['Id'] != info['image_id']:
            raise ValueError(f'image identity mismatch for {name}')
        local = 'trace-interop/' + info['client']
        tag = info['image_id'].split(':')[1]
        # A tag this capture adds to a digest-pulled image is removed afterwards: the image
        # can be pulled again, and an image still tagged upstream keeps its layers warm.
        # Source-built images and tags that already existed are left alone.
        if 'local_image' not in info and subprocess.run(['docker', 'image', 'inspect', local + ':' + tag],
                                                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False).returncode:
            created_tags.append(local + ':' + tag)
        run('docker', 'tag', image, local + ':' + tag)
        entries.append({'client': info['client'], 'nametag': name.removeprefix(info['client'] + '_'),
                        'build_args': {'baseimage': local, 'tag': tag}})
    # JSON is valid YAML; Hive's client-file loader accepts this representation.
    write(out / 'clients.yaml', entries)
    manifest = {'format': 1, 'started_at': dt.datetime.now(dt.timezone.utc).isoformat(),
                'corpus': args.corpus, 'selected_cases': cases, 'head': head,
                'clients': {n: lock['clients'][n] for n in names}, 'hive_commit': HIVE,
                'fixture_manifest_sha256': sha(ROOT / 'fixtures/checksums.json'),
                'source_commit': source_commit,
                'source_dirty': source_dirty,
                'runner_sha256': sha(Path(__file__)), 'hive_binary_sha256': sha(hive / 'hive'), 'spec': read(ROOT / 'spec.lock.json') if (ROOT / 'spec.lock.json').exists() else None}
    if corpus.get('scenario_phases'):
        manifest['scenario_phases'] = corpus['scenario_phases']
    write(out / 'manifest.json', manifest)
    command = [str(hive / 'hive'), '--client-file', str(out / 'clients.yaml'),
               '--sim', 'ethereum/rpc-compat', '--sim.limit', '/interop',
               '--sim.parallelism', '1', '--sim.timelimit', args.timeout,
               '--client.checktimelimit', '5m', '--results-root', str(out / 'hive')]
    before = docker_state()
    with (out / 'runner.log').open('w') as log:
        process = subprocess.run(command, cwd=hive, stdout=log, stderr=subprocess.STDOUT)
    remove_capture_leftovers(before, created_tags)
    manifest['runner_exit_code'] = process.returncode
    manifest['finished_at'] = dt.datetime.now(dt.timezone.utc).isoformat()
    write(out / 'manifest.json', manifest)
    result = collect(out)
    # rpc-compat exits nonzero for the deliberate capture placeholders.
    if not result['complete']:
        raise ValueError(f'run incomplete; evidence saved to {out}')
    print(f'Captured {result["exchange_count"]} responses in {out}')


def parse_exchange(log, expected):
    requests, replies = [], []
    invalid_json = object()
    for line in log.splitlines():
        match = re.search(r'(>>|<<)\s+(.*)$', line)
        if not match:
            continue
        raw = match[2]
        try:
            value = decode_response(raw)
        except ValueError:
            value = invalid_json
        (requests if match[1] == '>>' else replies).append((raw, value))
    if len(requests) != 1 or requests[0][1] != expected:
        return {'status': 'harness_error', 'detail': 'request mismatch', 'raw_log': log}
    if len(replies) != 1:
        return {'status': 'transport_error', 'detail': f'{len(replies)} responses', 'raw_log': log}
    raw, response = replies[0]
    if response is invalid_json:
        return {'status': 'malformed_json', 'raw_response': raw}
    if not isinstance(response, dict) or response.get('jsonrpc') != '2.0' or type(response.get('id')) is not type(expected['id']) or response.get('id') != expected['id'] or ('result' in response) == ('error' in response):
        return {'status': 'invalid_envelope', 'raw_response': raw, 'response': response}
    error = response.get('error')
    if 'error' in response and (not isinstance(error, dict) or type(error.get('code')) is not int or not isinstance(error.get('message'), str)):
        return {'status': 'invalid_envelope', 'raw_response': raw, 'response': response}
    status = 'unsupported' if isinstance(error, dict) and error.get('code') == -32601 else 'rpc_error' if error is not None else 'result'
    return {'status': status, 'raw_response': raw, 'response': response}


def collect(out):
    out = Path(out)
    manifest = read(out / 'manifest.json')
    if not manifest['selected_cases'] or not manifest['clients']:
        raise ValueError('capture manifest must select cases and clients')
    cases = {c['name']: c['request'] for c in manifest['selected_cases']}
    if len(cases) != len(manifest['selected_cases']):
        raise ValueError('duplicate case names in capture manifest')
    if '_control/head' not in cases:
        raise ValueError('capture manifest is missing the chain identity control')
    observations = {c: {} for c in cases}
    versions, launches = {}, []
    for file in sorted((out / 'hive').glob('*.json')):
        suite = read(file)
        if not isinstance(suite, dict) or 'testCases' not in suite:
            continue
        versions.update(suite.get('clientVersions', {}))
        logbytes = log_bytes(out / 'hive' / suite['testDetailsLog'])
        for test in suite['testCases'].values():
            result = test['summaryResult']
            span = result.get('log')
            log = logbytes[span['begin']:span['end']].decode(errors='replace') if span else result.get('details', '')
            match = re.fullmatch(r'interop/(.*?) \(([^()]+)\)', test['name'])
            if not match:
                launches.append({'name': test['name'], 'pass': result['pass'], 'log': log})
                continue
            name, client = match.groups()
            if name not in cases or client not in manifest['clients'] or client in observations[name]:
                raise ValueError(f'unexpected or duplicate result: {name}/{client}')
            observations[name][client] = parse_exchange(log, cases[name])
    eligibility, scenario_status = {}, {}
    from .scenarios import verify_setup
    corpus = read(ROOT / 'fixtures/corpora' / (manifest['corpus'] + '.json')) if manifest.get('corpus') else {}
    for client in manifest['clients']:
        ok, detail = verify_setup(manifest, corpus, observations, client, launches)
        eligibility[client] = ok
        scenario_status[client] = {'verified': ok, 'detail': detail}
    missing = [[case, client] for case in cases for client in manifest['clients'] if client not in observations[case]]
    transport = [[case, client] for case, clients in observations.items() for client, obs in clients.items() if obs['status'] in ['harness_error', 'transport_error']]
    summary = {'versions': versions, 'scenario': scenario_status, 'eligible': eligibility, 'missing': missing,
               'transport_errors': transport, 'launches': launches,
               'complete': not missing and not transport and all(eligibility.values()) and all(x['pass'] for x in launches),
               'exchange_count': sum(len(v) for v in observations.values()),
               'note': 'Hive placeholder failure counts are not conformance scores.'}
    write_observations(out, observations)
    compress_logs(out)
    write(out / 'summary.json', summary)
    write(out / 'checksums.json', {str(p.relative_to(out)): sha(p) for p in sorted(out.rglob('*')) if p.is_file() and p.name != 'checksums.json'})
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('verify')
    p = sub.add_parser('resolve', help='pull references and create an immutable client lock')
    p.add_argument('--clients', default=','.join(NAMES))
    p.add_argument('--output', required=True)
    p = sub.add_parser('check-versions', help='live preflight; reject a stale release/development lock')
    p.add_argument('--lock', required=True)
    p.add_argument('--output', help='optional preflight record')
    p = sub.add_parser('run', help='capture a corpus through Hive; differences are observations')
    p.add_argument('--lock', required=True)
    p.add_argument('--clients')
    p.add_argument('--corpus', choices=list(CHAINS), default='initial')
    p.add_argument('--case', default='.*', help='case name regex; zero matches is an error')
    p.add_argument('--output', required=True)
    p.add_argument('--timeout', default='30m')
    p = sub.add_parser('collect')
    p.add_argument('run')
    p = sub.add_parser('report')
    p.add_argument('--run', action='append', default=[])
    p.add_argument('--output', default='reports')
    args = parser.parse_args()
    try:
        if args.command == 'verify':
            verify()
        elif args.command == 'resolve':
            resolve(args)
        elif args.command == 'check-versions':
            from .versions import check_current
            result = check_current(read(args.lock))
            if args.output:
                write(args.output,result)
            print(json.dumps(result,indent=2))
        elif args.command == 'run':
            import fcntl
            (ROOT / '.cache').mkdir(exist_ok=True)
            with (ROOT / '.cache/run.lock').open('w') as guard:
                try:
                    fcntl.flock(guard, fcntl.LOCK_EX | fcntl.LOCK_NB)
                except BlockingIOError:
                    raise ValueError('another run owns the Hive build context')
                execute(args)
        elif args.command == 'collect':
            result = collect(args.run)
            print(json.dumps({k: v for k, v in result.items() if k != 'launches'}, indent=2))
            if not result['complete']:
                return 1
        else:
            from .report import generate
            generate(ROOT, [Path(p) for p in args.run], Path(args.output))
    except (ValueError, KeyError, FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())

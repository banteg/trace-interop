"""Portable Hive execution and immutable evidence collection."""
from __future__ import annotations

import argparse
import datetime as dt
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
          'reorg': 'a', 'reorg-safe': 'a', 'pruned': 'a'}
IMAGES = {
    'reth_release': ('reth', 'ghcr.io/paradigmxyz/reth:v2.6.0'),
    'reth_development': ('reth', 'ghcr.io/paradigmxyz/reth:nightly'),
    'erigon_release': ('erigon', 'erigontech/erigon:v3.6.1'),
    'erigon_development': ('erigon', 'erigontech/erigon:main-latest'),
    'nethermind_release': ('nethermind', 'nethermind/nethermind:1.39.3'),
    'nethermind_development': ('nethermind', 'nethermindeth/nethermind:master'),
    'besu_release': ('besu', 'hyperledger/besu:26.8.1'),
    'besu_development': ('besu', 'hyperledger/besu:develop'),
}


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(*args, cwd=None, capture=False):
    env = dict(os.environ)
    if args and args[0] == "go":
        env["GOTOOLCHAIN"] = "go1.26.1"
    return subprocess.run(args, cwd=cwd, check=True, text=True, env=env,
                          stdout=subprocess.PIPE if capture else None).stdout


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
    ledger = read(ROOT / 'decisions/ledger.json')
    for item in ledger['items']:
        for name in item['cases']:
            if not (ROOT / 'evidence/2026-09-15/cases' / (name + '.json')).exists():
                raise ValueError(f'missing evidence: {item["id"]}/{name}')
    print(f'Verified {len(manifest)} frozen inputs and {len(ledger["items"])} decisions.')


def resolve(args):
    output = Path(args.output)
    if output.exists():
        raise ValueError('use a new lock filename; existing locks are immutable')
    clients = {}
    for name in args.clients.split(','):
        client, image = IMAGES[name]
        run('docker', 'pull', image)
        meta = json.loads(run('docker', 'image', 'inspect', image, capture=True))[0]
        digest = next(x for x in meta['RepoDigests'] if x.startswith(image.rsplit(':', 1)[0] + '@'))
        clients[name] = {'client': client, 'requested': image, 'digest': digest,
                         'image_id': meta['Id'], 'architecture': meta['Architecture'],
                         'created': meta['Created'], 'labels': meta['Config'].get('Labels') or {}}
    write(output, {'resolved_at': dt.datetime.now(dt.timezone.utc).isoformat(),
                   'hive_commit': HIVE, 'clients': clients})


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
    return cases


def execute(args):
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
    elif any(c['request']['method'] == 'trace_filter' for c in cases):
        names_selected = {c['name'] for c in cases}
        cases += [c for c in corpus['cases'] if c['name'] not in names_selected and (c['name'] in ['transaction-tree', 'block-tree'] or c['name'].startswith('block-'))]
    chain = ROOT / 'fixtures/chains' / CHAINS[args.corpus]
    head = read(chain / 'headblock.json')
    cases = [{'name': '_control/head', 'request': {'jsonrpc': '2.0', 'id': 1,
              'method': 'eth_getBlockByNumber', 'params': [head['number'], False]}},
             {'name': '_control/version', 'request': {'jsonrpc': '2.0', 'id': 1,
              'method': 'web3_clientVersion', 'params': []}}] + cases
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
    prepare(hive, corpus, args.corpus, {n: lock['clients'][n] for n in names})
    out.mkdir(parents=True)
    entries = []
    for name in names:
        info = lock['clients'][name]
        run('docker', 'pull', info['digest'])
        meta = json.loads(run('docker', 'image', 'inspect', info['digest'], capture=True))[0]
        if meta['Id'] != info['image_id']:
            raise ValueError(f'image identity mismatch for {name}')
        local = 'trace-interop/' + info['client']
        tag = info['image_id'].split(':')[1]
        run('docker', 'tag', info['digest'], local + ':' + tag)
        entries.append({'client': info['client'], 'nametag': name.removeprefix(info['client'] + '_'),
                        'build_args': {'baseimage': local, 'tag': tag}})
    # JSON is valid YAML; Hive's client-file loader accepts this representation.
    write(out / 'clients.yaml', entries)
    manifest = {'format': 1, 'started_at': dt.datetime.now(dt.timezone.utc).isoformat(),
                'corpus': args.corpus, 'selected_cases': cases, 'head': head,
                'clients': {n: lock['clients'][n] for n in names}, 'hive_commit': HIVE,
                'fixture_manifest_sha256': sha(ROOT / 'fixtures/checksums.json'),
                'source_commit': run('git', 'rev-parse', 'HEAD', cwd=ROOT, capture=True).strip(),
                'source_dirty': bool(run('git', 'status', '--porcelain', cwd=ROOT, capture=True)),
                'runner_sha256': sha(Path(__file__)), 'hive_binary_sha256': sha(hive / 'hive'), 'spec': read(ROOT / 'spec.lock.json') if (ROOT / 'spec.lock.json').exists() else None}
    write(out / 'manifest.json', manifest)
    command = [str(hive / 'hive'), '--client-file', str(out / 'clients.yaml'),
               '--sim', 'ethereum/rpc-compat', '--sim.limit', '/interop',
               '--sim.parallelism', '1', '--sim.timelimit', args.timeout,
               '--client.checktimelimit', '5m', '--results-root', str(out / 'hive')]
    with (out / 'runner.log').open('w') as log:
        process = subprocess.run(command, cwd=hive, stdout=log, stderr=subprocess.STDOUT)
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
    for line in log.splitlines():
        match = re.search(r'(>>|<<)\s+(.*)$', line)
        if not match:
            continue
        raw = match[2]
        try:
            value = json.loads(raw)
        except json.JSONDecodeError:
            value = None
        (requests if match[1] == '>>' else replies).append((raw, value))
    if len(requests) != 1 or requests[0][1] != expected:
        return {'status': 'harness_error', 'detail': 'request mismatch', 'raw_log': log}
    if len(replies) != 1:
        return {'status': 'transport_error', 'detail': f'{len(replies)} responses', 'raw_log': log}
    raw, response = replies[0]
    if response is None:
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
        logbytes = (out / 'hive' / suite['testDetailsLog']).read_bytes()
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
    eligibility = {}
    for client in manifest['clients']:
        actual = observations.get('_control/head', {}).get(client, {}).get('response', {}).get('result')
        eligibility[client] = isinstance(actual, dict) and all(actual.get(k) == manifest['head'].get(k) for k in ['hash', 'stateRoot', 'transactionsRoot', 'receiptsRoot'])
    scenario_status = {}
    from .scenarios import verify_state
    corpus = read(ROOT / 'fixtures/corpora' / (manifest['corpus'] + '.json')) if manifest.get('corpus') else {}
    for client in manifest['clients']:
        ok, detail = verify_state(manifest.get('corpus', ''), corpus, observations, client)
        scenario_status[client] = {'verified': ok, 'detail': detail}
        eligibility[client] = eligibility[client] and ok
    missing = [[case, client] for case in cases for client in manifest['clients'] if client not in observations[case]]
    transport = [[case, client] for case, clients in observations.items() for client, obs in clients.items() if obs['status'] in ['harness_error', 'transport_error']]
    summary = {'versions': versions, 'scenario': scenario_status, 'eligible': eligibility, 'missing': missing,
               'transport_errors': transport, 'launches': launches,
               'complete': not missing and not transport and all(eligibility.values()) and all(x['pass'] for x in launches),
               'exchange_count': sum(len(v) for v in observations.values()),
               'note': 'Hive placeholder failure counts are not conformance scores.'}
    write(out / 'observations.json', observations)
    write(out / 'summary.json', summary)
    write(out / 'checksums.json', {str(p.relative_to(out)): sha(p) for p in sorted(out.rglob('*')) if p.is_file() and p.name != 'checksums.json'})
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('verify')
    p = sub.add_parser('resolve', help='pull references and create an immutable client lock')
    p.add_argument('--clients', default=','.join(IMAGES))
    p.add_argument('--output', required=True)
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

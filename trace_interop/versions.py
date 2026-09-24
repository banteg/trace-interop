"""Resolve current published client builds once, then capture immutable digests."""
import datetime as dt
import json
import os
from pathlib import Path
import re
import urllib.request

CLIENTS = {
    'reth': dict(repository='paradigmxyz/reth', release_image='ghcr.io/paradigmxyz/reth',
                 development='ghcr.io/paradigmxyz/reth:nightly', prefix='v'),
    'erigon': dict(repository='erigontech/erigon', release_image='erigontech/erigon',
                   development='erigontech/erigon:main-latest', prefix='v'),
    'nethermind': dict(repository='NethermindEth/nethermind', release_image='nethermind/nethermind',
                       development='nethermindeth/nethermind:master', prefix=''),
    'besu': dict(repository='besu-eth/besu', release_image='hyperledger/besu',
                 development='hyperledger/besu:develop', prefix=''),
}
NAMES = [f'{client}_{channel}' for client in CLIENTS for channel in ['release','development']]


def github_json(path):
    headers = {'Accept':'application/vnd.github+json', 'User-Agent':'trace-interop'}
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = 'Bearer '+token
    request = urllib.request.Request('https://api.github.com/'+path, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def current_references(names, fetch=None):
    """Never fall back to an old version if release discovery is unavailable."""
    if not names or len(names)!=len(set(names)) or any(n not in NAMES for n in names):
        raise ValueError('select distinct known client channels')
    fetch = fetch or github_json
    references = {}
    for name in names:
        client, channel = name.split('_')
        config = CLIENTS[client]
        info = dict(client=client, repository='https://github.com/'+config['repository'], channel=channel)
        if channel == 'release':
            release = fetch('repos/'+config['repository']+'/releases/latest')
            tag = release['tag_name']
            if release.get('draft') or release.get('prerelease') or not re.fullmatch(r'v?\d+\.\d+\.\d+',tag):
                raise ValueError('unexpected stable release: '+str(tag))
            info.update(requested=config['release_image']+':'+config['prefix']+tag.removeprefix('v'),
                        release=dict(tag=tag, published_at=release['published_at'], url=release['html_url']))
        else:
            info['requested'] = config['development']
        references[name] = info
    return references


def resolve_native(output, names=None):
    from .cli import run, write, HIVE
    output = Path(output)
    if output.exists():
        raise ValueError('use a new lock filename; existing locks are immutable')
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    references = current_references(NAMES if names is None else names)
    clients = {}
    for name, info in references.items():
        image = info['requested']
        run('docker','pull',image)
        meta = json.loads(run('docker','image','inspect',image,capture=True))[0]
        repository = image.rsplit(':',1)[0]
        digest = next(d for d in meta['RepoDigests'] if d.startswith(repository+'@'))
        clients[name] = dict(info, digest=digest, image_id=meta['Id'], architecture=meta['Architecture'],
                             created=meta['Created'], labels=meta['Config'].get('Labels') or {})
    lock = dict(resolution='latest-published', resolution_started_at=started,
                resolved_at=dt.datetime.now(dt.timezone.utc).isoformat(), hive_commit=HIVE, clients=clients)
    write(output,lock)
    return lock


def resolve_geth(output):
    """Build the current remote draft branch in a harness-owned isolated cache."""
    from .cli import ROOT, run, read
    import sys
    source = ROOT/'.cache/geth-current'
    repository = 'https://github.com/banteg/go-ethereum'
    if not source.exists():
        source.mkdir(parents=True)
        run('git','init','-q',str(source))
        run('git','remote','add','origin',repository,cwd=source)
    if run('git','remote','get-url','origin',cwd=source,capture=True).strip()!=repository:
        raise ValueError('unexpected Geth cache origin')
    if run('git','status','--porcelain',cwd=source,capture=True).strip():
        raise ValueError('Geth resolver cache is dirty; refusing to replace local work')
    run('git','fetch','--depth=1','origin','refs/heads/feat/trace',cwd=source)
    run('git','checkout','--detach','FETCH_HEAD',cwd=source)
    run(sys.executable,str(ROOT/'scripts/build_geth.py'),'--source',str(source),'--output',str(output))
    return read(output)


def matrix_lock(output, reproduce=None):
    from .cli import read, write, HIVE
    output = Path(output)
    if output.exists():
        raise ValueError('use a new lock filename; existing locks are immutable')
    if reproduce:
        lock = read(reproduce)
        if set(lock['clients']) != set(NAMES)|{'go-ethereum_trace'}:
            raise ValueError('reproduction requires a combined nine-build lock')
    else:
        lock = resolve_native(output.parent/'native.lock.json')
        geth = resolve_geth(output.parent/'geth.lock.json')
        if lock['hive_commit'] != geth['hive_commit']:
            raise ValueError('incompatible Hive revisions')
        lock['clients'].update(geth['clients'])
    if lock['hive_commit'] != HIVE:
        raise ValueError('incompatible Hive revision')
    write(output,lock)
    return lock


def check_current(lock):
    """Live preflight: stale references/digests or a moved draft head fail closed.

    A suite checks once before its first corpus and uses that immutable snapshot
    throughout. Moving tags are never re-resolved in the middle of a matrix.
    """
    from .cli import run
    if not lock.get('clients'):
        raise ValueError('empty client lock')
    native = [name for name in lock['clients'] if name != 'go-ethereum_trace']
    references = current_references(native) if native else {}
    stale = []
    for name, info in references.items():
        pinned = lock['clients'][name]
        image = info['requested']
        if pinned['requested'] != image:
            stale.append(f'{name}: {pinned["requested"]} -> {image}')
            continue
        # pull contacts the registry; inspecting the local tag alone can be stale.
        run('docker','pull',image)
        meta = json.loads(run('docker','image','inspect',image,capture=True))[0]
        if meta['Id'] != pinned.get('image_id') or pinned.get('digest') not in meta['RepoDigests']:
            stale.append(f'{name}: published image moved from {pinned.get("image_id")} to {meta["Id"]}')
    geth = lock['clients'].get('go-ethereum_trace')
    if geth:
        refs = run('git','ls-remote','https://github.com/banteg/go-ethereum','refs/heads/feat/trace',capture=True).splitlines()
        if len(refs)!=1 or not re.fullmatch(r'[0-9a-f]{40}\s+refs/heads/feat/trace',refs[0]):
            raise ValueError('could not establish current Geth draft head')
        head = refs[0].split()[0]
        if geth.get('source',{}).get('dirty') or geth.get('source',{}).get('commit') != head:
            stale.append(f'go-ethereum_trace: source moved to {head}')
    if stale:
        raise ValueError('stale client lock; resolve a fresh matrix or explicitly reproduce history:\n'+'\n'.join(stale))
    return dict(checked_at=dt.datetime.now(dt.timezone.utc).isoformat(), status='current',
                clients={name:info['image_id'] for name,info in lock['clients'].items()})

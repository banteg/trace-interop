"""Generate client impact pages from decisions and independently checked runs."""
from collections import defaultdict
import hashlib
import json
import os

from .cli import read, write, sha, load_observations, observations_file, verify_evidence
from .rules import evaluate, is_extension_request
from .validation import request_errors
from .inventory import verify_inventory, cover_topics, previous_runs
from .scenarios import verify_setup
from .coverage import supplement

ASSESSMENT_SOURCES = ['pyproject.toml','uv.lock','fixtures/checksums.json','trace_interop/coverage.py','trace_interop/chain_model.py','trace_interop/execution_models.py','trace_interop/fee_policy.py','trace_interop/probes.py','trace_interop/vm_model.py','trace_interop/rules.py','trace_interop/oracles.py','trace_interop/report.py','trace_interop/presentation.py','trace_interop/status.py','trace_interop/scenarios.py','trace_interop/validation.py','trace_interop/inventory.py','trace_interop/versions.py','scripts/run_matrix.py','reports.lock.json','decisions/sources.json','locks/source-revisions.json','spec.lock.json','decisions/ledger.json','decisions/impact.json','decisions/status.json']


def link(path, output):
    return os.path.relpath(path, output).replace(os.sep, '/')


def assessed_cases(captured, corpus):
    """Captured requests with the current corpus expectations for the identical request.

    Observations stay immutable; expectation fields (fee policy, models, references)
    follow the checksummed corpus, so a corrected expectation reassesses old evidence.
    A request that has since changed keeps the expectations it was captured with.
    """
    current = {c['name']: c for c in corpus}
    return [current[c['name']] if c['name'] in current and current[c['name']]['request'] == c['request'] else c
            for c in captured]


def run_context(root, manifest):
    """The corpus definition plus the frozen chain facts every assessment of a captured run uses."""
    from .cli import CHAINS
    from .chain_model import load_chain
    context=read(root/'fixtures/corpora'/(manifest['corpus']+'.json'))
    context['_chain']=manifest['corpus']
    context['_scenario_phases']=manifest.get('scenario_phases')
    chain = root/'fixtures/chains'/CHAINS[manifest['corpus']]
    genesis = read(chain/'genesis.json')
    header = read(chain/'headblock.json')
    context['_codes'] = {'0x'+a.removeprefix('0x').lower(): v.get('code','0x') for a,v in genesis['alloc'].items()}
    context['_alloc'] = {'0x'+a.removeprefix('0x').lower(): v for a,v in genesis['alloc'].items()}
    context['_chain_id'] = genesis['config']['chainId']
    context['_blocks'] = load_chain(chain/'chain.rlp')
    context['_head'] = header
    context['txinfo'] = dict(context.get('txinfo', {}), _decoded=[
        {'txhash':t['hash'],'sender':t['sender'],'block':number,'indexInBlock':i}
        for number,b in context['_blocks'].items() for i,t in enumerate(b['transactions'])])
    if manifest['corpus'] in ['reorg','reorg-safe']:
        context['_alternate_blocks'] = load_chain(root/'fixtures/chains/b/chain.rlp')
    context['_environment'] = {k:int(header[v],16) for k,v in [('BASEFEE','baseFeePerGas'),('NUMBER','number'),('TIMESTAMP','timestamp'),('GASLIMIT','gasLimit')] if v in header}
    return context


def result_validator(schema):
    """One validator per method, over a pre-crawled registry: the recursive vmTrace `$ref` resolves
    against an embedded `$id`, which an uncrawled registry would re-crawl on every lookup."""
    from jsonschema import Draft201909Validator
    from referencing import Registry
    from referencing.jsonschema import DRAFT201909
    return Draft201909Validator(schema, registry=Registry().with_resource('', DRAFT201909.create_resource(schema)).crawl())


def generate(root, runs, output):
    output=output.resolve();output.mkdir(parents=True,exist_ok=True)
    verify_inventory(root)
    for name,digest in read(root/'fixtures/checksums.json').items():
        if sha(root/'fixtures'/name)!=digest:
            raise ValueError(f'fixture modified: {name}')
    ledger=read(root/'decisions/ledger.json')
    decisions={x['id']:x for x in ledger['items']}
    # Schemas are a generated artifact of the pinned fork, not another editable spec.
    spec=read(root/'spec/trace-openrpc.json') if (root/'spec/trace-openrpc.json').exists() else None
    pinned=None
    if spec:
        lock=read(root/'spec.lock.json')
        if sha(root/'spec/trace-openrpc.json') != lock['generated_sha256']:
            raise ValueError('generated schema does not match spec lock')
        methods={m['name']:m for m in spec['methods']}
        pinned=(lock, methods, {name:result_validator(m['result']['schema']) for name,m in methods.items()}, {})
    records, by_client, case_pages, run_rows = assess_runs(root, runs, output, decisions, pinned)
    selection = read(root/'reports.lock.json')
    selected = {(root/name).resolve() for name in selection['runs']}
    matrix = root/selection['matrix'] if selection.get('matrix') and {p.resolve() for p in runs} == selected else None
    previous = None
    if matrix and selection.get('previous'):
        # The same code, ledger and draft assess the previous matrix, so its verdicts differ only by evidence.
        before = previous_runs(root)
        prior, prior_checks = assess_runs(root, before, output, decisions, pinned)[:2]
        previous = dict(matrix=before[0].parent, records=prior, by_client=prior_checks)
    write(output/'assessment.json', {
        'matrix': {link(matrix/name,output):sha(matrix/name) for name in ['clients.lock.json','preflight.json','matrix.json']} if matrix else None,
        'previous': {link(previous['matrix']/name,output):sha(previous['matrix']/name) for name in ['clients.lock.json','preflight.json','matrix.json']} if previous else None,
        'spec_commit': lock['commit'] if spec else None,
        'sources': {name:sha(root/name) for name in ASSESSMENT_SOURCES},
        'contexts': {p.name:sha(p) for p in sorted((root/'fixtures/corpora').glob('*.json'))},
        'coverage': {status:sum(r.get('assessment')==status for r in records if r['method'].startswith('trace_')) for status in ['assessed','partial','unassessed','blocked','control']},
        'evidence': {row['manifest']:row['digest'] for row in run_rows},
    })
    write(output/'checks.json',records)
    comparisons=[]
    for (corpus,name),entries in sorted(case_pages.items()):
        groups={}
        for entry in entries:
            r=entry['record'];obs=entry['observation'];response=obs.get('response')
            normalized={k:v for k,v in response.items() if k not in ['jsonrpc','id']} if isinstance(response,dict) else obs.get('raw_response',obs.get('status'))
            fingerprint=hashlib.sha256(json.dumps(normalized,sort_keys=True).encode()).hexdigest()
            groups.setdefault(fingerprint,[]).append({'client':r['client'],'version':r['version'],'status':r['status'],'eligible':r['eligible']})
        comparisons.append({'corpus':corpus,'case':name,'groups':[{'sha256':h,'observations':clients} for h,clients in groups.items()]})
    write(output/'comparisons.json',comparisons)
    write(output/'runs.json',run_rows)
    from .presentation import render
    render(root, output, records, by_client, case_pages, run_rows, decisions, lock, previous)
    print(f'Generated {len(records)} observation assessments and {len(decisions)} decision pages in {output}')


def assess_runs(root, runs, output, decisions, pinned):
    """Records, per-client checks, case pages and run rows for captured runs; `pinned` is
    (spec lock, methods, result validators, memoized result shapes), or None without a pinned draft."""
    spec = pinned is not None
    lock, methods, validators, shapes = pinned or (None, {}, {}, {})
    by_client=defaultdict(lambda:defaultdict(list)); records=[]; run_rows=[]; case_pages=defaultdict(list); requests={}
    for folder in runs:
        folder=folder.resolve()
        manifest=read(folder/'manifest.json'); summary=read(folder/'summary.json'); obs=load_observations(folder)
        digest=sha(folder/'manifest.json')
        verify_evidence(folder)
        run_rows.append({'name':folder.name,'manifest':link(folder/'manifest.json',output),'corpus':manifest['corpus'],'complete':summary['complete'],'versions':summary['versions'],'digest':digest})
        context=run_context(root, manifest)
        cases = assessed_cases(manifest['selected_cases'], context['cases'])
        rule_context = dict(context, cases=cases)
        lock_link, evidence_link = link(folder/'manifest.json',root), link(observations_file(folder),output/'clients')
        for client in manifest['clients']:
            eligible, scenario_detail=verify_setup(manifest,context,obs,client,summary.get('launches',[]))
            peers={name:clients.get(client,{}) for name,clients in obs.items()}
            for case in cases:
                name=case['name']; observation=peers.get(name,{})
                record={'run':folder.name,'corpus':manifest['corpus'],'case':name,'method':case['request']['method'],'client':client,'version':summary['versions'].get(client,'unknown'),'status':observation.get('status','not_observed'),'eligible':eligible,'capture_eligible':summary['eligible'].get(client,False),'eligibility_detail':scenario_detail,'checks':[],'spec_commit':lock['commit'] if spec else None}
                info=manifest['clients'][client]
                record['build_id']=info.get('image_id') or info.get('digest')
                record['captured_at']=manifest.get('started_at')
                expected=[t for t,d in decisions.items() if manifest['corpus']+'/'+name in d['cases']]
                references=[t for t,d in decisions.items() if manifest['corpus']+'/'+name in d.get('references', [])]
                if record['eligible'] and observation:
                    request=json.dumps(case['request'])  # every client and run sends the same request
                    if request not in requests:
                        requests[request]=request_errors(case['request'],methods) if spec and not is_extension_request(case['request']) else []
                    errors=list(requests[request])
                    record['request_errors']=errors
                    checks=evaluate(dict(case,context=rule_context),observation,peers,invalid_params=errors)
                    checks=supplement(dict(case,context=rule_context),observation,peers,checks,expected)
                    record['checks']=cover_topics(checks,expected)
                    if spec and observation.get('status')=='result' and case['request']['method'] in methods and not is_extension_request(case['request']):
                        result=observation['response']['result']; key=(case['request']['method'],json.dumps(result))
                        if key not in shapes:  # clients and runs often return identical results
                            errors=list(validators[key[0]].iter_errors(result))
                            shapes[key]={'status':'invalid' if errors else 'valid','errors':[{'path':'/'.join(map(str,e.absolute_path)), 'message':e.message[:300]} for e in errors[:8]]}
                        record['schema']=shapes[key]
                record['checks']=cover_topics(record['checks'],expected)
                record['checks'] += [dict(topic=t,status='control',requirement='Retain supporting reference evidence.',
                    detail='Ledger reference; executable requirements are assessed by the linked topic cases.') for t in references]
                if not record['eligible'] or not observation:
                    for check in record['checks']:
                        check['status']='blocked'
                        check['detail']=scenario_detail if not record['eligible'] else 'No response captured for this declared case.'
                scored=any(c['status'] in ['matches','change_needed','unsupported','observation'] for c in record['checks'])
                gaps=any(c['status'] in ['unassessed','blocked'] for c in record['checks'])
                record['assessment']=('blocked' if not record['eligible'] else
                    'partial' if scored and gaps else 'assessed' if scored else
                    'blocked' if any(c['status']=='blocked' for c in record['checks']) else
                    'control' if record['checks'] and all(c['status'] in ['control','not_applicable'] for c in record['checks']) else 'unassessed')
                for check in record['checks']:
                    by_client[client][check['topic']].append(dict(check,case=name,run=folder.name,corpus=manifest['corpus'],lock=lock_link,evidence=evidence_link))
                records.append(record)
                case_pages[(manifest['corpus'],name)].append({'record':record,'request':case['request'],'observation':observation,'raw':observations_file(folder)})
    return records, by_client, case_pages, run_rows

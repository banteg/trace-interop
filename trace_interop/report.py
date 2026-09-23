"""Generate client impact pages from decisions and independently checked runs."""
from collections import defaultdict
import hashlib
import json
import os

from .cli import read, write, sha
from .rules import evaluate, is_extension_request
from .validation import request_errors
from .inventory import verify_inventory, cover_topics
from .scenarios import verify_setup
from .coverage import supplement


def link(path, output):
    return os.path.relpath(path, output).replace(os.sep, '/')


def generate(root, runs, output):
    output=output.resolve();output.mkdir(parents=True,exist_ok=True)
    verify_inventory(root)
    ledger=read(root/'decisions/ledger.json')
    decisions={x['id']:x for x in ledger['items']}
    by_client=defaultdict(lambda:defaultdict(list)); records=[]; run_rows=[]; case_pages=defaultdict(list)
    # Schemas are a generated artifact of the pinned fork, not another editable spec.
    spec=read(root/'spec/trace-openrpc.json') if (root/'spec/trace-openrpc.json').exists() else None
    if spec:
        from jsonschema import Draft201909Validator
        lock=read(root/'spec.lock.json')
        if sha(root/'spec/trace-openrpc.json') != lock['generated_sha256']:
            raise ValueError('generated schema does not match spec lock')
        methods={m['name']:m for m in spec['methods']}
    for folder in runs:
        folder=folder.resolve()
        manifest=read(folder/'manifest.json'); summary=read(folder/'summary.json'); obs=read(folder/'observations.json')
        digest=sha(folder/'manifest.json')
        for name, value in read(folder/'checksums.json').items():
            if sha(folder/name) != value:raise ValueError(f'evidence modified: {folder.name}/{name}')
        run_rows.append({'name':folder.name,'manifest':link(folder/'manifest.json',output),'corpus':manifest['corpus'],'complete':summary['complete'],'versions':summary['versions'],'digest':digest})
        context=read(root/'fixtures/corpora'/(manifest['corpus']+'.json'))
        context['_chain']=manifest['corpus']
        context['_scenario_phases']=manifest.get('scenario_phases')
        from .cli import CHAINS
        chain = root/'fixtures/chains'/CHAINS[manifest['corpus']]
        genesis = read(chain/'genesis.json')
        header = read(chain/'headblock.json')
        context['_codes'] = {'0x'+a.removeprefix('0x').lower(): v.get('code','0x') for a,v in genesis['alloc'].items()}
        context['_alloc'] = {'0x'+a.removeprefix('0x').lower(): v for a,v in genesis['alloc'].items()}
        from .chain_model import load_chain
        context['_blocks'] = load_chain(chain/'chain.rlp')
        context['_head'] = header
        context['txinfo'] = dict(context.get('txinfo', {}), _decoded=[
            {'txhash':t['hash'],'sender':t['sender'],'block':number,'indexInBlock':i}
            for number,b in context['_blocks'].items() for i,t in enumerate(b['transactions'])])
        if manifest['corpus'] in ['reorg','reorg-safe']:
            context['_alternate_blocks'] = load_chain(root/'fixtures/chains/b/chain.rlp')
        rule_context = dict(context, cases=manifest['selected_cases'])
        context['_environment'] = {k:int(header[v],16) for k,v in [('BASEFEE','baseFeePerGas'),('NUMBER','number'),('TIMESTAMP','timestamp'),('GASLIMIT','gasLimit')] if v in header}
        for client in manifest['clients']:
            eligible, scenario_detail=verify_setup(manifest,context,obs,client)
            peers={name:clients.get(client,{}) for name,clients in obs.items()}
            for case in manifest['selected_cases']:
                name=case['name']; observation=peers.get(name,{})
                record={'run':folder.name,'corpus':manifest['corpus'],'case':name,'method':case['request']['method'],'client':client,'version':summary['versions'].get(client,'unknown'),'status':observation.get('status','not_observed'),'eligible':eligible,'capture_eligible':summary['eligible'].get(client,False),'eligibility_detail':scenario_detail,'checks':[],'spec_commit':lock['commit'] if spec else None}
                info=manifest['clients'][client]
                record['build_id']=info.get('image_id') or info.get('digest')
                record['captured_at']=manifest.get('started_at')
                expected=[t for t,d in decisions.items() if manifest['corpus']+'/'+name in d['cases']]
                if record['eligible'] and observation:
                    errors=request_errors(case['request'],methods) if spec and not is_extension_request(case['request']) else []
                    record['request_errors']=errors
                    checks=evaluate(dict(case,context=rule_context),observation,peers,invalid_params=errors)
                    checks=supplement(dict(case,context=rule_context),observation,peers,checks,expected)
                    record['checks']=cover_topics(checks,expected)
                    if spec and observation.get('status')=='result' and case['request']['method'] in methods and not is_extension_request(case['request']):
                        schema=methods[case['request']['method']]['result']['schema']
                        errors=list(Draft201909Validator(schema).iter_errors(observation['response']['result']))
                        record['schema']={'status':'invalid' if errors else 'valid','errors':[{'path':'/'.join(map(str,e.absolute_path)), 'message':e.message[:300]} for e in errors[:8]]}
                record['checks']=cover_topics(record['checks'],expected)
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
                    by_client[client][check['topic']].append(dict(check,case=name,run=folder.name,corpus=manifest['corpus'],lock=link(folder/'manifest.json',root),evidence=link(folder/'observations.json',output/'clients')))
                records.append(record)
                case_pages[(manifest['corpus'],name)].append({'record':record,'request':case['request'],'observation':observation,'raw':folder/'observations.json'})
    write(output/'assessment.json', {
        'spec_commit': lock['commit'] if spec else None,
        'sources': {name:sha(root/name) for name in ['trace_interop/coverage.py','trace_interop/chain_model.py','trace_interop/execution_models.py','trace_interop/vm_model.py','trace_interop/rules.py','trace_interop/oracles.py','trace_interop/report.py','trace_interop/presentation.py','trace_interop/status.py','trace_interop/scenarios.py','trace_interop/validation.py','trace_interop/inventory.py','reports.lock.json','decisions/sources.json','locks/source-revisions.json','spec.lock.json','decisions/ledger.json','decisions/impact.json','decisions/status.json']},
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
    render(root, output, records, by_client, case_pages, run_rows, decisions, lock)
    print(f'Generated {len(records)} observation assessments and {len(decisions)} decision pages in {output}')

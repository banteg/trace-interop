"""Generate client impact pages from decisions and independently checked runs."""
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path

from .cli import read, write, sha
from .rules import evaluate


def link(path, output):
    return os.path.relpath(path, output).replace(os.sep, '/')


def escape(value):
    return str(value).replace('|','\\|').replace('\n',' ')


def generate(root, runs, output):
    output=output.resolve();output.mkdir(parents=True,exist_ok=True)
    ledger=read(root/'decisions/ledger.json')
    decisions={x['id']:x for x in ledger['items']}
    impacts=read(root/'decisions/impact.json') if (root/'decisions/impact.json').exists() else {}
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
        for client in manifest['clients']:
            peers={name:clients.get(client,{}) for name,clients in obs.items()}
            for case in manifest['selected_cases']:
                name=case['name']; observation=peers.get(name,{})
                record={'run':folder.name,'corpus':manifest['corpus'],'case':name,'client':client,'version':summary['versions'].get(client,'unknown'),'status':observation.get('status','not_observed'),'eligible':summary['eligible'].get(client,False),'checks':[],'spec_commit':lock['commit'] if spec else None}
                if record['eligible'] and observation:
                    record['checks']=evaluate(dict(case,context=context),observation,peers)
                    if spec and observation.get('status')=='result' and case['request']['method'] in methods:
                        schema=methods[case['request']['method']]['result']['schema']
                        errors=list(Draft201909Validator(schema).iter_errors(observation['response']['result']))
                        record['schema']={'status':'invalid' if errors else 'valid','errors':[{'path':'/'.join(map(str,e.absolute_path)), 'message':e.message[:300]} for e in errors[:8]]}
                for check in record['checks']:
                    by_client[client][check['topic']].append(dict(check,case=name,run=folder.name,corpus=manifest['corpus'],lock=link(folder/'manifest.json',root),evidence=link(folder/'observations.json',output/'clients')))
                records.append(record)
                case_pages[(manifest['corpus'],name)].append({'record':record,'request':case['request'],'observation':observation,'raw':folder/'observations.json'})
    write(output/'assessment.json', {
        'spec_commit': lock['commit'] if spec else None,
        'sources': {name:sha(root/name) for name in ['trace_interop/rules.py','trace_interop/report.py','spec.lock.json','decisions/ledger.json','decisions/impact.json']},
        'evidence': {row['manifest']:row['digest'] for row in run_rows},
    })
    write(output/'checks.json',records)
    comparisons=[]
    for (corpus,name),entries in sorted(case_pages.items()):
        path=output/'cases'/corpus/(name+'.md');path.parent.mkdir(parents=True,exist_ok=True)
        groups={}
        text=f'# {corpus}/{name}\n\nExact observations; group size is not a correctness vote.\n\n```json\n'+json.dumps(entries[0]['request'],indent=2)+'\n```\n\n'
        for entry in entries:
            r=entry['record'];obs=entry['observation'];response=obs.get('response')
            normalized={k:v for k,v in response.items() if k not in ['jsonrpc','id']} if isinstance(response,dict) else obs.get('raw_response',obs.get('status'))
            fingerprint=hashlib.sha256(json.dumps(normalized,sort_keys=True).encode()).hexdigest()
            groups.setdefault(fingerprint,[]).append({'client':r['client'],'version':r['version'],'status':r['status'],'eligible':r['eligible']})
            text+=f'## {r["client"]} · {r["version"]}\n\nCapture: **{r["status"]}**; scenario eligible: **{r["eligible"]}**. [Full evidence]({link(entry["raw"],path.parent)}).\n\n'
            for check in r['checks']:text+=f'- {check["topic"]}: **{check["status"]}** — {check["requirement"]}\n'
            if 'schema' in r:
                text+=f'\nDraft result schema: **{r["schema"]["status"]}**.\n'
                for err in r['schema']['errors']:text+=f'- `{err["path"]}`: {escape(err["message"])}\n'
            preview=json.dumps(response if response is not None else obs,indent=2)
            if len(preview)>2000:preview=preview[:2000]+'\n… preview truncated; use the full evidence link above.'
            text+='\n<details><summary>Response preview</summary>\n\n```json\n'+preview+'\n```\n\n</details>\n\n'
        path.write_text('\n'.join(line.rstrip() for line in text.splitlines())+'\n')
        comparisons.append({'corpus':corpus,'case':name,'groups':[{'sha256':h,'observations':clients} for h,clients in groups.items()]})
    write(output/'comparisons.json',comparisons)
    write(output/'runs.json',run_rows)
    introduction='# Trace API draft impact\n\nProposals for review, not an adopted standard or a client ranking. '
    introduction+='Results apply to the pinned builds and selected cases. '
    introduction+='Schema validity, partial semantic assertions and full conformance are different claims.\n\n'
    if (root/'spec.lock.json').exists():
        lock=read(root/'spec.lock.json');introduction+=f'Draft: [{lock["commit"][:12]}]({lock["repository"]}/commit/{lock["commit"]}).\n\n'
    introduction+='## Method observations\n\nR = at least one result; E = error responses only; U = method not found. Mixed results remain visible.\n\n'
    clients=sorted({r['client'] for r in records})
    introduction+='| Method | '+' | '.join(clients)+' |\n| --- | '+' | '.join('---' for _ in clients)+' |\n'
    for method in sorted(methods if spec else []):
        cells=[]
        for client in clients:
            statuses={e['record']['status'] for entries in case_pages.values() for e in entries if e['record']['client']==client and e['record']['eligible'] and e['request']['method']==method}
            cells.append(', '.join(label for status,label in [('result','R'),('rpc_error','E'),('unsupported','U'),('malformed_json','malformed JSON'),('invalid_envelope','invalid envelope')] if status in statuses) or 'not observed')
        introduction+='| `'+method+'` | '+' | '.join(cells)+' |\n'
    introduction+='\n## Client impact\n\n'
    all_clients=sorted(set(by_client)|{'besu_release','erigon_release','nethermind_release','reth_release'})
    for client in all_clients:
        introduction+=f'- [{client}](clients/{client}.md)\n'
        path=output/'clients'/f'{client}.md';path.parent.mkdir(exist_ok=True)
        text=f'# {client}: proposed changes\n\n'
        versions=sorted({r['version'] for r in records if r['client']==client})
        text+='Tested builds: '+(', '.join(f'`{v}`' for v in versions) or 'not run')+'.\n\n'
        text+='Matches mean only the linked assertions matched. They do not certify a whole decision or method.\n\n'
        text+='| Decision | Assertion results | Required change / review task |\n| --- | --- | --- |\n'
        base=client.split('_')[0]
        for id,d in decisions.items():
            checks=by_client[client][id]
            counts={s:sum(c['status']==s for c in checks) for s in ['change_needed','matches','unsupported']}
            verdict=', '.join(f'{n} {s.replace("_"," ")}' for s,n in counts.items() if n) or 'Not asserted / needs review'
            if counts['change_needed']:
                impact=impacts.get(id,{}).get(base,'; '.join(dict.fromkeys(c['requirement'] for c in checks if c['status']=='change_needed')))
            elif counts['unsupported']:
                impact=impacts.get(id,{}).get(base,'Implement the method or agree its exclusion from the profile.')
            elif checks:
                impact='No change identified by these checks.'
            else:
                impact='Needs review; no assertion covers this decision.'
            text+=f'| [{id} — {escape(d["title"])}](../decisions/{id}.md) | {verdict} | {escape(impact)} |\n'
        for id,checks in by_client[client].items():
            if not checks:continue
            text+=f'\n<details><summary>{id}: {len(checks)} assertion checks</summary>\n\n'
            for c in checks:
                text+=f'- **{c["status"]}** · `{c["run"]}` / `{c["case"]}`: {c["requirement"]} {c.get("detail","")}\n'
                text+=f'  [Compare responses](../cases/{c["corpus"]}/{c["case"]}.md) · [Raw responses]({c["evidence"]}).\n'
                text+=f'  Reproduce: `uv run trace-interop run --lock {c["lock"]} --clients {client} --corpus {c["corpus"]} --case "^{c["case"]}$" --output runs/reproduce`\n'
            text+='\n</details>\n'
        path.write_text('\n'.join(line.rstrip() for line in text.splitlines())+'\n')
    introduction+='\n## Runs\n\n| Run | Corpus | Capture complete | Versions |\n| --- | --- | --- | --- |\n'
    for row in run_rows:introduction+=f'| [{row["name"]}]({row["manifest"]}) | {row["corpus"]} | {row["complete"]} | {escape(row["versions"])} |\n'
    introduction+='\n## Review decisions\n\n'
    for id,d in decisions.items():
        introduction+=f'- [{id} — {d["title"]}](decisions/{id}.md)\n'
        path=output/'decisions'/f'{id}.md';path.parent.mkdir(exist_ok=True)
        text=f'# {id} — {d["title"]}\n\n**Disposition:** {d["kind"]}. Proposal, awaiting client review.\n\n'
        for title,key in [('Proposed behavior','recommendation'),('Rationale','rationale'),('Open questions','next_step')]:text+=f'## {title}\n\n{d[key]}\n\n'
        text+='## Evidence\n\n'
        for name in d['cases']:
            text+=f'- [{name}]({link(root/"evidence/2026-09-15/cases"/(name+".json"),path.parent)})\n'
        text+='\n## Observations\n\n'
        found=False
        for client,topics in by_client.items():
            for c in topics[id]:
                found=True;text+=f'- {client}: **{c["status"]}**, `{c["run"]}/{c["case"]}` — {c["requirement"]}\n'
        if not found:text+='No automated assertion for this decision in the selected runs. Review remains manual.\n'
        path.write_text('\n'.join(line.rstrip() for line in text.splitlines())+'\n')
    (output/'README.md').write_text(introduction)
    index='# Trace API decisions\n\nEach decision links proposed behavior, rationale, observations and open questions.\n\n| Decision | Question |\n| --- | --- |\n'
    for id,d in decisions.items():index+=f'| [{id}](../reports/decisions/{id}.md) | {escape(d["title"])} |\n'
    if output == (root/'reports').resolve():
        (root/'decisions/README.md').write_text(index)
    print(f'Generated {len(records)} observation assessments and {len(decisions)} decision pages in {output}')

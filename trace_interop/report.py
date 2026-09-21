"""Generate client impact pages from dated decisions and independently checked runs."""
from collections import defaultdict
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
    by_client=defaultdict(lambda:defaultdict(list)); records=[]; run_rows=[]
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
        for client in manifest['clients']:
            peers={name:clients.get(client,{}) for name,clients in obs.items()}
            for case in manifest['selected_cases']:
                name=case['name']; observation=peers.get(name,{})
                record={'run':folder.name,'corpus':manifest['corpus'],'case':name,'client':client,'version':summary['versions'].get(client,'unknown'),'status':observation.get('status','not_observed'),'eligible':summary['eligible'].get(client,False),'checks':[]}
                if record['eligible'] and observation:
                    record['checks']=evaluate(case,observation,peers)
                    if spec and observation.get('status')=='result' and case['request']['method'] in methods:
                        schema=methods[case['request']['method']]['result']['schema']
                        errors=list(Draft201909Validator(schema).iter_errors(observation['response']['result']))
                        record['schema']={'status':'invalid' if errors else 'valid','errors':[{'path':'/'.join(map(str,e.absolute_path)), 'message':e.message[:300]} for e in errors[:8]]}
                for check in record['checks']:
                    by_client[client][check['topic']].append(dict(check,case=name,run=folder.name,corpus=manifest['corpus']))
                records.append(record)
    write(output/'checks.json',records)
    write(output/'runs.json',run_rows)
    introduction='# Trace API draft impact\n\nProposals for review, not an adopted standard or a client ranking. '
    introduction+='Historical recommendations date to September 15. Fresh checks below are restricted to the exact pinned builds and selected cases. '
    introduction+='Schema validity, partial semantic assertions and full conformance are different claims.\n\n'
    if (root/'spec.lock.json').exists():
        lock=read(root/'spec.lock.json');introduction+=f'Draft: [{lock["commit"][:12]}]({lock["repository"]}/commit/{lock["commit"]}).\n\n'
    introduction+='## Client impact\n\n'
    all_clients=sorted(set(by_client)|{'besu_release','erigon_release','nethermind_release','reth_release'})
    for client in all_clients:
        introduction+=f'- [{client}](clients/{client}.md)\n'
        path=output/'clients'/f'{client}.md';path.parent.mkdir(exist_ok=True)
        text=f'# {client}: proposed changes\n\n'
        versions=sorted({r['version'] for r in records if r['client']==client})
        text+='Fresh builds: '+(', '.join(f'`{v}`' for v in versions) or 'not run')+'.\n\n'
        text+='Matches mean only the linked assertions matched. They do not certify a whole decision or method. Historical change descriptions require review against fresh results.\n\n'
        text+='| Decision | Fresh assertion results | Historical candidate change / review task |\n| --- | --- | --- |\n'
        base=client.split('_')[0]
        for id,d in decisions.items():
            checks=by_client[client][id]
            counts={s:sum(c['status']==s for c in checks) for s in ['change_needed','matches','unsupported']}
            verdict=', '.join(f'{n} {s.replace("_"," ")}' for s,n in counts.items() if n) or 'Not asserted / needs review'
            impact=impacts.get(id,{}).get(base,'Review the proposed rule and linked evidence; no automated client-specific conclusion.')
            text+=f'| [{id} — {escape(d["title"])}](../decisions/{id}.md) | {verdict} | {escape(impact)} |\n'
        for id,checks in by_client[client].items():
            if not checks:continue
            text+=f'\n## {id} assertion evidence\n\n'
            for c in checks:
                text+=f'- **{c["status"]}** · `{c["run"]}` / `{c["case"]}`: {c["requirement"]} {c.get("detail","")}\n'
                text+=f'  Reproduce: `uv run trace-interop run --lock clients.lock.json --clients {client} --corpus {c["corpus"]} --case "^{c["case"]}$" --output runs/reproduce`\n'
        path.write_text(text)
    introduction+='\n## Runs\n\n| Run | Corpus | Capture complete | Versions |\n| --- | --- | --- | --- |\n'
    for row in run_rows:introduction+=f'| [{row["name"]}]({row["manifest"]}) | {row["corpus"]} | {row["complete"]} | {escape(row["versions"])} |\n'
    introduction+='\n## Review decisions\n\n'
    for id,d in decisions.items():
        introduction+=f'- [{id} — {d["title"]}](decisions/{id}.md)\n'
        path=output/'decisions'/f'{id}.md';path.parent.mkdir(exist_ok=True)
        text=f'# {id} — {d["title"]}\n\n**Disposition:** {d["kind"]}. Proposal, awaiting client review.\n\n'
        for title,key in [('Proposed behavior','recommendation'),('Rationale','rationale'),('September 15 observation','observed'),('Unresolved review','next_step')]:text+=f'## {title}\n\n{d[key]}\n\n'
        text+='## Historical evidence\n\n'
        for name in d['cases']:
            text+=f'- [{name}]({link(root/"evidence/2026-09-15/cases"/(name+".json"),path.parent)})\n'
        text+='\n## Fresh assertions\n\n'
        found=False
        for client,topics in by_client.items():
            for c in topics[id]:
                found=True;text+=f'- {client}: **{c["status"]}**, `{c["run"]}/{c["case"]}` — {c["requirement"]}\n'
        if not found:text+='No automated assertion for this decision in the selected runs. Review remains manual.\n'
        path.write_text(text)
    (output/'README.md').write_text(introduction)
    print(f'Generated {len(records)} observation assessments and {len(decisions)} decision pages in {output}')

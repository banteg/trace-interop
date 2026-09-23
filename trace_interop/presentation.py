"""Maintainer-facing views of the independently evaluated observations."""
from collections import defaultdict
from datetime import datetime, timezone
import json
import os

from .status import decision_status, LEGEND


SOURCE_GROUPS = {
    'H01': ['replay'], 'H02': ['lookup'], 'H03': ['filter'],
    'H04': ['filter'], 'H05': ['filter', 'frames'], 'H06': ['lookup', 'replay'],
    'H07': ['replay'], 'H08': ['replay', 'call'], 'H09': ['frames'],
    'H10': ['frames'], 'H11': ['call'], 'H12': ['raw'], 'H13': ['raw'],
    'H14': ['raw', 'call'], 'H15': ['call'], 'H16': ['call', 'state'],
    'H17': ['state'], 'H18': ['state', 'replay'], 'H19': ['vm', 'replay'],
    'H20': ['vm'], 'H21': ['vm'], 'H22': ['frames'], 'H23': ['filter'],
    'H24': ['frames'], 'H25': ['raw', 'replay'], 'H26': ['state'],
    'H27': ['filter'], 'H28': ['call'], 'H29': ['frames'],
    'H30': ['bounds'], 'H31': ['many'], 'H32': ['tags', 'many'],
}
BAD = {'change_needed', 'unsupported'}


def relative(path, parent):
    return os.path.relpath(path, parent).replace(os.sep, '/')


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def table(headers, rows):
    lines = ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join('---' for _ in headers) + ' |']
    lines.extend('| ' + ' | '.join(cell(c) for c in row) + ' |' for row in rows)
    return '\n'.join(lines) + '\n\n'


def save(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(line.rstrip() for line in text.splitlines()).rstrip() + '\n')


def family(client):
    return 'geth' if client == 'go-ethereum_trace' else client.split('_')[0]


def channel(client):
    return 'Draft fork' if client == 'go-ethereum_trace' else client.split('_', 1)[1].capitalize()


def verdict(checks):
    statuses = {c['status'] for c in checks}
    if 'unsupported' in statuses:
        return 'Method unavailable'
    if 'change_needed' in statuses:
        return 'Differs'
    if 'unassessed' in statuses:
        return 'Partially assessed' if statuses - {'unassessed'} else 'Not assessed'
    if 'observation' in statuses:
        return 'Policy open'
    if 'matches' in statuses:
        return 'Checked cases agree'
    return 'Not assessed'


def utc_date(timestamp):
    if not timestamp:
        return 'Not recorded'
    return datetime.fromisoformat(timestamp.replace('Z', '+00:00')).astimezone(timezone.utc).date().isoformat()


def build_rows(selected, runs, revisions, parent):
    """Pair exact tested versions with source commits, never infer from a channel label."""
    groups = {}
    for client in selected:
        for run in runs:
            if client not in run['manifest']['clients']:
                continue
            version = run['versions'].get(client, 'unknown')
            dates = groups.setdefault((client, version), {})
            tested = utc_date(run['manifest'].get('started_at'))
            dates.setdefault(tested, run['path'])
    rows = []
    for (client, version), dates in groups.items():
        refs = [ref for ref in revisions.get(client, []) if ref['version'] == version]
        if len(refs) > 1:
            raise ValueError(f'ambiguous source revision for {client}: {version}')
        committed = 'Not recorded'
        if refs:
            ref = refs[0]
            committed = f'[{utc_date(ref["committed_at"])}]({ref["repository"]}/commit/{ref["commit"]})'
        tested = '<br>'.join(f'[{date}]({relative(path, parent)})' for date,path in sorted(dates.items()))
        rows.append([channel(client), f'`{version}`', committed, tested])
    return rows


def source_url(source):
    return f'{source["repository"]}/blob/{source["commit"]}/{source["path"]}#L{source["line"]}'


def source_links(sources, client, topic):
    links = []
    for group in SOURCE_GROUPS[topic]:
        ref = sources.get(family(client), {}).get(group)
        if ref:
            links.append(f'[{ref["label"]}]({source_url(ref)})')
    return ' · '.join(links)


def case_link(output, parent, check, label='Example'):
    path = output/'cases'/check['corpus']/(check['case'] + '.md')
    return f'[{label}]({relative(path, parent)})'


def examples(output, parent, checks, limit=2):
    selected = {}
    for c in sorted(checks, key=lambda x: (x['status'] not in BAD, x['corpus'], x['case'])):
        selected.setdefault((c['corpus'], c['case']), c)
    return ' · '.join(case_link(output, parent, c, c['case'].replace('-', ' ').capitalize()) for c in list(selected.values())[:limit])


def outcome(entry):
    """Describe the RPC outcome without treating intentional errors as test failures."""
    r = entry['record']; obs = entry['observation']
    if not r['eligible']:
        return 'Setup incomplete; not assessed'
    response = obs.get('response') or {}
    status = r['status']
    if status in ('rpc_error', 'unsupported'):
        error = response.get('error') or {}
        label = 'Method unavailable' if status == 'unsupported' else 'RPC error'
        return f'{label} `{error.get("code", "?")}`'
    if status != 'result':
        return {'malformed_json': 'Incomplete or malformed JSON', 'invalid_envelope': 'Invalid JSON-RPC envelope', 'not_observed': 'No response captured'}.get(status, status.replace('_', ' '))
    value = response.get('result')
    if value is None:
        return '`null`'
    if isinstance(value, list):
        return f'{len(value)} records' if value else '`[]`'
    if isinstance(value, dict):
        if value.get('jsonrpc') == '2.0' and 'error' in value:
            return 'Error envelope nested inside result'
        if 'traceAddress' in value:
            return f'One frame, path `{json.dumps(value["traceAddress"])}`'
        if 'output' in value:
            output = value['output']
            suffix = f'{len(value["trace"])} call frames; ' if isinstance(value.get('trace'), list) else ''
            return suffix + ('output `null`' if output is None else 'output `0x`' if output == '0x' else 'nonempty output')
        return 'Object returned'
    return f'`{str(value)[:80]}`'


def note(editorial, client, topic, checks):
    topic_notes = editorial['topics'].get(topic, {})
    entry = topic_notes.get(family(client))
    if entry:
        requirements = list(dict.fromkeys(c['requirement'] for c in checks if c['status'] in BAD))
        suffix = ' Checked requirements: ' + ' '.join(requirements) if requirements and topic_notes.get('append_checked_requirements', True) else ''
        return entry['observed'], entry['change'] + suffix
    failed = list(dict.fromkeys(c['requirement'] for c in checks if c['status'] in BAD))
    return 'The linked case differs from the proposed behavior.', ' '.join(failed)


def prune_case_pages(output, cases):
    """Keep generated case pages aligned with the active report inventory."""
    expected = {output/'cases'/corpus/(name+'.md') for corpus,name in cases}
    for path in (output/'cases').rglob('*.md'):
        if path not in expected:
            path.unlink()


def render(root, output, records, by_client, case_pages, run_rows, decisions, lock):
    prune_case_pages(output, case_pages)
    editorial = json.loads((root/'decisions/impact.json').read_text())
    positions = json.loads((root/'decisions/status.json').read_text())
    if set(positions) - set(decisions):
        raise ValueError('Policy status references an unknown decision')
    statuses = {topic: decision_status(d, records, positions.get(topic, {})) for topic, d in decisions.items()}
    sources = json.loads((root/'decisions/sources.json').read_text())
    revisions = json.loads((root/'locks/source-revisions.json').read_text())
    clients = sorted({r['client'] for r in records})
    run_manifests = {row['name']: output/row['manifest'] for row in run_rows}
    build_runs = [{'manifest': json.loads(run_manifests[row['name']].read_text()),
                   'versions': row['versions'], 'path': run_manifests[row['name']]} for row in run_rows]
    availability = defaultdict(lambda: defaultdict(set))
    for entries in case_pages.values():
        for e in entries:
            r = e['record']
            if r['eligible']:
                availability[e['request']['method']][r['client']].add(r['status'])

    def method_status(method, client):
        statuses = availability[method][client]
        if 'unsupported' in statuses:
            return 'Unavailable' if statuses == {'unsupported'} else 'Mixed responses'
        if 'result' in statuses:
            return 'Returns results'
        return 'Errors only' if statuses else 'Not observed'

    families = sorted({family(c) for c in clients})
    names = {c: editorial['clients'][family(c)]['name'] for c in clients}
    by_family = {f: sorted((c for c in clients if family(c) == f), key=lambda c: c.endswith('_development')) for f in families}

    # Case pages are the drill-down, keeping the overview free of wire dumps.
    for (corpus, name), entries in sorted(case_pages.items()):
        path = output/'cases'/corpus/(name + '.md')
        method = entries[0]['request']['method']
        text = f'# {name.replace("-", " ").capitalize()}\n\n`{method}` · {corpus} · [All reports]({relative(output/"README.md", path.parent)})\n\n'
        requirements = list(dict.fromkeys(c['requirement'] for e in entries for c in e['record']['checks']))
        if requirements:
            text += '**What this checks:** ' + ' '.join(requirements) + '\n\n'
        rows = []
        for e in sorted(entries, key=lambda e: (family(e['record']['client']), e['record']['client'].endswith('_development'), e['record']['run'])):
            r = e['record']; client = r['client']
            assessment = verdict(r['checks']) if r['eligible'] else 'Not assessed'
            if r.get('schema', {}).get('status') == 'invalid':
                assessment += '; result shape differs'
            rows.append([f'[{names[client]} · {channel(client)}]({relative(output/"clients"/(client+".md"), path.parent)})', outcome(e), assessment, f'[Response]({relative(e["raw"], path.parent)}) · [Build/run]({relative(run_manifests[r["run"]], path.parent)})'])
        text += table(['Build', 'Returned', 'Compared with draft', 'Evidence'], rows)
        text += '<details><summary>Request and assertion details</summary>\n\n```json\n' + json.dumps(entries[0]['request'], indent=2) + '\n```\n\n'
        for e in entries:
            r = e['record']; failures = [c for c in r['checks'] if c['status'] in BAD or c['status'] in {'observation','unassessed'}]
            errors = r.get('schema', {}).get('errors', [])
            if not failures and not errors:
                continue
            text += f'**{names[r["client"]]} · {channel(r["client"])}** (`{r["version"]}`)\n\n'
            for c in failures:
                text += f'- [{c["topic"]}]({relative(output/"decisions"/(c["topic"]+".md"), path.parent)}): {c["requirement"]} {c.get("detail", "")}\n'
            for err in errors:
                text += f'- Result shape at `{err["path"] or "/"}`: {cell(err["message"])}\n'
            text += '\n'
        text += '</details>\n'
        save(path, text)

    # Each family has one review page, with stable per-build entry points as well.
    def client_page(f, selected, path):
        profile = editorial['clients'][f]
        text = f'# {profile["name"]}: changes to review\n\n{profile["summary"]}\n\n[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)\n\n'
        text += table(['Build', 'Tested version', 'Commit date (UTC)', 'Tested (UTC)'], build_rows(selected, build_runs, revisions, path.parent))
        versions = {r['version'] for r in records if r['client'] in selected}
        for build_note in profile.get('build_notes', []):
            if versions and versions <= set(build_note['versions']):
                text += build_note['text'] + '\n\n'
        text += 'Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method.\n\n'
        rows = []; matched = []; untested = []; observations = []; partial = []
        for topic, d in decisions.items():
            checks = [q for c in selected for q in by_client[c].get(topic, [])]
            if checks and any(q['status'] == 'observation' for q in checks) and not any(q['status'] in BAD for q in checks):
                observations.append(topic)
                continue
            if not any(q['status'] in BAD for q in checks):
                if topic != 'H01':
                    (partial if any(q['status']=='unassessed' for q in checks) else matched if checks else untested).append(topic)
                continue
            affected = next(c for c in selected if any(q['status'] in BAD for q in by_client[c].get(topic, [])))
            observed, change = note(editorial, affected, topic, checks)
            subject = f'[{d["title"]}](../decisions/{topic}.md)<br>{observed}'
            statuses = []
            for c in selected:
                cchecks = by_client[c].get(topic, [])
                value = verdict(cchecks)
                if cchecks:
                    value += '<br>' + examples(output, path.parent, cchecks, 1)
                statuses.append(value)
            links = source_links(sources, affected, topic)
            rows.append([subject, *statuses, change + ('<br>' + links if links else '')])
        text += '## Changes to discuss\n\n'
        text += table(['Behavior', *[channel(c) for c in selected], 'Proposed change'], rows) if rows else 'No differences were found by the selected semantic assertions.\n\n'
        if observations:
            text += '## Open policy observations\n\nThese results record behavior whose policy is unresolved. Passing a checked part of a topic does not settle the remaining choices.\n\n'
            observation_rows = []
            for topic in observations:
                for c in selected:
                    checks = by_client[c].get(topic, [])
                    if checks:
                        detail = ' '.join(dict.fromkeys(q['detail'] for q in checks if q['status'] == 'observation'))
                        observation_rows.append([channel(c), f'[{decisions[topic]["title"]}](../decisions/{topic}.md)', detail, examples(output, path.parent, checks)])
            text += table(['Build', 'Decision', 'Observed', 'Example'], observation_rows)
        other_schema = [r for r in records if r['client'] in selected and r.get('schema', {}).get('status') == 'invalid']
        if other_schema:
            text += 'Result-shape differences are recorded on the [case pages](../technical.md#result-shape-checks); schema validity is separate from semantic coverage.\n\n'
        if partial:
            text += '**Partially assessed:** some declared cases lack an evaluated assertion. ' + ', '.join(f'[{decisions[t]["title"]}](../decisions/{t}.md)' for t in partial) + '.\n\n'
        if matched:
            text += '<details><summary>Behaviors with no difference in the checked cases</summary>\n\n'
            text += table(['Behavior', 'Examples'], [[f'[{decisions[t]["title"]}](../decisions/{t}.md)', examples(output, path.parent, [q for c in selected for q in by_client[c].get(t, [])])] for t in matched])
            text += '</details>\n\n'
        if untested:
            text += '**Still needs review:** ' + ', '.join(f'[{decisions[t]["title"]}](../decisions/{t}.md)' for t in untested) + '.\n\n'
        text += '[Method availability](../decisions/H01.md) · [All behavior decisions](../../decisions/README.md)\n\n'
        text += 'For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).\n'
        save(path, text)

    for f, selected in by_family.items():
        client_page(f, selected, output/'clients'/(f + '.md'))
        for c in selected:
            client_page(f, [c], output/'clients'/(c + '.md'))

    for topic, d in decisions.items():
        path = output/'decisions'/(topic + '.md')
        text = f'# {d["title"]}\n\n{topic} · {d["kind"]} · [All decisions](../README.md#decisions-to-review)\n\n'
        position = positions.get(topic, {})
        text += f'**Status: {statuses[topic]}** · [Status definitions](../../decisions/README.md#status-key)\n\n'
        text += position.get('note', 'No policy conclusion has been recorded. Implementation observations below do not establish client-team agreement.') + '\n\n'
        if position.get('sources'):
            text += 'Policy evidence: ' + ' · '.join(f'[{source["label"]}]({source["url"]})' for source in position['sources']) + '.\n\n'
        sections = {'H12': 'explicit-choices-in-this-draft', 'H13': 'open-details-requiring-focused-review', 'H29': 'precompile-frames-h29'}
        if topic in sections:
            text += f'[Rule in the pinned draft]({lock["repository"]}/blob/{lock["commit"]}/docs-api/docs/trace-profile.md#{sections[topic]})\n\n'
        text += f'## Recommendation\n\n{d["recommendation"]}\n\n{d["rationale"]}\n\n'
        if d.get('background'):
            text += '## Background\n\n' + '\n\n'.join(d['background']) + '\n\n'
        text += f'## {d.get("comparison_heading", "What changes for clients")}\n\n'
        rows = []
        for f, selected in by_family.items():
            checks = [q for c in selected for q in by_client[c].get(topic, [])]
            affected = next((c for c in selected if any(q['status'] in BAD for q in by_client[c].get(topic, []))), None)
            if affected:
                observed, change = note(editorial, affected, topic, checks)
                behavior = observed + '<br>**Proposed:** ' + change
            elif any(q['status'] == 'unassessed' for q in checks):
                behavior = 'Some declared cases were not assessed. Matching checks do not establish agreement for this topic.'
            elif any(q['status'] == 'observation' for q in checks):
                details = []
                for c in selected:
                    observed = list(dict.fromkeys(q['detail'] for q in by_client[c].get(topic, [])
                                                  if q['status'] == 'observation' and q['detail']))
                    if observed:
                        details.append(f'{channel(c)}: ' + ' '.join(observed))
                behavior = '<br>'.join(details) + ' Policy remains open; these observations alone do not require a baseline change.'
            else:
                behavior = 'No change identified in the checked cases.' if checks else 'No automated assertion yet; review the recommendation.'
            build_cells = '<br>'.join(f'{channel(c)}: {verdict(by_client[c].get(topic, []))}' for c in selected)
            links = examples(output, path.parent, checks)
            code = source_links(sources, selected[0], topic)
            evidence_links = '<br>'.join(x for x in (
                '🧪 Tests: ' + links if links else '',
                '💻 Client code: ' + code if code else '',
            ) if x)
            rows.append([f'[{editorial["clients"][f]["name"]}](../clients/{f}.md)', build_cells, behavior, evidence_links])
        if topic == 'H01':
            text += 'A returned result establishes method availability, not conformance. Errors for malformed input are expected.\n\n'
            method_rows = []
            for method in sorted(m for m in availability if m.startswith('trace_')):
                values = []
                for f, selected in by_family.items():
                    labels = [method_status(method, c) for c in selected]
                    values.append(labels[0] if len(set(labels)) == 1 else '<br>'.join(f'{channel(c)}: {value}' for c,value in zip(selected,labels)))
                method_rows.append([f'`{method}`', *values])
            text += table(['Method', *[editorial['clients'][f]['name'] for f in families]], method_rows)
            text += 'Besu needs individual transaction replay or an agreed exclusion from the profile; the [block replay implementation](' + source_url(sources['besu']['replay']) + ') is a starting point.\n\n'
        else:
            text += table(['Client', 'Tested builds', 'Impact', 'Examples and code'], rows)
        text += f'## Decision needed\n\n{d["next_step"]}\n'
        save(path, text)

    text = '# Trace API: what would change?\n\nThe clients already share much of the `trace_*` API. These reports show where adopting the [draft specification](' + lock['repository'] + '/tree/' + lock['commit'] + ') would change their behavior. Start with your client, then use the examples and source links to review a proposed change.\n\n'
    text += '## Start with your client\n\n'
    text += table(['Client', 'Main review areas'], [[f'[{editorial["clients"][f]["name"]}](clients/{f}.md)', editorial['clients'][f]['summary']] for f in families])
    text += '## Decisions to review\n\n'
    text += 'The largest API choices are [tree-path lookup](decisions/H02.md), [address-filter composition](decisions/H03.md), and [failed-frame results](decisions/H09.md). Other rows concern missing information or inconsistent execution/reporting. All recommendations remain proposals for client review.\n\n'
    text += table(['Question', 'Status', 'Proposed behavior'], [
        [f'[{title}](decisions/{topic}.md)', statuses[topic], behavior]
        for topic, title, behavior in [
            ('H02', 'How does trace_get select a frame?', 'Follow one tree path; return one object or null. An empty path selects the root.'),
            ('H03', 'How do address filters combine?', 'OR within each list, AND between sender and recipient lists.'),
            ('H30', 'Where does an unbounded filter start?', 'Search from the earliest available block through latest.'),
            ('H31', 'What block does trace_callMany use by default?', 'Accept an omitted block and use latest, matching trace_call.'),
            ('H32', 'Which tags and pending state can trace methods use?', 'Resolve mined-block tags; agree pending state and localization per method.'),
            ('H09', 'What survives a failed call?', 'Keep the error on that frame and preserve revert bytes and measured gas when available.'),
            ('H29', 'Which precompile frames are visible?', 'Keep root frames and nested frames with nonzero value; omit zero-value nested frames.'),
            ('H13', 'Signed transaction execution validity', 'Validate against the selected state, including nonce, funds and gas. Keep pool policies separate; propose -32003 for validation rejection.'),
        ]])
    text += '[Status definitions](../decisions/README.md#status-key). Policy direction is distinct from verified implementation on the captured builds.\n\n'
    text += f'[All {len(decisions)} decisions](../decisions/README.md) · [Method availability](decisions/H01.md)\n\n'
    text += '[Client fixes](../docs/client-fixes.md) · [Client source guide](sources.md) · [Run a case](../docs/usage.md) · [Builds, coverage and raw results](technical.md) · [Standardization discussion](https://github.com/ethereum/execution-apis/issues/890)\n'
    save(output/'README.md', text)

    text = '# Client source guide\n\nEntry points for reviewing the proposed changes. Links are pinned to the tested development revisions (or the experimental Geth fork), so line numbers remain stable. They identify relevant code, not necessarily the full fix.\n\n'
    for f in families:
        text += f'## {editorial["clients"][f]["name"]}\n\n'
        text += table(['Area', 'Source', 'Revision'], [[group.capitalize(), f'[{ref["label"]}]({source_url(ref)})', f'`{ref["commit"][:12]}`'] for group, ref in sources[f].items()])
    text += 'Reth’s inspector links point into its locked `revm-inspectors` 0.43.0 dependency. File hashes and anchor text are retained in [the source catalog](../decisions/sources.json).\n'
    save(output/'sources.md', text)

    text = '# Technical appendix\n\n[Back to the maintainer overview](README.md)\n\n'
    text += 'The human reports summarize selected assertions against a proposed specification. Agreement is not full conformance, and an RPC error can be the correct result for an invalid-input case. Setup failures are excluded from semantic assessment. Release and development labels refer to the captured builds; they do not imply version ordering.\n\n'
    text += 'The experimental Geth fork implements the draft and is not an independent vote for its decisions. No verified pruning scenario is included for that fork.\n\n'
    text += '## Reproduction and machine-readable results\n\nSee [usage](../docs/usage.md) for commands and [stateful scenarios](../docs/scenarios.md) for setup requirements. '
    text += '[checks.json](checks.json) retains every assertion; [comparisons.json](comparisons.json) groups exact responses; [assessment.json](assessment.json) pins the specification and assessment source hashes. Each case links its original response and run manifest.\n\n'
    text += 'To reproduce one case, use its linked manifest and the exact client, corpus and case name:\n\n```sh\nuv run trace-interop run --lock evidence/2026-09-21/RUN/manifest.json \\\n  --clients CLIENT --corpus CORPUS --case "^CASE$" --output runs/reproduce\n```\n\n'
    gaps = sorted({(r['client'],r['run'],r['corpus']) for r in records if not r['eligible']})
    text += '## Assertion coverage\n\nCoverage below counts all selected trace observations, including missing responses and failed setup, separately from schema validation. Partially assessed means at least one declared topic was not checked. A checked assertion is not proof of the rest of the topic.\n\n'
    text += table(['Coverage', 'Observations'], [[status, sum(r.get('assessment')==status for r in records if r['method'].startswith('trace_'))] for status in ['assessed','partial','unassessed']])
    text += 'Eligibility is recomputed from the frozen head and independent scenario controls. `capture_eligible` in checks.json preserves the original capture decision; original summaries and wire observations are unchanged.\n\n'
    text += '## Setup gaps\n\n'
    text += table(['Build', 'Scenario', 'Run evidence'], [[names[c]+' · '+channel(c), corpus, f'[{run}]({relative(run_manifests[run].parent/"summary.json", output)})'] for c,run,corpus in gaps]) if gaps else 'All selected runs passed their scenario eligibility checks.\n\n'
    text += '## Result-shape checks\n\nThese cases returned results that differ from the draft schema. The case pages retain the validation details; an unclassified schema failure is not silently counted as agreement.\n\n'
    shape = defaultdict(list)
    for r in records:
        if r.get('schema', {}).get('status') == 'invalid':
            shape[(r['corpus'],r['case'])].append(r['client'])
    text += table(['Case', 'Affected builds'], [[f'[{corpus}/{case}](cases/{corpus}/{case}.md)', ', '.join(names[c]+' '+channel(c) for c in sorted(set(cs)))] for (corpus,case),cs in sorted(shape.items())])
    text += '## Runs\n\n'
    text += table(['Run', 'Corpus', 'Capture complete'], [[f'[{row["name"]}]({row["manifest"]})',row['corpus'],'Yes' if row['complete'] else 'No'] for row in run_rows])
    save(output/'technical.md', text)
    if output == (root/'reports').resolve():
        text = '# Trace API decisions\n\n[Client impact overview](../reports/README.md) · [Source guide](../reports/sources.md)\n\n'
        text += table(['Decision', 'Status', 'Question'], [[f'[{t}](../reports/decisions/{t}.md)',statuses[t],d['title']] for t,d in decisions.items()])
        text += '## Status key\n\n' + LEGEND + '\n'
        save(root/'decisions/README.md', text)

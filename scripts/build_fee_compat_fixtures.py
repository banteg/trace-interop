"""Pair identical eth_call/trace_call environment and funding probes."""
import copy
from pathlib import Path

from scripts.build_fee_policy_fixtures import build as fee_cases
from trace_interop.cli import read, write, sha

ROOT = Path(__file__).resolve().parents[1]


def build():
    original = fee_cases()['cases']
    cases = [copy.deepcopy(c) for c in original if c['name'].startswith('_control/')]
    for case in original:
        if case['request']['method'] != 'trace_call' or case.get('fee_policy', {}).get('programs') != ['environment']:
            continue
        family, _, selection = case['name'].split('/')
        reference = family+'/eth'
        if selection == 'none':
            call, _, block = case['request']['params']
            cases.append(dict(name=reference, request=dict(jsonrpc='2.0', id=1, method='eth_call', params=[copy.deepcopy(call), block])))
        paired = copy.deepcopy(case)
        paired['name'] = family+'/trace/'+selection
        paired['fee_reference'] = reference
        cases.append(paired)
    return dict(description='H15 identical eth_call/trace_call requests, with independent environment and balance witnesses; all eight trace selections.', cases=cases)


if __name__ == '__main__':
    write(ROOT/'fixtures/corpora/fee-compat.json', build())
    checksums = read(ROOT/'fixtures/checksums.json')
    checksums['corpora/fee-compat.json'] = sha(ROOT/'fixtures/corpora/fee-compat.json')
    write(ROOT/'fixtures/checksums.json', checksums)

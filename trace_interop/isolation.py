"""Judge each defect under the one decision whose rule it breaks.

A check's topic often comes from the case it sits in, and a check that reads an executed
result also fires on an error response, so one defect could fail several decisions. Assertion
sites tag each check with the rule it tests (for example rules.accounting_topic). Assertion
sites also give a check these internal tags, which the functions here resolve and remove:

- `role: 'result'`: the check reads an executed result. On an error response, or an error
  envelope wrapped as a result, whose rejection another decision owns, it is blocked and names
  that owner. An error no decision's rule identifies stays a difference: the check's own
  decision may require the request to execute.
- `role: 'rejection'`: the check judges how this request is rejected. A schema-derived check
  (`role: 'schema'`, H14) yields to another decision's rejection check on the same request and
  becomes not applicable, naming that owner.
- `depends: [topic, ...]`: the check cannot separate its property from those decisions. It is
  blocked while a dependency's check differs on the same response or, when the response has none,
  anywhere in the same build's run.
"""
from collections import defaultdict

from .rules import SIMULATIONS, embedded_error, mapping, violation

# Which decision judges a validation rejection, by method.
VALIDATION_OWNERS = {**{method: 'H15' for method in SIMULATIONS}, 'trace_rawTransaction': 'H13'}


def error_owner(method, response):
    """(decision, reason) for the decision whose rule identifies this error response, or None."""
    if embedded_error(response):
        return 'H25', 'an error envelope returned as a successful result'
    message = mapping(response.get('error')).get('message')
    if method in VALIDATION_OWNERS and violation(message):
        return VALIDATION_OWNERS[method], f'a {violation(message)} validation rejection: {str(message)[:120]}'
    return None


def deferred(topic, case):
    """The decision whose rule governs a declared topic's property for this request, or None."""
    method, params = case['request']['method'], case['request'].get('params', [])
    if topic == 'H16' and method in SIMULATIONS:
        return 'H15', 'For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.'
    if topic in ['H02', 'H06'] and method == 'trace_get' and params:
        known = {t['hash'] for b in mapping(case.get('context', {}).get('_blocks')).values() for t in b['transactions']}
        if topic == 'H02' and known and params[0] not in known:
            return 'H06', 'The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.'
        if topic == 'H06' and params[0] in known:
            return 'H02', 'The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.'
    return None


def isolate(case, observation, checks):
    """Resolve the `role` tags of one response's checks."""
    response = mapping(observation.get('response'))
    error = observation.get('status') == 'rpc_error' or embedded_error(response)
    owner = error_owner(case['request']['method'], response) if error else None
    rejections = {c['topic'] for c in checks if c.get('role') == 'rejection'}
    isolated = []
    for check in checks:
        check = dict(check)
        role = check.pop('role', None)
        owners = sorted(rejections - {check['topic']}) if role == 'schema' else []
        if owners:
            check.update(status='not_applicable', detail=f'{" and ".join(owners)} owns this request’s rejection. {check["detail"]}')
        elif role == 'result' and owner and owner[0] != check['topic'] and check['status'] == 'change_needed':
            check.update(status='blocked', detail=f'{owner[0]} owns this error, {owner[1]}. There is no executed result to inspect.')
        isolated.append(check)
    return isolated


def resolve_dependencies(records):
    """Resolve the `depends` tags of one build's checks in one run."""
    differing = defaultdict(list)
    for record in records:
        for check in record['checks']:
            if check['status'] == 'change_needed':
                differing[check['topic']].append(record['case'])
    for record in records:
        for check in record['checks']:
            for topic in check.pop('depends', ()):
                own = [c for c in record['checks'] if c['topic'] == topic]
                cases = [record['case']] if any(c['status'] == 'change_needed' for c in own) else [] if own else differing[topic]
                if cases and check['status'] == 'change_needed':
                    check.update(status='blocked', detail=f'Depends on {topic}, which differs for this build in '
                                 + ', '.join(sorted(set(cases))[:3]) + '. ' + check['detail'])
    return records

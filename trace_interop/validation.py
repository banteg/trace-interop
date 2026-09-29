"""Validate request shapes against the same pinned artifact as response shapes."""
from jsonschema import Draft201909Validator

# Members a decision under review adds beyond the pinned draft, by method and parameter position.
# That decision's checks judge them, so the schema sees the request without them rather than
# rejecting them as unknown members (H14): trace_filter's blockHash is H33's.
PROPOSED_MEMBERS = {'trace_filter': (0, {'blockHash'})}


def without_proposed(method, params):
    index, members = PROPOSED_MEMBERS.get(method, (None, set()))
    if index is None or len(params) <= index or not isinstance(params[index], dict):
        return params
    return [*params[:index], {k: v for k, v in params[index].items() if k not in members}, *params[index+1:]]


def request_errors(request, methods):
    method = methods.get(request['method'])
    if method is None:
        return []
    params = without_proposed(request['method'], request.get('params', []))
    descriptors = method['params']
    schema = {'type': 'array', 'items': [p['schema'] for p in descriptors],
              'minItems': sum(bool(p.get('required')) for p in descriptors),
              'maxItems': len(descriptors)}
    errors = [e.message for e in Draft201909Validator(schema).iter_errors(params)]
    calls = params[:1] if request['method'] == 'trace_call' else [p[0] for p in params[0] if isinstance(p, list) and p] if request['method'] == 'trace_callMany' and params and isinstance(params[0], list) else []
    for call in calls:
        # An explicit null is an omitted member, so only two present values can disagree.
        if isinstance(call, dict) and call.get('data') is not None and call.get('input') is not None and call['data'] != call['input']:
            errors.append('data and input must agree')
    return errors

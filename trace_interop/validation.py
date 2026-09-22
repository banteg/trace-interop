"""Validate request shapes against the same pinned artifact as response shapes."""
from jsonschema import Draft201909Validator


def request_errors(request, methods):
    method = methods.get(request['method'])
    if method is None:
        return []
    params = request.get('params', [])
    descriptors = method['params']
    schema = {'type': 'array', 'items': [p['schema'] for p in descriptors],
              'minItems': sum(bool(p.get('required')) for p in descriptors),
              'maxItems': len(descriptors)}
    errors = [e.message for e in Draft201909Validator(schema).iter_errors(params)]
    calls = params[:1] if request['method'] == 'trace_call' else [p[0] for p in params[0] if isinstance(p, list) and p] if request['method'] == 'trace_callMany' and params and isinstance(params[0], list) else []
    for call in calls:
        if isinstance(call, dict) and 'data' in call and 'input' in call and call['data'] != call['input']:
            errors.append('data and input must agree')
    return errors

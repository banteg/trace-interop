"""Validate request shapes against the same pinned artifact as response shapes."""
from jsonschema import Draft201909Validator, validators


def folded(validator, schema, instance):
    """A closed object's members renamed to the defined member each matches case-insensitively.
    Servers may fold member names, so only a member that matches no defined member, or one another
    member already takes, is unknown (H14). Responses keep the exact names."""
    properties = schema.get('properties', {})
    if schema.get('additionalProperties') is not False or not validator.is_type(instance, 'object'):
        return instance
    by_name = {}
    for name in properties:
        by_name.setdefault(name.lower(), []).append(name)
    renamed = {key: matches[0] for key in instance
               if key not in properties and len(matches := by_name.get(key.lower(), [])) == 1}
    targets = [renamed.get(key, key) for key in instance]
    return {renamed[key] if key in renamed and targets.count(renamed[key]) == 1 else key: value
            for key, value in instance.items()}


def on_folded(check):
    return lambda validator, value, instance, schema: check(validator, value, folded(validator, schema, instance), schema)


# Every keyword of a closed object sees the folded members, so a matched member also meets if/then, not and required.
RequestValidator = validators.extend(Draft201909Validator, {
    keyword: on_folded(check) for keyword, check in Draft201909Validator.VALIDATORS.items()})


def request_errors(request, methods):
    method = methods.get(request['method'])
    if method is None:
        return []
    params = request.get('params', [])
    descriptors = method['params']
    schema = {'type': 'array', 'items': [p['schema'] for p in descriptors],
              'minItems': sum(bool(p.get('required')) for p in descriptors),
              'maxItems': len(descriptors)}
    errors = [e.message for e in RequestValidator(schema).iter_errors(params)]
    calls = params[:1] if request['method'] == 'trace_call' else [p[0] for p in params[0] if isinstance(p, list) and p] if request['method'] == 'trace_callMany' and params and isinstance(params[0], list) else []
    for call in calls:
        # An explicit null is an omitted member, so only two present values can disagree.
        if isinstance(call, dict) and call.get('data') is not None and call.get('input') is not None and call['data'] != call['input']:
            errors.append('data and input must agree')
    return errors

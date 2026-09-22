"""Policy progress is editorial; implementation milestones require captured evidence."""

from datetime import datetime

NATIVE_CLIENTS = ('besu', 'erigon', 'nethermind', 'reth')
POLICY_LABELS = {'review': '⚪ Under review', 'diverging': '🔀 Diverging', 'converged': '🤝 Converged'}
LEGEND = (
    '- ⚪ **Under review:** no recorded policy conclusion. '
    '\n- 🔀 **Diverging:** competing policy positions. '
    '\n- 🤝 **Converged:** direction aligned, implementation work or verification remains; not unanimous formal approval. '
    '\n- 🧪 **Harmonized · dev:** converged and all declared cases pass on the captured development builds of Besu, Erigon, Nethermind and Reth. '
    '\n- ✅ **Harmonized · stable:** the same is also verified on their captured releases. '
    '\n\nMissing cases, ineligible runs, unsupported methods, unchecked assertions and invalid result schemas prevent harmonization. '
    'Each client/channel uses its most recently captured immutable build; evidence from different builds is never combined. These are milestones for the declared cases at the linked revisions, not full conformance or a claim about the latest builds. '
    'The experimental Geth fork is reported separately and is not a policy vote.'
)


def channel_harmonized(decision, records, channel):
    required = set(decision['cases'])
    if not required:
        return False
    topic = decision['id']
    for family in NATIVE_CLIENTS:
        captured = [r for r in records if r['client'] == f'{family}_{channel}']
        if not captured or any(not r.get('build_id') or not r.get('captured_at') for r in captured):
            return False
        try:
            times = [datetime.fromisoformat(r['captured_at']) for r in captured]
            if any(t.tzinfo is None for t in times):
                return False
            newest = max(times)
        except (ValueError, TypeError):
            return False
        builds = {r['build_id'] for r,t in zip(captured,times) if t == newest}
        if len(builds) != 1:
            return False
        current = next(iter(builds))
        relevant = [r for r in captured if r['build_id'] == current
                    and (r['corpus']+'/'+r['case'] in required
                         or any(c['topic'] == topic for c in r['checks']))]
        if not required <= {r['corpus']+'/'+r['case'] for r in relevant}:
            return False
        for record in relevant:
            checks = [c for c in record['checks'] if c['topic'] == topic]
            if not record['eligible'] or not checks or any(c['status'] != 'matches' for c in checks):
                return False
            if record.get('schema', {}).get('status') == 'invalid':
                return False
    return True


def decision_status(decision, records, position):
    policy = position.get('policy', 'review')
    if policy not in POLICY_LABELS:
        raise ValueError(f'Unknown policy status: {policy}')
    if policy != 'review' and (not position.get('sources') or not position.get('note')):
        raise ValueError('A policy conclusion needs a note and source links')
    if policy == 'converged' and channel_harmonized(decision, records, 'development'):
        if channel_harmonized(decision, records, 'release'):
            return '✅ Harmonized · stable'
        return '🧪 Harmonized · dev'
    return POLICY_LABELS[policy]

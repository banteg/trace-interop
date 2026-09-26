"""Policy progress is editorial; implementation milestones require captured evidence."""

from datetime import datetime

NATIVE_CLIENTS = ('besu', 'erigon', 'nethermind', 'reth')
# Implementations shown with the native clients' progress but outside harmonization, positions and totals.
REPORTED_CLIENTS = ('anvil',)
POLICY_LABELS = {'review': '⚪ Under review', 'diverging': '🔀 Diverging', 'converged': '🤝 Converged'}
LEGEND = (
    '- ⚪ **Under review:** no recorded policy conclusion. '
    '\n- 🔀 **Diverging:** competing policy positions. '
    '\n- 🤝 **Converged:** direction aligned, implementation work or verification remains; not unanimous formal approval. '
    '\n- 🧪 **Harmonized · dev:** converged and all declared cases pass on the captured development builds of Besu, Erigon, Nethermind and Reth. '
    '\n- ✅ **Harmonized · stable:** the same is also verified on their captured releases. '
    '\n\nMissing cases, ineligible runs, unsupported methods, unchecked assertions and invalid result schemas prevent harmonization. '
    'Each client/channel uses its most recently captured immutable build; evidence from different builds is never combined. These are milestones for the declared cases at the linked revisions, not full conformance or a claim about the latest builds. '
    'The experimental Geth fork and Foundry’s Anvil development node are reported separately and are not policy votes.'
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
            checks = [c for c in record['checks'] if c['topic'] == topic and c['status'] not in ['control','not_applicable']]
            if not checks and record['corpus']+'/'+record['case'] not in required:
                continue
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


POSITIONS = {'agree': '👍 Agrees', 'conditional': '✋ Conditional', 'object': '👎 Objects'}
NO_POSITION = '· No response'
POSITION_LEGEND = (
    '**Client order:** Besu → Erigon → Nethermind → Reth. 👍 agrees · ✋ agrees on conditions · 👎 objects · `·` no response. '
    'A position is a client team’s stated view of the recommendation, or a maintainer-merged fix that implements it '
    '(a complete, non-partial PR in [client fixes](../docs/client-fixes.md)). Positions are separate from the policy status and from the captured checks.'
)


def check_positions(status, decisions):
    """Recorded client positions name a known decision and native client, with a note and sources."""
    for topic, entry in status.items():
        if topic not in decisions:
            raise ValueError(f'Policy status references an unknown decision: {topic}')
        for client, position in entry.get('positions', {}).items():
            if (client not in NATIVE_CLIENTS or position.get('position') not in POSITIONS or not position.get('note')
                    or not position.get('sources') or any(not s.get('label') or not s.get('url') for s in position['sources'])):
                raise ValueError(f'invalid client position: {topic}/{client}')
    return status


def client_positions(recorded, merged):
    """Recorded positions, plus agreement by implementation from merged (client, source) fixes; a recorded position wins."""
    positions = {}
    for client, source in merged:
        positions.setdefault(client, {'position': 'agree', 'note': 'Merged a fix implementing the recommendation.', 'sources': []})['sources'].append(source)
    for client, position in recorded.items():
        known = {s['url'] for s in position['sources']}
        positions[client] = dict(position, sources=position['sources'] + [s for s in positions.get(client, {}).get('sources', []) if s['url'] not in known])
    return positions

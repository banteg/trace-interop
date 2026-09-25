"""Aggregate progress: each client's decision outcomes on a captured build, and its upstream fix PRs.

The unit is one decision for one client. A PR count alone would mislead, since one PR can cover
part of a decision or several decisions; a difference without a submitted fix is the rough measure
of pending work, split by whether its decision has converged.
"""
from collections import Counter
from html import escape

# (key, symbol, label, bar colour, number colour), in bar order.
BUCKETS = [
    ('agree', '✅', 'Agree', '#1a7f37', '#ffffff'),
    ('fix', '🛠️', 'Fix submitted', '#0969da', '#ffffff'),
    ('converged', '⚠️', 'No fix · converged', '#bc4c00', '#ffffff'),
    ('review', '⚠️', 'No fix · under review', '#d4a72c', '#1f2328'),
    ('policy', '❔', 'Policy open', '#8250df', '#ffffff'),
    ('unmeasured', '⚪', 'Not fully measured', '#8c959f', '#1f2328'),
]


def bucket(symbol, converged):
    """Classify a build verdict symbol; an unavailable method is a difference, a partial assessment is not."""
    if symbol == '✅':
        return 'agree'
    if symbol == '🛠️':
        return 'fix'
    if symbol in ('⚠️', '⛔'):
        return 'converged' if converged else 'review'
    if symbol == '❔':
        return 'policy'
    return 'unmeasured'


def tally(symbols, converged):
    """Counter of buckets for {topic: verdict symbol}, given the set of converged topics."""
    return Counter(bucket(symbol, topic in converged) for topic, symbol in symbols.items())


def pr_counts(fixes, client):
    """Merged and open fix PRs attributed to a client family; closed PRs are not progress."""
    states = Counter(pr['state'] for pr in fixes['prs'] if pr['client'] == client)
    return states['merged'], states['open']


def svg(rows, total):
    """Deterministic stacked bars: rows are (name, Counter) with `total` decisions each."""
    left, width, top, height, gap = 96, 512, 12, 20, 10
    step = height + gap
    legend_top = top + len(rows) * step + 8
    per_line = 3
    legend_height = ((len(BUCKETS) + per_line - 1) // per_line) * 20
    canvas = (left + width + 16, legend_top + legend_height + 4)
    summary = '; '.join(f'{name} ' + ', '.join(f'{counts[key]} {label.lower()}' for key, _, label, _, _ in BUCKETS if counts[key])
                        for name, counts in rows)
    out = [(f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas[0]}" height="{canvas[1]}" '
            f'viewBox="0 0 {canvas[0]} {canvas[1]}" role="img" aria-labelledby="title">'),
           f'<title id="title">Decision outcomes per client: {escape(summary)}</title>',
           ('<style>text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-size:12px}'
            '.label{fill:#1f2328}@media (prefers-color-scheme:dark){.label{fill:#e6edf3}}</style>')]
    for i, (name, counts) in enumerate(rows):
        y = top + i * step
        out.append(f'<text class="label" x="{left - 8}" y="{y + height / 2 + 4:g}" text-anchor="end">{escape(name)}</text>')
        x = 0
        for key, _, _, fill, ink in BUCKETS:
            if not counts[key]:
                continue
            start, x = x, x + counts[key]
            x0, w = left + round(start * width / total), round(x * width / total) - round(start * width / total)
            out.append(f'<rect x="{x0}" y="{y}" width="{w}" height="{height}" fill="{fill}"/>')
            if w >= 14:
                out.append(f'<text x="{x0 + w / 2:g}" y="{y + height / 2 + 4:g}" text-anchor="middle" fill="{ink}">{counts[key]}</text>')
    for i, (key, _, label, fill, _) in enumerate(BUCKETS):
        x, y = left + (i % per_line) * (width // per_line), legend_top + (i // per_line) * 20
        out.append(f'<rect x="{x}" y="{y}" width="12" height="12" fill="{fill}"/>')
        out.append(f'<text class="label" x="{x + 18}" y="{y + 10}">{escape(label)}</text>')
    return '\n'.join(out) + '\n</svg>\n'

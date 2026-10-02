"""Aggregate progress: each client's decision outcomes on a captured build, and its upstream fix PRs.

The unit is one decision for one client. A PR count alone would mislead, since one PR can cover
part of a decision or several decisions; a difference without a submitted fix is the rough measure
of pending work, split by whether its decision has converged.
"""
from collections import Counter
from html import escape

# (key, symbol, label), in bar order.
BUCKETS = [
    ('agree', '✅', 'Agree'),
    ('fix', '🛠️', 'Fix submitted'),
    ('converged', '⚠️', 'No fix · converged'),
    ('review', '⚠️', 'No fix · under review'),
    ('policy', '❔', 'Policy open'),
    ('unmeasured', '⚪', 'Not fully measured'),
]

# {key: (bar, number)} per colour scheme. Hue carries the group: teal is agreement and the fixes heading
# there, amber is unfixed work, violet is an open policy question; the solid shade is the settled state.
# In dark mode the tint is a dim shade so the pending state recedes toward the surface rather than glares.
COLOURS = {
    'light': {'agree': ('#11756f', '#ffffff'), 'fix': ('#79c7bd', '#1f2328'),
              'converged': ('#c8641a', '#ffffff'), 'review': ('#f2b36b', '#1f2328'),
              'policy': ('#8172c4', '#ffffff'), 'unmeasured': ('#dde1e6', '#1f2328')},
    'dark': {'agree': ('#3aa59a', '#0d1117'), 'fix': ('#1a6b62', '#ffffff'),
             'converged': ('#e5843a', '#0d1117'), 'review': ('#8f5420', '#ffffff'),
             'policy': ('#9b8fe0', '#0d1117'), 'unmeasured': ('#2d333b', '#e6edf3')},
}


def style(scheme):
    return ''.join(f'.b-{key}{{fill:{bar}}}.n-{key}{{fill:{number}}}' for key, (bar, number) in COLOURS[scheme].items())


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
    left, width, top, height, gap, spacer = 96, 512, 12, 20, 10, 2
    step = height + gap
    legend_top = top + len(rows) * step + 8
    per_line = 3
    legend_height = ((len(BUCKETS) + per_line - 1) // per_line) * 20
    canvas = (left + width + 16, legend_top + legend_height + 4)
    summary = '; '.join(f'{name} ' + ', '.join(f'{counts[key]} {label.lower()}' for key, _, label in BUCKETS if counts[key])
                        for name, counts in rows)
    out = [(f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas[0]}" height="{canvas[1]}" '
            f'viewBox="0 0 {canvas[0]} {canvas[1]}" role="img" aria-labelledby="title">'),
           f'<title id="title">Decision outcomes per client: {escape(summary)}</title>',
           ('<style>text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-size:12px}'
            f'.label{{fill:#1f2328}}{style("light")}'
            f'@media (prefers-color-scheme:dark){{.label{{fill:#e6edf3}}{style("dark")}}}</style>')]
    for i, (name, counts) in enumerate(rows):
        y = top + i * step
        out.append(f'<text class="label" x="{left - 8}" y="{y + height / 2 + 4:g}" text-anchor="end">{escape(name)}</text>')
        x = 0
        for key, *_ in BUCKETS:
            if not counts[key]:
                continue
            start, x = x, x + counts[key]
            # a transparent gap separates touching segments on either page background
            x0, w = left + round(start * width / total), round(x * width / total) - round(start * width / total) - (spacer if x < total else 0)
            out.append(f'<rect class="b-{key}" x="{x0}" y="{y}" width="{w}" height="{height}"/>')
            if w >= 14:
                out.append(f'<text class="n-{key}" x="{x0 + w / 2:g}" y="{y + height / 2 + 4:g}" text-anchor="middle">{counts[key]}</text>')
    for i, (key, _, label) in enumerate(BUCKETS):
        x, y = left + (i % per_line) * (width // per_line), legend_top + (i // per_line) * 20
        out.append(f'<rect class="b-{key}" x="{x}" y="{y}" width="12" height="12" rx="2"/>')
        out.append(f'<text class="label" x="{x + 18}" y="{y + 10}">{escape(label)}</text>')
    return '\n'.join(out) + '\n</svg>\n'

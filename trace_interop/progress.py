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


# Page text per colour scheme: (label, muted).
TEXT = {'light': ('#1f2328', '#59636e'), 'dark': ('#e6edf3', '#9198a1')}


def style(scheme):
    label, muted = TEXT[scheme]
    agree = COLOURS[scheme]['agree'][0]
    return (f'.label{{fill:{label}}}.muted{{fill:{muted}}}.pr{{fill:none;stroke:{agree}}}.edge{{stroke:{agree}}}'
            + ''.join(f'.b-{key}{{fill:{bar}}}.n-{key}{{fill:{number}}}' for key, (bar, number) in COLOURS[scheme].items()))


def header(width, height, title):
    """An svg root with the shared font and light and dark palettes; `title` is its accessible name."""
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title">',
            f'<title id="title">{escape(title)}</title>',
            ('<style>text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-size:12px}'
             f'.head{{font-weight:600}}.partial{{stroke-dasharray:3 2}}{style("light")}'
             f'@media (prefers-color-scheme:dark){{{style("dark")}}}</style>')]


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
    out = header(*canvas, f'Decision outcomes per client: {summary}')
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


# (rect, text) classes of a fix PR chip by stage: in the measured build, merged but not in it, open.
PR_STAGES = {'built': ('b-agree', 'n-agree'), 'merged': ('b-fix', 'n-fix'), 'open': ('pr', 'label')}


def chip_width(text):
    """An estimate of a 12px label's width, generous enough for the system fonts the chart names."""
    return round(len(text) * 6.8) + 14


def work_svg(name, entries):
    """Deterministic map of one client's remaining work: entries are (topic, title, bucket, prs, note), prs being
    (label, stage, partial) fix PRs, stage one of PR_STAGES, and note what stands in for them when there are
    none, such as why a decision is not fully measured. Decisions are grouped by bucket in bar order; agreeing
    decisions are listed compactly, the others one per row with their PRs: filled when in the measured build or
    merged but not in it yet, outlined when open, with a dashed edge when the PR covers only part of the decision."""
    width, left, title_x, pr_x, row, chip = 760, 16, 70, 400, 24, 18
    out, y = [], 12
    counts = {key: sum(1 for e in entries if e[2] == key) for key, *_ in BUCKETS}

    def chips(x, y, labels, classes):
        for text, cls in zip(labels, classes):
            w = chip_width(text)
            if x + w > width - left:
                x, y = pr_x, y + row
            out.append(f'<rect class="{cls[0]}" x="{x}" y="{y}" width="{w}" height="{chip}" rx="4"/>')
            out.append(f'<text class="{cls[1]}" x="{x + w / 2:g}" y="{y + 13}" text-anchor="middle">{escape(text)}</text>')
            x += w + 6
        return y

    for key, _, label in BUCKETS:
        group = [e for e in entries if e[2] == key]
        if not group:
            continue
        out.append(f'<text class="label head" x="{left}" y="{y + 13}">{escape(label)} ({len(group)})</text>')
        y += row
        if key == 'agree':
            x = left
            for topic, *_ in group:
                if x + 44 > width - left:
                    x, y = left, y + row
                out.append(f'<rect class="b-{key}" x="{x}" y="{y}" width="44" height="{chip}" rx="4"/>')
                out.append(f'<text class="n-{key}" x="{x + 22}" y="{y + 13}" text-anchor="middle">{topic}</text>')
                x += 50
            y += row + 8
            continue
        for topic, title, _, prs, note in group:
            out.append(f'<rect class="b-{key}" x="{left}" y="{y}" width="44" height="{chip}" rx="4"/>')
            out.append(f'<text class="n-{key}" x="{left + 22}" y="{y + 13}" text-anchor="middle">{topic}</text>')
            short = title if len(title) <= 46 else title[:45].rstrip() + '…'
            out.append(f'<text class="label" x="{title_x}" y="{y + 13}">{escape(short)}</text>')
            if prs:
                y = chips(pr_x, y, [p[0] for p in prs],
                          [(PR_STAGES[stage][0] + ' edge partial' * partial, PR_STAGES[stage][1]) for _, stage, partial in prs])
            else:
                note = note or 'no fix PR'
                out.append(f'<text class="muted" x="{pr_x}" y="{y + 13}">{escape(note if len(note) <= 50 else note[:49].rstrip() + "…")}</text>')
            y += row
        y += 8
    legend = [(*PR_STAGES['built'], 'in measured build'), (*PR_STAGES['merged'], 'merged, not in build'),
              (*PR_STAGES['open'], 'open'), ('pr partial', 'label', 'partial (any stage)')]
    x = left
    for rect, text, word in legend:
        w = chip_width(word)
        out.append(f'<rect class="{rect}" x="{x}" y="{y}" width="{w}" height="{chip}" rx="4"/>')
        out.append(f'<text class="{text}" x="{x + w / 2:g}" y="{y + 13}" text-anchor="middle">{word}</text>')
        x += w + 6
    out.append(f'<text class="muted" x="{x + 6}" y="{y + 13}">fix PRs, by state</text>')
    summary = ', '.join(f'{counts[key]} {label.lower()}' for key, _, label in BUCKETS if counts[key])
    return '\n'.join(header(width, y + chip + 12, f'{name} decisions and fix PRs: {summary}') + out) + '\n</svg>\n'

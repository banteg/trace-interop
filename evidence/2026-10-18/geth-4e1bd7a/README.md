# Geth draft at 4e1bd7a — 2026-10-18

A pinned capture of the Geth draft fork at
[`4e1bd7a0`](https://github.com/banteg/go-ethereum/commit/4e1bd7a006fbe9f1437fdf1f1a9ce652e1611e54), the head of
`banteg/go-ethereum:feat/trace` after its rebase on upstream master. The rebase adopts upstream's call defaults, so
`trace_call` builds its message the way `eth_call` now does, and fixes the state lookup for the new `StateAt`
signature. The [2026-10-17 eval](../../2026-10-17/eval/README.md) captured the previous head, `71db3b03`. These runs
measure the draft's column only, so [reports.lock.json](../../../reports.lock.json) does not select them. The next
eval's Geth build carries the result into the reports.

## Build

[clients.lock.json](clients.lock.json) was written by `trace-interop`'s Geth resolver, which builds the branch head
from source in an isolated cache: commit `4e1bd7a0` (clean tree), Go 1.26.1 without cgo, binary
`sha256:d7258fbe…`, on the pinned Alpine base image. It reports `Geth/v1.17.9-unstable-4e1bd7a0-2026-10-18`. Hive
commit `43ea47be`, as in the eval. Every corpus ran with `--clients go-ethereum_trace` from a clean clone at harness
commit `fee3f8b2` on Fedora (`source_dirty: false`).

## Capture completeness

All 19 corpora the draft captures completed with no missing cases or transport errors: 1,900 responses. `pruned`
has a Reth adapter only.

| Corpus | Responses | Corpus | Responses |
| --- | --- | --- | --- |
| [initial](initial/summary.json) | 76 | [fee-policy](fee-policy/summary.json) | 756 |
| [a](a/summary.json) | 94 | [fee-compat](fee-compat/summary.json) | 300 |
| [repeat](repeat/summary.json) | 44 | [callmany-isolation](callmany-isolation/summary.json) | 10 |
| [forks](forks/summary.json) | 92 | [h30](h30/summary.json) | 43 |
| [fork-followup](fork-followup/summary.json) | 24 | [pending](pending/summary.json) | 7 |
| [precompiles](precompiles/summary.json) | 19 | [raw-selector](raw-selector/summary.json) | 16 |
| [precompile-values](precompile-values/summary.json) | 15 | [probes-prague](probes-prague/summary.json) | 124 |
| [raw-validation](raw-validation/summary.json) | 71 | [probes-forks](probes-forks/summary.json) | 72 |
| [coverage](coverage/summary.json) | 24 | [mined-probes](mined-probes/summary.json) | 89 |
| [reorg-safe](reorg-safe/summary.json) | 24 | | |

## Result

`trace-interop report` assessed these runs together, and the result was compared with the draft's column in the
current reports by counting statuses per corpus, case and decision. All 3,654 case–decision pairs both builds share
are unchanged, and neither has a pair the other lacks: 6,591 matching checks and no differences. In the `pending`
corpus the draft traces block 49 holding the pooled transfer, as `71db3b03` does in the
[eval-builds capture](../eval-pending/README.md). **The rebased draft agrees on all 33 decisions.**

## Reproduction

From a clean checkout at `fee3f8b2` on Linux:

```sh
uv run python -m trace_interop run --lock evidence/2026-10-18/geth-4e1bd7a/clients.lock.json \
  --clients go-ethereum_trace --corpus pending --output runs/geth-4e1bd7a/pending
uv run trace-interop report --run evidence/2026-10-18/geth-4e1bd7a/pending --output runs/geth-4e1bd7a-report
```

Each run keeps its manifest, summary, compact observations and checksums. The capture logs sit beside the runs.

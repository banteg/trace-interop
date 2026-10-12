# Erigon main at b5f10db — 2026-10-12

A pinned capture of Erigon's development build at
[`b5f10dbd`](https://github.com/erigontech/erigon/commit/b5f10dbd54655a4dff8ff7ed90ec26836c0ffcd0), six commits after
the merge of [erigontech/erigon#24032](https://github.com/erigontech/erigon/pull/24032), which persists safe and
finalized block hashes from a same-head forkchoice update. The [2026-10-11 eval](../../2026-10-11/eval/README.md)
measured `main-latest` at `1d3ebbf2`, which predates it. These runs measure Erigon's column only, so
[reports.lock.json](../../../reports.lock.json) does not select them and no published verdict changes. The next eval's
development build carries the result into the reports.

## Build

[clients.lock.json](clients.lock.json) pins `erigontech/erigon@sha256:faad57ed…`, the published
`erigontech/erigon:main-b5f10db` image. Its `org.opencontainers.image.revision` label is `b5f10dbd`. The lock was
written from that tag the way `trace-interop resolve` records an image, because `resolve` only follows
`main-latest`. Its Hive commit `43ea47be` matches the 2026-10-11 matrix. Every corpus ran with
`--clients erigon_development` from a clean clone at harness commit `6c3a2aab` on Fedora (`source_dirty: false`).

## Capture completeness

All 18 corpora that capture Erigon completed with no missing cases or transport errors: 1,895 responses.
`probes-forks` has 8 more cases than the eval's run, the blob fee cap and empty-list probes added on 2026-10-12.

**`reorg-safe` is eligible.** On the eval's `1d3ebbf2` build, and on 3.7.1, Erigon failed the reorg scenario's setup
controls, so the corpus stopped after 10 responses and its cases were blocked. This build passes them and answers all
24.

| Corpus | Responses | Corpus | Responses |
| --- | --- | --- | --- |
| [initial](initial/summary.json) | 76 | [fee-policy](fee-policy/summary.json) | 756 |
| [a](a/summary.json) | 94 | [fee-compat](fee-compat/summary.json) | 300 |
| [repeat](repeat/summary.json) | 44 | [callmany-isolation](callmany-isolation/summary.json) | 10 |
| [forks](forks/summary.json) | 92 | [h30](h30/summary.json) | 45 |
| [fork-followup](fork-followup/summary.json) | 24 | [raw-selector](raw-selector/summary.json) | 16 |
| [precompiles](precompiles/summary.json) | 19 | [probes-prague](probes-prague/summary.json) | 124 |
| [precompile-values](precompile-values/summary.json) | 15 | [probes-forks](probes-forks/summary.json) | 72 |
| [raw-validation](raw-validation/summary.json) | 71 | [mined-probes](mined-probes/summary.json) | 89 |
| [coverage](coverage/summary.json) | 24 | [reorg-safe](reorg-safe/summary.json) | 24 |

## Result

`trace-interop report` assessed these runs together, and the result was compared check by check with Erigon's
development column in the current reports. None of the 6,553 checks both builds share regresses. The six H33
`filter-hash-a` and `filter-hash-b` checks of the reorg phases move from blocked to agreeing. The scenario's
`filter-tail` checks become the reference controls they are meant to be, and the newly eligible cases add 13 agreeing
checks (H02, H09, H27, H33).

| Decision | 1d3ebbf2 (2026-10-11) | b5f10dbd |
| --- | --- | --- |
| H33 | Not fully measured: the reorg cases were blocked | Agrees |
| H14 | Differs | Differs, on `a/filter-unknown-field` (an unknown `trace_filter` member is accepted; [#24706](https://github.com/erigontech/erigon/pull/24706)) and the two lone blob fee cap probes, which run with the cap ignored |

Erigon's development build agrees on **32 of 33** decisions, one more than in the eval. H14 is the only difference.

## Reproduction

From a clean checkout at `6c3a2aab` on Linux:

```sh
uv run python -m trace_interop run --lock evidence/2026-10-12/erigon-b5f10db/clients.lock.json \
  --clients erigon_development --corpus reorg-safe --output runs/erigon-b5f10db/reorg-safe
uv run trace-interop report --run evidence/2026-10-12/erigon-b5f10db/reorg-safe --output runs/erigon-b5f10db-report
```

Each run keeps its manifest, summary, compact observations and checksums. The capture logs sit beside the runs.

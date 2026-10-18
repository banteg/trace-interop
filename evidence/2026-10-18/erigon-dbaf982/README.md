# Erigon main at dbaf982 — 2026-10-18

A pinned capture of Erigon's development build at
[`dbaf982a`](https://github.com/erigontech/erigon/commit/dbaf982a31e38c77ebdf630948037ab4402d8476), the merge of
[erigontech/erigon#24990](https://github.com/erigontech/erigon/pull/24990). That PR rejects a call's `maxFeePerBlobGas`
without `blobVersionedHashes`, at every fork. In the [2026-10-17 eval](../../2026-10-17/eval/README.md), `main-latest` at
`5b452f41` agreed on 32 of 33 decisions, and this lone blob fee cap was its one difference. These runs measure Erigon's
column only, so [reports.lock.json](../../../reports.lock.json) does not select them and no published verdict changes.
The next eval's development build carries the result into the reports.

## Build

[clients.lock.json](clients.lock.json) pins `erigontech/erigon@sha256:69b6fef2…`, the published
`erigontech/erigon:main-dbaf982` image. Its `org.opencontainers.image.revision` label is `dbaf982a`, and it reports
version 3.9.0-dev. The lock was written from that tag the way `trace-interop resolve` records an image, because
`resolve` only follows `main-latest`. Hive commit `43ea47be`, as in the eval. Every corpus ran with
`--clients erigon_development` from a clean clone at harness commit `fe4cd0bd` on Fedora (`source_dirty: false`).

## Capture completeness

All 18 corpora that capture Erigon completed with no missing cases or transport errors: 1,895 responses.

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

`trace-interop report` assessed these runs together, and the result was compared with Erigon's development column in
the current reports by counting statuses per corpus, case and decision. Of the 3,500 case–decision pairs both builds
share, two change and none regresses: `fork-blob-fee-only-before` and `fork-blob-fee-only-at` (H14) move from change
needed to agreeing, because the call is now rejected at both blocks. Their H08 trace checks disappear, since the call
no longer runs.

**Erigon's development build agrees on all 33 decisions**, the second build to do so after Nethermind master
([2026-10-17 eval](../../2026-10-17/eval/README.md)).

## Reproduction

From a clean checkout at `fe4cd0bd` on Linux:

```sh
uv run python -m trace_interop run --lock evidence/2026-10-18/erigon-dbaf982/clients.lock.json \
  --clients erigon_development --corpus probes-forks --output runs/erigon-dbaf982/probes-forks
uv run trace-interop report --run evidence/2026-10-18/erigon-dbaf982/probes-forks --output runs/erigon-dbaf982-report
```

Each run keeps its manifest, summary, compact observations and checksums. The capture logs sit beside the runs.

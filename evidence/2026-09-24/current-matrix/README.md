# Current client matrix — 2026-09-24

Historical snapshot: the [12:56 UTC H15 comparison](../h15-call-compat/README.md)
reran all fifteen corpora and now supplies the active reports. This earlier capture remains
unchanged evidence for the initial assessment and before/after regressions.

The suite resolved the latest published stable releases and development images,
built the current Geth draft branch, and passed its live [freshness preflight](preflight.json)
at **2026-09-24 11:07:58 UTC**. [clients.lock.json](clients.lock.json) freezes that
snapshot across all fourteen corpora. These are current published builds as of
that preflight; moving development tags can advance while the suite runs.

Every capture uses clean harness commit
`fd5a260` on Fedora and disposable Hive chains. Manifests record exact source,
runner hashes and image identities; per-corpus checksums authenticate original
requests, observations and logs. The production node was not used.

## Capture completeness

The suite retained **11,341 RPC responses** across fourteen corpora. Thirteen
captures completed. The reorg capture is incomplete: Erigon `e26d9bd4` did not
establish the alternate canonical head, and both Reth builds failed the restored
canonical-head control within the scenario timeout. Twenty exchanges are missing;
all three builds' reorg observations remain blocked. No earlier passing run fills
these gaps. Both Reth pruning captures completed.

The [reorg summary](reorg-safe/summary.json) and [original logs](reorg-safe/runner.log.gz)
retain the setup evidence. Reports contain 11,361 assessment records, including the
missing exchanges; capture completeness is separate from policy agreement.

## Tested builds

| Client | Version | Commit |
| --- | --- | --- |
| Besu | `26.9-develop` | [`f9572aa8`](https://github.com/besu-eth/besu/commit/f9572aa82a2dadb3dd1b218d3ca97101540faf97) |
| Besu | `26.8.1` | [`d97cbd61`](https://github.com/besu-eth/besu/commit/d97cbd61976a52bb109e637196fef9a8ebf2b617) |
| Erigon | `3.8.0-dev` | [`e26d9bd4`](https://github.com/erigontech/erigon/commit/e26d9bd4056586e004488c31b561fb2663d46019) |
| Erigon | `3.6.1` | [`0c4d9c91`](https://github.com/erigontech/erigon/commit/0c4d9c91dbaffd52890235f7ea395b0231738501) |
| Geth draft fork | `1.17.7-unstable` | [`fa8ecb92`](https://github.com/banteg/go-ethereum/commit/fa8ecb9242dda61858c44cf43c70d00548fbd7cd) |
| Nethermind | `2.1.0-unstable` | [`2a3b2531`](https://github.com/NethermindEth/nethermind/commit/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e) |
| Nethermind | `2.0.0` | [`bec830cd`](https://github.com/NethermindEth/nethermind/commit/bec830cdfbd28c3a4d6040bc967c68c49d19dc9f) |
| Reth | `2.5.2` | [`58a51b3e`](https://github.com/paradigmxyz/reth/commit/58a51b3ee3f6714ded9207b244a273c8afb592fd) |
| Reth | `2.6.0` | [`73a3a008`](https://github.com/paradigmxyz/reth/commit/73a3a00862a8f14f89e30da8de001456f18cfae0) |

The full [matrix summary](matrix.json) retains all completed and incomplete runs.
The [report inventory](../../../reports.lock.json) selected this entire
snapshot before the H17 retest superseded it. Captures remain immutable historical evidence. Report generation
rejects a mixed-build selection or omission of an incomplete current run.

## Changes visible after refreshing

- Reth `58a51b3e` fixes tree-path lookup, default filter intersection,
  missing-replay `null` and replay transaction hashes. The `73a3a008` build
  still differs on those cases.
- Nethermind `2a3b2531` retains output for stateDiff-only selections and accepts
  empty selections. Those fixes remove 110 H15 mismatching requests compared
  with its tested release. Malformed validation responses still block assessment.
- Geth `fa8ecb92` matches all 664 proposed-policy H15 requests. Another 80
  requests per build cover unresolved omitted/incomplete fee defaults.
- Erigon `0c4d9c91` still returns `method handler crashed` for 26 empty-selection
  H15 requests. `e26d9bd4` has none. This is the same release-only nil tracer
  result described in the [crash investigation](../h15-fee-policy/README.md#erigon-empty-selection-crash-investigation),
  fixed upstream before the tested development revision.

## H15 policy requests

Each row covers the same 664 requests. A mismatch means at least one H15 property
differs. Blocked includes generic/internal/malformed errors that cannot prove the
intended validation. The separate 80 default-field observations are excluded.
These counts describe this bounded corpus, not overall client conformance or ranking.

| Client | Version · commit | Matches | Differs | Blocked |
| --- | --- | --- | --- | --- |
| Besu | `26.9-develop · f9572aa8` | 288 | 272 | 104 |
| Besu | `26.8.1 · d97cbd61` | 288 | 272 | 104 |
| Erigon | `3.8.0-dev · e26d9bd4` | 184 | 480 | 0 |
| Erigon | `3.6.1 · 0c4d9c91` | 178 | 481 | 5 |
| Geth draft fork | `1.17.7-unstable · fa8ecb92` | 664 | 0 | 0 |
| Nethermind | `2.1.0-unstable · 2a3b2531` | 448 | 0 | 216 |
| Nethermind | `2.0.0 · bec830cd` | 338 | 110 | 216 |
| Reth | `2.5.2 · 58a51b3e` | 128 | 536 | 0 |
| Reth | `2.6.0 · 73a3a008` | 128 | 536 | 0 |

[H15 report](../../../reports/decisions/H15.md) ·
[Fee-policy requests and raw responses](fee-policy/observations.json.gz) ·
[Probe design](../../../docs/h15-fee-policy.md).

## Repeat the workflow

```sh
uv run python scripts/run_matrix.py --output runs/next-matrix
```

This resolves fresh builds and refuses a stale or unverifiable preflight. The old
September 21 lock was also tested against the new guard: it was rejected for four
moved development images and Nethermind's `1.39.3` → `2.0.0` release update.
Use `--reproduce-lock` explicitly for historical comparisons; that mode never
claims the reproduced builds are current.

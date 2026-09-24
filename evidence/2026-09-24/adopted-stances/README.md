# Adopted stances: fresh client matrix — 2026-09-24

The fifteen-corpus suite resolved all nine published builds together and passed
its live [freshness preflight](preflight.json) at **2026-09-24 18:52:50 UTC**.
[clients.lock.json](clients.lock.json) freezes that snapshot across every corpus.
This matrix measures the Geth draft fork after it adopted the source-review stances,
and picks up the native development images published since the
[previous matrix](../h15-call-compat/README.md).

Every capture uses harness commit `26f9c9d8` on Fedora and disposable Hive chains.
Manifests retain `source_dirty: true`: the matrix created its untracked output
folder before each corpus checked git status. The [source audit](source-audit.json)
confirms that output folder is the only dirty path, tracked source equals the
commit, and the runner hash matches every capture. No manifest was rewritten.
[reports.lock.json](../../../reports.lock.json) selects this entire snapshot,
including the incomplete run.

## Tested builds

| Client | Version | Commit |
| --- | --- | --- |
| Besu | `26.8.1` | [`d97cbd61`](https://github.com/besu-eth/besu/commit/d97cbd61976a52bb109e637196fef9a8ebf2b617) |
| Besu | `26.9-develop` | [`85b32978`](https://github.com/besu-eth/besu/commit/85b32978312c5ec290c24e2dc4c346c368bf9258) |
| Erigon | `3.6.1` | [`0c4d9c91`](https://github.com/erigontech/erigon/commit/0c4d9c91dbaffd52890235f7ea395b0231738501) |
| Erigon | `3.8.0-dev` | [`e26d9bd4`](https://github.com/erigontech/erigon/commit/e26d9bd4056586e004488c31b561fb2663d46019) |
| Nethermind | `2.0.0` | [`bec830cd`](https://github.com/NethermindEth/nethermind/commit/bec830cdfbd28c3a4d6040bc967c68c49d19dc9f) |
| Nethermind | `2.1.0-preview` | [`ce501a97`](https://github.com/NethermindEth/nethermind/commit/ce501a9734ac0b39b5a5195fd93a5bf67ba9c161) |
| Reth | `2.6.0` | [`73a3a008`](https://github.com/paradigmxyz/reth/commit/73a3a00862a8f14f89e30da8de001456f18cfae0) |
| Reth | `2.5.2` | [`58a51b3e`](https://github.com/paradigmxyz/reth/commit/58a51b3ee3f6714ded9207b244a273c8afb592fd) |
| Geth draft fork | `1.17.7-unstable` | [`bb5c4682`](https://github.com/banteg/go-ethereum/commit/bb5c4682a5e0765159edefe779f9606db8115483) |

Besu and Nethermind development images advanced; Erigon development and both Reth
images are unchanged. The Reth nightly image still reports `58a51b3e`, so Reth fixes
merged after it are not measured here. The later Geth fork commit `0a663f3c`, which
runs over-cap unsigned gas at the RPC cap, is not exercised by any corpus.

## Capture completeness

The suite retained **14,051 RPC responses**; **14 of 15 corpora completed**.

| Corpus | Complete | Responses | Builds failing setup controls |
| --- | --- | --- | --- |
| [initial](initial/summary.json) | Yes | 684 | — |
| [a](a/summary.json) | Yes | 819 | — |
| [repeat](repeat/summary.json) | Yes | 396 | — |
| [forks](forks/summary.json) | Yes | 828 | — |
| [fork-followup](fork-followup/summary.json) | Yes | 216 | — |
| [precompiles](precompiles/summary.json) | Yes | 171 | — |
| [precompile-values](precompile-values/summary.json) | Yes | 135 | — |
| [raw-validation](raw-validation/summary.json) | Yes | 639 | — |
| [coverage](coverage/summary.json) | Yes | 216 | — |
| [fee-policy](fee-policy/summary.json) | Yes | 6,804 | — |
| [fee-compat](fee-compat/summary.json) | Yes | 2,700 | — |
| [callmany-isolation](callmany-isolation/summary.json) | Yes | 90 | — |
| [h30](h30/summary.json) | Yes | 171 | — |
| [reorg-safe](reorg-safe/summary.json) | No | 152 | erigon_development |
| [pruned](pruned/summary.json) | Yes | 30 | — |

The reorg scenario stops at Erigon development's first branch switch: every
`engine_newPayloadV4` returns VALID, then `engine_forkchoiceUpdatedV3` to the sibling
head returns `Invalid forkchoice state` (-38002), so the later height controls are
never sent. Every captured Erigon development build fails at this step, and 3.6.1
passes. Source reading attributes it to Erigon marking the imported tip as finalized
at import, which a later forkchoice update's lower finalized block does not replace;
see [scenarios](../../../docs/scenarios.md#tested-matrix). Failed setup remains
blocked, and older observations never fill current gaps.

## Geth draft fork

The fork now follows the adopted stances. Compared with the previous matrix, its
checked cases agree on H06, H08, H15, H16, H19, H21 and H30. The remaining H20
difference is the `coverage/model-environment-free` zero-fee call, where the
replay/raw model predated the H15 zero BASEFEE rule; the corrected model agrees.
H12 and H32 simulation `pending` remain policy observations.

## Validation

[validation.json](validation.json) records the harness tests, frozen-input
verification and report assessment hash for this selection.

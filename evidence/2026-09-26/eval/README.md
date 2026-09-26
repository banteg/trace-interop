# Eval: fresh client matrix — 2026-09-26

The eighteen-corpus suite resolved all nine published builds together and passed its live
[freshness preflight](preflight.json) at **2026-09-26 06:31:54 UTC**. [clients.lock.json](clients.lock.json)
freezes that snapshot across every corpus. The eval measures Besu 26.9.0, the day's development builds,
the first Reth nightly with revm-inspectors 0.44.0, and the Geth draft fork after its precheck-frame and
null-member changes. It is also the first capture of the call depth limit, the debug-tracer precheck
references and the null-member cases (see
[precheck, depth and null cases](../../../docs/assertion-models.md#precheck-depth-and-null-cases)).

Every capture uses harness commit `b46e0f25` on Fedora and disposable Hive chains.
Manifests retain `source_dirty: true` because the matrix created its untracked output
folder before each corpus checked git status; the [source audit](source-audit.json)
confirms it is the only dirty path and the runner hash matches every capture.
[reports.lock.json](../../../reports.lock.json) selects this snapshot, including incomplete
runs, and compares it with the [2026-09-25 refresh](../../2026-09-25/refresh/README.md).

## Tested builds

Besu released 26.9.0; its development image is unchanged. Erigon and Nethermind development builds
advanced, and Reth's nightly `df7b7fdf` is the first to lock revm-inspectors 0.44.0. Erigon 3.7.0,
Nethermind 2.0.0 and Reth 2.6.0 are the same releases as the refresh. The Geth draft fork is `c8449896`.
Exact versions and commits are in the [client reports](../../../reports/README.md) and the
[changes since the refresh](../../../reports/changes.md).

## Capture completeness

The suite retained **15,625 RPC responses**; **17 of 18 corpora completed**.

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
| [probes-prague](probes-prague/summary.json) | Yes | 477 | — |
| [probes-forks](probes-forks/summary.json) | Yes | 306 | — |
| [mined-probes](mined-probes/summary.json) | Yes | 801 | — |
| [reorg-safe](reorg-safe/summary.json) | No | 142 | erigon_development, erigon_release |
| [pruned](pruned/summary.json) | Yes | 30 | — |

The reorg scenario stops at its branch switch for both Erigon builds ("Invalid forkchoice state", fixed in
open [#24032](https://github.com/erigontech/erigon/pull/24032)). Both Reth builds passed it this time; its
race ([#27429](https://github.com/paradigmxyz/reth/pull/27429)) is intermittent. Failed setup remains blocked,
and older observations never fill current gaps.

## Validation

[validation.json](validation.json) records the harness tests, frozen-input verification and
report assessment hash for this selection.

# Fixture wave: fresh client matrix — 2026-09-25

The eighteen-corpus suite resolved all nine published builds together and passed its live
[freshness preflight](preflight.json) at **2026-09-24 21:54:10 UTC**.
[clients.lock.json](clients.lock.json) freezes that snapshot across every corpus. It adds
three corpora from the fixture wave: [`probes-prague`](../../../fixtures/corpora/probes-prague.json)
and [`probes-forks`](../../../fixtures/corpora/probes-forks.json) on the existing chains, and
[`mined-probes`](../../../docs/mined-probes.md) on a new generated chain.

Every capture uses harness commit `5ac0fb37` on Fedora and disposable Hive chains.
Manifests retain `source_dirty: true` because the matrix created its untracked output
folder before each corpus checked git status; the [source audit](source-audit.json)
confirms it is the only dirty path and the runner hash matches every capture.
[reports.lock.json](../../../reports.lock.json) selects this snapshot, including incomplete
runs, and compares it with the [previous matrix](../../2026-09-24/adopted-stances/README.md).

## Tested builds

Besu and Nethermind development and Erigon development advanced; the Geth draft fork is
`0a663f3c`. Reth's nightly image is still `58a51b3e`: the capture ran before its next
scheduled build, so Reth fixes merged on 2026-09-24 are not measured here. Exact versions
and commits are in the [client reports](../../../reports/README.md).

## Capture completeness

The suite retained **15,473 RPC responses**; **16 of 18 corpora completed**.

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
| [probes-prague](probes-prague/summary.json) | Yes | 387 | — |
| [probes-forks](probes-forks/summary.json) | No | 234 | erigon_release |
| [mined-probes](mined-probes/summary.json) | Yes | 801 | — |
| [reorg-safe](reorg-safe/summary.json) | No | 152 | erigon_development |
| [pruned](pruned/summary.json) | Yes | 30 | — |

Erigon development again stops the reorg scenario at its first branch switch
([#24292](https://github.com/erigontech/erigon/pull/24292)). Erigon 3.6.1 fails the
`probes-forks` setup control `_control/beacon-timestamp-55`, so that corpus is ineligible
for it. Failed setup remains blocked, and older observations never fill current gaps.

## Validation

[validation.json](validation.json) records the harness tests, frozen-input verification and
report assessment hash for this selection.

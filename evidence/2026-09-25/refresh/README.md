# Release refresh: fresh client matrix — 2026-09-25

The eighteen-corpus suite resolved all nine published builds together and passed its live
[freshness preflight](preflight.json) at **2026-09-25 08:32:17 UTC**.
[clients.lock.json](clients.lock.json) freezes that snapshot across every corpus. The
refresh measures Erigon 3.7.0, released the same morning, the day's development builds,
and four corrected probe cases that the
[fixture wave](../fixture-wave/README.md) could not yet capture (see
[corrected siblings](../../../docs/assertion-models.md#corrected-siblings)).

Every capture uses harness commit `bda5d9f3` on Fedora and disposable Hive chains.
Manifests retain `source_dirty: true` because the matrix created its untracked output
folder before each corpus checked git status; the [source audit](source-audit.json)
confirms it is the only dirty path and the runner hash matches every capture.
[reports.lock.json](../../../reports.lock.json) selects this snapshot, including incomplete
runs, and compares it with the fixture wave.

## Tested builds

Besu, Erigon, Nethermind and Reth development builds advanced, and Erigon's stable
release moved from 3.6.1 to 3.7.0. Besu 26.8.1, Nethermind 2.0.0, Reth 2.6.0 and the Geth
draft fork (`0a663f3c`) are byte-identical to the fixture wave; the whole matrix was
recaptured anyway, since it takes about twenty minutes. Exact versions and commits are
in the [client reports](../../../reports/README.md) and the
[changes since the fixture wave](../../../reports/changes.md).

## Capture completeness

The suite retained **15,489 RPC responses**; **17 of 18 corpora completed**.

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
| [probes-prague](probes-prague/summary.json) | Yes | 414 | — |
| [probes-forks](probes-forks/summary.json) | Yes | 243 | — |
| [mined-probes](mined-probes/summary.json) | Yes | 801 | — |
| [reorg-safe](reorg-safe/summary.json) | No | 132 | erigon_development, erigon_release, reth_development, reth_release |
| [pruned](pruned/summary.json) | Yes | 30 | — |

The reorg scenario stops at its branch switch for both Erigon builds ("Invalid forkchoice
state": a same-head forkchoice update drops safe and finalized, fixed in open
[#24032](https://github.com/erigontech/erigon/pull/24032)) and for both Reth builds (the
canonical head never returns to the restored branch, the race fixed in open
[#27429](https://github.com/paradigmxyz/reth/pull/27429)). Erigon 3.7.0 passes the
`probes-forks` setup control that 3.6.1 failed. Failed setup remains blocked, and older
observations never fill current gaps.

## Validation

[validation.json](validation.json) records the harness tests, frozen-input verification and
report assessment hash for this selection.

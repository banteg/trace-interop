# Anvil: first matrix with Foundry's Anvil — 2026-09-26

The eighteen-corpus suite resolved all eleven published builds together and passed its live
[freshness preflight](preflight.json). [clients.lock.json](clients.lock.json) freezes that snapshot
across every corpus. This is the first matrix with Foundry's Anvil: 1.8.3 · `cae51ad4` and the
nightly `5a99f1a8`, captured by [replaying each chain](../../../docs/usage.md#replica-captures)
because Anvil has no Engine API. Every other build is the same as in the [eval](../eval/README.md)
except Nethermind's development build, which advanced to `fca93966`.

Every capture uses harness commit `7b34ebe9` on Fedora and disposable chains. Manifests retain
`source_dirty: true` because the matrix created its untracked output folder before each corpus
checked git status; the [source audit](source-audit.json) confirms it is the only dirty path and the
runner and replica hashes match every capture. [reports.lock.json](../../../reports.lock.json) selects
this snapshot, including incomplete runs, and compares it with the eval.

## Capture completeness

The suite retained **18,754 RPC responses**; **16 of 18 corpora completed**. Anvil is captured on
the 13 corpora whose chains run one fork from genesis; `forks`, `fork-followup`, `probes-forks`,
`reorg-safe` and `pruned` need fork transitions or Hive-only setup.

| Corpus | Complete | Responses | Builds failing setup controls |
| --- | --- | --- | --- |
| [initial](initial/summary.json) | Yes | 836 | — |
| [a](a/summary.json) | Yes | 1,001 | — |
| [repeat](repeat/summary.json) | Yes | 484 | — |
| [forks](forks/summary.json) | Yes | 828 | — |
| [fork-followup](fork-followup/summary.json) | Yes | 216 | — |
| [precompiles](precompiles/summary.json) | Yes | 209 | — |
| [precompile-values](precompile-values/summary.json) | Yes | 165 | — |
| [raw-validation](raw-validation/summary.json) | Yes | 781 | — |
| [coverage](coverage/summary.json) | Yes | 264 | — |
| [fee-policy](fee-policy/summary.json) | Yes | 8,316 | — |
| [fee-compat](fee-compat/summary.json) | Yes | 3,300 | — |
| [callmany-isolation](callmany-isolation/summary.json) | Yes | 110 | — |
| [h30](h30/summary.json) | Yes | 209 | — |
| [probes-prague](probes-prague/summary.json) | Yes | 583 | — |
| [probes-forks](probes-forks/summary.json) | Yes | 306 | — |
| [mined-probes](mined-probes/summary.json) | No | 979 | anvil_development, anvil_release |
| [reorg-safe](reorg-safe/summary.json) | No | 137 | erigon_development, erigon_release, reth_release |
| [pruned](pruned/summary.json) | Yes | 30 | — |

Both Anvil builds replayed every block of `initial`, `a` and `raw-validation` exactly. In `mined-probes`, block
`0x2` differs in gas used and receipts root: its probe reads the block's own parent beacon root, which Anvil
cannot set. The replica is therefore ineligible and those cases are blocked rather than compared.

The reorg scenario stops at its branch switch for both Erigon builds ("Invalid forkchoice state", open
[#24032](https://github.com/erigontech/erigon/pull/24032)). Reth 2.6.0 did not publish the restored head this
time; the race is intermittent and fixed on main ([#27429](https://github.com/paradigmxyz/reth/pull/27429)).
Failed setup remains blocked, and older observations never fill current gaps.

## Validation

[validation.json](validation.json) records the harness tests, frozen-input verification and
report assessment hash for this selection.

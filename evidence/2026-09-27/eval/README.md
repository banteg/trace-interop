# Eval: fresh client matrix — 2026-09-27

The eighteen-corpus suite resolved all eleven published builds together and passed its live
[freshness preflight](preflight.json) at **2026-09-27 18:12:29 UTC**. [clients.lock.json](clients.lock.json)
freezes that snapshot across every corpus. The eval measures the day's Erigon, Nethermind and Reth
development builds, the Foundry nightly with revm-inspectors 0.44.0 and the Geth draft fork after its
label, error-code and pending changes. It is also the first capture of the divergent-decisions review cases
and the unpriced null-list probes (see [cases from the divergent-decisions review](../../../docs/assertion-models.md#cases-from-the-divergent-decisions-review)).

Every capture uses harness commit `395d8a55` on Fedora and disposable chains: Hive for the native builds
and the Geth draft, [replicas](../../../docs/usage.md#replica-captures) for Anvil. Manifests retain
`source_dirty: true` because the matrix created its untracked output folder before each corpus checked
git status; the [source audit](source-audit.json) confirms it is the only dirty path and the runner and
replica hashes match every capture. [reports.lock.json](../../../reports.lock.json) selects this snapshot,
including incomplete runs, and compares it with the [2026-09-26 Anvil matrix](../../2026-09-26/anvil/README.md).

## Tested builds

Erigon's development build advanced to `3904de43`, which carries #24334, #24345, #24351 and #24352.
Nethermind's advanced to `5ece5fba`, with #13666 and #13936. Reth's nightly `863f7055` still locks
revm-inspectors 0.44.0 and does not yet take up Alloy #4257. The Foundry nightly `07915e32` takes up
revm-inspectors 0.44.0 (#17073) and the trace request defaults (#17078) but predates #17089. The Geth
draft fork is `e26833e3`. Besu 26.9.0, its development image and Erigon 3.7.0, Nethermind 2.0.0,
Reth 2.6.0 and Anvil 1.8.3 are the same builds as in the previous matrix. Exact versions and commits
are in the [client reports](../../../reports/README.md) and the [changes since the previous matrix](../../../reports/changes.md).

## Capture completeness

The suite retained **18,968 RPC responses**; **16 of 18 corpora completed**. Anvil is captured on
the 13 corpora whose chains run one fork from genesis.

| Corpus | Complete | Responses | Builds failing setup controls |
| --- | --- | --- | --- |
| [initial](initial/summary.json) | Yes | 836 | — |
| [a](a/summary.json) | Yes | 1,034 | — |
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
| [h30](h30/summary.json) | Yes | 253 | — |
| [probes-prague](probes-prague/summary.json) | Yes | 715 | — |
| [probes-forks](probes-forks/summary.json) | Yes | 306 | — |
| [mined-probes](mined-probes/summary.json) | No | 979 | anvil_development, anvil_release |
| [reorg-safe](reorg-safe/summary.json) | No | 142 | erigon_development, erigon_release |
| [pruned](pruned/summary.json) | Yes | 30 | — |

Both Anvil builds again replay block `0x2` of `mined-probes` with a different gas used and receipts root,
because its probe reads the block's own parent beacon root, which Anvil cannot set; those cases are blocked.
The reorg scenario stops at its branch switch for both Erigon builds ("Invalid forkchoice state", open
[#24032](https://github.com/erigontech/erigon/pull/24032)). Both Reth builds passed it this time; the race
([#27429](https://github.com/paradigmxyz/reth/pull/27429)) is intermittent in 2.6.0. Failed setup remains
blocked, and older observations never fill current gaps.

## Validation

[validation.json](validation.json) records the harness tests, frozen-input verification and
report assessment hash for this selection.

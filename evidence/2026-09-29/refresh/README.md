# Refresh: fresh client matrix — 2026-09-29

The eighteen-corpus suite resolved all eleven published builds together and passed its live
[freshness preflight](preflight.json) at **2026-09-29 08:19:31 UTC**. [clients.lock.json](clients.lock.json)
freezes that snapshot across every corpus. The refresh measures the Nethermind development build that took
up #13981, merged after the [morning eval](../eval/README.md), and the first Reth nightly built after the
2.7.0 release; no development build is older than its release (`lagging_development` is empty).

Every capture uses harness commit `a35b754e` on Fedora and disposable chains: Hive for the native builds
and the Geth draft, [replicas](../../../docs/usage.md#replica-captures) for Anvil. Manifests retain
`source_dirty: true` because the matrix created its untracked output folder before each corpus checked
git status; the [source audit](source-audit.json) confirms it is the only dirty path and the runner and
replica hashes match every capture. [reports.lock.json](../../../reports.lock.json) selects this snapshot,
including incomplete runs, and compares it with the [2026-09-29 eval](../eval/README.md).

## Tested builds

Nethermind's development build advanced to `287f54f0` (2.2.0-preview after the version bump in #14010), the
merge of #13971. It carries #13981 (reverted-frame results and Parity failure labels) on top of the fixes
of `82516987`. The Reth nightly is now 2.7.0 `60aeb532`, built at 01:38 UTC from main. It has twelve commits
that the 2.7.0 release commit `3d592ece` lacks, among them main's release bump (#27489); only #27465
(tracing permits for the otterscan and debug methods) touches the RPC. Erigon's development build advanced to `a2a19253` (merge of #24321) and the
Foundry nightly to `00989695`; both return byte-identical responses to their previous builds. Besu's
development build (`c197ac57`), the Geth draft fork (`e26833e3`), Reth 2.7.0, Besu 26.9.0, Erigon 3.7.0,
Nethermind 2.0.0 and Anvil 1.8.3 are the same builds as in the previous matrix. Exact versions and commits
are in the [client reports](../../../reports/README.md) and the [changes since the previous matrix](../../../reports/changes.md).

The Reth nightly returns the same response as Reth 2.7.0 in 1,768 of 1,769 captured requests, apart from
the reported version. The exception is a setup query in the reorg scenario, not an assessed case: after the
branch switch, `eth_getTransactionReceipt` for the transaction dropped from the canonical chain returns
-32001 ("block not found") instead of null.

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
[#24032](https://github.com/erigontech/erigon/pull/24032)). Failed setup remains blocked, and older
observations never fill current gaps.

## Validation

[validation.json](validation.json) records the harness tests, frozen-input verification and
report assessment hash for this selection.

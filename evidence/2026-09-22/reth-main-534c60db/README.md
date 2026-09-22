# Reth merged-fix verification

Tested upstream [`main@534c60db9d`](https://github.com/paradigmxyz/reth/commit/534c60db9d4be32d349e5b31456416ecb4b4dbee) on 2026-09-22. This includes the merged replay-hash and pruned-history patches, with the original locked dependencies and no unmerged changes.

| Change | Result |
| --- | --- |
| [#27365: replay transaction hash](https://github.com/paradigmxyz/reth/pull/27365) | **Verified in all 12 cases:** call tree, revert, EIP-7702 and transfer transactions, each with `trace`, `stateDiff` and `vmTrace` selection. Every returned hash matches the requested transaction. |
| [#27367: unavailable history](https://github.com/paradigmxyz/reth/pull/27367) | **Partial:** the old-state nonce query returns `4444`. The four historical trace methods still return `-32603`: the blockhash system-call path stringifies the database error before the new mapping can handle it. This remaining path is explicitly outside the PR's coverage. |

The pruning scenario retained the old header and receipt, successfully executed the latest-state call, and independently confirmed old state was unavailable. Both runs completed with all setup controls satisfied.

| Historical request | Observed error |
| --- | --- |
| `eth_getTransactionCount` | `4444`: pruned history unavailable |
| `trace_transaction` | `-32603`: failed to apply blockhash contract call; insufficient changesets |
| `trace_replayTransaction` | Same wrapped system-call error |
| `trace_block` | Same wrapped system-call error |
| `trace_filter` | Same wrapped system-call error |

No reruns were made for open #27364/#27366 or for the Alloy/inspector fixes absent from Reth's locked dependency versions. These results supplement the pinned client reports; they do not replace the full matrix or establish release verification.

## Evidence

- [Replay responses](initial/observations.json) and [run controls](initial/summary.json).
- [Pruned-state responses](pruned/observations.json) and [run controls](pruned/summary.json).
- [Scoped assertions](checks.json), [client build lock](clients.lock.json), and [upstream merge/dependency status](upstream-status.json).
- Each run retains its original manifest, raw Hive logs and checksums. The runner source was clean at `f34628780cee911b0dbc285321a0c332249bc803`.

The source-built binary uses Rust 1.96.0, the dev profile with debug information disabled, `--locked --no-default-features`, and the source commit recorded in its version metadata. Source files were byte-compared with the commit archive before execution. The lock records the source archive, binary and Docker image hashes. This is a functional check, not a performance comparison with release or nightly builds.

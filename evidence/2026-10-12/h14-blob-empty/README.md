# H14 empty blob hash list — 2026-10-12

A focused recapture of `probes-forks` that adds `fork-blob-empty-before` and `fork-blob-empty-at`, each with an
`eth_call` twin. It runs with the [2026-10-11 eval](../../2026-10-11/eval/README.md)'s
[build lock](../../2026-10-11/eval/clients.lock.json), like the [blob fee cap recapture](../h14-blob-cap/README.md)
earlier the same day, and keeps that run's lone-cap cases. It resends every request of the eval's `probes-forks` run,
so [reports.lock.json](../../../reports.lock.json) selects it in place of that run. Anvil is not captured for
`probes-forks`, because it needs Hive. Captured on Fedora from harness commit `6c3a2aab` (`source_dirty: false`)
with disposable Hive chains.

[probes-forks](probes-forks/summary.json) is complete: **648 responses**, and every build passed the setup controls.
The 68 cases it shares with the blob fee cap recapture return the same responses. The only exception is Besu, whose
`Invalid transaction type` rejections again list the accepted types in a different order.

## Probe

[ethereum/execution-apis#939](https://github.com/ethereum/execution-apis/pull/939) and
[ethereum/go-ethereum#35928](https://github.com/ethereum/go-ethereum/pull/35928) count an empty
`blobVersionedHashes` list as no hashes and reject it at every fork. A blob transaction carries at least one versioned
hash, so H14 rejects it too (2026-10-12). The probe sends an unpriced call to a code-free address with
`blobVersionedHashes: []` and no blob fee cap, one block before Cancun (block 55) and at Cancun (block 56) on the
forks chain.

## Findings

The same at both blocks:

| Builds | `trace_call` | `eth_call` |
| --- | --- | --- |
| Reth 2.7.0 (both builds) | -32003 `blob transaction missing blob hashes` | -32003, the same |
| Nethermind 2.1.0 and 2.2.0-preview | -32000 `need at least 1 blob for a blob transaction` | -32000, the same |
| Erigon 3.8.0-dev | -32000 (`BlobTx transactions require Cancun` before, `must contain at least one blob versioned hash` at) | -32000, the same |
| Geth draft | -32602 `blob transaction missing blob hashes` | -32000 (upstream `eth_call`) |
| Erigon 3.7.1 | runs | -32000, as the development build |
| Besu 26.9.0 and develop | -32603 `Internal error` | -32603 `Internal error` |

Unlike a lone blob fee cap, which only Reth rejects, an empty list is already rejected by most builds. Besu fails with
an internal error, which is no rejection. [besu-eth/besu#11556](https://github.com/besu-eth/besu/pull/11556) turns
it into -32602 `Invalid blob count`.

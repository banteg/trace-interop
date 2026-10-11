# H14 blob fee cap without hashes — 2026-10-12

A focused recapture of `probes-forks` that adds `fork-blob-fee-only-before` and `fork-blob-fee-only-at`, each with an
`eth_call` twin. It runs with the [2026-10-11 eval](../../2026-10-11/eval/README.md)'s
[build lock](../../2026-10-11/eval/clients.lock.json) (`trace_interop run --lock`), so every build is that matrix's
image. Anvil is not captured for `probes-forks`, because it needs Hive. The run resends every request of that matrix's
`probes-forks` run, so [reports.lock.json](../../../reports.lock.json) selects it in place of that run. Captured on
Fedora from harness commit `66155b7d` (`source_dirty: false`) with disposable Hive chains.

[probes-forks](probes-forks/summary.json) is complete: **612 responses**, and every build passed the setup controls.
The 64 cases it shares with the eval run return the same responses. The only exception is Besu, whose
`Invalid transaction type` rejections list the accepted types in a different order.

## Probe

On [execution-apis#884](https://github.com/ethereum/execution-apis/issues/884), the profile agreed with Erigon to
reject `maxFeePerBlobGas` without `blobVersionedHashes` at every fork (H14, 2026-10-12). A blob transaction carries
at least one versioned hash, so a lone cap describes no transaction. The probe sends an unpriced call to a code-free
address with `maxFeePerBlobGas: "0x1"` and no hashes, one block before Cancun (block 55) and at Cancun (block 56) on
the forks chain. Running the call means the cap was ignored.

## Findings

The same at both blocks:

| Builds | `trace_call` | `eth_call` |
| --- | --- | --- |
| Reth 2.7.0 (both builds) | -32003 `blob transaction missing blob hashes` | -32003, the same |
| Geth draft | -32602 `blob transaction missing blob hashes` | runs (upstream `eth_call`) |
| Besu develop | runs | runs |
| Besu 26.9.0 | -32603 `Internal error` | runs |
| Erigon 3.7.1 and 3.8.0-dev | runs | runs |
| Nethermind 2.1.0 and 2.2.0-preview | runs | runs |

Only Reth rejects the lone cap. Erigon has offered the one-line gate on #884, and the others run the call with the
cap neither validated nor charged. Besu 26.9.0's internal error is no rejection.

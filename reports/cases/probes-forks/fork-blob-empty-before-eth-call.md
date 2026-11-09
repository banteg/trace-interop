# Fork blob empty before eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** An empty blobVersionedHashes list at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "blobVersionedHashes": [],
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x186a0",
      "maxFeePerGas": "0x0",
      "maxPriorityFeePerGas": "0x0",
      "to": "0x00000000000000000000000000000000000000ee"
    },
    "0x37"
  ]
}
```

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-empty-before. Observed: Observed rpc_error -32602: Invalid blob count (blob transactions must have at least one blob)

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-empty-before. Observed: Observed rpc_error -32602: Invalid blob count (blob transactions must have at least one blob)

**Erigon · 3.9.0-dev · cf91acee** (`3.9.0-dev-cf91acee`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-empty-before. Observed: Observed rpc_error -32000: BlobTx transactions require Cancun (-32602 recommended); the rejection does not report the defect the requirement names.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-empty-before. Observed: Observed rpc_error -32000: BlobTx transactions require Cancun (-32602 recommended); the rejection does not report the defect the requirement names.

**Geth draft fork · 1.17.11-unstable · e487da1e** (`Geth/v1.17.11-unstable-e487da1e-2026-11-01/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-empty-before. Observed: Observed rpc_error -32000: err: transaction type not supported: blob tx (sender 0x7435ed30A8b4AEb0877CEf0c6E8cFFe834eb865f) (supplied gas 100000) (-32602 recommended); the rejection does not report the defect the requirement names.

**Nethermind · 2.3.0-preview · 4079edfa** (`2.3.0-preview+4079edfa`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-empty-before. Observed: Observed rpc_error -32000: need at least 1 blob for a blob transaction (-32602 recommended)

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-empty-before. Observed: Observed rpc_error -32000: need at least 1 blob for a blob transaction (-32602 recommended)

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-empty-before. Observed: Observed rpc_error -32003: blob transaction missing blob hashes (-32602 recommended)

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-empty-before. Observed: Observed rpc_error -32003: blob transaction missing blob hashes (-32602 recommended)

</details>

# Fork blob fee only before eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** A maxFeePerBlobGas without blobVersionedHashes at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x186a0",
      "maxFeePerBlobGas": "0x1",
      "maxFeePerGas": "0x0",
      "maxPriorityFeePerGas": "0x0",
      "to": "0x00000000000000000000000000000000000000ee"
    },
    "0x37"
  ]
}
```

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-fee-only-before. Observed: Observed rpc_error -32602: Invalid blob count (blob transactions must have at least one blob)

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-fee-only-before. Observed: Observed rpc_error -32602: Invalid blob count (blob transactions must have at least one blob)

**Erigon · 3.9.0-dev · e91aca7f** (`3.9.0-dev-e91aca7f`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-fee-only-before. Observed: Observed rpc_error -32000: maxFeePerBlobGas requires blobVersionedHashes: blob txn must contain at least one blob versioned hash (-32602 recommended)

**Erigon · 3.8.2 · 8a3f3b2c** (`3.8.2-8a3f3b2c`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-fee-only-before. Observed: Observed rpc_error -32000: maxFeePerBlobGas requires blobVersionedHashes: blob txn must contain at least one blob versioned hash (-32602 recommended)

**Geth draft fork · 1.17.11-unstable · edbd5f17** (`Geth/v1.17.11-unstable-edbd5f17-2026-11-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-fee-only-before. Observed: Observed rpc_error -32000: maxFeePerBlobGas specified without blobVersionedHashes (-32602 recommended)

**Nethermind · 2.4.0-preview · e2f069a6** (`2.4.0-preview+e2f069a6`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-fee-only-before. Observed: Observed rpc_error -32000: maxFeePerBlobGas specified without blobVersionedHashes (-32602 recommended)

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-fee-only-before. Observed: Observed result with output 0x

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-fee-only-before. Observed: Observed rpc_error -32003: blob transaction missing blob hashes (-32602 recommended)

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 55, before Cancun (block 56) describes no transaction, so the call is rejected for that defect (-32602 recommended), never run with the field ignored. The defect is invalid regardless of state, so it takes precedence over the inactive blob feature. eth_call parity control for fork-blob-fee-only-before. Observed: Observed rpc_error -32003: blob transaction missing blob hashes (-32602 recommended)

</details>

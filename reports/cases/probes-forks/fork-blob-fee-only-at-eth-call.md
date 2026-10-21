# Fork blob fee only at eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |

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
    "0x38"
  ]
}
```

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed rpc_error -32602: Invalid blob count (blob transactions must have at least one blob) (-32003 recommended)

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed result with output 0x

**Erigon · 3.9.0-dev · d23467c5** (`3.9.0-dev-d23467c5`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed rpc_error -32000: maxFeePerBlobGas requires blobVersionedHashes: blob txn must contain at least one blob versioned hash (-32003 recommended)

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed result with output 0x

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed result with output 0x

**Nethermind · 2.3.0-preview · e2e011c8** (`2.3.0-preview+e2e011c8`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed rpc_error -32000: maxFeePerBlobGas specified without blobVersionedHashes (-32003 recommended)

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed result with output 0x

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed rpc_error -32003: blob transaction missing blob hashes

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed rpc_error -32003: blob transaction missing blob hashes

</details>

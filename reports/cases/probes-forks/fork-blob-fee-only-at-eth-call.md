# Fork blob fee only at eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/manifest.json) |
| [Besu · 26.10-develop · d05d8e74](../../clients/besu_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 1d3ebbf2](../../clients/erigon_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 204457ad](../../clients/nethermind_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 1a4dbbe1](../../clients/reth_development.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-12/h14-blob-cap/probes-forks/manifest.json) |

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

**Besu · 26.10-develop · d05d8e74** (`besu/v26.10-develop-d05d8e7/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed result with output 0x

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed result with output 0x

**Erigon · 3.8.0-dev · 1d3ebbf2** (`3.8.0-dev-1d3ebbf2`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed result with output 0x

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed result with output 0x

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed result with output 0x

**Nethermind · 2.2.0-preview · 204457ad** (`2.2.0-preview+204457ad`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed result with output 0x

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed result with output 0x

**Reth · 2.7.0 · 1a4dbbe1** (`Reth Version: 2.7.0+1a4dbbe1`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed rpc_error -32003: blob transaction missing blob hashes

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): A maxFeePerBlobGas without blobVersionedHashes at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-fee-only-at. Observed: Observed rpc_error -32003: blob transaction missing blob hashes

</details>

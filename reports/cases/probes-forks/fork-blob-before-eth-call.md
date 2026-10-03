# Fork blob before eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | RPC error `-32603` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "blobVersionedHashes": [
        "0x015a4cab4911426699ed34483de6640cf55a568afc5c5edffdcbd8bcd4452f68"
      ],
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

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32602: Invalid transaction type (Transaction type BLOB is invalid, accepted transaction types are [FRONTIER, ACCESS_LIST, EIP15 (-32003 recommended)

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32602: Invalid transaction type (Transaction type BLOB is invalid, accepted transaction types are [EIP1559, FRONTIER, ACCESS_LI (-32003 recommended)

**Erigon · 3.8.0-dev · 6da806cb** (`3.8.0-dev-6da806cb`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32000: BlobTx transactions require Cancun (-32003 recommended)

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32000: BlobTx transactions require Cancun (-32003 recommended)

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32000: err: transaction type not supported: blob tx (sender 0x7435ed30A8b4AEb0877CEf0c6E8cFFe834eb865f) (supplied gas 100000) (-32003 recommended)

**Nethermind · 2.2.0-preview · 3370d566** (`2.2.0-preview+3370d566`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed result with output 0x

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32603: Internal error (-32003 recommended)

**Reth · 2.7.0 · 078d0262** (`Reth Version: 2.7.0+078d0262`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32003: transaction type not supported

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32003: transaction type not supported

</details>

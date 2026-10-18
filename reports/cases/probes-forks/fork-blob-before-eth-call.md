# Fork blob before eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |

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

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32602: Invalid transaction type (Transaction type BLOB is invalid, accepted transaction types are [EIP1559, ACCESS_LIST, FRONTI (-32003 recommended)

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32602: Invalid transaction type (Transaction type BLOB is invalid, accepted transaction types are [ACCESS_LIST, FRONTIER, EIP15 (-32003 recommended)

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32000: BlobTx transactions require Cancun (-32003 recommended)

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32000: BlobTx transactions require Cancun (-32003 recommended)

**Geth draft fork · 1.17.9-unstable · fdbb46a5** (`Geth/v1.17.9-unstable-fdbb46a5-2026-10-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32000: err: transaction type not supported: blob tx (sender 0x7435ed30A8b4AEb0877CEf0c6E8cFFe834eb865f) (supplied gas 100000) (-32003 recommended)

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32000: InvalidTxType: Transaction type in Custom is not supported. (-32003 recommended)

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed result with output 0x

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32003: transaction type not supported

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-blob-before. Observed: Observed rpc_error -32003: transaction type not supported

</details>

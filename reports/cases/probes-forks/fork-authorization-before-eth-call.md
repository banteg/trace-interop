# Fork authorization before eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32603` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
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
      "authorizationList": [
        {
          "address": "0x00000000000000000000000000000000000000ee",
          "chainId": "0xc72dd9d5e883e",
          "nonce": "0x0",
          "r": "0x86af3a52abd32c04ce6704ee2710dab8447f7af79930e97d893a2ec773c02964",
          "s": "0x4043b2933aefee93438b1a0599d16ee5f806844140a43d4883e5a2f99423862b",
          "yParity": "0x1"
        }
      ],
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x186a0",
      "maxFeePerGas": "0x0",
      "maxPriorityFeePerGas": "0x0",
      "to": "0x00000000000000000000000000000000000000ee"
    },
    "0x3b"
  ]
}
```

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32602: Invalid transaction type (Transaction type DELEGATE_CODE is invalid, accepted transaction types are [ACCESS_LIST, FRONTI (-32003 recommended)

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32602: Invalid transaction type (Transaction type DELEGATE_CODE is invalid, accepted transaction types are [EIP1559, BLOB, ACCE (-32003 recommended)

**Erigon · 3.9.0-dev · d23467c5** (`3.9.0-dev-d23467c5`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32000: SetCode transaction not allowed before Prague fork (-32003 recommended)

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32000: SetCode transaction not allowed before Prague fork (-32003 recommended)

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32000: err: transaction type not supported: setcode tx (sender 0x7435ed30A8b4AEb0877CEf0c6E8cFFe834eb865f) (supplied gas 100000 (-32003 recommended)

**Nethermind · 2.3.0-preview · e2e011c8** (`2.3.0-preview+e2e011c8`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32000: InvalidTxType: Transaction type in Custom is not supported. (-32003 recommended)

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32603: Internal error (-32003 recommended)

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32003: transaction type not supported

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32003: transaction type not supported

</details>

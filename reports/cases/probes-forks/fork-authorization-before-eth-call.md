# Fork authorization before eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32603` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
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

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32602: Invalid transaction type (Transaction type DELEGATE_CODE is invalid, accepted transaction types are [ACCESS_LIST, FRONTI (-32003 recommended)

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32602: Invalid transaction type (Transaction type DELEGATE_CODE is invalid, accepted transaction types are [ACCESS_LIST, FRONTI (-32003 recommended)

**Erigon · 3.9.0-dev · e91aca7f** (`3.9.0-dev-e91aca7f`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32000: SetCode transaction not allowed before Prague fork (-32003 recommended)

**Erigon · 3.8.2 · 8a3f3b2c** (`3.8.2-8a3f3b2c`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32000: SetCode transaction not allowed before Prague fork (-32003 recommended)

**Geth draft fork · 1.17.11-unstable · edbd5f17** (`Geth/v1.17.11-unstable-edbd5f17-2026-11-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32000: err: transaction type not supported: setcode tx (sender 0x7435ed30A8b4AEb0877CEf0c6E8cFFe834eb865f) (supplied gas 100000 (-32003 recommended)

**Nethermind · 2.4.0-preview · e2f069a6** (`2.4.0-preview+e2f069a6`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32000: InvalidTxType: Transaction type in Custom is not supported. (-32003 recommended)

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32603: Internal error (-32003 recommended)

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32003: transaction type not supported

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-authorization-before. Observed: Observed rpc_error -32003: transaction type not supported

</details>

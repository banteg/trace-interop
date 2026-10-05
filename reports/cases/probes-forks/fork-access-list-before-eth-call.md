# Fork access list before eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** The access-list fields at block 31, before Berlin (block 32) name a feature not active at the selected block, so the call is rejected (-32003 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | RPC error `-32603` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | RPC error `-32603` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "accessList": [
        {
          "address": "0x00000000000000000000000000000000000000ee",
          "storageKeys": []
        }
      ],
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x186a0",
      "to": "0x00000000000000000000000000000000000000ee"
    },
    "0x1f"
  ]
}
```

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The access-list fields at block 31, before Berlin (block 32) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-access-list-before. Observed: Observed rpc_error -32602: Invalid transaction type (Transaction type ACCESS_LIST is invalid, accepted transaction types are [FRONTIER]) (-32003 recommended)

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The access-list fields at block 31, before Berlin (block 32) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-access-list-before. Observed: Observed rpc_error -32602: Invalid transaction type (Transaction type ACCESS_LIST is invalid, accepted transaction types are [FRONTIER]) (-32003 recommended)

**Erigon · 3.8.0-dev · 96188a47** (`3.8.0-dev-96188a47`)

- [H14](../../decisions/H14.md): The access-list fields at block 31, before Berlin (block 32) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-access-list-before. Observed: Observed rpc_error -32000: eip-2930 transactions require Berlin (-32003 recommended)

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): The access-list fields at block 31, before Berlin (block 32) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-access-list-before. Observed: Observed rpc_error -32000: eip-2930 transactions require Berlin (-32003 recommended)

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The access-list fields at block 31, before Berlin (block 32) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-access-list-before. Observed: Observed rpc_error -32000: err: transaction type not supported: access list tx (sender 0x7435ed30A8b4AEb0877CEf0c6E8cFFe834eb865f) (supplied gas 10 (-32003 recommended)

**Nethermind · 2.2.0-preview · e8955c4c** (`2.2.0-preview+e8955c4c`)

- [H14](../../decisions/H14.md): The access-list fields at block 31, before Berlin (block 32) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-access-list-before. Observed: Observed rpc_error -32603: Internal error (-32003 recommended)

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): The access-list fields at block 31, before Berlin (block 32) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-access-list-before. Observed: Observed rpc_error -32603: Internal error (-32003 recommended)

**Reth · 2.7.0 · 42fa3c56** (`Reth Version: 2.7.0+42fa3c56`)

- [H14](../../decisions/H14.md): The access-list fields at block 31, before Berlin (block 32) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-access-list-before. Observed: Observed rpc_error -32003: transaction type not supported

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): The access-list fields at block 31, before Berlin (block 32) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-access-list-before. Observed: Observed rpc_error -32003: transaction type not supported

</details>

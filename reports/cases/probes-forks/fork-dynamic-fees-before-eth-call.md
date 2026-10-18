# Fork dynamic fees before eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** The dynamic-fees fields at block 35, before London (block 36) name a feature not active at the selected block, so the call is rejected (-32003 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |

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
      "maxFeePerGas": "0x0",
      "maxPriorityFeePerGas": "0x0",
      "to": "0x00000000000000000000000000000000000000ee"
    },
    "0x23"
  ]
}
```

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The dynamic-fees fields at block 35, before London (block 36) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-dynamic-fees-before. Observed: Observed rpc_error -32602: Invalid transaction type (Transaction type EIP1559 is invalid, accepted transaction types are [ACCESS_LIST, FRONTIER]) (-32003 recommended)

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The dynamic-fees fields at block 35, before London (block 36) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-dynamic-fees-before. Observed: Observed rpc_error -32602: Invalid transaction type (Transaction type EIP1559 is invalid, accepted transaction types are [FRONTIER, ACCESS_LIST]) (-32003 recommended)

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- [H14](../../decisions/H14.md): The dynamic-fees fields at block 35, before London (block 36) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-dynamic-fees-before. Observed: Observed rpc_error -32000: eip-1559 transactions require London (-32003 recommended)

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): The dynamic-fees fields at block 35, before London (block 36) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-dynamic-fees-before. Observed: Observed result with output 0x

**Geth draft fork · 1.17.9-unstable · fdbb46a5** (`Geth/v1.17.9-unstable-fdbb46a5-2026-10-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The dynamic-fees fields at block 35, before London (block 36) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-dynamic-fees-before. Observed: Observed rpc_error -32000: maxFeePerGas and maxPriorityFeePerGas are not valid before London is active (-32003 recommended)

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H14](../../decisions/H14.md): The dynamic-fees fields at block 35, before London (block 36) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-dynamic-fees-before. Observed: Observed rpc_error -32000: InvalidTxType: Transaction type in Custom is not supported. (-32003 recommended)

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H14](../../decisions/H14.md): The dynamic-fees fields at block 35, before London (block 36) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-dynamic-fees-before. Observed: Observed result with output 0x

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H14](../../decisions/H14.md): The dynamic-fees fields at block 35, before London (block 36) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-dynamic-fees-before. Observed: Observed rpc_error -32003: transaction type not supported

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): The dynamic-fees fields at block 35, before London (block 36) name a feature not active at the selected block, so the call is rejected (-32003 recommended). eth_call parity control for fork-dynamic-fees-before. Observed: Observed rpc_error -32003: transaction type not supported

</details>

# Combo gasprice dynamic equal eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "data": "0x3a60005260206000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "gasPrice": "0x77359400",
      "maxFeePerGas": "0x77359400",
      "maxPriorityFeePerGas": "0x77359400"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.6-nightly · 9089a6bf** (`anvil Version: 1.8.6-nightly+9089a6bf`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-gasprice-dynamic-equal. Observed: Observed rpc_error -32602: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-gasprice-dynamic-equal. Observed: Observed rpc_error -32602: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-gasprice-dynamic-equal. Observed: Observed rpc_error -32602: Invalid params

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-gasprice-dynamic-equal. Observed: Observed rpc_error -32602: Invalid params

**Erigon · 3.9.0-dev · d23467c5** (`3.9.0-dev-d23467c5`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-gasprice-dynamic-equal. Observed: Observed rpc_error -32000: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified (-32602 recommended)

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-gasprice-dynamic-equal. Observed: Observed rpc_error -32000: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified (-32602 recommended)

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-gasprice-dynamic-equal. Observed: Observed rpc_error -32000: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified (-32602 recommended)

**Nethermind · 2.3.0-preview · e2e011c8** (`2.3.0-preview+e2e011c8`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-gasprice-dynamic-equal. Observed: Observed rpc_error -32000: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified (-32602 recommended)

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-gasprice-dynamic-equal. Observed: Observed rpc_error -32000: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified (-32602 recommended)

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-gasprice-dynamic-equal. Observed: Observed rpc_error -32602: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-gasprice-dynamic-equal. Observed: Observed rpc_error -32602: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified

</details>

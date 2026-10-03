# Combo auth gasprice dynamic eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | ❔ Policy open | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 328811cb](../../clients/anvil_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | ❔ Policy open | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | ❔ Policy open | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | ❔ Policy open | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |

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
          "address": "0x0000000000000000000000000000000000001002",
          "chainId": "0xc72dd9d5e883e",
          "nonce": "0xa",
          "r": "0x4e9c1a2430ff1f88a19f6567e51648c181b00616b4adcff8548b9785e3898814",
          "s": "0x707840665ae678f4933987814326a609a2ddb271ed461970ad744c0aae11779f",
          "yParity": "0x0"
        }
      ],
      "data": "0x",
      "from": "0x0c2c51a0990aee1d73c1228de158688341557508",
      "gas": "0x493e0",
      "gasPrice": "0x77359400",
      "maxFeePerGas": "0xb2d05e00",
      "maxPriorityFeePerGas": "0xb2d05e00",
      "to": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · 328811cb** (`anvil Version: 1.8.4-nightly+328811cb`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-auth-gasprice-dynamic. Observed: Observed result with output 0x000000000000000000000000000000000000000000000000000000000000002a

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-auth-gasprice-dynamic. Observed: Observed result with output 0x000000000000000000000000000000000000000000000000000000000000002a

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-auth-gasprice-dynamic. Observed: Observed result with output 0x000000000000000000000000000000000000000000000000000000000000002a

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-auth-gasprice-dynamic. Observed: Observed result with output 0x000000000000000000000000000000000000000000000000000000000000002a

**Erigon · 3.8.0-dev · 6da806cb** (`3.8.0-dev-6da806cb`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-auth-gasprice-dynamic. Observed: Observed rpc_error -32000: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified (-32602 recommended)

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-auth-gasprice-dynamic. Observed: Observed rpc_error -32000: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified (-32602 recommended)

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-auth-gasprice-dynamic. Observed: Observed rpc_error -32000: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified (-32602 recommended)

**Nethermind · 2.2.0-preview · 3370d566** (`2.2.0-preview+3370d566`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-auth-gasprice-dynamic. Observed: Observed rpc_error -32000: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified (-32602 recommended)

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-auth-gasprice-dynamic. Observed: Observed rpc_error -32000: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified (-32602 recommended)

**Reth · 2.7.0 · 078d0262** (`Reth Version: 2.7.0+078d0262`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-auth-gasprice-dynamic. Observed: Observed rpc_error -32602: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). eth_call parity control for combo-auth-gasprice-dynamic. Observed: Observed rpc_error -32602: both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified

</details>

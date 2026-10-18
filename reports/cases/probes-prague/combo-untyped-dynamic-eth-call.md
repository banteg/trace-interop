# Combo untyped dynamic eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** The call runs at GASPRICE 3000000000, from its dynamic fee caps.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |

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
      "maxFeePerGas": "0xb2d05e00",
      "maxPriorityFeePerGas": "0xb2d05e00"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.6-nightly · 6c21ffe2** (`anvil Version: 1.8.6-nightly+6c21ffe2`)

- [H14](../../decisions/H14.md): The call runs at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-untyped-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H14](../../decisions/H14.md): The call runs at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-untyped-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-untyped-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-untyped-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- [H14](../../decisions/H14.md): The call runs at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-untyped-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): The call runs at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-untyped-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Geth draft fork · 1.17.9-unstable · fdbb46a5** (`Geth/v1.17.9-unstable-fdbb46a5-2026-10-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The call runs at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-untyped-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H14](../../decisions/H14.md): The call runs at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-untyped-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H14](../../decisions/H14.md): The call runs at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-untyped-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H14](../../decisions/H14.md): The call runs at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-untyped-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): The call runs at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-untyped-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

</details>

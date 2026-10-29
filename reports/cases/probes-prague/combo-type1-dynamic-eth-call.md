# Combo type1 dynamic eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "accessList": [],
      "data": "0x3a60005260206000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "maxFeePerGas": "0xb2d05e00",
      "maxPriorityFeePerGas": "0xb2d05e00",
      "type": "0x1"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.7-nightly · 716e795c** (`anvil Version: 1.8.7-nightly+716e795c`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Erigon · 3.9.0-dev · 6955d198** (`3.9.0-dev-6955d198`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Geth draft fork · 1.17.11-unstable · 0f1fb2ae** (`Geth/v1.17.11-unstable-0f1fb2ae-2026-10-28/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Nethermind · 2.3.0-preview · fc9abf09** (`2.3.0-preview+fc9abf09`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x0000000000000000000000000000000000000000000000000000000000000000']

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

</details>

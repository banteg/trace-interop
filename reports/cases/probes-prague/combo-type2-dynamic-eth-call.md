# Combo type2 dynamic eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** The call runs with type 2, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |

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
      "maxPriorityFeePerGas": "0xb2d05e00",
      "type": "0x2"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · 60255eee** (`anvil Version: 1.8.4-nightly+60255eee`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type2-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type2-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type2-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type2-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Erigon · 3.8.0-dev · 5cb6c867** (`3.8.0-dev-5cb6c867`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type2-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type2-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type2-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Nethermind · 2.2.0-preview · 6dff813b** (`2.2.0-preview+6dff813b`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type2-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type2-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Reth · 2.7.0 · 10bcf461** (`Reth Version: 2.7.0+10bcf461`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type2-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type2-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

</details>

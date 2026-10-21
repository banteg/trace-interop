# Combo type0 dynamic eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |

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
      "type": "0x0"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.6-nightly · 9089a6bf** (`anvil Version: 1.8.6-nightly+9089a6bf`)

- [H14](../../decisions/H14.md): The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type0-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H14](../../decisions/H14.md): The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type0-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type0-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type0-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Erigon · 3.9.0-dev · d23467c5** (`3.9.0-dev-d23467c5`)

- [H14](../../decisions/H14.md): The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type0-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H14](../../decisions/H14.md): The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type0-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type0-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Nethermind · 2.3.0-preview · e2e011c8** (`2.3.0-preview+e2e011c8`)

- [H14](../../decisions/H14.md): The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type0-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H14](../../decisions/H14.md): The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type0-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x0000000000000000000000000000000000000000000000000000000000000000']

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H14](../../decisions/H14.md): The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type0-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H14](../../decisions/H14.md): The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type0-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

</details>

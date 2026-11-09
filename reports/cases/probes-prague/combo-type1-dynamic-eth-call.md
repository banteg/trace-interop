# Combo type1 dynamic eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | `0x00000000000000000000000000000000000000000000000000000000b2d05e00` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |

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

**Anvil · 1.9.1-nightly · 6165f031** (`anvil Version: 1.9.1-nightly+6165f031`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Anvil · 1.9.0 · 6056c584** (`anvil Version: 1.9.0+6056c584`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Erigon · 3.9.0-dev · cf91acee** (`3.9.0-dev-cf91acee`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Geth draft fork · 1.17.11-unstable · e487da1e** (`Geth/v1.17.11-unstable-e487da1e-2026-11-01/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Nethermind · 2.3.0-preview · 4079edfa** (`2.3.0-preview+4079edfa`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x0000000000000000000000000000000000000000000000000000000000000000']

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. eth_call parity control for combo-type1-dynamic. Observed: Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']

</details>

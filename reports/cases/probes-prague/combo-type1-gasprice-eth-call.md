# Combo type1 gasprice eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** The call runs with type 1, which does not change execution, at GASPRICE 2000000000, its legacy gasPrice serving as both fee caps.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |

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
      "gasPrice": "0x77359400",
      "type": "0x1"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · e15c2f1c** (`anvil Version: 1.8.4-nightly+e15c2f1c`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 2000000000, its legacy gasPrice serving as both fee caps. eth_call parity control for combo-type1-gasprice. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 2000000000, its legacy gasPrice serving as both fee caps. eth_call parity control for combo-type1-gasprice. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 2000000000, its legacy gasPrice serving as both fee caps. eth_call parity control for combo-type1-gasprice. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 2000000000, its legacy gasPrice serving as both fee caps. eth_call parity control for combo-type1-gasprice. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Erigon · 3.8.0-dev · 96188a47** (`3.8.0-dev-96188a47`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 2000000000, its legacy gasPrice serving as both fee caps. eth_call parity control for combo-type1-gasprice. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 2000000000, its legacy gasPrice serving as both fee caps. eth_call parity control for combo-type1-gasprice. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 2000000000, its legacy gasPrice serving as both fee caps. eth_call parity control for combo-type1-gasprice. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Nethermind · 2.2.0-preview · e8955c4c** (`2.2.0-preview+e8955c4c`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 2000000000, its legacy gasPrice serving as both fee caps. eth_call parity control for combo-type1-gasprice. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 2000000000, its legacy gasPrice serving as both fee caps. eth_call parity control for combo-type1-gasprice. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Reth · 2.7.0 · 42fa3c56** (`Reth Version: 2.7.0+42fa3c56`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 2000000000, its legacy gasPrice serving as both fee caps. eth_call parity control for combo-type1-gasprice. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): The call runs with type 1, which does not change execution, at GASPRICE 2000000000, its legacy gasPrice serving as both fee caps. eth_call parity control for combo-type1-gasprice. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

</details>

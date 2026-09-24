# Field gas omitted eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "input": "0x5a60005260206000f3"
    },
    "latest"
  ]
}
```

**Besu · 26.9-develop · cf89071f** (`besu/v26.9-develop-cf89071/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 01c118ee** (`3.8.0-dev-01c118ee`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · 0a663f3c** (`Geth/v1.17.7-unstable-0a663f3c-2026-09-24/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0-preview · 54b760cd** (`2.1.0-preview+54b760cd`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

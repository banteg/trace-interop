# Typed zero/eth

`eth_call` · fee-compat · [All reports](../../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../../clients/anvil_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../../clients/anvil_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../../clients/besu_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../../clients/besu_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../clients/erigon_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../../clients/erigon_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../../clients/go-ethereum_trace.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../clients/nethermind_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../../clients/nethermind_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../../clients/reth_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../../clients/reth_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x30d40",
      "maxFeePerGas": "0x0",
      "maxPriorityFeePerGas": "0x0",
      "value": "0x7"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.7-nightly · 716e795c** (`anvil Version: 1.8.7-nightly+716e795c`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.9.0-dev · 6955d198** (`3.9.0-dev-6955d198`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.11-unstable · 0f1fb2ae** (`Geth/v1.17.11-unstable-0f1fb2ae-2026-10-28/linux-amd64/go1.26.1`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.3.0-preview · fc9abf09** (`2.3.0-preview+fc9abf09`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

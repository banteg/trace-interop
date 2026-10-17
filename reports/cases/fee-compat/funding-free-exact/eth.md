# Funding free exact/eth

`eth_call` · fee-compat · [All reports](../../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../../clients/anvil_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-17/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/fee-compat/manifest.json) |
| [Anvil · 1.8.6-nightly · de005f70](../../../clients/anvil_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-17/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/fee-compat/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../../clients/besu_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-17/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/fee-compat/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../../clients/besu_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-17/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/fee-compat/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../clients/erigon_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-17/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/fee-compat/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../../clients/erigon_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-17/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../../clients/go-ethereum_trace.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-17/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../clients/nethermind_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-17/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../../clients/nethermind_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-17/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/fee-compat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-17/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/fee-compat/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../../clients/reth_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-17/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/fee-compat/manifest.json) |

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
      "gasPrice": "0x0",
      "value": "0xde0b6b3a7640000"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.6-nightly · de005f70** (`anvil Version: 1.8.6-nightly+de005f70`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · 0776d82f** (`besu/v26.10-develop-0776d82/linux-x86_64/openjdk-java-25`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 5b452f41** (`3.8.0-dev-5b452f41`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · 71db3b03** (`Geth/v1.17.7-unstable-71db3b03-2026-10-14/linux-amd64/go1.26.1`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · cd336c4c** (`2.2.0-preview+cd336c4c`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · ec3e7e42** (`Reth Version: 2.7.0+ec3e7e42`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

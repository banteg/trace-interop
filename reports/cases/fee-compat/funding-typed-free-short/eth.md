# Funding typed free short/eth

`eth_call` · fee-compat · [All reports](../../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../../clients/anvil_release.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-05/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/fee-compat/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../../clients/anvil_development.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-05/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/fee-compat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | RPC error `-32004` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-05/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/fee-compat/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../../clients/besu_development.md) | RPC error `-32004` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-05/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/fee-compat/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../clients/erigon_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-05/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/fee-compat/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-05/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-05/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/fee-compat/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../../clients/nethermind_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-05/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../../clients/nethermind_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-05/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/fee-compat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-05/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/fee-compat/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../../clients/reth_development.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-05/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/fee-compat/manifest.json) |

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
      "value": "0xde0b6b3a7640001"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · e15c2f1c** (`anvil Version: 1.8.4-nightly+e15c2f1c`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 96188a47** (`3.8.0-dev-96188a47`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · e8955c4c** (`2.2.0-preview+e8955c4c`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 42fa3c56** (`Reth Version: 2.7.0+42fa3c56`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

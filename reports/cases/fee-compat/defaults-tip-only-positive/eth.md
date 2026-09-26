# Defaults tip only positive/eth

`eth_call` · fee-compat · [All reports](../../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | RPC error `-32009` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-09-26/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/eval/fee-compat/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../../clients/besu_development.md) | RPC error `-32009` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-09-26/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/eval/fee-compat/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../clients/erigon_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-09-26/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/eval/fee-compat/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-09-26/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/eval/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-09-26/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/eval/fee-compat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-09-26/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/eval/fee-compat/manifest.json) |
| [Nethermind · 2.1.0-preview · b4211ad9](../../../clients/nethermind_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-09-26/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/eval/fee-compat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../clients/reth_release.md) | `0x000000000000000000000000000000000000000000000000000000002da282a900000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-09-26/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/eval/fee-compat/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../../clients/reth_development.md) | `0x000000000000000000000000000000000000000000000000000000002da282a900000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-09-26/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/eval/fee-compat/manifest.json) |

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
      "maxPriorityFeePerGas": "0x1",
      "value": "0x7"
    },
    "latest"
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · c8449896** (`Geth/v1.17.7-unstable-c8449896-2026-09-26/linux-amd64/go1.26.1`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0-preview · b4211ad9** (`2.1.0-preview+b4211ad9`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

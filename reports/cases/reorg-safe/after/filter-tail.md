# After/filter tail

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Every phase range has exactly the frozen canonical roots and block hashes; restoration returns the original inventory. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../../clients/besu_release.md) | 9 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-17/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/reorg-safe/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../../clients/besu_development.md) | 9 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-17/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/reorg-safe/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../clients/erigon_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-10-17/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-17/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-17/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-17/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-17/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-17/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-17/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-17/eval/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x28",
      "toBlock": "0x30"
    }
  ]
}
```

**Besu · 26.10-develop · 0776d82f** (`besu/v26.10-develop-0776d82/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 5b452f41** (`3.8.0-dev-5b452f41`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Scenario setup stopped: Invalid forkchoice state

**Geth draft fork · 1.17.7-unstable · 71db3b03** (`Geth/v1.17.7-unstable-71db3b03-2026-10-14/linux-amd64/go1.26.1`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · cd336c4c** (`2.2.0-preview+cd336c4c`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · ec3e7e42** (`Reth Version: 2.7.0+ec3e7e42`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

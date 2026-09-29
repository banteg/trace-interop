# After/filter tail

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Every phase range has exactly the frozen canonical roots and block hashes; restoration returns the original inventory. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | 9 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../../clients/besu_development.md) | 9 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../clients/erigon_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | 9 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |

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

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · a2a19253** (`3.8.0-dev-a2a19253`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Scenario setup stopped: Invalid forkchoice state

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Scenario setup stopped: Invalid forkchoice state

**Geth draft fork · 1.17.7-unstable · e26833e3** (`Geth/v1.17.7-unstable-e26833e3-2026-09-26/linux-amd64/go1.26.1`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · 287f54f0** (`2.2.0-preview+287f54f0`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `1`: 'transactionHash' is a required property
- Result shape at `1`: 'transactionPosition' is a required property
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

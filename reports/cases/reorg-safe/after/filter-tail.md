# After/filter tail

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Every phase range has exactly the frozen canonical roots and block hashes; restoration returns the original inventory. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | 9 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../../clients/besu_development.md) | 9 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../clients/erigon_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../../clients/nethermind_release.md) | 9 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |

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

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 5cb6c867** (`3.8.0-dev-5cb6c867`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Scenario setup stopped: Invalid forkchoice state

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Scenario setup stopped: Invalid forkchoice state

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · 6dff813b** (`2.2.0-preview+6dff813b`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `1`: 'transactionHash' is a required property
- Result shape at `1`: 'transactionPosition' is a required property
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Reth · 2.7.0 · 10bcf461** (`Reth Version: 2.7.0+10bcf461`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

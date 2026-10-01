# After/filter hash a

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** After the switch to branch B, A’s block 0x2d is noncanonical: its hash is an error (-32001 recommended), never B’s [] or records. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | 1 records | ⚠️ Differs | [Response](../../../../evidence/2026-10-01/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/reorg-safe/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../../clients/besu_development.md) | 1 records | ⚠️ Differs | [Response](../../../../evidence/2026-10-01/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/reorg-safe/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../clients/erigon_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-10-01/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-10-01/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-01/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-10-01/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-01/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-01/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-01/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xe6d9078b4964bc1b329fb12242254e21cf88ffa9a88058e515d6e79f7d8fce0d"
    }
  ]
}
```

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): After the switch to branch B, A’s block 0x2d is noncanonical: its hash is an error (-32001 recommended), never B’s [] or records. Accepted: answered another block, 1 record from block 0x30 (the head).

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): After the switch to branch B, A’s block 0x2d is noncanonical: its hash is an error (-32001 recommended), never B’s [] or records. Accepted: answered another block, 1 record from block 0x30 (the head).

**Erigon · 3.8.0-dev · 50e2cc4f** (`3.8.0-dev-50e2cc4f`)

- [H33](../../../decisions/H33.md): Assess this declared topic case. Scenario setup stopped: Invalid forkchoice state

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H33](../../../decisions/H33.md): Assess this declared topic case. Scenario setup stopped: Invalid forkchoice state

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H33](../../../decisions/H33.md): After the switch to branch B, A’s block 0x2d is noncanonical: its hash is an error (-32001 recommended), never B’s [] or records. Accepted: answered another block, 1 record from block 0x30 (the head).
- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property

</details>

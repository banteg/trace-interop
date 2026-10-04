# After/filter hash b

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** After the switch, B’s block 0x2d is canonical: its hash selects that block, which has no records, as the numeric range shows. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | 1 records | ⚠️ Differs | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../../clients/besu_development.md) | 1 records | ⚠️ Differs | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../clients/erigon_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../../clients/nethermind_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-04/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-04/eval/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xb75975dcf8dc29c9d8f63272511a20eb5c16c8466634e83f6b840d3baaa54110"
    }
  ]
}
```

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): After the switch, B’s block 0x2d is canonical: its hash selects that block, which has no records, as the numeric range shows. Answered another block: 1 record from block 0x30 (the head), where the numeric equivalent after/filter-tail has 1 record from block 0x2d.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): After the switch, B’s block 0x2d is canonical: its hash selects that block, which has no records, as the numeric range shows. Answered another block: 1 record from block 0x30 (the head), where the numeric equivalent after/filter-tail has 1 record from block 0x2d.

**Erigon · 3.8.0-dev · 5cb6c867** (`3.8.0-dev-5cb6c867`)

- [H33](../../../decisions/H33.md): Assess this declared topic case. Scenario setup stopped: Invalid forkchoice state

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H33](../../../decisions/H33.md): Assess this declared topic case. Scenario setup stopped: Invalid forkchoice state

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H33](../../../decisions/H33.md): After the switch, B’s block 0x2d is canonical: its hash selects that block, which has no records, as the numeric range shows. Answered another block: 1 record from block 0x30 (the head), where the numeric equivalent after/filter-tail has 1 record from block 0x2d.
- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property

**Reth · 2.7.0 · 10bcf461** (`Reth Version: 2.7.0+10bcf461`)

- [H33](../../../decisions/H33.md): After the switch, B’s block 0x2d is canonical: its hash selects that block, which has no records, as the numeric range shows. Rejected (-32602: Invalid params), where the numeric equivalent after/filter-tail has [].

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../../decisions/H33.md): After the switch, B’s block 0x2d is canonical: its hash selects that block, which has no records, as the numeric range shows. Rejected (-32602: Invalid params), where the numeric equivalent after/filter-tail has [].

</details>

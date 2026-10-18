# Before/filter hash a

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Before the switch, branch A’s block 0x2d is canonical: its hash selects A’s records, as the numeric range does. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../clients/erigon_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |

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

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H33](../../../decisions/H33.md): Assess this declared topic case. Scenario setup stopped: Invalid forkchoice state

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H33](../../../decisions/H33.md): Before the switch, branch A’s block 0x2d is canonical: its hash selects A’s records, as the numeric range does. Rejected (-32602: Invalid params), where the numeric equivalent before/filter-tail has 2 records from block 0x2d.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../../decisions/H33.md): Before the switch, branch A’s block 0x2d is canonical: its hash selects A’s records, as the numeric range does. Rejected (-32602: Invalid params), where the numeric equivalent before/filter-tail has 2 records from block 0x2d.

</details>

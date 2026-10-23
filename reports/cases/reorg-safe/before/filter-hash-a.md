# Before/filter hash a

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. Before the switch, branch A’s block 0x2d is canonical: its hash selects A’s records, as the numeric range does.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.1 · e83703cd](../../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |

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

**Reth · 2.8.0 · 53bf066f** (`Reth Version: 2.8.0+53bf066f`)

- [H33](../../../decisions/H33.md): Before the switch, branch A’s block 0x2d is canonical: its hash selects A’s records, as the numeric range does. Rejected (-32602: Invalid params), where the numeric equivalent before/filter-tail has 2 records from block 0x2d.

**Reth · 2.8.1 · d763342f** (`Reth Version: 2.8.1+d763342f`)

- [H33](../../../decisions/H33.md): Before the switch, branch A’s block 0x2d is canonical: its hash selects A’s records, as the numeric range does. Rejected (-32602: Invalid params), where the numeric equivalent before/filter-tail has 2 records from block 0x2d.

</details>

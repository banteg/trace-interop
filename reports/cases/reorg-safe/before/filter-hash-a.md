# Before/filter hash a

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. Before the switch, branch A’s block 0x2d is canonical: its hash selects A’s records, as the numeric range does.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.2 · d3e1aea7](../../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |

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

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H33](../../../decisions/H33.md): Before the switch, branch A’s block 0x2d is canonical: its hash selects A’s records, as the numeric range does. Rejected (-32602: Invalid params), where the numeric equivalent before/filter-tail has 2 records from block 0x2d.

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H33](../../../decisions/H33.md): Before the switch, branch A’s block 0x2d is canonical: its hash selects A’s records, as the numeric range does. Rejected (-32602: Invalid params), where the numeric equivalent before/filter-tail has 2 records from block 0x2d.

</details>

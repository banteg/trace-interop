# Restored/filter hash a

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. Once branch A is restored, the hash of its block 0x2d selects A’s records again.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.2 · 09b9e94d](../../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |

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

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H33](../../../decisions/H33.md): Once branch A is restored, the hash of its block 0x2d selects A’s records again. Rejected (-32602: Invalid params), where the numeric equivalent restored/filter-tail has 2 records from block 0x2d.

</details>

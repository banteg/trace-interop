# Restored/block tail

`trace_block` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-30/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/eval/reorg-safe/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-30/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/eval/reorg-safe/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../clients/erigon_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-30/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-30/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-30/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-30/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-30/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-30/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-30/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/eval/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0x2d"
  ]
}
```

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x0', 'input': '0x', 'to': '0x16c57edf7fa9d9525378b0b81bf8a3ced0620c1c', 'value': '0x1'}, 'blockHash': '0xe6d9078b4964bc1b329fb12242254e21cf88ffa9a88058e515d6e79f7d8fce0d', 'blockNumber': 45, 'result': {'g

</details>

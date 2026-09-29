# After/block tail

`trace_block` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../clients/erigon_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |

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

- Result shape at `/`: [{'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x0'}, 'blockHash': '0xb75975dcf8dc29c9d8f63272511a20eb5c16c8466634e83f6b840d3baaa54110', 'blockNumber': 45, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}] is not valid under any of the give

</details>

# After/block tail

`trace_block` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../clients/erigon_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |

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

</details>

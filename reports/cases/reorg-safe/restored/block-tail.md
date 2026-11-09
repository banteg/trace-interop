# Restored/block tail

`trace_block` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.0 · 0e595f9e](../../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |

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

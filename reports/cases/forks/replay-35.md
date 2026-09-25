# Replay 35

`trace_replayBlockTransactions` · forks · [All reports](../../README.md)

**What this checks:** Block replay has exactly one envelope per frozen transaction, with hashes in transaction order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x23",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

</details>

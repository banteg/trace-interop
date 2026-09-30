# Replay 52

`trace_replayBlockTransactions` · forks · [All reports](../../README.md)

**What this checks:** Block replay has exactly one envelope per frozen transaction, with hashes in transaction order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x34",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

</details>

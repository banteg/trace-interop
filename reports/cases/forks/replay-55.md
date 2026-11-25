# Replay 55

`trace_replayBlockTransactions` · forks · [All reports](../../README.md)

**What this checks:** Block replay has exactly one envelope per frozen transaction, with hashes in transaction order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x37",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

</details>

# Replay 59

`trace_replayBlockTransactions` · forks · [All reports](../../README.md)

**What this checks:** Block replay has exactly one envelope per frozen transaction, with hashes in transaction order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/forks/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x3b",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

</details>

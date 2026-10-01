# Filter 52

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** A single-block filter agrees with trace_block at the same fork.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x34",
      "toBlock": "0x34"
    }
  ]
}
```

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

</details>

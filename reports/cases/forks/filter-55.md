# Filter 55

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** A single-block filter agrees with trace_block at the same fork.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/forks/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 3904de43](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-27/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/forks/manifest.json) |
| [Nethermind · 2.1.0-preview · 5ece5fba](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-27/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/forks/manifest.json) |
| [Reth · 2.5.2 · 863f7055](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x37",
      "toBlock": "0x37"
    }
  ]
}
```

**Nethermind · 2.1.0-preview · 5ece5fba** (`2.1.0-preview+5ece5fba`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

</details>

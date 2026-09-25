# Filter 35

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** A single-block filter agrees with trace_block at the same fork.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x23",
      "toBlock": "0x23"
    }
  ]
}
```

**Erigon · 3.8.0-dev · f8cfe5a7** (`3.8.0-dev-f8cfe5a7`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Nethermind · 2.1.0-preview · ee1f57da** (`2.1.0-preview+ee1f57da`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

</details>

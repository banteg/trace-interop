# Filter 35

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** A single-block filter agrees with trace_block at the same fork.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |

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

**Erigon · 3.8.0-dev · 85e1ca92** (`3.8.0-dev-85e1ca92`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Nethermind · 2.2.0-preview · f69690c5** (`2.2.0-preview+f69690c5`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

</details>

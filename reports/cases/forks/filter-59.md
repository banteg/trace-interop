# Filter 59

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** A single-block filter agrees with trace_block at the same fork.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/forks/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/forks/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/forks/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/forks/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/forks/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x3b",
      "toBlock": "0x3b"
    }
  ]
}
```

**Nethermind · 2.1.0-unstable · 2a3b2531** (`2.1.0-unstable+2a3b2531`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

</details>

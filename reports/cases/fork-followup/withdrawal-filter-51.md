# Withdrawal filter 51

`trace_filter` · fork-followup · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x33",
      "toBlock": "0x33",
      "toAddress": [
        "0x717f8aa2b982bee0e29f573d31df288663e1ce16"
      ]
    }
  ]
}
```

</details>

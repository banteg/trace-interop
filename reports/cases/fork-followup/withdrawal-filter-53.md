# Withdrawal filter 53

`trace_filter` · fork-followup · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x35",
      "toBlock": "0x35",
      "toAddress": [
        "0x717f8aa2b982bee0e29f573d31df288663e1ce16"
      ]
    }
  ]
}
```

</details>

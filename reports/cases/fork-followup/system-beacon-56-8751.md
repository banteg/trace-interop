# System beacon 56 8751

`eth_getStorageAt` · fork-followup · [All reports](../../README.md)

**What this checks:** Historical beacon-root storage excludes the following block system update.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/fork-followup/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "eth_getStorageAt",
  "params": [
    "0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02",
    "0x222f",
    "0x38"
  ]
}
```

</details>

# System beacon 56 8751

`eth_getStorageAt` · fork-followup · [All reports](../../README.md)

**What this checks:** Historical beacon-root storage excludes the following block system update.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/fork-followup/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/fork-followup/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/fork-followup/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/fork-followup/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/fork-followup/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/fork-followup/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/fork-followup/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/fork-followup/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/fork-followup/manifest.json) |

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

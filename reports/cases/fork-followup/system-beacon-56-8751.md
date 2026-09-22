# System beacon 56 8751

`eth_getStorageAt` · fork-followup · [All reports](../../README.md)

**What this checks:** Historical beacon-root storage excludes the following block system update.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-geth-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-geth-fork-followup/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getStorageAt",
  "params": [
    "0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02",
    "0x222f",
    "0x38"
  ]
}
```

</details>

# After write revert read/storage

`eth_getStorageAt` · callmany-isolation · [All reports](../../../README.md)

**What this checks:** Canonical storage remains unchanged after the ordered multi-call simulation.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/manifest.json) |
| [Besu · 🛠️ Development](../../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/manifest.json) |
| [Erigon · 📦 Release](../../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/manifest.json) |
| [Erigon · 🛠️ Development](../../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-23/geth-contract-sync/geth-contract-callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-23/geth-contract-sync/geth-contract-callmany-isolation/manifest.json) |
| [Nethermind · 📦 Release](../../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/manifest.json) |
| [Nethermind · 🛠️ Development](../../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/manifest.json) |
| [Reth · 📦 Release](../../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/manifest.json) |
| [Reth · 🛠️ Development](../../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-2-native-isolation-verified/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getStorageAt",
  "params": [
    "0x0000000000000000000000000000000000001001",
    "0x0",
    "0x30"
  ]
}
```

</details>

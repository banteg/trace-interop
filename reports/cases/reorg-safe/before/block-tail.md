# Before/block tail

`trace_block` · reorg-safe · [All reports](../../../README.md)

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../../clients/besu_release.md) | 3 records | ⚪ Not assessed | [Response](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/manifest.json) |
| [Besu · 🛠️ Development](../../../clients/besu_development.md) | 3 records | ⚪ Not assessed | [Response](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/manifest.json) |
| [Erigon · 📦 Release](../../../clients/erigon_release.md) | 2 records | ⚪ Not assessed | [Response](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/manifest.json) |
| [Erigon · 🛠️ Development](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../../clients/go-ethereum_trace.md) | 2 records | ⚪ Not assessed | [Response](../../../../evidence/2026-09-23/geth-contract-sync/geth-contract-reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-23/geth-contract-sync/geth-contract-reorg-safe/manifest.json) |
| [Nethermind · 📦 Release](../../../clients/nethermind_release.md) | 3 records | ⚪ Not assessed; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/manifest.json) |
| [Nethermind · 🛠️ Development](../../../clients/nethermind_development.md) | 3 records | ⚪ Not assessed; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/manifest.json) |
| [Reth · 📦 Release](../../../clients/reth_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/manifest.json) |
| [Reth · 🛠️ Development](../../../clients/reth_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-23/harness-audit-native-reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "0x2d"
  ]
}
```

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

</details>

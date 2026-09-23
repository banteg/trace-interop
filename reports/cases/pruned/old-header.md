# Old header

`eth_getBlockByNumber` · pruned · [All reports](../../README.md)

**What this checks:** Retain independent reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · 📦 Release](../../clients/reth_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-pruned/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-pruned/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-pruned/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-pruned/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getBlockByNumber",
  "params": [
    "0x2",
    false
  ]
}
```

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H06](../../decisions/H06.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H06](../../decisions/H06.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

</details>

# Latest call

`trace_call` · pruned · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · 📦 Release](../../clients/reth_release.md) | 1 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-pruned/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-pruned/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 1 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-pruned/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-pruned/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "to": "0x0000000000000000000000000000000000001002"
    },
    [
      "trace"
    ],
    "0x30"
  ]
}
```

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H06](../../decisions/H06.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H06](../../decisions/H06.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

</details>

# Many number latest

`trace_callMany` · h30 · [All reports](../../README.md)

**What this checks:** trace_callMany accepts an omitted block and uses latest (NUMBER 48).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_callMany",
  "params": [
    [
      [
        {
          "data": "0x4360005260206000f3",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x77359400"
        },
        [
          "trace"
        ]
      ]
    ],
    "latest"
  ]
}
```

</details>

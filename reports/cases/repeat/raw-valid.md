# Raw valid

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/repeat/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/repeat/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/repeat/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/repeat/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/repeat/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/repeat/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/repeat/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/repeat/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b8185847735940082520894000000000000000000000000000000000000123401808718e5bb3abd10a0a0a8d391fb09e2f92ffc93fe7ac7b1eb7f1e24289f707eec0f34292c1713f795ffa0554e314f2ec6166290fc977d4bd4c86a9e0cadc2366f6139bd907d893bb4e237",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

</details>

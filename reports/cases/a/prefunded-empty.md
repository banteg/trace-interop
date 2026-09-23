# Prefunded empty

`trace_call` · a · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. An existing prefunded account does not acquire creation markers for empty code or zero nonce.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "to": "0x000000000000000000000000000000000000100b",
      "value": "0x1"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "0x30"
  ]
}
```

</details>

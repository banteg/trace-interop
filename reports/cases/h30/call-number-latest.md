# Call number latest

`trace_call` · h30 · [All reports](../../README.md)

**What this checks:** An omitted or explicit latest trace_call block uses the frozen head (NUMBER 48). Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-h30/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-h30/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x4360005260206000f3",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

</details>

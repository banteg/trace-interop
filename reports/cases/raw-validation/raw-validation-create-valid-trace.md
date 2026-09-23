# Raw validation create valid trace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. The valid signed control reports its expected execution success or halt in a root frame. Valid creation uses the address derived from the matching signed and state nonce.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf8600a842da282a9830186a08001893060005260206000f38718e5bb3abd109fa0371d5f6be359abfc8aa07862de5609e2374dea339665f9fcfe54ebfeef4e5d53a00de19f45781c0c3903dca51e8da7bf4ac28cc805e9a63e27c4bf1ef1d00f951a",
    [
      "trace"
    ]
  ]
}
```

</details>

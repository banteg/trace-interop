# Filter safe

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** The safe tag resolves to the fixture safe head, block 48.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "count": 3,
      "fromBlock": "safe",
      "toBlock": "safe"
    }
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

</details>

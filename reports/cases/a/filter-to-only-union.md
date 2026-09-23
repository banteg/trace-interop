# Filter to only union

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "mode": "union",
      "toAddress": [
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      ],
      "toBlock": "0x2"
    }
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 2 records from this client's block trace.

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 2 records from this client's block trace.

</details>

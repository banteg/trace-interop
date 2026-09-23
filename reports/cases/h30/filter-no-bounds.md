# Filter no bounds

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Omitting both range bounds selects latest only, as an explicit head-only query does.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "count": 3
    }
  ]
}
```

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H30](../../decisions/H30.md): Omitting both range bounds selects latest only, as an explicit head-only query does.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H30](../../decisions/H30.md): Omitting both range bounds selects latest only, as an explicit head-only query does.

**Geth draft fork · 🧪 Draft fork** (`Geth/v1.17.6-unstable-c36ee43e-2026-09-23/linux-amd64/go1.26.1`)

- [H30](../../decisions/H30.md): Omitting both range bounds selects latest only, as an explicit head-only query does.

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H30](../../decisions/H30.md): Omitting both range bounds selects latest only, as an explicit head-only query does.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H30](../../decisions/H30.md): Omitting both range bounds selects latest only, as an explicit head-only query does.

</details>

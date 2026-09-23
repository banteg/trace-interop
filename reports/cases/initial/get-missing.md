# Get missing

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** A missing transaction or tree path returns null. A missing selected frame is null, not an empty collection.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | `[]` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | `[]` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "0xffff"
    ]
  ]
}
```

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H06](../../decisions/H06.md): A missing transaction or tree path returns null.
- [H02](../../decisions/H02.md): A missing selected frame is null, not an empty collection.
- Result shape at `/`: [] is not valid under any of the given schemas

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H06](../../decisions/H06.md): A missing transaction or tree path returns null.
- [H02](../../decisions/H02.md): A missing selected frame is null, not an empty collection.
- Result shape at `/`: [] is not valid under any of the given schemas

</details>

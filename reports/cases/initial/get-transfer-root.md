# Get transfer root

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Return the transaction-tree record at [], or null if absent.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | `[]` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_get",
  "params": [
    "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    []
  ]
}
```

**Nethermind · 2.1.0-preview · ee1f57da** (`2.1.0-preview+ee1f57da`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.
- Result shape at `/`: [] is not valid under any of the given schemas

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.
- Result shape at `/`: [] is not valid under any of the given schemas

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.

</details>

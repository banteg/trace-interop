# Filter no bounds

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Omitting both range bounds selects latest only, as an explicit head-only query does.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/h30/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/h30/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/h30/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/h30/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/h30/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "count": 3
    }
  ]
}
```

**Erigon · 3.8.0-dev · 01c118ee** (`3.8.0-dev-01c118ee`)

- [H30](../../decisions/H30.md): Omitting both range bounds selects latest only, as an explicit head-only query does.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H30](../../decisions/H30.md): Omitting both range bounds selects latest only, as an explicit head-only query does.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H30](../../decisions/H30.md): Omitting both range bounds selects latest only, as an explicit head-only query does.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H30](../../decisions/H30.md): Omitting both range bounds selects latest only, as an explicit head-only query does.

</details>

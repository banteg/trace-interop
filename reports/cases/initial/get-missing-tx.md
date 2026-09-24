# Get missing tx

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Unknown transaction returns null, not an empty collection or RPC error. A missing selected frame is null, not an empty collection.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_get",
  "params": [
    "0xfefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefe",
    []
  ]
}
```

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.
- [H02](../../decisions/H02.md): A missing selected frame is null, not an empty collection.

**Nethermind · 2.1.0-preview · ce501a97** (`2.1.0-preview+ce501a97`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.
- [H02](../../decisions/H02.md): A missing selected frame is null, not an empty collection.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.
- [H02](../../decisions/H02.md): A missing selected frame is null, not an empty collection.

</details>

# Transaction missing

`trace_transaction` · initial · [All reports](../../README.md)

**What this checks:** Unknown transaction returns null, not an empty collection or RPC error.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_transaction",
  "params": [
    "0xfefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefe"
  ]
}
```

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.

**Nethermind · 2.1.0-unstable · 2a3b2531** (`2.1.0-unstable+2a3b2531`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.

</details>

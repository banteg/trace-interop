# Filter to 2 implicit from

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** An omitted fromBlock resolves to latest; an earlier explicit toBlock gives a range error, not a historical search.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "count": 3,
      "toBlock": "0x2"
    }
  ]
}
```

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H30](../../decisions/H30.md): An omitted fromBlock resolves to latest; an earlier explicit toBlock gives a range error, not a historical search.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H30](../../decisions/H30.md): An omitted fromBlock resolves to latest; an earlier explicit toBlock gives a range error, not a historical search.

**Geth draft fork · 1.17.7-unstable · fa8ecb92** (`Geth/v1.17.7-unstable-fa8ecb92-2026-09-24/linux-amd64/go1.26.1`)

- [H30](../../decisions/H30.md): An omitted fromBlock resolves to latest; an earlier explicit toBlock gives a range error, not a historical search.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H30](../../decisions/H30.md): An omitted fromBlock resolves to latest; an earlier explicit toBlock gives a range error, not a historical search.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H30](../../decisions/H30.md): An omitted fromBlock resolves to latest; an earlier explicit toBlock gives a range error, not a historical search.

</details>

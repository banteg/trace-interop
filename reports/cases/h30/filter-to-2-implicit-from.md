# Filter to 2 implicit from

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** An omitted fromBlock resolves to latest; an earlier explicit toBlock is a reversed range (-32602, as eth_getLogs), not a historical search.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "toBlock": "0x2",
      "count": 3
    }
  ]
}
```

**Erigon · 3.8.0-dev · f8cfe5a7** (`3.8.0-dev-f8cfe5a7`)

- [H30](../../decisions/H30.md): An omitted fromBlock resolves to latest; an earlier explicit toBlock is a reversed range (-32602, as eth_getLogs), not a historical search.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H30](../../decisions/H30.md): An omitted fromBlock resolves to latest; an earlier explicit toBlock is a reversed range (-32602, as eth_getLogs), not a historical search.

**Nethermind · 2.1.0-preview · ee1f57da** (`2.1.0-preview+ee1f57da`)

- [H30](../../decisions/H30.md): An omitted fromBlock resolves to latest; an earlier explicit toBlock is a reversed range (-32602, as eth_getLogs), not a historical search.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H30](../../decisions/H30.md): An omitted fromBlock resolves to latest; an earlier explicit toBlock is a reversed range (-32602, as eth_getLogs), not a historical search.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H30](../../decisions/H30.md): An omitted fromBlock resolves to latest; an earlier explicit toBlock is a reversed range (-32602, as eth_getLogs), not a historical search.

</details>

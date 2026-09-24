# Missing block filter

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32001` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | RPC error `-32001` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2f",
      "toBlock": "0xffff",
      "count": 1
    }
  ]
}
```

**Erigon · 3.8.0-dev · 01c118ee** (`3.8.0-dev-01c118ee`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

**Nethermind · 2.1.0-preview · 54b760cd** (`2.1.0-preview+54b760cd`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

</details>

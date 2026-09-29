# Missing block filter next

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/a/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/a/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/a/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32001` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/a/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | RPC error `-32001` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x30",
      "toBlock": "0x31",
      "count": 1
    }
  ]
}
```

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

**Erigon · 3.8.0-dev · a2a19253** (`3.8.0-dev-a2a19253`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

**Nethermind · 2.2.0-preview · 287f54f0** (`2.2.0-preview+287f54f0`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.

</details>

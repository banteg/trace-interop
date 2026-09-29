# Filter earliest

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** The earliest tag resolves like explicit block 0 on this fixture.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/h30/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/h30/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/h30/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "earliest",
      "toBlock": "0x2",
      "count": 3
    }
  ]
}
```

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H32](../../decisions/H32.md): The earliest tag resolves like explicit block 0 on this fixture.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H32](../../decisions/H32.md): The earliest tag resolves like explicit block 0 on this fixture.

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H32](../../decisions/H32.md): The earliest tag resolves like explicit block 0 on this fixture.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H32](../../decisions/H32.md): The earliest tag resolves like explicit block 0 on this fixture.

</details>

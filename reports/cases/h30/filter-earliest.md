# Filter earliest

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** The earliest tag resolves like explicit block 0 on this fixture.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |

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

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H32](../../decisions/H32.md): The earliest tag resolves like explicit block 0 on this fixture.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H32](../../decisions/H32.md): The earliest tag resolves like explicit block 0 on this fixture.

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H32](../../decisions/H32.md): The earliest tag resolves like explicit block 0 on this fixture.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H32](../../decisions/H32.md): The earliest tag resolves like explicit block 0 on this fixture.

</details>

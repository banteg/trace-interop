# Filter earliest

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** The earliest tag resolves like explicit block 0 on this fixture.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |

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

**Anvil · 1.8.7-nightly · 716e795c** (`anvil Version: 1.8.7-nightly+716e795c`)

- [H32](../../decisions/H32.md): The earliest tag resolves like explicit block 0 on this fixture.

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H32](../../decisions/H32.md): The earliest tag resolves like explicit block 0 on this fixture.

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H32](../../decisions/H32.md): The earliest tag resolves like explicit block 0 on this fixture.

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H32](../../decisions/H32.md): The earliest tag resolves like explicit block 0 on this fixture.

</details>

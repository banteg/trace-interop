# Filter past end page

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toBlock": "0x2",
      "after": 10000,
      "count": 1
    }
  ]
}
```

</details>

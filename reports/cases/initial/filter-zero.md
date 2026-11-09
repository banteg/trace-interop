# Filter zero

`trace_filter` · initial · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |

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
      "count": 0
    }
  ]
}
```

</details>

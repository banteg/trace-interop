# Filter zero

`trace_filter` · initial · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |

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

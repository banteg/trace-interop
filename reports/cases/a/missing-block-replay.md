# Missing block replay

`trace_replayBlockTransactions` · a · [All reports](../../README.md)

**What this checks:** An unknown selected block returns null or an error (-32001 recommended), never a successful collection.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayBlockTransactions",
  "params": [
    "0xffff",
    [
      "trace"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · df92604b** (`anvil Version: 1.8.4-nightly+df92604b`)

- [H06](../../decisions/H06.md): An unknown selected block returns null or an error (-32001 recommended), never a successful collection.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H06](../../decisions/H06.md): An unknown selected block returns null or an error (-32001 recommended), never a successful collection.

</details>

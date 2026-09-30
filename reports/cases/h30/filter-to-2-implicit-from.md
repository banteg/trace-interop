# Filter to 2 implicit from

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** An omitted fromBlock resolves to latest; an earlier explicit toBlock is a reversed range and is rejected (-32602 recommended, as eth_getLogs), not a historical search.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |

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

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H30](../../decisions/H30.md): An omitted fromBlock resolves to latest; an earlier explicit toBlock is a reversed range and is rejected (-32602 recommended, as eth_getLogs), not a historical search.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H30](../../decisions/H30.md): An omitted fromBlock resolves to latest; an earlier explicit toBlock is a reversed range and is rejected (-32602 recommended, as eth_getLogs), not a historical search.

</details>

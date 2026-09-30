# Filter blockhash empty

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "fromAddress": [
        "0x0000000000000000000000000000000000000000"
      ]
    }
  ]
}
```

**Anvil · 1.8.4-nightly · e3429853** (`anvil Version: 1.8.4-nightly+e3429853`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-empty has [].

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-empty has [].

**Nethermind · 2.2.0-preview · 79173d14** (`2.2.0-preview+79173d14`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-empty has [].

**Reth · 2.7.0 · 43a93dbc** (`Reth Version: 2.7.0+43a93dbc`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-empty has [].

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-empty has [].

</details>

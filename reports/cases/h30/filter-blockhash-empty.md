# Filter blockhash empty

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |

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

**Anvil · 1.9.1-nightly · 6165f031** (`anvil Version: 1.9.1-nightly+6165f031`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-empty has [].

**Anvil · 1.9.0 · 6056c584** (`anvil Version: 1.9.0+6056c584`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-empty has [].

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-empty has [].

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-empty has [].

</details>

# Filter blockhash empty

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/h30/manifest.json) |
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
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "fromAddress": [
        "0x0000000000000000000000000000000000000000"
      ]
    }
  ]
}
```

**Anvil · 1.8.7-nightly · 716e795c** (`anvil Version: 1.8.7-nightly+716e795c`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-empty has [].

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-empty has [].

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-empty has [].

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-empty has [].

</details>

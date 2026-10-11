# Filter blockhash empty

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-11/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/h30/manifest.json) |
| [Anvil · 1.8.6-nightly · 32624734](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-11/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-11/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/h30/manifest.json) |
| [Besu · 26.10-develop · d05d8e74](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-11/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/h30/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-11/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 1d3ebbf2](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-11/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-11/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/h30/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-11/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 204457ad](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-11/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-11/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 1a4dbbe1](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-11/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/h30/manifest.json) |

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

**Anvil · 1.8.6-nightly · 32624734** (`anvil Version: 1.8.6-nightly+32624734`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-empty has [].

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-empty has [].

**Reth · 2.7.0 · 1a4dbbe1** (`Reth Version: 2.7.0+1a4dbbe1`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-empty has [].

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-empty has [].

</details>

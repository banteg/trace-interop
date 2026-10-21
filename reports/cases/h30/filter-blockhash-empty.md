# Filter blockhash empty

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |

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

**Anvil · 1.8.6-nightly · 9089a6bf** (`anvil Version: 1.8.6-nightly+9089a6bf`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-empty has [].

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-empty has [].

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-empty has [].

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H33](../../decisions/H33.md): A known block without matching records returns [], not an error, as the numeric single-block filter does; alone it cannot show which block was selected. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-empty has [].

</details>

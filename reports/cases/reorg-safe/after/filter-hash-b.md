# After/filter hash b

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. After the switch, B’s block 0x2d is canonical: its hash selects that block, which has no records, as the numeric range shows.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.0 · 0e595f9e](../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xb75975dcf8dc29c9d8f63272511a20eb5c16c8466634e83f6b840d3baaa54110"
    }
  ]
}
```

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H33](../../../decisions/H33.md): After the switch, B’s block 0x2d is canonical: its hash selects that block, which has no records, as the numeric range shows. Rejected (-32602: Invalid params), where the numeric equivalent after/filter-tail has [].

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H33](../../../decisions/H33.md): After the switch, B’s block 0x2d is canonical: its hash selects that block, which has no records, as the numeric range shows. Rejected (-32602: Invalid params), where the numeric equivalent after/filter-tail has [].

</details>

# After/filter hash b

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. After the switch, B’s block 0x2d is canonical: its hash selects that block, which has no records, as the numeric range shows.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |

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

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H33](../../../decisions/H33.md): After the switch, B’s block 0x2d is canonical: its hash selects that block, which has no records, as the numeric range shows. Rejected (-32602: Invalid params), where the numeric equivalent after/filter-tail has [].

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H33](../../../decisions/H33.md): After the switch, B’s block 0x2d is canonical: its hash selects that block, which has no records, as the numeric range shows. Rejected (-32602: Invalid params), where the numeric equivalent after/filter-tail has [].

</details>

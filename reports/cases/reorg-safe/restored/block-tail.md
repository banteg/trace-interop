# Restored/block tail

`trace_block` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-26/anvil/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/anvil/reorg-safe/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-26/anvil/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/anvil/reorg-safe/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../clients/erigon_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-26/anvil/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/anvil/reorg-safe/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-26/anvil/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/anvil/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-26/anvil/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/anvil/reorg-safe/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-26/anvil/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/anvil/reorg-safe/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-26/anvil/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/anvil/reorg-safe/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../clients/reth_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-26/anvil/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/anvil/reorg-safe/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-26/anvil/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-26/anvil/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0x2d"
  ]
}
```

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

</details>

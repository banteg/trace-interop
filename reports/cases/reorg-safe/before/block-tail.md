# Before/block tail

`trace_block` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/reorg-safe/manifest.json) |

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

**Nethermind · 2.1.0-preview · ce501a97** (`2.1.0-preview+ce501a97`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

</details>

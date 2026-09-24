# Before/block tail

`trace_block` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/h17-retest/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h17-retest/reorg-safe/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/h17-retest/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h17-retest/reorg-safe/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/h17-retest/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h17-retest/reorg-safe/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-24/h17-retest/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h17-retest/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/h17-retest/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h17-retest/reorg-safe/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/h17-retest/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h17-retest/reorg-safe/manifest.json) |
| [Nethermind · 2.1.0-unstable · 9d6e8b8d](../../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/h17-retest/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h17-retest/reorg-safe/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../clients/reth_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-24/h17-retest/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h17-retest/reorg-safe/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/h17-retest/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h17-retest/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "0x2d"
  ]
}
```

**Nethermind · 2.1.0-unstable · 9d6e8b8d** (`2.1.0-unstable+9d6e8b8d`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

</details>

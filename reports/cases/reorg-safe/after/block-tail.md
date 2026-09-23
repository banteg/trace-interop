# After/block tail

`trace_block` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Besu · 🛠️ Development](../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Erigon · 📦 Release](../../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Erigon · 🛠️ Development](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Nethermind · 📦 Release](../../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Nethermind · 🛠️ Development](../../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Reth · 📦 Release](../../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Reth · 🛠️ Development](../../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |

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

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property

</details>

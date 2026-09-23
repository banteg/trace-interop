# Withdrawal filter 51

`trace_filter` · fork-followup · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x33",
      "toAddress": [
        "0x717f8aa2b982bee0e29f573d31df288663e1ce16"
      ],
      "toBlock": "0x33"
    }
  ]
}
```

</details>

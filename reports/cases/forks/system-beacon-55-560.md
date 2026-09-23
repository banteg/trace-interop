# System beacon 55 560

`eth_getStorageAt` · forks · [All reports](../../README.md)

**What this checks:** Historical beacon-root storage excludes the following block system update.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getStorageAt",
  "params": [
    "0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02",
    "0x230",
    "0x37"
  ]
}
```

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H28](../../decisions/H28.md): Historical beacon-root storage excludes the following block system update.

</details>

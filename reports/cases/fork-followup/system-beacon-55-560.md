# System beacon 55 560

`eth_getStorageAt` · fork-followup · [All reports](../../README.md)

**What this checks:** Historical beacon-root storage excludes the following block system update. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |

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

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H28](../../decisions/H28.md): Historical beacon-root storage excludes the following block system update.
- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 🧪 Draft fork** (`Geth/v1.17.6-unstable-c36ee43e-2026-09-23/linux-amd64/go1.26.1`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

# System beacon 56 560

`eth_getStorageAt` · fork-followup · [All reports](../../README.md)

**What this checks:** Historical beacon-root storage excludes the following block system update. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/fork-followup/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/fork-followup/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/fork-followup/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/fork-followup/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/fork-followup/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/fork-followup/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/fork-followup/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/fork-followup/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/fork-followup/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "eth_getStorageAt",
  "params": [
    "0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02",
    "0x230",
    "0x38"
  ]
}
```

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · bb5c4682** (`Geth/v1.17.7-unstable-bb5c4682-2026-09-24/linux-amd64/go1.26.1`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0-preview · ce501a97** (`2.1.0-preview+ce501a97`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

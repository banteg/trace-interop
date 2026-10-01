# System beacon 56 560

`eth_getStorageAt` · fork-followup · [All reports](../../README.md)

**What this checks:** Historical beacon-root storage excludes the following block system update. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/fork-followup/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/fork-followup/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/fork-followup/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/fork-followup/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/fork-followup/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/fork-followup/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/fork-followup/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/fork-followup/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000230` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/fork-followup/manifest.json) |

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

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 50e2cc4f** (`3.8.0-dev-50e2cc4f`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · 759efed7** (`2.2.0-preview+759efed7`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 5b686303** (`Reth Version: 2.7.0+5b686303`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

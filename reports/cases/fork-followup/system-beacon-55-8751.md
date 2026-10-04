# System beacon 55 8751

`eth_getStorageAt` · fork-followup · [All reports](../../README.md)

**What this checks:** Historical beacon-root storage excludes the following block system update. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/fork-followup/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/fork-followup/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/fork-followup/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/fork-followup/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/fork-followup/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/fork-followup/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/fork-followup/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/fork-followup/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/fork-followup/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "eth_getStorageAt",
  "params": [
    "0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02",
    "0x222f",
    "0x37"
  ]
}
```

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 5cb6c867** (`3.8.0-dev-5cb6c867`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · 6dff813b** (`2.2.0-preview+6dff813b`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 10bcf461** (`Reth Version: 2.7.0+10bcf461`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H28](../../decisions/H28.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

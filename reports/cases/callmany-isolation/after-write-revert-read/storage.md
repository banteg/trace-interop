# After write revert read/storage

`eth_getStorageAt` · callmany-isolation · [All reports](../../../README.md)

**What this checks:** Canonical storage remains unchanged after the ordered multi-call simulation. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../../clients/anvil_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-05/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/callmany-isolation/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../../clients/anvil_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-05/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/callmany-isolation/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-05/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/callmany-isolation/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-05/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/callmany-isolation/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-05/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/callmany-isolation/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-05/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/callmany-isolation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-05/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/callmany-isolation/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-05/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/callmany-isolation/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-05/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/callmany-isolation/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-05/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/callmany-isolation/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-05/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-05/eval/callmany-isolation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getStorageAt",
  "params": [
    "0x0000000000000000000000000000000000001001",
    "0x0",
    "0x30"
  ]
}
```

**Anvil · 1.8.4-nightly · e15c2f1c** (`anvil Version: 1.8.4-nightly+e15c2f1c`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 96188a47** (`3.8.0-dev-96188a47`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · e8955c4c** (`2.2.0-preview+e8955c4c`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 42fa3c56** (`Reth Version: 2.7.0+42fa3c56`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

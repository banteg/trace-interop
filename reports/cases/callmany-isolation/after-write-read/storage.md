# After write read/storage

`eth_getStorageAt` · callmany-isolation · [All reports](../../../README.md)

**What this checks:** Canonical storage remains unchanged after the ordered multi-call simulation. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../../clients/anvil_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/callmany-isolation/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../../clients/anvil_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/callmany-isolation/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/callmany-isolation/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/callmany-isolation/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/callmany-isolation/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/callmany-isolation/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/callmany-isolation/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/callmany-isolation/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/callmany-isolation/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/callmany-isolation/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/callmany-isolation/manifest.json) |

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

**Anvil · 1.10.1-nightly · 50d75f19** (`anvil Version: 1.10.1-nightly+50d75f19`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.10.0 · 083e2299** (`anvil Version: 1.10.0+083e2299`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.9.0-dev · e91aca7f** (`3.9.0-dev-e91aca7f`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.2 · 8a3f3b2c** (`3.8.2-8a3f3b2c`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.11-unstable · edbd5f17** (`Geth/v1.17.11-unstable-edbd5f17-2026-11-18/linux-amd64/go1.26.1`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.4.0-preview · e2f069a6** (`2.4.0-preview+e2f069a6`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H16](../../../decisions/H16.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

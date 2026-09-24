# Withdrawal block 52

`eth_getBlockByNumber` · fork-followup · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-24/h17-retest/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/fork-followup/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-24/h17-retest/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/fork-followup/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-24/h17-retest/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/fork-followup/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-24/h17-retest/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/fork-followup/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-24/h17-retest/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/fork-followup/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-24/h17-retest/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/fork-followup/manifest.json) |
| [Nethermind · 2.1.0-unstable · 9d6e8b8d](../../clients/nethermind_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-24/h17-retest/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/fork-followup/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-24/h17-retest/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/fork-followup/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-24/h17-retest/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/fork-followup/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getBlockByNumber",
  "params": [
    "0x34",
    true
  ]
}
```

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H05](../../decisions/H05.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H05](../../decisions/H05.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · fa8ecb92** (`Geth/v1.17.7-unstable-fa8ecb92-2026-09-24/linux-amd64/go1.26.1`)

- [H05](../../decisions/H05.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0-unstable · 9d6e8b8d** (`2.1.0-unstable+9d6e8b8d`)

- [H05](../../decisions/H05.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H05](../../decisions/H05.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H05](../../decisions/H05.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H05](../../decisions/H05.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

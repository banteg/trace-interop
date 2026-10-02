# Typed tip equals cap/eth

`eth_call` · fee-compat · [All reports](../../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../../clients/anvil_release.md) | `0x000000000000000000000000000000000000000000000000000000002da282a800000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-02/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/fee-compat/manifest.json) |
| [Anvil · 1.8.4-nightly · 328811cb](../../../clients/anvil_development.md) | `0x000000000000000000000000000000000000000000000000000000002da282a800000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-02/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/fee-compat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | `0x000000000000000000000000000000000000000000000000000000002da282a800000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-02/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/fee-compat/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../../clients/besu_development.md) | `0x000000000000000000000000000000000000000000000000000000002da282a800000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-02/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/fee-compat/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../clients/erigon_release.md) | `0x000000000000000000000000000000000000000000000000000000002da282a800000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-02/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/fee-compat/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../../clients/erigon_development.md) | `0x000000000000000000000000000000000000000000000000000000002da282a800000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-02/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../../clients/go-ethereum_trace.md) | `0x000000000000000000000000000000000000000000000000000000002da282a800000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-02/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/fee-compat/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../../clients/nethermind_release.md) | `0x000000000000000000000000000000000000000000000000000000002da282a800000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-02/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../../clients/nethermind_development.md) | `0x000000000000000000000000000000000000000000000000000000002da282a800000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-02/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/fee-compat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | `0x000000000000000000000000000000000000000000000000000000002da282a800000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-02/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/fee-compat/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../../clients/reth_development.md) | `0x000000000000000000000000000000000000000000000000000000002da282a800000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-02/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/fee-compat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x30d40",
      "maxFeePerGas": "0x2da282a8",
      "maxPriorityFeePerGas": "0x2da282a8",
      "value": "0x7"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · 328811cb** (`anvil Version: 1.8.4-nightly+328811cb`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 6da806cb** (`3.8.0-dev-6da806cb`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · 3370d566** (`2.2.0-preview+3370d566`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 078d0262** (`Reth Version: 2.7.0+078d0262`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

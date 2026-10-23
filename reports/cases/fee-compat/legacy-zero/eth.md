# Legacy zero/eth

`eth_call` · fee-compat · [All reports](../../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../../clients/anvil_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-23/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/fee-compat/manifest.json) |
| [Anvil · 1.8.7-nightly · 4e8874b2](../../../clients/anvil_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-23/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/fee-compat/manifest.json) |
| [Besu · 26.10.1 · e83703cd](../../../clients/besu_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-23/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/fee-compat/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../../clients/besu_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-23/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/fee-compat/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../../clients/erigon_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-23/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/fee-compat/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../../clients/erigon_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-23/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../../clients/go-ethereum_trace.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-23/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../../clients/nethermind_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-23/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/fee-compat/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../../clients/nethermind_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-23/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/fee-compat/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../../clients/reth_release.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-23/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/fee-compat/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../../clients/reth_development.md) | `0x000000000000000000000000000000000000000000000000000000000000000000000000000000` | 🔎 Control / not applicable | [Response](../../../../evidence/2026-10-23/eval/fee-compat/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/fee-compat/manifest.json) |

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
      "gasPrice": "0x0",
      "value": "0x7"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.7-nightly · 4e8874b2** (`anvil Version: 1.8.7-nightly+4e8874b2`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · 781a7e1d** (`besu/v26.10-develop-781a7e1/linux-x86_64/openjdk-java-25`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.9.0-dev · 598ba625** (`3.9.0-dev-598ba625`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.3.0-preview · 7192e7f3** (`2.3.0-preview+7192e7f3`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.1 · c4f1015b** (`2.2.1+c4f1015b`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.8.0 · 53bf066f** (`Reth Version: 2.8.0+53bf066f`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.8.1 · d763342f** (`Reth Version: 2.8.1+d763342f`)

- [H15](../../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

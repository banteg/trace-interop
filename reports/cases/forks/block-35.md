# Block 35

`trace_block` · forks · [All reports](../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0x23"
  ]
}
```

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.9.0-dev · e91aca7f** (`3.9.0-dev-e91aca7f`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.2 · 8a3f3b2c** (`3.8.2-8a3f3b2c`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.11-unstable · edbd5f17** (`Geth/v1.17.11-unstable-edbd5f17-2026-11-18/linux-amd64/go1.26.1`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.4.0-preview · e2f069a6** (`2.4.0-preview+e2f069a6`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress []: error None, result null.
- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `2`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x1c9f78d2893e4000'}, 'blockHash': '0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f', 'blockNumber': 35, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under an
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'uncle', 'value': '0x18493fba64ef0000'}, 'blockHash': '0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f', 'blockNumber': 35, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under an
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

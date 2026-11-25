# After/filter tail

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. Every phase range has exactly the frozen canonical roots and block hashes; restoration returns the original inventory. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.2 · 09b9e94d](../../../clients/besu_release.md) | 9 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../../clients/besu_development.md) | 9 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x28",
      "toBlock": "0x30"
    }
  ]
}
```

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.9.0-dev · e91aca7f** (`3.9.0-dev-e91aca7f`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.2 · 8a3f3b2c** (`3.8.2-8a3f3b2c`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.11-unstable · edbd5f17** (`Geth/v1.17.11-unstable-edbd5f17-2026-11-18/linux-amd64/go1.26.1`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.4.0-preview · e2f069a6** (`2.4.0-preview+e2f069a6`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

# Empty sender priced/call/none

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. Unrequested trace is an empty array. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Reject this independently invalid fee/funding request before execution.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../../../clients/besu_release.md) | RPC error `-32004` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../../../clients/besu_development.md) | RPC error `-32004` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../../../clients/erigon_release.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../../../clients/erigon_development.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../../../clients/go-ethereum_trace.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../../clients/nethermind_release.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../../../clients/nethermind_development.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../../../clients/reth_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../../../clients/reth_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
      "from": "0x0000000000000000000000000000000000004444",
      "gas": "0x30d40",
      "gasPrice": "0x2da282a9",
      "value": "0x0"
    },
    [],
    "latest"
  ]
}
```

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. An unfunded sender cannot afford positive gas fees.

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. An unfunded sender cannot afford positive gas fees.

</details>

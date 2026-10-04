# Typed revert/many/statediff vmtrace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../../clients/erigon_release.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../../../clients/reth_development.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_callMany",
  "params": [
    [
      [
        {
          "data": "0x602a60005260206000fd",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "maxFeePerGas": "0x5b450550",
          "maxPriorityFeePerGas": "0x1",
          "value": "0x7"
        },
        [
          "stateDiff",
          "vmTrace"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999959302437446844; miner 0->53156; burn 40697562500000.

**Reth · 2.7.0 · 10bcf461** (`Reth Version: 2.7.0+10bcf461`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999959302437446844; miner 0->53156; burn 40697562500000.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999959302437446844; miner 0->53156; burn 40697562500000.

</details>

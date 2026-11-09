# Typed refund/many/statediff

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../../../clients/reth_release.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../../../clients/reth_development.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |

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
          "data": "0x6001600055600060005560006000f3",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "maxFeePerGas": "0x5b450550",
          "maxPriorityFeePerGas": "0x1",
          "value": "0x7"
        },
        [
          "stateDiff"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999953817499939673; miner 0->60320; burn 46182500000000.

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999953817499939673; miner 0->60320; burn 46182500000000.

</details>

# Legacy at base/trace/statediff

`trace_call` · fee-compat · [All reports](../../../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../../../clients/anvil_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../../../clients/anvil_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../../clients/nethermind_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../../../clients/reth_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../../../clients/reth_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-29/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-compat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x30d40",
      "gasPrice": "0x2da282a8",
      "value": "0x7"
    },
    [
      "stateDiff"
    ],
    "latest"
  ]
}
```

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999924491765624993; miner 0->0; burn 75508234375000.

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999924491765624993; miner 0->0; burn 75508234375000.

</details>

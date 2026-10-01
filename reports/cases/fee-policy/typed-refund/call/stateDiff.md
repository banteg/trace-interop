# Typed refund/call/statediff

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../../../clients/anvil_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../../../clients/anvil_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../../../clients/besu_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../../../clients/erigon_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../../../clients/go-ethereum_trace.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | 0 call frames; output `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../../../clients/nethermind_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../../../clients/reth_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
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
    ],
    "latest"
  ]
}
```

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999953817499939673; miner 0->60320; burn 46182500000000.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H08](../../../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x; independently charged gas 60320.
- Result shape at `output`: None is not of type 'string'
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0xeba0'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x00de48310d77a4d56aa400248b0b1613508f5b73': {'balance': {'+': '0x7'}, 'code': '=', 'nonce': {'+': '0x1'}, 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'

**Reth · 2.7.0 · 5b686303** (`Reth Version: 2.7.0+5b686303`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999953817499939673; miner 0->60320; burn 46182500000000.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999953817499939673; miner 0->60320; burn 46182500000000.

</details>

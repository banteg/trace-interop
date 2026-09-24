# Typed out of gas/call/statediff

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Failed frames have an error string; an exceptional halt omits result or sets it to null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../../clients/besu_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../../../clients/besu_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../../../clients/erigon_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../../../clients/go-ethereum_trace.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | 0 call frames; output `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../../../clients/nethermind_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../../clients/reth_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x63ffffffff51",
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

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H08](../../../../decisions/H08.md): Unrequested trace is an empty array.
- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H08](../../../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x; independently charged gas 200000.
- Result shape at `output`: None is not of type 'string'
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0x30d40'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0xde0b6b3a7640000', 'to': '0xde02b6f7625c0c0'}}, 'code': '=', 'nonce': {'*': {'from': '0xa', 'to'

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.

</details>

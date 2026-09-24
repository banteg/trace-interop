# Legacy revert/many/statediff

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../../clients/erigon_release.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../../../clients/erigon_development.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../../clients/reth_development.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |

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
          "gasPrice": "0x2da282a9",
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

**Erigon · 3.8.0-dev · 01c118ee** (`3.8.0-dev-01c118ee`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999959302437446844; miner 0->53156; burn 40697562500000.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999959302437446844; miner 0->53156; burn 40697562500000.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H16](../../../../decisions/H16.md): Return one execution envelope per input call, in order.
- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000000000002a; independently charged gas 53156.
- Result shape at `0/output`: None is not of type 'string'
- Result shape at `0/stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0xcfa4'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0xde0b6b3a7640000', 'to': '0xde091b003a1a4bc'}}, 'code': '=', 'nonce': {'*': {'from': '0xa', 'to':

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999959302437446844; miner 0->53156; burn 40697562500000.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999959302437446844; miner 0->53156; burn 40697562500000.

</details>

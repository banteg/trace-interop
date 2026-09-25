# Typed refund/many/trace statediff

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../../../clients/erigon_development.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../../../clients/reth_development.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |

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
          "trace",
          "stateDiff"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23d82', 'init': '0x6001600055600060005560006000f3', 'value': '0x7'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x', 'gasUsed': '0x56ca'}, 'subtraces': 0, 'traceAddress': [], 'type': 'create

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23d82', 'init': '0x6001600055600060005560006000f3', 'value': '0x7'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x', 'gasUsed': '0x56ca'}, 'subtraces': 0, 'traceAddress': [], 'type': 'create

**Erigon · 3.8.0-dev · f8cfe5a7** (`3.8.0-dev-f8cfe5a7`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999953817499939673; miner 0->60320; burn 46182500000000.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999953817499939673; miner 0->60320; burn 46182500000000.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `0/stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0xeba0'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x00de48310d77a4d56aa400248b0b1613508f5b73': {'balance': {'+': '0x7'}, 'code': '=', 'nonce': {'+': '0x1'}, 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999953817499939673; miner 0->60320; burn 46182500000000.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999953817499939673; miner 0->60320; burn 46182500000000.

</details>

# Legacy out of gas then observe/many/trace statediff vmtrace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Failed frames have an error string; an exceptional halt omits result or sets it to null. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 1: distinguish admission from the known execution success/failure. Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../../../clients/besu_development.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../../clients/erigon_release.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-10-04/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-policy/manifest.json) |

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
          "data": "0x63ffffffff51",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "gasPrice": "0x2da282a9",
          "value": "0x7"
        },
        [
          "trace",
          "stateDiff",
          "vmTrace"
        ]
      ],
      [
        {
          "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "gasPrice": "0x2da282a9",
          "value": "0x7"
        },
        [
          "trace",
          "stateDiff",
          "vmTrace"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `0/vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any
- Result shape at `1/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23c1c', 'init': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'value': '0x7'}, 'result': {'address': '0xe69a847cd5bc0c9480ada0b339d7f0a8cac2b667', 'code': '0x000000000000000000000000000000000000

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `0/vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any
- Result shape at `1/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23c1c', 'init': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'value': '0x7'}, 'result': {'address': '0xe69a847cd5bc0c9480ada0b339d7f0a8cac2b667', 'code': '0x000000000000000000000000000000000000

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.
- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000ddfa02b44e781790000000000000000000000000000000000000000000000000000000000030d40; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999846874999800000->999771366765326370; miner 200000->298623; burn 75508234375000.

**Reth · 2.7.0 · 10bcf461** (`Reth Version: 2.7.0+10bcf461`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.
- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000ddfa02b44e781790000000000000000000000000000000000000000000000000000000000030d40; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999846874999800000->999771366765326370; miner 200000->298623; burn 75508234375000.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.
- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000ddfa02b44e781790000000000000000000000000000000000000000000000000000000000030d40; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999846874999800000->999771366765326370; miner 200000->298623; burn 75508234375000.

</details>

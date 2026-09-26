# Mixed typed priced free priced/many/trace statediff

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 1: distinguish admission from the known execution success/failure. Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Call 2: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 2: distinguish admission from the known execution success/failure. Call 2: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Return one complete JSON-RPC response; never wrap an error envelope as a successful result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../../../clients/anvil_release.md) | 3 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../../../clients/anvil_development.md) | 3 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../../../clients/besu_development.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | 3 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../../../clients/erigon_development.md) | 3 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../../../clients/nethermind_development.md) | 3 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 3 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../../../clients/reth_development.md) | 3 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |

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
          "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
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
      ],
      [
        {
          "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "maxFeePerGas": "0x0",
          "maxPriorityFeePerGas": "0x0",
          "value": "0x7"
        },
        [
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
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

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0720705e5af5b000000000000000000000000000000000000000000000000000000000001813f; independently charged gas 98623.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0720705e5af5b000000000000000000000000000000000000000000000000000000000001813f; independently charged gas 98623.

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H16](../../../../decisions/H16.md): Return one execution envelope per input call, in order.
- [H15](../../../../decisions/H15.md): Execute each valid simulation and return one envelope per call.
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H16](../../../../decisions/H16.md): Return one execution envelope per input call, in order.
- [H15](../../../../decisions/H15.md): Execute each valid simulation and return one envelope per call.
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7625c0b90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999924491765526370; miner 0->98623; burn 75508234375000.
- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0720705e5af5b000000000000000000000000000000000000000000000000000000000001813f; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999924491765526370->999924491765526363; miner 98623->98623; burn 0.
- [H15](../../../../decisions/H15.md): Call 2: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000ddfe6c2d4a77014000000000000000000000000000000000000000000000000000000000001813f; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 2: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999924491765526363->999848983531052733; miner 98623->197246; burn 75508234375000.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7625c0b90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999924491765526370; miner 0->98623; burn 75508234375000.
- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0720705e5af5b000000000000000000000000000000000000000000000000000000000001813f; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999924491765526370->999924491765526363; miner 98623->98623; burn 0.
- [H15](../../../../decisions/H15.md): Call 2: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000ddfe6c2d4a77014000000000000000000000000000000000000000000000000000000000001813f; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 2: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999924491765526363->999848983531052733; miner 98623->197246; burn 75508234375000.

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0720705e5af5b000000000000000000000000000000000000000000000000000000000001813f; independently charged gas 98623.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0720705e5af5b000000000000000000000000000000000000000000000000000000000001813f; independently charged gas 98623.
- Result shape at `0/stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0x1813f'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x00de48310d77a4d56aa400248b0b1613508f5b73': {'balance': {'+': '0x7'}, 'code': {'+': '0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7625c0b90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999924491765526370; miner 0->98623; burn 75508234375000.
- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0720705e5af5b000000000000000000000000000000000000000000000000000000000001813f; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999924491765526370->999924491765526363; miner 98623->98623; burn 0.
- [H15](../../../../decisions/H15.md): Call 2: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000ddfe6c2d4a77014000000000000000000000000000000000000000000000000000000000001813f; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 2: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999924491765526363->999848983531052733; miner 98623->197246; burn 75508234375000.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7625c0b90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999924491765526370; miner 0->98623; burn 75508234375000.
- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0720705e5af5b000000000000000000000000000000000000000000000000000000000001813f; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999924491765526370->999924491765526363; miner 98623->98623; burn 0.
- [H15](../../../../decisions/H15.md): Call 2: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000ddfe6c2d4a77014000000000000000000000000000000000000000000000000000000000001813f; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 2: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999924491765526363->999848983531052733; miner 98623->197246; burn 75508234375000.

</details>

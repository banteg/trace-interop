# Mixed legacy free priced free/many/trace statediff vmtrace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Call 1: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Call 1: distinguish admission from the known execution success/failure. Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Call 2: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Call 2: distinguish admission from the known execution success/failure. Call 2: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../../../clients/besu_release.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Besu · 🛠️ Development](../../../../clients/besu_development.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Erigon · 📦 Release](../../../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Erigon · 🛠️ Development](../../../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Nethermind · 📦 Release](../../../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Nethermind · 🛠️ Development](../../../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Reth · 📦 Release](../../../../clients/reth_release.md) | 3 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Reth · 🛠️ Development](../../../../clients/reth_development.md) | 3 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |

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
          "gasPrice": "0x0",
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
      ],
      [
        {
          "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "gasPrice": "0x0",
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

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H16](../../../../decisions/H16.md): Return one execution envelope per input call, in order.
- [H15](../../../../decisions/H15.md): Execute each valid simulation and return one envelope per call.
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H16](../../../../decisions/H16.md): Return one execution envelope per input call, in order.
- [H15](../../../../decisions/H15.md): Execute each valid simulation and return one envelope per call.
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H15](../../../../decisions/H15.md): Execute each valid simulation and return one envelope per call.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H15](../../../../decisions/H15.md): Execute each valid simulation and return one envelope per call.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- Result shape at `0/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0000000000000000000000000000000000000000000000000000000000000000'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push':
- Result shape at `1/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x000000000000000000000000000000000000000000000000000000002da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push':
- Result shape at `2/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0000000000000000000000000000000000000000000000000000000000000000'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push':

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- Result shape at `0/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0000000000000000000000000000000000000000000000000000000000000000'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push':
- Result shape at `1/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x000000000000000000000000000000000000000000000000000000002da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push':
- Result shape at `2/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0000000000000000000000000000000000000000000000000000000000000000'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push':

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H15](../../../../decisions/H15.md): Call 0: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0b6b3a763fff90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7625c0b20000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999999999999999993->999924491765526363; miner 0->98623; burn 75508234375000.
- [H15](../../../../decisions/H15.md): Call 2: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0720705e5af54000000000000000000000000000000000000000000000000000000000001813f; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 2: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999924491765526363->999924491765526356; miner 98623->98623; burn 0.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Call 0: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0b6b3a763fff90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7625c0b20000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999999999999999993->999924491765526363; miner 0->98623; burn 75508234375000.
- [H15](../../../../decisions/H15.md): Call 2: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0720705e5af54000000000000000000000000000000000000000000000000000000000001813f; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 2: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999924491765526363->999924491765526356; miner 98623->98623; burn 0.

</details>

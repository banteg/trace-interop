# Typed out of gas then observe/many/trace vmtrace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Failed frames have an error string and an explicit object or null result. Execute each valid simulation and return one envelope per call. Call 0: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure. Call 1: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Call 1: distinguish admission from the known execution success/failure.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../../../clients/besu_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Besu · 🛠️ Development](../../../../clients/besu_development.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Erigon · 📦 Release](../../../../clients/erigon_release.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Erigon · 🛠️ Development](../../../../clients/erigon_development.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Nethermind · 📦 Release](../../../../clients/nethermind_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Nethermind · 🛠️ Development](../../../../clients/nethermind_development.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Reth · 📦 Release](../../../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Reth · 🛠️ Development](../../../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |

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
          "maxFeePerGas": "0x5b450550",
          "maxPriorityFeePerGas": "0x1",
          "value": "0x7"
        },
        [
          "trace",
          "vmTrace"
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
          "vmTrace"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H09](../../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `0/vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `0/vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H15](../../../../decisions/H15.md): Call 1: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000ddfa02b44e781790000000000000000000000000000000000000000000000000000000000030d40; independently charged gas 98623.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H15](../../../../decisions/H15.md): Call 1: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000ddfa02b44e781790000000000000000000000000000000000000000000000000000000000030d40; independently charged gas 98623.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `0/trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `1/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x000000000000000000000000000000000000000000000000000000002da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push':

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H09](../../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `0/trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `1/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x000000000000000000000000000000000000000000000000000000002da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push':

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H15](../../../../decisions/H15.md): Call 1: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000ddfa02b44e781790000000000000000000000000000000000000000000000000000000000030d40; independently charged gas 98623.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Call 1: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000ddfa02b44e781790000000000000000000000000000000000000000000000000000000000030d40; independently charged gas 98623.

</details>

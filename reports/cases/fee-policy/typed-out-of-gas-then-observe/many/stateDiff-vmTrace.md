# Typed out of gas then observe/many/statediff vmtrace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.7-nightly · 4e8874b2](../../../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Besu · 26.10.1 · e83703cd](../../../../clients/besu_release.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../../../clients/besu_development.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |

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
          "stateDiff",
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
          "stateDiff",
          "vmTrace"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Besu · 26.10-develop · 781a7e1d** (`besu/v26.10-develop-781a7e1/linux-x86_64/openjdk-java-25`)

- Result shape at `0/vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any
- Result shape at `1/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x2da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub':

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- Result shape at `0/vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any
- Result shape at `1/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x2da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub':

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- Result shape at `0/vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'idx': '0-0', 'op': 'PUSH4', 'pc': 0, 'sub': None}, {'cost': 35184775266310, 'ex': None, 'idx': '0-1', 'op': 'MLOAD', 'pc': 5, 'sub': None}]} is not valid under any of the given
- Result shape at `1/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x2da282a9'], 'store': None, 'used': 146458}, 'idx': '1-0', 'op': 'GASPRICE', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None,

**Nethermind · 2.2.1 · c4f1015b** (`2.2.1+c4f1015b`)

- Result shape at `0/vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 146899, 'ex': None, 'pc': 5, 'sub': None}]} is not valid under any of the given schemas
- Result shape at `1/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x2da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub':

**Reth · 2.8.0 · 53bf066f** (`Reth Version: 2.8.0+53bf066f`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.
- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000ddfa02b44e781790000000000000000000000000000000000000000000000000000000000030d40; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999846874999800000->999771366765326370; miner 200000->298623; burn 75508234375000.

**Reth · 2.8.1 · d763342f** (`Reth Version: 2.8.1+d763342f`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.
- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000ddfa02b44e781790000000000000000000000000000000000000000000000000000000000030d40; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999846874999800000->999771366765326370; miner 200000->298623; burn 75508234375000.

</details>

# Legacy revert then observe/many/trace statediff vmtrace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 1: distinguish admission from the known execution success/failure. Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../../../clients/besu_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../../../clients/besu_development.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |

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

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H09](../../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0/trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dae', 'init': '0x602a60005260206000fd', 'value': '0x7'}, 'error': 'Reverted', 'revertReason': '0x000000000000000000000000000000000000000000000000000000000000002a', 'subtraces': 0, 'traceAddress'
- Result shape at `0/vmTrace`: {'code': '0x602a60005260206000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 146859}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146856}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x0000000000
- Result shape at `1/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x2da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub':

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H09](../../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0/trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dae', 'init': '0x602a60005260206000fd', 'value': '0x7'}, 'error': 'Reverted', 'revertReason': '0x000000000000000000000000000000000000000000000000000000000000002a', 'subtraces': 0, 'traceAddress'
- Result shape at `0/vmTrace`: {'code': '0x602a60005260206000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 146859}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146856}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x0000000000
- Result shape at `1/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x2da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub':

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- Result shape at `0/vmTrace`: {'code': '0x602a60005260206000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 146859}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146856}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x0000000000
- Result shape at `1/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x2da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub':

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999959302437446844; miner 0->53156; burn 40697562500000.
- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0066bd2636575000000000000000000000000000000000000000000000000000000000000cfa4; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999959302437446844->999883794202973214; miner 53156->151779; burn 75508234375000.

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999959302437446844; miner 0->53156; burn 40697562500000.
- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0066bd2636575000000000000000000000000000000000000000000000000000000000000cfa4; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 1: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 999959302437446844->999883794202973214; miner 53156->151779; burn 75508234375000.

</details>

# Defaults cap only zero/many/statediff vmtrace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../../clients/erigon_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |

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
          "maxFeePerGas": "0x0",
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

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- Result shape at `0/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub': None},

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- Result shape at `0/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub': None},

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- Result shape at `0/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146458}, 'idx': '0-0', 'op': 'GASPRICE', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used':

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0b6b3a763fff90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.
- Result shape at `0/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x2da282a8'], 'store': None, 'used': 146458}, 'idx': '0-0', 'op': 'GASPRICE', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None,

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- Result shape at `0/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub': None},

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- Result shape at `0/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub': None},

</details>

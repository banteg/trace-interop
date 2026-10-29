# Defaults omitted/many/trace statediff vmtrace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |

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

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23c1c', 'init': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'value': '0x7'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x000000000000000000000000000000000000
- Result shape at `0/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub': None},

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23c1c', 'init': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'value': '0x7'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x000000000000000000000000000000000000
- Result shape at `0/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub': None},

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- Result shape at `0/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146458}, 'idx': '0-0', 'op': 'GASPRICE', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used':

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- Result shape at `0/vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub': None},

</details>

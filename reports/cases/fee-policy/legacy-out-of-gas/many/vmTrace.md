# Legacy out of gas/many/vmtrace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Besu · 🛠️ Development](../../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Erigon · 📦 Release](../../../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Erigon · 🛠️ Development](../../../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Nethermind · 📦 Release](../../../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Nethermind · 🛠️ Development](../../../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Reth · 📦 Release](../../../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Reth · 🛠️ Development](../../../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |

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
          "vmTrace"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- Result shape at `0/vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- Result shape at `0/vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any

</details>

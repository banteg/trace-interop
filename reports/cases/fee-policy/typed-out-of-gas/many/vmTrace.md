# Typed out of gas/many/vmtrace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |

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
          "vmTrace"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- Result shape at `0/vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- Result shape at `0/vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- Result shape at `0/vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 146899, 'ex': None, 'pc': 5, 'sub': None}]} is not valid under any of the given schemas

</details>

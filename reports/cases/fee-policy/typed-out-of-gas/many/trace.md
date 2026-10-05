# Typed out of gas/many/trace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Failed frames have an error string; an exceptional halt omits result or sets it to null. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |

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
          "trace"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

</details>

# Legacy out of gas/many/trace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Failed frames have an error string; an exceptional halt carries result null. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../../../clients/besu_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../../../clients/besu_development.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../../clients/nethermind_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../../../clients/nethermind_development.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
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
          "data": "0x63ffffffff51",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "gasPrice": "0x2da282a9",
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

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H09](../../../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress []: error 'Out of gas', result null.
- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H09](../../../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress []: error 'Out of gas', result null.
- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H09](../../../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress []: error 'Out of gas', result null.
- Result shape at `0/trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H09](../../../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress []: error 'Out of gas', result null.
- Result shape at `0/trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

</details>

# Legacy revert/call/trace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../../../clients/besu_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../../../clients/besu_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x602a60005260206000fd",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x30d40",
      "gasPrice": "0x2da282a9",
      "value": "0x7"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H10](../../../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H09](../../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dae', 'init': '0x602a60005260206000fd', 'value': '0x7'}, 'error': 'Reverted', 'revertReason': '0x000000000000000000000000000000000000000000000000000000000000002a', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is n

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H10](../../../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H09](../../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dae', 'init': '0x602a60005260206000fd', 'value': '0x7'}, 'error': 'Reverted', 'revertReason': '0x000000000000000000000000000000000000000000000000000000000000002a', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is n

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H09](../../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result {"address": "0x00de48310d77a4d56aa400248b0b1613508f5b73", "code": "0x000000000000000000000000000000000000000000000000000000000000002a", "gasUsed": "0x12"}.
- Result shape at `trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dae', 'init': '0x602a60005260206000fd', 'value': '0x7'}, 'error': 'Reverted', 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H09](../../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result {"address": "0x00de48310d77a4d56aa400248b0b1613508f5b73", "code": "0x000000000000000000000000000000000000000000000000000000000000002a", "gasUsed": "0x12"}.
- Result shape at `trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dae', 'init': '0x602a60005260206000fd', 'value': '0x7'}, 'error': 'Reverted', 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000

</details>

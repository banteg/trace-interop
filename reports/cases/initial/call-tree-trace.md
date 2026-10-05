# Call tree trace

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 9 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 9 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "gas": "0x927c0",
      "gasPrice": "0x0",
      "data": "0x"
    },
    [
      "trace"
    ],
    "0x30"
  ]
}
```

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Successful creation uses address, code and gasUsed.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `trace/7`: {'action': {'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0xe5f841427f4e0c33bb76fd34499298a93916ba51', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceAddress': [6], 'type': 'creat

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H09](../../decisions/H09.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H09](../../decisions/H09.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres

</details>

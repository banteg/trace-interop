# Replay 51

`trace_replayBlockTransactions` · forks · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Reward and SELFDESTRUCT records carry result null. Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. An account created and destroyed within the transaction is absent at both endpoints and has no account diff.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x33",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `1/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000
- Result shape at `2/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `2/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under an
- Result shape at `2/trace/7`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70d', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0x302cb90c0d0edb96d0f45cc53a6e286ca192c872', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceA

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `1/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000
- Result shape at `2/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `2/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under an
- Result shape at `2/trace/7`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70d', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0x302cb90c0d0edb96d0f45cc53a6e286ca192c872', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceA

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [3]: error 'Mutable Call In Static Context', result null.
- Result shape at `2/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Mutable Call In Static Context', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not vali

</details>

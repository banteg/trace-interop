# Call tree trace priced

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 9 call frames; nonempty output | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 9 call frames; nonempty output | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 9 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 9 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 9 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/geth-e29edff-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-initial/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 9 call frames; nonempty output | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 9 call frames; nonempty output | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 9 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 9 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
    },
    [
      "trace"
    ],
    "0x30"
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Successful creation uses address, code and gasUsed.
- [H09](../../decisions/H09.md): Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under an
- Result shape at `trace/7`: {'action': {'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0xe5f841427f4e0c33bb76fd34499298a93916ba51', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceAddress': [6], 'type': 'creat

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Successful creation uses address, code and gasUsed.
- [H09](../../decisions/H09.md): Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under an
- Result shape at `trace/7`: {'action': {'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0xe5f841427f4e0c33bb76fd34499298a93916ba51', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceAddress': [6], 'type': 'creat

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../decisions/H09.md): Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H09](../../decisions/H09.md): Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a

</details>

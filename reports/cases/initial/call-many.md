# Call many

`trace_callMany` · initial · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Failed frames have an error string and an explicit object or null result. Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks. The declared state-diff fixture returns the requested account changes. Return one complete JSON-RPC response; never wrap an error envelope as a successful result. The declared failing execution contains its failed frame. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-initial/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |

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
          "data": "0x",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x0",
          "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
        },
        [
          "trace"
        ]
      ],
      [
        {
          "data": "0x",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x0",
          "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
        },
        [
          "trace"
        ]
      ]
    ],
    "0x30"
  ]
}
```

**Geth draft fork · 🧪 Draft fork** (`Geth/v1.17.6-unstable-c36ee43e-2026-09-23/linux-amd64/go1.26.1`)

- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order.
- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
- [H09](../../decisions/H09.md): The declared failing execution contains its failed frame. No failed frame was returned for this failure-bearing fixture.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order.
- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
- [H09](../../decisions/H09.md): The declared failing execution contains its failed frame. No failed frame was returned for this failure-bearing fixture.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order.
- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
- [H09](../../decisions/H09.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order.
- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
- [H09](../../decisions/H09.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- Result shape at `0/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `0/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a
- Result shape at `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- Result shape at `0/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `0/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a
- Result shape at `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.

</details>

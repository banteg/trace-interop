# Replay 60

`trace_replayBlockTransactions` · forks · [All reports](../../README.md)

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 5 records | Not assessed; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 5 records | Not assessed; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 5 records | Not assessed | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 5 records | Not assessed | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 5 records | Not assessed | [Response](../../../evidence/2026-09-21/geth-e29edff-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-forks/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 5 records | Not assessed; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 5 records | Not assessed; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 5 records | Not assessed | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 5 records | Not assessed | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x3c",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- Result shape at `4/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- Result shape at `4/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- Result shape at `4/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given s

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- Result shape at `4/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given s

</details>

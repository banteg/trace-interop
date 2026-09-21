# Filter page 0

`trace_filter` · a · [All reports](../../README.md)

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | Setup incomplete; not assessed | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Besu · Release](../../clients/besu_release.md) | 4 records | Not assessed; result shape differs | [Response](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a-besu-retry/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 4 records | Not assessed; result shape differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 4 records | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 4 records | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 4 records | Not assessed | [Response](../../../evidence/2026-09-21/geth-e29edff-a/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-a/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 4 records | Not assessed; result shape differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 4 records | Not assessed; result shape differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 4 records | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 4 records | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "after": 0,
      "count": 4,
      "fromBlock": "0x2",
      "toBlock": "0x2"
    }
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a9

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a9

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a9

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a9

</details>

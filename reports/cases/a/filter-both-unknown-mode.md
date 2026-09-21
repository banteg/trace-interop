# Filter both unknown mode

`trace_filter` · a · [All reports](../../README.md)

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | Setup incomplete; not assessed | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Besu · Release](../../clients/besu_release.md) | RPC error `-32602` | Not assessed | [Response](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a-besu-retry/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | RPC error `-32602` | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 6 records | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 6 records | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | RPC error `-32602` | Not assessed | [Response](../../../evidence/2026-09-21/geth-e29edff-a/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-a/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 1 records | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 1 records | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | RPC error `-32602` | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | RPC error `-32602` | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromAddress": [
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f"
      ],
      "fromBlock": "0x2",
      "mode": "garbage",
      "toAddress": [
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      ],
      "toBlock": "0x2"
    }
  ]
}
```

</details>

# Call unknown mode

`trace_call` · a · [All reports](../../README.md)

**What this checks:** Malformed input returns invalid params (-32602).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | Setup incomplete; not assessed | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Besu · Release](../../clients/besu_release.md) | RPC error `-32602` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a-besu-retry/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | RPC error `-32602` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | RPC error `-32602` | Checked cases agree | [Response](../../../evidence/2026-09-21/geth-e29edff-a/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-a/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | RPC error `-32602` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | RPC error `-32602` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | RPC error `-32602` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | RPC error `-32602` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |

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
      "to": "0x0000000000000000000000000000000000001002"
    },
    [
      "garbage"
    ],
    "0x30"
  ]
}
```

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 'garbage' is not one of ['trace', 'stateDiff', 'vmTrace']

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 'garbage' is not one of ['trace', 'stateDiff', 'vmTrace']

</details>

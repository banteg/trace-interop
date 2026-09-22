# Missing block call

`trace_call` · a · [All reports](../../README.md)

**What this checks:** An unknown selected block or range endpoint returns Resource not found (-32001).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | Setup incomplete; not assessed | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Besu · Release](../../clients/besu_release.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a-besu-retry/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/geth-e29edff-a/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-a/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | RPC error `-32001` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | RPC error `-32001` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |

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
      "trace"
    ],
    "0xffff"
  ]
}
```

**Geth draft fork · Draft fork** (`Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1`)

- [H06](../../decisions/H06.md): An unknown selected block or range endpoint returns Resource not found (-32001).

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): An unknown selected block or range endpoint returns Resource not found (-32001).

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H06](../../decisions/H06.md): An unknown selected block or range endpoint returns Resource not found (-32001).

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H06](../../decisions/H06.md): An unknown selected block or range endpoint returns Resource not found (-32001).

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H06](../../decisions/H06.md): An unknown selected block or range endpoint returns Resource not found (-32001).

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H06](../../decisions/H06.md): An unknown selected block or range endpoint returns Resource not found (-32001).

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): An unknown selected block or range endpoint returns Resource not found (-32001).

</details>

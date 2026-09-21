# Replay missing

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** Unknown transaction returns null, not an empty collection or RPC error. trace_replayTransaction

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | Method unavailable `-32601` | Method unavailable | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | Method unavailable `-32601` | Method unavailable | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | `null` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | `null` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | `null` | Checked cases agree | [Response](../../../evidence/2026-09-21/geth-e29edff-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-initial/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | RPC error `-32001` | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | RPC error `-32001` | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0xfefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefe",
    [
      "trace"
    ]
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.

</details>

# Get transfer root

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Return one object whose traceAddress equals [].

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | One frame, path `[]` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | One frame, path `[]` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | One frame, path `[]` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | One frame, path `[]` | Checked cases agree | [Response](../../../evidence/2026-09-23/geth-40eecf3-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-40eecf3-initial/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | `[]` | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | `[]` | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | `null` | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | `null` | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_get",
  "params": [
    "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    []
  ]
}
```

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H02](../../decisions/H02.md): Return one object whose traceAddress equals []. Observed NoneType.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H02](../../decisions/H02.md): Return one object whose traceAddress equals []. Observed list.
- Result shape at `/`: [] is not valid under any of the given schemas

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H02](../../decisions/H02.md): Return one object whose traceAddress equals []. Observed list.
- Result shape at `/`: [] is not valid under any of the given schemas

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H02](../../decisions/H02.md): Return one object whose traceAddress equals []. Observed NoneType.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H02](../../decisions/H02.md): Return one object whose traceAddress equals []. Observed NoneType.

</details>

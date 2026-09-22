# Filter to only intersection

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Malformed input returns invalid params (-32602). The pinned draft rejected every mode value; the revised H03 recommendation accepts recognized modes.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | Setup incomplete; not assessed | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Besu · Release](../../clients/besu_release.md) | RPC error `-32602` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a-besu-retry/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | RPC error `-32602` | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | `[]` | Differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | `[]` | Differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | RPC error `-32602` | Checked cases agree | [Response](../../../evidence/2026-09-21/geth-e29edff-a/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-a/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 2 records | Differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 2 records | Differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 2 records | Differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 2 records | Differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "mode": "intersection",
      "toAddress": [
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      ],
      "toBlock": "0x2"
    }
  ]
}
```

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). Additional properties are not allowed ('mode' was unexpected)
- [H03](../../decisions/H03.md): The pinned draft rejected every mode value; the revised H03 recommendation accepts recognized modes.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). Additional properties are not allowed ('mode' was unexpected)
- [H03](../../decisions/H03.md): The pinned draft rejected every mode value; the revised H03 recommendation accepts recognized modes.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). Additional properties are not allowed ('mode' was unexpected)
- [H03](../../decisions/H03.md): The pinned draft rejected every mode value; the revised H03 recommendation accepts recognized modes.

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). Additional properties are not allowed ('mode' was unexpected)
- [H03](../../decisions/H03.md): The pinned draft rejected every mode value; the revised H03 recommendation accepts recognized modes.

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). Additional properties are not allowed ('mode' was unexpected)
- [H03](../../decisions/H03.md): The pinned draft rejected every mode value; the revised H03 recommendation accepts recognized modes.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). Additional properties are not allowed ('mode' was unexpected)
- [H03](../../decisions/H03.md): The pinned draft rejected every mode value; the revised H03 recommendation accepts recognized modes.

</details>

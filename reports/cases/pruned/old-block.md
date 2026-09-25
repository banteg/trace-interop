# Old block

`trace_block` · pruned · [All reports](../../README.md)

**What this checks:** Unavailable historical state uses the proposed pruned-history error (4444).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/pruned/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/pruned/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/pruned/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/pruned/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0x2"
  ]
}
```

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H06](../../decisions/H06.md): Unavailable historical state uses the proposed pruned-history error (4444).

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H06](../../decisions/H06.md): Unavailable historical state uses the proposed pruned-history error (4444).

</details>

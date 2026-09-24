# Old transaction

`trace_transaction` · pruned · [All reports](../../README.md)

**What this checks:** Unavailable historical state uses the proposed pruned-history error (4444).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/pruned/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/pruned/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/pruned/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/pruned/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_transaction",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738"
  ]
}
```

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H06](../../decisions/H06.md): Unavailable historical state uses the proposed pruned-history error (4444).

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H06](../../decisions/H06.md): Unavailable historical state uses the proposed pruned-history error (4444).

</details>

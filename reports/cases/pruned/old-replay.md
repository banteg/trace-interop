# Old replay

`trace_replayTransaction` · pruned · [All reports](../../README.md)

**What this checks:** Unavailable historical state uses the proposed pruned-history error (4444).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/pruned/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/pruned/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/pruned/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/pruned/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayTransaction",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H06](../../decisions/H06.md): Unavailable historical state uses the proposed pruned-history error (4444).

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H06](../../decisions/H06.md): Unavailable historical state uses the proposed pruned-history error (4444).

</details>

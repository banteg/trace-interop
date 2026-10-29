# Old replay

`trace_replayTransaction` · pruned · [All reports](../../README.md)

**What this checks:** Unavailable historical state returns an error (4444, pruned history, recommended), never a result or null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/pruned/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/pruned/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/pruned/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/pruned/manifest.json) |

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

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H06](../../decisions/H06.md): Unavailable historical state returns an error (4444, pruned history, recommended), never a result or null. Code -32603 (4444 recommended).

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H06](../../decisions/H06.md): Unavailable historical state returns an error (4444, pruned history, recommended), never a result or null. Code -32603 (4444 recommended).

</details>

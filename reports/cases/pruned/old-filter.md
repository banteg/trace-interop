# Old filter

`trace_filter` · pruned · [All reports](../../README.md)

**What this checks:** Unavailable historical state returns an error (4444, pruned history, recommended), never a result or null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/pruned/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/pruned/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/pruned/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/pruned/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toBlock": "0x3"
    }
  ]
}
```

**Reth · 2.7.0 · 43a93dbc** (`Reth Version: 2.7.0+43a93dbc`)

- [H06](../../decisions/H06.md): Unavailable historical state returns an error (4444, pruned history, recommended), never a result or null. Code -32603 (4444 recommended).

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H06](../../decisions/H06.md): Unavailable historical state returns an error (4444, pruned history, recommended), never a result or null. Code -32603 (4444 recommended).

</details>

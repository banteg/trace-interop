# Old block

`trace_block` · pruned · [All reports](../../README.md)

**What this checks:** Unavailable historical state returns an error (4444, pruned history, recommended), never a result or null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/pruned/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/pruned/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/pruned/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/pruned/manifest.json) |

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

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H06](../../decisions/H06.md): Unavailable historical state returns an error (4444, pruned history, recommended), never a result or null. Code -32603 (4444 recommended).

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H06](../../decisions/H06.md): Unavailable historical state returns an error (4444, pruned history, recommended), never a result or null. Code -32603 (4444 recommended).

</details>

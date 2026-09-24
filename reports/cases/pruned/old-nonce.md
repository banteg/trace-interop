# Old nonce

`eth_getTransactionCount` · pruned · [All reports](../../README.md)

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32603` | ⚪ Not assessed | [Response](../../../evidence/2026-09-24/h15-call-compat/pruned/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/pruned/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | RPC error `4444` | ⚪ Not assessed | [Response](../../../evidence/2026-09-24/h15-call-compat/pruned/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/pruned/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "eth_getTransactionCount",
  "params": [
    "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
    "0x2"
  ]
}
```

</details>

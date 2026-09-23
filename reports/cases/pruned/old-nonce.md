# Old nonce

`eth_getTransactionCount` · pruned · [All reports](../../README.md)

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · 📦 Release](../../clients/reth_release.md) | RPC error `-32603` | ⚪ Not assessed | [Response](../../../evidence/2026-09-24/coverage-matrix/pruned/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/pruned/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | RPC error `-32603` | ⚪ Not assessed | [Response](../../../evidence/2026-09-24/coverage-matrix/pruned/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/pruned/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getTransactionCount",
  "params": [
    "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
    "0x2"
  ]
}
```

</details>

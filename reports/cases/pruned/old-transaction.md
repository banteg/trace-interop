# Old transaction

`trace_transaction` · pruned · [All reports](../../README.md)

**What this checks:** Unavailable historical state uses the proposed pruned-history error (4444).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · Release](../../clients/reth_release.md) | RPC error `-32603` | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-pruned/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-pruned/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | RPC error `-32603` | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-pruned/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-pruned/manifest.json) |

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

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H06](../../decisions/H06.md): Unavailable historical state uses the proposed pruned-history error (4444).

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H06](../../decisions/H06.md): Unavailable historical state uses the proposed pruned-history error (4444).

</details>

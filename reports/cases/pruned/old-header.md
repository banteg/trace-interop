# Old header

`eth_getBlockByNumber` · pruned · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/refresh/pruned/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/pruned/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/refresh/pruned/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/pruned/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "eth_getBlockByNumber",
  "params": [
    "0x2",
    false
  ]
}
```

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H06](../../decisions/H06.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H06](../../decisions/H06.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

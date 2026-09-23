# Old header

`eth_getBlockByNumber` · pruned · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · 📦 Release](../../clients/reth_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-24/coverage-matrix/pruned/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/pruned/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-24/coverage-matrix/pruned/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/pruned/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getBlockByNumber",
  "params": [
    "0x2",
    false
  ]
}
```

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H06](../../decisions/H06.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H06](../../decisions/H06.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

# Old header

`eth_getBlockByNumber` · pruned · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/pruned/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/pruned/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/pruned/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/pruned/manifest.json) |

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

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H06](../../decisions/H06.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H06](../../decisions/H06.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

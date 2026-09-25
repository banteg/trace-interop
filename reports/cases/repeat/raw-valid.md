# Raw valid

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/repeat/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/repeat/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/repeat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/repeat/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/repeat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/repeat/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b8185847735940082520894000000000000000000000000000000000000123401808718e5bb3abd10a0a0a8d391fb09e2f92ffc93fe7ac7b1eb7f1e24289f707eec0f34292c1713f795ffa0554e314f2ec6166290fc977d4bd4c86a9e0cadc2366f6139bd907d893bb4e237",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x66863b', 'to': '0x262aafd8968b'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000001234': {'balance': {'+': '0x1'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x7435ed30a8b4aeb087

</details>

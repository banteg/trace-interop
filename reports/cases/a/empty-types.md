# Empty types

`trace_call` · a · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. An empty trace-type selection executes and preserves the fixture return bytes.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001002",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x"
    },
    [],
    "0x30"
  ]
}
```

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H11](../../decisions/H11.md): An empty trace-type selection executes and preserves the fixture return bytes. Expected 0x000000000000000000000000000000000000000000000000000000000000002a

</details>

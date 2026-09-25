# Raw validation execution oog valid trace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. The valid signed control reports its expected execution success or halt in a root frame. Failed frames have an error string; an exceptional halt omits result or sets it to null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86a0a842da282a982520894000000000000000000000000000000000000100201808718e5bb3abd109fa0438c25241c47cb30acced697295dbdc7efd1c51379f4d9a278676f0a234be35ba03a1865e41b9a3ae09cb8e900d0295dc60fa0d1412a2b6658dffc7498eb8ca34d",
    [
      "trace"
    ]
  ]
}
```

</details>

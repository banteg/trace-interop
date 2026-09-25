# Raw validation valid trace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. The valid signed control reports its expected execution success or halt in a root frame.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b0a842da282a9830186a094000000000000000000000000000000000000100201808718e5bb3abd109fa0a2f62f19fe621aee70421dbc7406655686d0cff2bedd6aaccbddf7f94b497168a068ee9aa988adb25c24c1dd48868f13ac72615bd55e2b471953c8ee9c824e66fe",
    [
      "trace"
    ]
  ]
}
```

</details>

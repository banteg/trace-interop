# Raw validation valid statediff

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. Requested stateDiff records the signed execution state changes. Marker stateDiff records slot zero changing from zero to word 42.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b0a842da282a9830186a094000000000000000000000000000000000000100201808718e5bb3abd109fa0a2f62f19fe621aee70421dbc7406655686d0cff2bedd6aaccbddf7f94b497168a068ee9aa988adb25c24c1dd48868f13ac72615bd55e2b471953c8ee9c824e66fe",
    [
      "stateDiff"
    ]
  ]
}
```

</details>

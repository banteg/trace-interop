# Raw validation delegated sender valid trace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. The valid signed control reports its expected execution success or halt in a root frame.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/raw-validation/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/raw-validation/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/raw-validation/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/raw-validation/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · 558586f0](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/raw-validation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/raw-validation/manifest.json) |
| [Nethermind · 2.1.0-preview · 82516987](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/raw-validation/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b0a842da282a9830186a094000000000000000000000000000000000000100201808718e5bb3abd10a0a0aa1b8729627d5a66946b22f6256be16265f68013b90e71720864ae4f4e1e8b44a017dcd6b45f65b0e48dbb962707ade5cd4de5909deefe038808a8dc243b44188a",
    [
      "trace"
    ]
  ]
}
```

</details>

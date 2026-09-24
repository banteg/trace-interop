# Raw validation delegated sender valid statediff

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. Requested stateDiff records the signed execution state changes. Marker stateDiff records slot zero changing from zero to word 42.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/raw-validation/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/raw-validation/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/raw-validation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; output `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h15-call-compat/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/raw-validation/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/raw-validation/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/raw-validation/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b0a842da282a9830186a094000000000000000000000000000000000000100201808718e5bb3abd10a0a0aa1b8729627d5a66946b22f6256be16265f68013b90e71720864ae4f4e1e8b44a017dcd6b45f65b0e48dbb962707ade5cd4de5909deefe038808a8dc243b44188a",
    [
      "stateDiff"
    ]
  ]
}
```

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H13](../../decisions/H13.md): The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection.
- Result shape at `output`: None is not of type 'string'

</details>

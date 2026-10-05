# Raw validation delegated sender valid vmtrace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. Requested vmTrace holds the executing fixture bytecode. Requested vmTrace lists every operation that began executing, in order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-validation/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-validation/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-validation/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-validation/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-validation/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b0a842da282a9830186a094000000000000000000000000000000000000100201808718e5bb3abd10a0a0aa1b8729627d5a66946b22f6256be16265f68013b90e71720864ae4f4e1e8b44a017dcd6b45f65b0e48dbb962707ade5cd4de5909deefe038808a8dc243b44188a",
    [
      "vmTrace"
    ]
  ]
}
```

</details>

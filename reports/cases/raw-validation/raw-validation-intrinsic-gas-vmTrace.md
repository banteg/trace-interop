# Raw validation intrinsic gas vmtrace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | RPC error `800` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86a0a842da282a982520794000000000000000000000000000000000000100201808718e5bb3abd10a0a03e2bb48ffdc3a7718afc598d928b473e31cb4f1757a33a884d91d0e2bacc3eb7a00ff33e7901b8f83ce9451b3a94d395953062ce98020698dea332741bd49e596c",
    [
      "vmTrace"
    ]
  ]
}
```

</details>

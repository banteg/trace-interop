# Raw validation execution oog valid statediff

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. Requested stateDiff records the signed execution state changes. The first-opcode out-of-gas control cannot commit a marker storage write.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86a0a842da282a982520894000000000000000000000000000000000000100201808718e5bb3abd109fa0438c25241c47cb30acced697295dbdc7efd1c51379f4d9a278676f0a234be35ba03a1865e41b9a3ae09cb8e900d0295dc60fa0d1412a2b6658dffc7498eb8ca34d",
    [
      "stateDiff"
    ]
  ]
}
```

</details>

# Raw validation execution oog valid trace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. The valid signed control reports its expected execution success or halt in a root frame. Failed frames have an error string; an exceptional halt omits result or sets it to null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |

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

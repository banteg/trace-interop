# Raw validation create valid statediff

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. Requested stateDiff records the signed execution state changes. Creation stateDiff installs the constructor ADDRESS bytes at the signed creation address.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf8600a842da282a9830186a08001893060005260206000f38718e5bb3abd109fa0371d5f6be359abfc8aa07862de5609e2374dea339665f9fcfe54ebfeef4e5d53a00de19f45781c0c3903dca51e8da7bf4ac28cc805e9a63e27c4bf1ef1d00f951a",
    [
      "stateDiff"
    ]
  ]
}
```

</details>

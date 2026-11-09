# Call unknown field

`trace_call` · a · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Unknown call-object fields are ignored without changing execution output.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001002",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x",
      "unknownDiagnosticFlag": true
    },
    [
      "trace"
    ],
    "0x30"
  ]
}
```

</details>

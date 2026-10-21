# Root success

`trace_call` · precompiles · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Retain the root precompile frame, even with zero value. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/precompiles/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/precompiles/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/precompiles/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/precompiles/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/precompiles/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/precompiles/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/precompiles/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/precompiles/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/precompiles/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/precompiles/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/precompiles/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000000006",
      "gas": "0x100000",
      "gasPrice": "0x3b9aca00",
      "data": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

</details>

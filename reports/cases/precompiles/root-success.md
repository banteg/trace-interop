# Root success

`trace_call` · precompiles · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Retain the root precompile frame, even with zero value. Stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/precompiles/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/precompiles/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/precompiles/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/precompiles/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/precompiles/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/precompiles/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/precompiles/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/precompiles/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/precompiles/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/precompiles/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/precompiles/manifest.json) |

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

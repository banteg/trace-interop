# Root success

`trace_call` · precompiles · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Retain the root precompile frame, even with zero value. Stack words use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/precompiles-final/observations.json) · [Build/run](../../../evidence/2026-09-21/precompiles-final/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/precompiles-final/observations.json) · [Build/run](../../../evidence/2026-09-21/precompiles-final/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/precompiles-final/observations.json) · [Build/run](../../../evidence/2026-09-21/precompiles-final/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/precompiles-final/observations.json) · [Build/run](../../../evidence/2026-09-21/precompiles-final/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/geth-e29edff-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-precompiles/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/precompiles-final/observations.json) · [Build/run](../../../evidence/2026-09-21/precompiles-final/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/precompiles-final/observations.json) · [Build/run](../../../evidence/2026-09-21/precompiles-final/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/precompiles-final/observations.json) · [Build/run](../../../evidence/2026-09-21/precompiles-final/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/precompiles-final/observations.json) · [Build/run](../../../evidence/2026-09-21/precompiles-final/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x100000",
      "gasPrice": "0x3b9aca00",
      "to": "0x0000000000000000000000000000000000000006"
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

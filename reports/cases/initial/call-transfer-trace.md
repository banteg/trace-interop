# Call transfer trace

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001234",
      "gas": "0x186a0",
      "gasPrice": "0x77359400",
      "value": "0x1",
      "data": "0x"
    },
    [
      "trace"
    ],
    "0x30"
  ]
}
```

</details>

# Debug destroy

`debug_traceCall` · a · [All reports](../../README.md)

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "debug_traceCall",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001007",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x"
    },
    "0x30",
    {
      "tracer": "callTracer"
    }
  ]
}
```

</details>

# Destroy prestate 55

`debug_traceCall` · forks · [All reports](../../README.md)

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | Incomplete or malformed JSON | ⚪ Not assessed | [Response](../../../evidence/2026-09-25/fixture-wave/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/forks/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-09-25/fixture-wave/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/forks/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-09-25/fixture-wave/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-09-25/fixture-wave/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-09-25/fixture-wave/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-09-25/fixture-wave/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/forks/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-09-25/fixture-wave/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-09-25/fixture-wave/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/forks/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | Object returned | ⚪ Not assessed | [Response](../../../evidence/2026-09-25/fixture-wave/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/forks/manifest.json) |

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
    "0x37",
    {
      "tracer": "prestateTracer",
      "tracerConfig": {
        "diffMode": true
      }
    }
  ]
}
```

</details>

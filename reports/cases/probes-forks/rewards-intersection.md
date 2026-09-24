# Rewards intersection

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** A reward has no from side, so an intersection with a populated fromAddress excludes it.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromAddress": [
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f"
      ],
      "fromBlock": "0x2",
      "mode": "intersection",
      "toAddress": [
        "0x0000000000000000000000000000000000000000"
      ],
      "toBlock": "0x5"
    }
  ]
}
```

**Besu · 26.9-develop · cf89071f** (`besu/v26.9-develop-cf89071/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A reward has no from side, so an intersection with a populated fromAddress excludes it. Expected a result; observed rpc_error -32602 Invalid filter params

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A reward has no from side, so an intersection with a populated fromAddress excludes it. Expected a result; observed rpc_error -32602 Invalid filter params

</details>

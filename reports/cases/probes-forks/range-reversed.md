# Range reversed

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** An explicit fromBlock above toBlock is rejected (-32602 recommended), as eth_getLogs does.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x3",
      "toBlock": "0x2"
    }
  ]
}
```

</details>

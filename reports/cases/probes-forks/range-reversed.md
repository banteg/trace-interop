# Range reversed

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** An explicit fromBlock above toBlock is rejected (-32602 recommended), as eth_getLogs does.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |

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

# Range reversed

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** An explicit fromBlock above toBlock is rejected (-32602 recommended), as eth_getLogs does.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |

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

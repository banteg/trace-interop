# Sender skip

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** Filter first, then skip after matching records and take count, across block boundaries.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "after": 2,
      "count": 3,
      "fromAddress": [
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f"
      ],
      "fromBlock": "0x2",
      "toBlock": "0x5"
    }
  ]
}
```

</details>

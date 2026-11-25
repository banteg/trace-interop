# Sender skip

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** Filter first, then skip after matching records and take count, across block boundaries.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-forks/manifest.json) |

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

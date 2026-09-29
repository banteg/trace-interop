# Beacon many 56

`trace_callMany` · probes-forks · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. The first trace_callMany item at block 56 runs on the same post-block state as trace_call. The one-item trace_callMany output equals trace_call at the same block.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_callMany",
  "params": [
    [
      [
        {
          "data": "0x0000000000000000000000000000000000000000000000000000000000000230",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x77359400",
          "to": "0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02"
        },
        [
          "trace"
        ]
      ]
    ],
    "0x38"
  ]
}
```

</details>

# Beacon trace 56

`trace_call` · probes-forks · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. trace_call at block 56 reads the beacon root of timestamp 560 only if block 56 stored it.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x0000000000000000000000000000000000000000000000000000000000000230",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "to": "0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02"
    },
    [
      "trace"
    ],
    "0x38"
  ]
}
```

</details>

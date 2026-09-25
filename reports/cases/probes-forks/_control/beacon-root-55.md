# _control/beacon root 55

`eth_getStorageAt` · probes-forks · [All reports](../../../README.md)

**What this checks:** State at block 55 predates block 56's beacon-root write: the root slot reads zero.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getStorageAt",
  "params": [
    "0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02",
    "0x222f",
    "0x37"
  ]
}
```

</details>

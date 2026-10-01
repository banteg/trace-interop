# _control/beacon timestamp 55

`eth_getStorageAt` · probes-forks · [All reports](../../../README.md)

**What this checks:** State at block 55 predates block 56's beacon-root write: the timestamp slot reads zero.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-01/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-01/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-01/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-01/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-01/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-01/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-01/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-01/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-01/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-01/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getStorageAt",
  "params": [
    "0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02",
    "0x230",
    "0x37"
  ]
}
```

</details>

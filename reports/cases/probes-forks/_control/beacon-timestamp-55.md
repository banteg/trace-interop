# _control/beacon timestamp 55

`eth_getStorageAt` · probes-forks · [All reports](../../../README.md)

**What this checks:** State at block 55 predates block 56's beacon-root write: the timestamp slot reads zero.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-02/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-02/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-02/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-02/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-02/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/probes-forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-02/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-02/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-02/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-02/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-10-02/eval/probes-forks/manifest.json) |

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

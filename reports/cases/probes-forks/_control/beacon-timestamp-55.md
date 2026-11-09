# _control/beacon timestamp 55

`eth_getStorageAt` · probes-forks · [All reports](../../../README.md)

**What this checks:** State at block 55 predates block 56's beacon-root write: the timestamp slot reads zero.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.0 · 0e595f9e](../../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |

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

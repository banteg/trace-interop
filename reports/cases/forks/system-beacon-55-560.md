# System beacon 55 560

`eth_getStorageAt` · forks · [All reports](../../README.md)

**What this checks:** Historical beacon-root storage excludes the following block system update.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.1 · e83703cd](../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "eth_getStorageAt",
  "params": [
    "0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02",
    "0x230",
    "0x37"
  ]
}
```

</details>

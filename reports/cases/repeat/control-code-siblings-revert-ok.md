# Control code siblings revert ok

`eth_getCode` · repeat · [All reports](../../README.md)

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | `0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000` | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | `0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000` | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000` | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | `0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000` | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000` | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | `0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000` | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | `0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000` | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | `0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000` | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | `0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000` | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000` | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | `0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000` | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "eth_getCode",
  "params": [
    "0x0000000000000000000000000000000000001005",
    "0x30"
  ]
}
```

</details>

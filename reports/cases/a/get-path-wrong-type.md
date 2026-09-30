# Get path wrong type

`trace_get` · a · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "0x6"
  ]
}
```

</details>

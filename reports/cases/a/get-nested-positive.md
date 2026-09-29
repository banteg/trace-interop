# Get nested positive

`trace_get` · a · [All reports](../../README.md)

**What this checks:** Return the transaction-tree record at [6, 0], or null if absent.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "0x6",
      "0x0"
    ]
  ]
}
```

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [6, 0], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.
- Result shape at `/`: [{'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d

</details>

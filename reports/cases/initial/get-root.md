# Get root

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Return the transaction-tree record at [], or null if absent.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../clients/anvil_development.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · a1ce80fb](../../clients/erigon_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · 45912ba3](../../clients/nethermind_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    []
  ]
}
```

**Anvil · 1.8.4-nightly · dd372126** (`anvil Version: 1.8.4-nightly+dd372126`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.
- Result shape at `/`: [] is not valid under any of the given schemas

</details>

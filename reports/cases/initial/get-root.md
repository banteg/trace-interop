# Get root

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Return the transaction-tree record at [], or null if absent.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | `[]` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |

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

**Anvil · 1.8.4-nightly · 60255eee** (`anvil Version: 1.8.4-nightly+60255eee`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.
- Result shape at `/`: [] is not valid under any of the given schemas

</details>

# Get transfer root

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Return the transaction-tree record at [], or null if absent.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | One frame, path `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_get",
  "params": [
    "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    []
  ]
}
```

**Anvil · 1.8.4-nightly · e3429853** (`anvil Version: 1.8.4-nightly+e3429853`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.
- Result shape at `/`: [] is not valid under any of the given schemas

</details>

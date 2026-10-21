# Get nested

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Return the transaction-tree record at [0, 0], or null if absent. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "0x0",
      "0x0"
    ]
  ]
}
```

**Anvil · 1.8.6-nightly · 9089a6bf** (`anvil Version: 1.8.6-nightly+9089a6bf`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Erigon · 3.9.0-dev · d23467c5** (`3.9.0-dev-d23467c5`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Nethermind · 2.3.0-preview · e2e011c8** (`2.3.0-preview+e2e011c8`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

</details>

# Get missing

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** A missing selected frame is null, not an empty collection. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "0xffff"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · e3429853** (`anvil Version: 1.8.4-nightly+e3429853`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Erigon · 3.8.0-dev · 923b4d31** (`3.8.0-dev-923b4d31`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Geth draft fork · 1.17.7-unstable · ec1cec0b** (`Geth/v1.17.7-unstable-ec1cec0b-2026-09-30/linux-amd64/go1.26.1`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Nethermind · 2.2.0-preview · 79173d14** (`2.2.0-preview+79173d14`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H02](../../decisions/H02.md): A missing selected frame is null, not an empty collection.
- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.
- Result shape at `/`: [] is not valid under any of the given schemas

**Reth · 2.7.0 · 43a93dbc** (`Reth Version: 2.7.0+43a93dbc`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

</details>

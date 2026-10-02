# Get missing

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** A missing selected frame is null, not an empty collection. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 328811cb](../../clients/anvil_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/initial/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | `[]` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-02/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/initial/manifest.json) |

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

**Anvil · 1.8.4-nightly · 328811cb** (`anvil Version: 1.8.4-nightly+328811cb`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Erigon · 3.8.0-dev · 6da806cb** (`3.8.0-dev-6da806cb`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Nethermind · 2.2.0-preview · 3370d566** (`2.2.0-preview+3370d566`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H02](../../decisions/H02.md): A missing selected frame is null, not an empty collection.
- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.
- Result shape at `/`: [] is not valid under any of the given schemas

**Reth · 2.7.0 · 078d0262** (`Reth Version: 2.7.0+078d0262`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

</details>

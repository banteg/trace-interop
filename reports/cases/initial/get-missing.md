# Get missing

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** A missing selected frame is null, not an empty collection. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Anvil · 1.8.7-nightly · 4e8874b2](../../clients/anvil_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Besu · 26.10.1 · e83703cd](../../clients/besu_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../clients/besu_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../clients/nethermind_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../clients/nethermind_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |

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

**Anvil · 1.8.7-nightly · 4e8874b2** (`anvil Version: 1.8.7-nightly+4e8874b2`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Besu · 26.10-develop · 781a7e1d** (`besu/v26.10-develop-781a7e1/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Erigon · 3.9.0-dev · 598ba625** (`3.9.0-dev-598ba625`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Nethermind · 2.3.0-preview · 7192e7f3** (`2.3.0-preview+7192e7f3`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Nethermind · 2.2.1 · c4f1015b** (`2.2.1+c4f1015b`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Reth · 2.8.0 · 53bf066f** (`Reth Version: 2.8.0+53bf066f`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Reth · 2.8.1 · d763342f** (`Reth Version: 2.8.1+d763342f`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

</details>

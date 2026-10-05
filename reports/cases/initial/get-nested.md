# Get nested

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Return the transaction-tree record at [0, 0], or null if absent. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |

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

**Anvil · 1.8.4-nightly · e15c2f1c** (`anvil Version: 1.8.4-nightly+e15c2f1c`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Erigon · 3.8.0-dev · 96188a47** (`3.8.0-dev-96188a47`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Nethermind · 2.2.0-preview · e8955c4c** (`2.2.0-preview+e8955c4c`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [0, 0], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.
- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xf35c', 'input': '0xff01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1', 'value': '0x1'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'result

**Reth · 2.7.0 · 42fa3c56** (`Reth Version: 2.7.0+42fa3c56`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H06](../../decisions/H06.md): Assess the declared property. The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule.

</details>

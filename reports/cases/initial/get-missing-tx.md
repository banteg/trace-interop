# Get missing tx

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Unknown transaction returns null, not an empty collection or RPC error. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Anvil · 1.8.6-nightly · de005f70](../../clients/anvil_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../clients/besu_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../clients/nethermind_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_get",
  "params": [
    "0xfefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefe",
    []
  ]
}
```

**Anvil · 1.8.6-nightly · de005f70** (`anvil Version: 1.8.6-nightly+de005f70`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Besu · 26.10-develop · 0776d82f** (`besu/v26.10-develop-0776d82/linux-x86_64/openjdk-java-25`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Erigon · 3.8.0-dev · 5b452f41** (`3.8.0-dev-5b452f41`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Geth draft fork · 1.17.7-unstable · 71db3b03** (`Geth/v1.17.7-unstable-71db3b03-2026-10-14/linux-amd64/go1.26.1`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Nethermind · 2.2.0-preview · cd336c4c** (`2.2.0-preview+cd336c4c`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Reth · 2.7.0 · ec3e7e42** (`Reth Version: 2.7.0+ec3e7e42`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

</details>

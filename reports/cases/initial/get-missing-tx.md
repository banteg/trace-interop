# Get missing tx

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Unknown transaction returns null, not an empty collection or RPC error. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |

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

**Anvil · 1.8.7-nightly · 716e795c** (`anvil Version: 1.8.7-nightly+716e795c`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Erigon · 3.9.0-dev · 6955d198** (`3.9.0-dev-6955d198`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Geth draft fork · 1.17.11-unstable · 0f1fb2ae** (`Geth/v1.17.11-unstable-0f1fb2ae-2026-10-28/linux-amd64/go1.26.1`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Nethermind · 2.3.0-preview · fc9abf09** (`2.3.0-preview+fc9abf09`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

</details>

# Get missing tx

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Unknown transaction returns null, not an empty collection or RPC error. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |

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

**Anvil · 1.8.6-nightly · 6c21ffe2** (`anvil Version: 1.8.6-nightly+6c21ffe2`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Geth draft fork · 1.17.9-unstable · fdbb46a5** (`Geth/v1.17.9-unstable-fdbb46a5-2026-10-18/linux-amd64/go1.26.1`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

</details>

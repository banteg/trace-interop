# Get missing tx

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Unknown transaction returns null, not an empty collection or RPC error. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |

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

**Anvil · 1.8.4-nightly · df92604b** (`anvil Version: 1.8.4-nightly+df92604b`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Erigon · 3.8.0-dev · 50e2cc4f** (`3.8.0-dev-50e2cc4f`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Nethermind · 2.2.0-preview · 759efed7** (`2.2.0-preview+759efed7`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.
- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Reth · 2.7.0 · 5b686303** (`Reth Version: 2.7.0+5b686303`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

</details>

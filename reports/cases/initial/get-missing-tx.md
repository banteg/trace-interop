# Get missing tx

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Unknown transaction returns null, not an empty collection or RPC error. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |

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

**Anvil · 1.10.1-nightly · 50d75f19** (`anvil Version: 1.10.1-nightly+50d75f19`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Anvil · 1.10.0 · 083e2299** (`anvil Version: 1.10.0+083e2299`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Erigon · 3.9.0-dev · e91aca7f** (`3.9.0-dev-e91aca7f`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Erigon · 3.8.2 · 8a3f3b2c** (`3.8.2-8a3f3b2c`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Geth draft fork · 1.17.11-unstable · edbd5f17** (`Geth/v1.17.11-unstable-edbd5f17-2026-11-18/linux-amd64/go1.26.1`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Nethermind · 2.4.0-preview · e2f069a6** (`2.4.0-preview+e2f069a6`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H02](../../decisions/H02.md): Assess the declared property. The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection.

</details>

# Filter head only

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x30",
      "toBlock": "0x30",
      "count": 3
    }
  ]
}
```

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Geth draft fork · 1.17.7-unstable · c8449896** (`Geth/v1.17.7-unstable-c8449896-2026-09-26/linux-amd64/go1.26.1`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

</details>

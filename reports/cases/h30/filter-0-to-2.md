# Filter 0 to 2

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x0",
      "toBlock": "0x2",
      "count": 3
    }
  ]
}
```

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Erigon · 3.8.0-dev · a2a19253** (`3.8.0-dev-a2a19253`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Geth draft fork · 1.17.7-unstable · e26833e3** (`Geth/v1.17.7-unstable-e26833e3-2026-09-26/linux-amd64/go1.26.1`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Nethermind · 2.2.0-preview · 287f54f0** (`2.2.0-preview+287f54f0`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

</details>

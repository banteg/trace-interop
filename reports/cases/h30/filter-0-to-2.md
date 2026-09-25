# Filter 0 to 2

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-25/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/h30/manifest.json) |

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

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Erigon · 3.8.0-dev · f8cfe5a7** (`3.8.0-dev-f8cfe5a7`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Geth draft fork · 1.17.7-unstable · 0a663f3c** (`Geth/v1.17.7-unstable-0a663f3c-2026-09-24/linux-amd64/go1.26.1`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Nethermind · 2.1.0-preview · ee1f57da** (`2.1.0-preview+ee1f57da`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

</details>

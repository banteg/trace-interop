# Filter 0 to 2

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |

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

**Anvil · 1.8.4-nightly · 60255eee** (`anvil Version: 1.8.4-nightly+60255eee`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Erigon · 3.8.0-dev · 5cb6c867** (`3.8.0-dev-5cb6c867`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Nethermind · 2.2.0-preview · 6dff813b** (`2.2.0-preview+6dff813b`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Reth · 2.7.0 · 10bcf461** (`Reth Version: 2.7.0+10bcf461`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H32](../../decisions/H32.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

</details>

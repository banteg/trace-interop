# Filter head only

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../clients/anvil_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/h30/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 558586f0](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/h30/manifest.json) |
| [Nethermind · 2.1.0-preview · 82516987](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/h30/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/h30/manifest.json) |

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

**Anvil · 1.8.4-nightly · dd372126** (`anvil Version: 1.8.4-nightly+dd372126`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Erigon · 3.8.0-dev · 558586f0** (`3.8.0-dev-558586f0`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Geth draft fork · 1.17.7-unstable · e26833e3** (`Geth/v1.17.7-unstable-e26833e3-2026-09-26/linux-amd64/go1.26.1`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Nethermind · 2.1.0-preview · 82516987** (`2.1.0-preview+82516987`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Reth · 2.5.2 · 5723a3fe** (`Reth Version: 2.5.2+5723a3fe`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H30](../../decisions/H30.md): Assess the declared property. Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion.

</details>

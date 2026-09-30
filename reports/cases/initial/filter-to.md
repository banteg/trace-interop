# Filter to

`trace_filter` · initial · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toBlock": "0x2",
      "toAddress": [
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      ]
    }
  ]
}
```

**Anvil · 1.8.4-nightly · e3429853** (`anvil Version: 1.8.4-nightly+e3429853`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Expected 1 such records from this client's block trace; got 0.
- [H09](../../decisions/H09.md): Assess the declared property. Address selection differs from its reference; failure-bearing frame selection is not established.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Expected 1 such records from this client's block trace; got 0.
- [H09](../../decisions/H09.md): Assess the declared property. Address selection differs from its reference; failure-bearing frame selection is not established.

**Erigon · 3.8.0-dev · 923b4d31** (`3.8.0-dev-923b4d31`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

**Geth draft fork · 1.17.7-unstable · ec1cec0b** (`Geth/v1.17.7-unstable-ec1cec0b-2026-09-30/linux-amd64/go1.26.1`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

**Nethermind · 2.2.0-preview · 79173d14** (`2.2.0-preview+79173d14`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

**Reth · 2.7.0 · 43a93dbc** (`Reth Version: 2.7.0+43a93dbc`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

</details>

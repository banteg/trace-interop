# Filter to

`trace_filter` · initial · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toAddress": [
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      ],
      "toBlock": "0x2"
    }
  ]
}
```

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 2 records from this client's block trace.
- [H09](../../decisions/H09.md): Assess the declared property. Address selection differs from its reference; failure-bearing frame selection is not established.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 2 records from this client's block trace.
- [H09](../../decisions/H09.md): Assess the declared property. Address selection differs from its reference; failure-bearing frame selection is not established.

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

**Geth draft fork · 1.17.7-unstable · fa8ecb92** (`Geth/v1.17.7-unstable-fa8ecb92-2026-09-24/linux-amd64/go1.26.1`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

**Nethermind · 2.1.0-unstable · 641592d2** (`2.1.0-unstable+641592d2`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H09](../../decisions/H09.md): Assess the declared property. No failed frame is selected; the address-filter assertion independently checks the selected inventory.

</details>

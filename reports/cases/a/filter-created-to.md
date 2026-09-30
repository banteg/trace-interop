# Filter created to

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/a/manifest.json) |

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
        "0x2d303c5b7911d87d594bf1b31fbb9aa187888893"
      ]
    }
  ]
}
```

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

</details>

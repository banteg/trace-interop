# Filter created to

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |

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

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

</details>

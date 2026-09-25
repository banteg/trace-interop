# Filter page 2

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |

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
      "after": 8,
      "count": 4
    }
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

</details>

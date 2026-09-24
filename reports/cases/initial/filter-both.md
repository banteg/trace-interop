# Filter both

`trace_filter` · initial · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Failed frames have an error string and an explicit object or null result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 6 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 6 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 6 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromAddress": [
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f"
      ],
      "fromBlock": "0x2",
      "toAddress": [
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      ],
      "toBlock": "0x2"
    }
  ]
}
```

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

</details>

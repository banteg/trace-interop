# Filter both

`trace_filter` · initial · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Failed frames have an error string and an explicit object or null result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 1 records | Checked cases agree | [Response](../../../evidence/2026-09-23/h03-modes-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-initial/manifest.json) |
| [Besu · Release](../../clients/besu_release.md) | 1 records | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 1 records | Checked cases agree | [Response](../../../evidence/2026-09-23/h03-modes-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-initial/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 1 records | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 6 records | Differs | [Response](../../../evidence/2026-09-23/h03-modes-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-initial/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 6 records | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 6 records | Differs | [Response](../../../evidence/2026-09-23/h03-modes-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-initial/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 6 records | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 1 records | Checked cases agree | [Response](../../../evidence/2026-09-23/geth-40eecf3-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-40eecf3-initial/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 1 records | Checked cases agree | [Response](../../../evidence/2026-09-23/h03-modes-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-initial/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 1 records | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 1 records | Checked cases agree | [Response](../../../evidence/2026-09-23/h03-modes-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-initial/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 1 records | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 6 records | Differs | [Response](../../../evidence/2026-09-23/h03-modes-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-initial/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 6 records | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 6 records | Differs | [Response](../../../evidence/2026-09-23/h03-modes-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-initial/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 6 records | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |

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

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

</details>

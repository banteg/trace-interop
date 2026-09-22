# Filter from only union

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Failed frames have an error string and an explicit object or null result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | RPC error `-32602` | Differs | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | RPC error `-32602` | Differs | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 5 records | Checked cases agree | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 5 records | Checked cases agree | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | RPC error `-32602` | Differs | [Response](../../../evidence/2026-09-23/h03-modes-geth-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-geth-a/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 5 records | Differs; result shape differs | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 5 records | Differs; result shape differs | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 5 records | Checked cases agree | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 5 records | Checked cases agree | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |

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
      "mode": "union",
      "toBlock": "0x2"
    }
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 5 records from this client's block trace.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 5 records from this client's block trace.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Geth draft fork · Draft fork** (`Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 5 records from this client's block trace.

</details>

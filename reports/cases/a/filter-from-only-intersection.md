# Filter from only intersection

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Failed frames have an error string and an explicit object or null result. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | RPC error `-32602` | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | RPC error `-32602` | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | `[]` | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | `[]` | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 5 records | Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-geth-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-geth-a/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 5 records | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 5 records | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 5 records | Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 5 records | Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |

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
      "mode": "intersection",
      "toBlock": "0x2"
    }
  ]
}
```

**Geth draft fork · Draft fork** (`Geth/v1.17.6-unstable-40eecf36-2026-09-23/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 5 records from this client's block trace.
- [H14](../../decisions/H14.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 5 records from this client's block trace.
- [H14](../../decisions/H14.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 5 records from this client's block trace.
- [H14](../../decisions/H14.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 5 records from this client's block trace.
- [H14](../../decisions/H14.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H14](../../decisions/H14.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H14](../../decisions/H14.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H14](../../decisions/H14.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H14](../../decisions/H14.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

</details>

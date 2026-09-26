# Filter across 52

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. A fork-crossing range equals the corresponding per-block traces.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 15 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/forks/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 15 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 15 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/forks/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 15 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/forks/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x33",
      "toBlock": "0x34"
    }
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `1`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'error':
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b
- Result shape at `9`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70d', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'result': {'address': '0x30

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `1`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'error':
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b
- Result shape at `9`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70d', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'result': {'address': '0x30

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `1`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'error':
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b
- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property
- Result shape at `14`: 'transactionHash' is a required property
- Result shape at `14`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `1`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'error':
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b
- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property
- Result shape at `14`: 'transactionHash' is a required property
- Result shape at `14`: 'transactionPosition' is a required property

</details>

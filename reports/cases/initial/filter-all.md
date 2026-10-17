# Filter all

`trace_filter` · initial · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Omitted address lists impose no address restriction. The declared PoS range contains no synthetic PoW reward records, including withdrawal blocks.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Anvil · 1.8.6-nightly · de005f70](../../clients/anvil_development.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 14 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../clients/besu_development.md) | 14 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../clients/erigon_development.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../clients/go-ethereum_trace.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../clients/nethermind_development.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../clients/reth_development.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toBlock": "0x2"
    }
  ]
}
```

**Besu · 26.10-develop · 0776d82f** (`besu/v26.10-develop-0776d82/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H05](../../decisions/H05.md): The declared PoS range contains no synthetic PoW reward records, including withdrawal blocks. 1 reward records.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b
- Result shape at `8`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'result': {'address': '0x2d3

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H05](../../decisions/H05.md): The declared PoS range contains no synthetic PoW reward records, including withdrawal blocks. 1 reward records.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b
- Result shape at `8`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'result': {'address': '0x2d3

</details>

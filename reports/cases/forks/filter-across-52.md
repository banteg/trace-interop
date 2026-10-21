# Filter across 52

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. A fork-crossing range equals the corresponding per-block traces.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 15 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 15 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 13 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |

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

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `1`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'error':
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b
- Result shape at `6`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'erro
- Result shape at `9`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70d', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'result': {'address': '0x30

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `1`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'error':
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b
- Result shape at `6`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'erro
- Result shape at `9`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70d', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'result': {'address': '0x30

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [3]: error 'Mutable Call In Static Context', result null.
- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [6, 0]: error None, result null.
- Result shape at `6`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'erro
- Result shape at `10`: {'action': {'address': '0x302cb90c0d0edb96d0f45cc53a6e286ca192c872', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'subtraces': 0, 'traceAddress': [6, 0], 'transa

</details>

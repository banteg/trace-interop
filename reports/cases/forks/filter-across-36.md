# Filter across 36

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. A fork-crossing range equals the corresponding per-block traces. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 8 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 8 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 16 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | 16 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 16 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 16 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | 16 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 16 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 16 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x23",
      "toBlock": "0x24"
    }
  ]
}
```

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): A fork-crossing range equals the corresponding per-block traces.
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'result': {'gasUsed': '0x0
- Result shape at `5`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'result': {'gasUsed': '0x0',
- Result shape at `6`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x48b7c57589928d75656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'res

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): A fork-crossing range equals the corresponding per-block traces.
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'result': {'gasUsed': '0x0
- Result shape at `5`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'result': {'gasUsed': '0x0',
- Result shape at `6`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x48b7c57589928d75656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'res

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `15`: 'transactionHash' is a required property
- Result shape at `15`: 'transactionPosition' is a required property

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [3]: error 'Mutable Call In Static Context', result null.
- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress []: error None, result null.
- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `2`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x1c9f78d2893e4000'}, 'blockHash': '0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f', 'blockNumber': 35, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under an
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'uncle', 'value': '0x18493fba64ef0000'}, 'blockHash': '0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f', 'blockNumber': 35, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under an
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `9`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'erro
- Result shape at `13`: {'action': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'subtraces': 0, 'traceAddress': [6, 0], 'transa

</details>

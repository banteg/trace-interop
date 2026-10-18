# Filter null toblock

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. A null toBlock is omitted, so it resolves to the same latest head. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 279 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 279 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 350 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 350 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 350 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 350 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 350 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 350 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 350 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toBlock": null
    }
  ]
}
```

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- Result shape at `24`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x92c0a3cd8b571ac5656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0xc80abc7c7ff55e123dd2a22190a845894ebb363b3a0355c1cb5dfc57cbeb613e', 'blockNumber': 8, 'resu
- Result shape at `25`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x4dde844b71bcdf95512fb4dc94e84fb67b512ed8', 'value': '0x1'}, 'blockHash': '0xc80abc7c7ff55e123dd2a22190a845894ebb363b3a0355c1cb5dfc57cbeb613e', 'blockNumber': 8, 'result': {'gasUsed': '0x0',
- Result shape at `28`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xa66c701845710c6c656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x9b33350a0ba145d68e650268822204c0b76798a7724e7c1ebc60268f8ee0f968', 'blockNumber': 9, 'resu
- Result shape at `29`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x1f5bde34b4afc686f136c7a3cb6ec376f7357759', 'value': '0x1'}, 'blockHash': '0x9b33350a0ba145d68e650268822204c0b76798a7724e7c1ebc60268f8ee0f968', 'blockNumber': 9, 'result': {'gasUsed': '0x0',
- Result shape at `32`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x06072144caa6635a656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x46b9527975bd5b8a68582a18e68eaac0618048e6386f9e1fa0a6e18de6e8c96f', 'blockNumber': 10, 'res
- Result shape at `33`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x3ae75c08b4c907eb63a8960c45b86e1e9ab6123c', 'value': '0x1'}, 'blockHash': '0x46b9527975bd5b8a68582a18e68eaac0618048e6386f9e1fa0a6e18de6e8c96f', 'blockNumber': 10, 'result': {'gasUsed': '0x0',
- Result shape at `36`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xb2cbef3dfb5e69d8656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0xaa6cc431712ea8ebe17e14682184305add9f375af0cd6187d6b2b136eac85d1d', 'blockNumber': 11, 'res
- Result shape at `37`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x5f552da00dfb4d3749d9e62dcee3c918855a86a0', 'value': '0x1'}, 'blockHash': '0xaa6cc431712ea8ebe17e14682184305add9f375af0cd6187d6b2b136eac85d1d', 'blockNumber': 11, 'result': {'gasUsed': '0x0',

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- Result shape at `24`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x92c0a3cd8b571ac5656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0xc80abc7c7ff55e123dd2a22190a845894ebb363b3a0355c1cb5dfc57cbeb613e', 'blockNumber': 8, 'resu
- Result shape at `25`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x4dde844b71bcdf95512fb4dc94e84fb67b512ed8', 'value': '0x1'}, 'blockHash': '0xc80abc7c7ff55e123dd2a22190a845894ebb363b3a0355c1cb5dfc57cbeb613e', 'blockNumber': 8, 'result': {'gasUsed': '0x0',
- Result shape at `28`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xa66c701845710c6c656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x9b33350a0ba145d68e650268822204c0b76798a7724e7c1ebc60268f8ee0f968', 'blockNumber': 9, 'resu
- Result shape at `29`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x1f5bde34b4afc686f136c7a3cb6ec376f7357759', 'value': '0x1'}, 'blockHash': '0x9b33350a0ba145d68e650268822204c0b76798a7724e7c1ebc60268f8ee0f968', 'blockNumber': 9, 'result': {'gasUsed': '0x0',
- Result shape at `32`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x06072144caa6635a656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x46b9527975bd5b8a68582a18e68eaac0618048e6386f9e1fa0a6e18de6e8c96f', 'blockNumber': 10, 'res
- Result shape at `33`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x3ae75c08b4c907eb63a8960c45b86e1e9ab6123c', 'value': '0x1'}, 'blockHash': '0x46b9527975bd5b8a68582a18e68eaac0618048e6386f9e1fa0a6e18de6e8c96f', 'blockNumber': 10, 'result': {'gasUsed': '0x0',
- Result shape at `36`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xb2cbef3dfb5e69d8656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0xaa6cc431712ea8ebe17e14682184305add9f375af0cd6187d6b2b136eac85d1d', 'blockNumber': 11, 'res
- Result shape at `37`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x5f552da00dfb4d3749d9e62dcee3c918855a86a0', 'value': '0x1'}, 'blockHash': '0xaa6cc431712ea8ebe17e14682184305add9f375af0cd6187d6b2b136eac85d1d', 'blockNumber': 11, 'result': {'gasUsed': '0x0',

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [3]: error 'Mutable Call In Static Context', result null.
- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress []: error None, result null.
- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `3`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0x395e712438dd92dc5d88276418e20a940d2ce71bd6a5c28cc62dab41acdd6436', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under any
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x49b9ca9a69434000'}, 'blockHash': '0x2cd37cf31e57ceb56e7d009ffda233a84acf52ae9a630ee91600b0f17099d092', 'blockNumber': 3, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under any
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'uncle', 'value': '0x3cb71f51fc558000'}, 'blockHash': '0x2cd37cf31e57ceb56e7d009ffda233a84acf52ae9a630ee91600b0f17099d092', 'blockNumber': 3, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under any
- Result shape at `6`: 'transactionHash' is a required property

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [3]: error 'Mutable Call In Static Context', result null.
- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress []: error None, result null.
- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `3`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0x395e712438dd92dc5d88276418e20a940d2ce71bd6a5c28cc62dab41acdd6436', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under any
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x49b9ca9a69434000'}, 'blockHash': '0x2cd37cf31e57ceb56e7d009ffda233a84acf52ae9a630ee91600b0f17099d092', 'blockNumber': 3, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under any
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'uncle', 'value': '0x3cb71f51fc558000'}, 'blockHash': '0x2cd37cf31e57ceb56e7d009ffda233a84acf52ae9a630ee91600b0f17099d092', 'blockNumber': 3, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under any
- Result shape at `6`: 'transactionHash' is a required property

</details>

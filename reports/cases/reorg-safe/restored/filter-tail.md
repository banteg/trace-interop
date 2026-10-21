# Restored/filter tail

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. Every phase range has exactly the frozen canonical roots and block hashes; restoration returns the original inventory. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../../clients/besu_release.md) | 50 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../../clients/besu_development.md) | 50 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../../clients/erigon_release.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../../clients/erigon_development.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../../clients/go-ethereum_trace.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../clients/nethermind_release.md) | 41 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../../clients/nethermind_development.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../../clients/reth_release.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../../clients/reth_development.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-21/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-21/eval/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x28",
      "toBlock": "0x30"
    }
  ]
}
```

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H09](../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- Result shape at `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52
- Result shape at `15`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'erro
- Result shape at `18`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'result': {'address': '0x05
- Result shape at `30`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'error':
- Result shape at `33`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431
- Result shape at `35`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'erro
- Result shape at `38`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'result': {'address': '0x9e

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H09](../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- Result shape at `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52
- Result shape at `15`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'erro
- Result shape at `18`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'result': {'address': '0x05
- Result shape at `30`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'error':
- Result shape at `33`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431
- Result shape at `35`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'erro
- Result shape at `38`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'result': {'address': '0x9e

**Erigon · 3.9.0-dev · d23467c5** (`3.9.0-dev-d23467c5`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.3.0-preview · e2e011c8** (`2.3.0-preview+e2e011c8`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H09](../../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [3]: error 'Mutable Call In Static Context', result null.
- [H09](../../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [6, 0]: error None, result null.
- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `12`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'erro
- Result shape at `16`: {'action': {'address': '0x05032e03adbca6d5d04236000a2bbb6b4fec87f5', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'subtraces': 0, 'traceAddress': [6, 0], 'transa
- Result shape at `29`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'erro
- Result shape at `33`: {'action': {'address': '0x9ee5c90ad0a83dd07800c64adb87c584092f8e37', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'subtraces': 0, 'traceAddress': [6, 0], 'transa

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

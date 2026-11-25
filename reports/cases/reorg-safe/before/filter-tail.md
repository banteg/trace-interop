# Before/filter tail

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. Every phase range has exactly the frozen canonical roots and block hashes; restoration returns the original inventory. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.2 · 09b9e94d](../../../clients/besu_release.md) | 50 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../../clients/besu_development.md) | 50 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../../clients/erigon_release.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../../clients/erigon_development.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../../clients/go-ethereum_trace.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../clients/nethermind_release.md) | 41 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../../clients/nethermind_development.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../../clients/reth_release.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../../clients/reth_development.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-25/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-25/eval/reorg-safe/manifest.json) |

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

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H09](../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- Result shape at `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52
- Result shape at `15`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'erro
- Result shape at `30`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'error':
- Result shape at `33`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431
- Result shape at `35`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'erro

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H09](../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- Result shape at `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52
- Result shape at `15`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'erro
- Result shape at `30`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'error':
- Result shape at `33`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431
- Result shape at `35`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'erro

**Erigon · 3.9.0-dev · e91aca7f** (`3.9.0-dev-e91aca7f`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.2 · 8a3f3b2c** (`3.8.2-8a3f3b2c`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.11-unstable · edbd5f17** (`Geth/v1.17.11-unstable-edbd5f17-2026-11-18/linux-amd64/go1.26.1`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.4.0-preview · e2f069a6** (`2.4.0-preview+e2f069a6`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H09](../../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [3]: error 'Mutable Call In Static Context', result null.
- [H09](../../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [6, 0]: error None, result null.
- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `12`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'erro
- Result shape at `16`: {'action': {'address': '0x05032e03adbca6d5d04236000a2bbb6b4fec87f5', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'subtraces': 0, 'traceAddress': [6, 0], 'transa
- Result shape at `29`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'erro
- Result shape at `33`: {'action': {'address': '0x9ee5c90ad0a83dd07800c64adb87c584092f8e37', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'subtraces': 0, 'traceAddress': [6, 0], 'transa

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H33](../../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>

# Restored/filter tail

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Every phase range has exactly the frozen canonical roots and block hashes; restoration returns the original inventory.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../clients/besu_release.md) | 50 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../../clients/besu_development.md) | 50 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../clients/erigon_release.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../../clients/go-ethereum_trace.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | 50 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../../clients/nethermind_development.md) | 50 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../clients/reth_release.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../clients/reth_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |

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

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H09](../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- Result shape at `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- Result shape at `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52
- Result shape at `18`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'result': {'address': '0x05
- Result shape at `30`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'error':
- Result shape at `33`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431
- Result shape at `38`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'result': {'address': '0x9e

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- Result shape at `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- Result shape at `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52
- Result shape at `18`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'result': {'address': '0x05
- Result shape at `30`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'error':
- Result shape at `33`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431
- Result shape at `38`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'result': {'address': '0x9e

**Nethermind · 2.1.0-unstable · 641592d2** (`2.1.0-unstable+641592d2`)

- [H09](../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property
- Result shape at `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- Result shape at `10`: 'transactionHash' is a required property
- Result shape at `10`: 'transactionPosition' is a required property
- Result shape at `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property
- Result shape at `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- Result shape at `10`: 'transactionHash' is a required property
- Result shape at `10`: 'transactionPosition' is a required property
- Result shape at `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52

</details>

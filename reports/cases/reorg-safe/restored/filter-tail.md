# Restored/filter tail

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Failed frames have an error string and an explicit object or null result. Every phase range has exactly the frozen canonical roots and block hashes; restoration returns the original inventory.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../../clients/besu_release.md) | 50 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Besu · 🛠️ Development](../../../clients/besu_development.md) | 50 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Erigon · 📦 Release](../../../clients/erigon_release.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Erigon · 🛠️ Development](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../../clients/go-ethereum_trace.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Nethermind · 📦 Release](../../../clients/nethermind_release.md) | 50 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Nethermind · 🛠️ Development](../../../clients/nethermind_development.md) | 50 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Reth · 📦 Release](../../../clients/reth_release.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |
| [Reth · 🛠️ Development](../../../clients/reth_development.md) | 41 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x28",
      "toBlock": "0x30"
    }
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H09](../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- Result shape at `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52
- Result shape at `15`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'erro
- Result shape at `18`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'result': {'address': '0x05
- Result shape at `30`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'error':
- Result shape at `33`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431
- Result shape at `35`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'erro
- Result shape at `38`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'result': {'address': '0x9e

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- Result shape at `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52
- Result shape at `15`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'erro
- Result shape at `18`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'result': {'address': '0x05
- Result shape at `30`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'error':
- Result shape at `33`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431
- Result shape at `35`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'erro
- Result shape at `38`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'result': {'address': '0x9e

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property
- Result shape at `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- Result shape at `10`: 'transactionHash' is a required property
- Result shape at `10`: 'transactionPosition' is a required property
- Result shape at `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H09](../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property
- Result shape at `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- Result shape at `10`: 'transactionHash' is a required property
- Result shape at `10`: 'transactionPosition' is a required property
- Result shape at `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52

</details>

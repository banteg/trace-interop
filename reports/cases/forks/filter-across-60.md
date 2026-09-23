# Filter across 60

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** A fork-crossing range equals the corresponding per-block traces. Failed frames have an error string and an explicit object or null result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x3b",
      "toBlock": "0x3c"
    }
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): A fork-crossing range equals the corresponding per-block traces.
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000000000', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'gasUsed': '0x0',
- Result shape at `5`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x696e766f6b6564', 'to': '0xeda8645ba6948855e3b3cd596bbb07596d59c603', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'ga
- Result shape at `6`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xb917cfdc0d25b72d55cf94db328e1629b7f4fde2c30cdacf873b664416f76a0c7f7cc50c9f72a3cb84be88144cde91250000000000000d80', 'to': '0x00000961ef480eb55e80d19ad83579a64c007002', 'value': '0x3b9aca00'}, 'blockHash'
- Result shape at `7`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'gasUsed': '0x0

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): A fork-crossing range equals the corresponding per-block traces.
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000000000', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'gasUsed': '0x0',
- Result shape at `5`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x696e766f6b6564', 'to': '0xeda8645ba6948855e3b3cd596bbb07596d59c603', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'ga
- Result shape at `6`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xb917cfdc0d25b72d55cf94db328e1629b7f4fde2c30cdacf873b664416f76a0c7f7cc50c9f72a3cb84be88144cde91250000000000000d80', 'to': '0x00000961ef480eb55e80d19ad83579a64c007002', 'value': '0x3b9aca00'}, 'blockHash'
- Result shape at `7`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'gasUsed': '0x0

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `7`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'error':
- Result shape at `8`: 'transactionHash' is a required property
- Result shape at `8`: 'transactionPosition' is a required property

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `7`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'error':
- Result shape at `8`: 'transactionHash' is a required property
- Result shape at `8`: 'transactionPosition' is a required property

</details>

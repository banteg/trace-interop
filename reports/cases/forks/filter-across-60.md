# Filter across 60

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** A fork-crossing range equals the corresponding per-block traces. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x3b",
      "toBlock": "0x3c"
    }
  ]
}
```

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): A fork-crossing range equals the corresponding per-block traces.
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000000000', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'gasUsed': '0x0',
- Result shape at `5`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x696e766f6b6564', 'to': '0xeda8645ba6948855e3b3cd596bbb07596d59c603', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'ga
- Result shape at `6`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xb917cfdc0d25b72d55cf94db328e1629b7f4fde2c30cdacf873b664416f76a0c7f7cc50c9f72a3cb84be88144cde91250000000000000d80', 'to': '0x00000961ef480eb55e80d19ad83579a64c007002', 'value': '0x3b9aca00'}, 'blockHash'
- Result shape at `7`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'gasUsed': '0x0

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): A fork-crossing range equals the corresponding per-block traces.
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000000000', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'gasUsed': '0x0',
- Result shape at `5`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x696e766f6b6564', 'to': '0xeda8645ba6948855e3b3cd596bbb07596d59c603', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'ga
- Result shape at `6`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xb917cfdc0d25b72d55cf94db328e1629b7f4fde2c30cdacf873b664416f76a0c7f7cc50c9f72a3cb84be88144cde91250000000000000d80', 'to': '0x00000961ef480eb55e80d19ad83579a64c007002', 'value': '0x3b9aca00'}, 'blockHash'
- Result shape at `7`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'gasUsed': '0x0

**Nethermind · 2.1.0-preview · ce501a97** (`2.1.0-preview+ce501a97`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `7`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'error':
- Result shape at `8`: 'transactionHash' is a required property
- Result shape at `8`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `7`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'error':
- Result shape at `8`: 'transactionHash' is a required property
- Result shape at `8`: 'transactionPosition' is a required property

</details>

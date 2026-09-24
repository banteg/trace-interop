# Block 60

`trace_block` · forks · [All reports](../../README.md)

**What this checks:** A PoS block has no synthetic PoW reward records. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 6 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | 6 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 6 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | 6 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0x3c"
  ]
}
```

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'error':

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'error':

**Nethermind · 2.1.0-preview · ce501a97** (`2.1.0-preview+ce501a97`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'error':
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'error':
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property

</details>

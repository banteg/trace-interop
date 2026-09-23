# Filter across 56

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** A fork-crossing range equals the corresponding per-block traces.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 7 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 7 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-forks/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 7 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 7 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x37",
      "toBlock": "0x38"
    }
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): A fork-crossing range equals the corresponding per-block traces.
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x74fb911b03a9f447656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x3'}, 'blockHash': '0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3', 'blockNumber': 56, 'res
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x0e3c9c409810ef1d656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x3'}, 'blockHash': '0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3', 'blockNumber': 56, 'res
- Result shape at `5`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xaea813e13a3d0897656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3', 'blockNumber': 56, 'res

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): A fork-crossing range equals the corresponding per-block traces.
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x74fb911b03a9f447656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x3'}, 'blockHash': '0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3', 'blockNumber': 56, 'res
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x0e3c9c409810ef1d656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x3'}, 'blockHash': '0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3', 'blockNumber': 56, 'res
- Result shape at `5`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xaea813e13a3d0897656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3', 'blockNumber': 56, 'res

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property

</details>

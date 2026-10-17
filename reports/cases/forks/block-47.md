# Block 47

`trace_block` · forks · [All reports](../../README.md)

**What this checks:** Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/forks/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../clients/besu_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../clients/erigon_development.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../clients/go-ethereum_trace.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../clients/nethermind_development.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/forks/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../clients/reth_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0x2f"
  ]
}
```

**Erigon · 3.8.0-dev · 5b452f41** (`3.8.0-dev-5b452f41`)

- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x133d8', 'input': '0xea41c6626bd2d71a656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826', 'blo

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x133d8', 'input': '0xea41c6626bd2d71a656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826', 'blo

**Nethermind · 2.2.0-preview · cd336c4c** (`2.2.0-preview+cd336c4c`)

- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x133d8', 'input': '0xea41c6626bd2d71a656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826', 'blo

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x133d8', 'input': '0xea41c6626bd2d71a656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826', 'blo

</details>

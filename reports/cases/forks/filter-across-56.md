# Filter across 56

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. A fork-crossing range equals the corresponding per-block traces.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 7 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 7 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x37",
      "toBlock": "0x38"
    }
  ]
}
```

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): A fork-crossing range equals the corresponding per-block traces.
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x74fb911b03a9f447656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x3'}, 'blockHash': '0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3', 'blockNumber': 56, 'res
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x0e3c9c409810ef1d656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x3'}, 'blockHash': '0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3', 'blockNumber': 56, 'res
- Result shape at `5`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xaea813e13a3d0897656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3', 'blockNumber': 56, 'res

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): A fork-crossing range equals the corresponding per-block traces.
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x74fb911b03a9f447656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x3'}, 'blockHash': '0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3', 'blockNumber': 56, 'res
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x0e3c9c409810ef1d656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x3'}, 'blockHash': '0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3', 'blockNumber': 56, 'res
- Result shape at `5`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xaea813e13a3d0897656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3', 'blockNumber': 56, 'res

</details>

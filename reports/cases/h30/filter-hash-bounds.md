# Filter hash bounds

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Filter bounds are block numbers or tags, never block hashes: a hash bound is invalid params (-32602), as eth_getLogs range bounds. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/h30/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-28/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · a1ce80fb](../../clients/erigon_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-28/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-28/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/h30/manifest.json) |
| [Nethermind · 2.1.0-preview · 45912ba3](../../clients/nethermind_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-28/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/h30/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "toBlock": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "count": 3
    }
  ]
}
```

**Erigon · 3.8.0-dev · a1ce80fb** (`3.8.0-dev-a1ce80fb`)

- [H32](../../decisions/H32.md): Filter bounds are block numbers or tags, never block hashes: a hash bound is invalid params (-32602), as eth_getLogs range bounds. Observed result with output [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H32](../../decisions/H32.md): Filter bounds are block numbers or tags, never block hashes: a hash bound is invalid params (-32602), as eth_getLogs range bounds. Observed result with output [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433

**Nethermind · 2.1.0-preview · 45912ba3** (`2.1.0-preview+45912ba3`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H32](../../decisions/H32.md): Filter bounds are block numbers or tags, never block hashes: a hash bound is invalid params (-32602), as eth_getLogs range bounds. Observed result with output [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H32](../../decisions/H32.md): Filter bounds are block numbers or tags, never block hashes: a hash bound is invalid params (-32602), as eth_getLogs range bounds. Observed result with output [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

</details>

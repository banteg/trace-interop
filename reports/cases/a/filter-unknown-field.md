# Filter unknown field

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 13 records | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 13 records | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 14 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toBlock": "0x2",
      "unknownDiagnosticFlag": true
    }
  ]
}
```

**Erigon · 3.8.0-dev · 5cb6c867** (`3.8.0-dev-5cb6c867`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). Additional properties are not allowed ('unknownDiagnosticFlag' was unexpected)

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). Additional properties are not allowed ('unknownDiagnosticFlag' was unexpected)

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). Additional properties are not allowed ('unknownDiagnosticFlag' was unexpected)
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a9
- Result shape at `13`: 'transactionHash' is a required property
- Result shape at `13`: 'transactionPosition' is a required property

</details>

# Filter wrong address type

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |

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
      "fromAddress": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f"
    }
  ]
}
```

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f' is not valid under any of the given schemas
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

</details>

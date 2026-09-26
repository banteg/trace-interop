# Filter both unknown mode

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Malformed input returns invalid params (-32602). Unknown mode values return invalid params (-32602).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 6 records | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |

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
      "fromAddress": [
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f"
      ],
      "toAddress": [
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      ],
      "mode": "garbage"
    }
  ]
}
```

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 'garbage' is not valid under any of the given schemas
- [H03](../../decisions/H03.md): Unknown mode values return invalid params (-32602).

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 'garbage' is not valid under any of the given schemas
- [H03](../../decisions/H03.md): Unknown mode values return invalid params (-32602).

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 'garbage' is not valid under any of the given schemas
- [H03](../../decisions/H03.md): Unknown mode values return invalid params (-32602).

</details>

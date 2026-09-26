# Get integer path

`trace_get` · a · [All reports](../../README.md)

**What this checks:** Malformed input returns invalid params (-32602).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | One frame, path `[6, 0]` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      6,
      0
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 6 is not of type 'string'; 0 is not of type 'string'

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 6 is not of type 'string'; 0 is not of type 'string'

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 6 is not of type 'string'; 0 is not of type 'string'

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 6 is not of type 'string'; 0 is not of type 'string'

</details>

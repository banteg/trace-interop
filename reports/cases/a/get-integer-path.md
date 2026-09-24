# Get integer path

`trace_get` · a · [All reports](../../README.md)

**What this checks:** Malformed input returns invalid params (-32602).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/a/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/a/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/a/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/a/manifest.json) |
| [Nethermind · 2.1.0-unstable · 9d6e8b8d](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h17-retest/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/a/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | One frame, path `[6, 0]` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h17-retest/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
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

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 6 is not of type 'string'; 0 is not of type 'string'

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 6 is not of type 'string'; 0 is not of type 'string'

</details>

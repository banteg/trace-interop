# Get integer path

`trace_get` · a · [All reports](../../README.md)

**What this checks:** Malformed input returns invalid params (-32602).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../clients/anvil_development.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 558586f0](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Nethermind · 2.1.0-preview · 82516987](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | One frame, path `[6, 0]` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | One frame, path `[6, 0]` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |

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

**Anvil · 1.8.4-nightly · dd372126** (`anvil Version: 1.8.4-nightly+dd372126`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 6 is not of type 'string'; 0 is not of type 'string'

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 6 is not of type 'string'; 0 is not of type 'string'

**Reth · 2.5.2 · 5723a3fe** (`Reth Version: 2.5.2+5723a3fe`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 6 is not of type 'string'; 0 is not of type 'string'

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 6 is not of type 'string'; 0 is not of type 'string'

</details>

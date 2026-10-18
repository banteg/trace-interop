# Get integer path

`trace_get` · a · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | One frame, path `[6, 0]` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | One frame, path `[6, 0]` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | One frame, path `[6, 0]` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |

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

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). 6 is not of type 'string'; 0 is not of type 'string'

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). 6 is not of type 'string'; 0 is not of type 'string'

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). 6 is not of type 'string'; 0 is not of type 'string'

</details>

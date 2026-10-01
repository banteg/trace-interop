# Raw invalid

`trace_rawTransaction` · initial · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Malformed input returns an error (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0x00",
    [
      "trace"
    ]
  ]
}
```

</details>

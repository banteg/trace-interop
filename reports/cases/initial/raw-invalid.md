# Raw invalid

`trace_rawTransaction` · initial · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Malformed input returns invalid params (-32602).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 558586f0](../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · 82516987](../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |

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

**Erigon · 3.8.0-dev · 558586f0** (`3.8.0-dev-558586f0`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602).

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602).

**Nethermind · 2.1.0-preview · 82516987** (`2.1.0-preview+82516987`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602).

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602).

</details>

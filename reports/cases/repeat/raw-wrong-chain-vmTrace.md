# Raw wrong chain vmtrace

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0xf86481858477359400825208940000000000000000000000000000000000001234018026a0680e20ade3f3bfbbb3d8e2246c26a13efb3a8e886c182c159cd240b4636342b8a027a25d70c994f869fa5abe6b841ddfff0ab32944d6e9719c830ace909c024a3b",
    [
      "vmTrace"
    ]
  ]
}
```

</details>

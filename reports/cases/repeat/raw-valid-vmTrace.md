# Raw valid vmtrace

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b8185847735940082520894000000000000000000000000000000000000123401808718e5bb3abd10a0a0a8d391fb09e2f92ffc93fe7ac7b1eb7f1e24289f707eec0f34292c1713f795ffa0554e314f2ec6166290fc977d4bd4c86a9e0cadc2366f6139bd907d893bb4e237",
    [
      "vmTrace"
    ]
  ]
}
```

</details>

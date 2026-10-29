# Raw valid

`trace_rawTransaction` · a · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b8185847735940082520894000000000000000000000000000000000000123401808718e5bb3abd10a0a0a8d391fb09e2f92ffc93fe7ac7b1eb7f1e24289f707eec0f34292c1713f795ffa0554e314f2ec6166290fc977d4bd4c86a9e0cadc2366f6139bd907d893bb4e237",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

</details>

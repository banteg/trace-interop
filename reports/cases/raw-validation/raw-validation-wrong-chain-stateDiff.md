# Raw validation wrong chain statediff

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b0a842da282a9830186a094000000000000000000000000000000000000100201808718e5bb3abd10a1a0a9a71b4f058fd89aace7adbd5ee61eea3c2835bc1cc824d38ce04dbd2ebef001a03fada387bb48b772cd034614ca62886282abed9a436e4d6597823eef30208f07",
    [
      "stateDiff"
    ]
  ]
}
```

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. wrong chain identity

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. wrong chain identity

</details>

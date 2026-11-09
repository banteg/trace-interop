# Raw validation code sender statediff

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b0a842da282a9830186a094000000000000000000000000000000000000100201808718e5bb3abd109fa094743fd3c647965db4f4a93a99df9f01fa1eb63ec9a9f8bd998ca6dbadee6110a03c16275b8dc73e8b639d3db3633f951e03347784a7554b6b55d86662d53b12ac",
    [
      "stateDiff"
    ]
  ]
}
```

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)

</details>

# Raw validation code sender all

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
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
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (9 in total).
- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)
- Result shape at `vmTrace`: {'code': '0x602a600055602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 78997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 78994}, 'pc': 2, 'sub': None}, {'cost': 22100, 'ex': {'mem': None, 'pus

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (9 in total).
- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)
- Result shape at `vmTrace`: {'code': '0x602a600055602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 78997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 78994}, 'pc': 2, 'sub': None}, {'cost': 22100, 'ex': {'mem': None, 'pus

</details>

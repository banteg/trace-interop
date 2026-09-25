# Raw validation code sender statediff

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; output `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/raw-validation/manifest.json) |

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

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)

**Erigon · 3.8.0-dev · f8cfe5a7** (`3.8.0-dev-f8cfe5a7`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)

**Nethermind · 2.1.0-preview · ee1f57da** (`2.1.0-preview+ee1f57da`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)
- Result shape at `output`: None is not of type 'string'
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0xa874'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x0000000000000000000000000000000000001002': {'balance': {'*': {'from': '0x0', 'to': '0x1'}}, 'code': '=', 'nonce': '=', 'storage': {'0x00000000000000000000000000000000000

</details>

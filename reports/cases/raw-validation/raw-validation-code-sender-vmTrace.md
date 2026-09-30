# Raw validation code sender vmtrace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b0a842da282a9830186a094000000000000000000000000000000000000100201808718e5bb3abd109fa094743fd3c647965db4f4a93a99df9f01fa1eb63ec9a9f8bd998ca6dbadee6110a03c16275b8dc73e8b639d3db3633f951e03347784a7554b6b55d86662d53b12ac",
    [
      "vmTrace"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · e3429853** (`anvil Version: 1.8.4-nightly+e3429853`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)

**Nethermind · 2.2.0-preview · 79173d14** (`2.2.0-preview+79173d14`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 2: ex {"mem": null, "push": ["0x00"], "store": null, "used": 78994} (3 in total).
- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. EIP-3607 ordinary-code sender (not delegation)
- Result shape at `vmTrace`: {'code': '0x602a600055602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 78997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 78994}, 'pc': 2, 'sub': None}, {'cost': 22100, 'ex': {'mem': None, 'pu

</details>

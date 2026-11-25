# Nested callcode outer1 value0 failed

`trace_call` · precompile-values · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree. A handled precompile failure must not mark the successful parent as failed. The constructor returns the precompile call success bit; a funded successful call must return one. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/precompile-values/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/precompile-values/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/precompile-values/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/precompile-values/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/precompile-values/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/precompile-values/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/precompile-values/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/precompile-values/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/precompile-values/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/precompile-values/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/precompile-values/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x100000",
      "gasPrice": "0x3b9aca00",
      "value": "0x1",
      "data": "0x602a600052604060006080600060006006620186a0f260005260206000f3"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (15 in total).
- Result shape at `vmTrace`: {'code': '0x602a600052604060006080600060006006620186a0f260005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 995163}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995160}, 'pc': 2, 'sub': None}, {'cost':

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (15 in total).
- Result shape at `vmTrace`: {'code': '0x602a600052604060006080600060006006620186a0f260005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 995163}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995160}, 'pc': 2, 'sub': None}, {'cost':

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (16 in total).
- Result shape at `vmTrace`: {'code': '0x602a600052604060006080600060006006620186a0f260005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 995163}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995160}, 'pc': 2, 'sub': None}, {'cost':

</details>

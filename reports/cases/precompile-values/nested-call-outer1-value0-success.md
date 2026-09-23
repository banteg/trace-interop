# Nested call outer1 value0 success

`trace_call` · precompile-values · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree. A handled precompile failure must not mark the successful parent as failed. The constructor returns the precompile call success bit; a funded successful call must return one. Successful creation uses address, code and gasUsed. Stack words use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompile-values/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompile-values/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompile-values/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompile-values/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-precompile-values/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompile-values/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompile-values/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompile-values/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompile-values/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x6000600052604060006080600060006006620186a0f160005260206000f3",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x100000",
      "gasPrice": "0x3b9aca00",
      "value": "0x1"
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

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x6000600052604060006080600060006006620186a0f160005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995175}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995172}, 'pc': 2, 'sub': None}, {'cost'

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x6000600052604060006080600060006006620186a0f160005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995175}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995172}, 'pc': 2, 'sub': None}, {'cost'

</details>

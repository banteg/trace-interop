# Raw validation create nonce low all

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. Reject a signed transaction that fails execution validity at the selected state before EVM execution. Proposed transaction-validation error code: -32003 (Transaction rejected).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-raw-validation/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86009842da282a9830186a08001893060005260206000f38718e5bb3abd109fa0f79bc81b54de5c56b99760bc92863bb4742e555f6f81ff00d3d2b6b7e53fadcea055a3935137685afe3b9738bb7563deede6b29147ecb36f00519df0f94b08127b",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. creation nonce below selected state
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'init': '0x3060005260206000f3', 'value': '0x1'}, 'result': {'address': '0x66a15edcc3b50a663e72f1457ffd49b9ae284ddc', 'code': '0x', 'gasUsed': '0x0'}, 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. creation nonce below selected state
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'init': '0x3060005260206000f3', 'value': '0x1'}, 'result': {'address': '0x66a15edcc3b50a663e72f1457ffd49b9ae284ddc', 'code': '0x', 'gasUsed': '0x0'}, 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. creation nonce below selected state

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. creation nonce below selected state

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. creation nonce below selected state
- Result shape at `vmTrace`: {'code': '0x3060005260206000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x00de48310d77a4d56aa400248b0b1613508f5b73'], 'store': None, 'used': 46876}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 46873}, 'pc': 1, 'sub': None}, {'cost': 6, '

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. creation nonce below selected state
- Result shape at `vmTrace`: {'code': '0x3060005260206000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x00de48310d77a4d56aa400248b0b1613508f5b73'], 'store': None, 'used': 46876}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 46873}, 'pc': 1, 'sub': None}, {'cost': 6, '

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

</details>

# Raw validation execution oog valid vmtrace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 0 call frames; output `0x` | Checked cases agree; result shape differs | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 0 call frames; output `0x` | Checked cases agree; result shape differs | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 0 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 0 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 0 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 0 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 0 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 0 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86a0a842da282a982520894000000000000000000000000000000000000100201808718e5bb3abd109fa0438c25241c47cb30acced697295dbdc7efd1c51379f4d9a278676f0a234be35ba03a1865e41b9a3ae09cb8e900d0295dc60fa0d1412a2b6658dffc7498eb8ca34d",
    [
      "vmTrace"
    ]
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- Result shape at `vmTrace`: {'code': '0x602a600055602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': -3}, 'pc': 0, 'sub': None}]} is not valid under any of the given schemas

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- Result shape at `vmTrace`: {'code': '0x602a600055602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': -3}, 'pc': 0, 'sub': None}]} is not valid under any of the given schemas

</details>

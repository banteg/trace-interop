# Raw validation valid vmtrace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 0 call frames; nonempty output | Differs; result shape differs | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 0 call frames; nonempty output | Differs; result shape differs | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b0a842da282a9830186a094000000000000000000000000000000000000100201808718e5bb3abd109fa0a2f62f19fe621aee70421dbc7406655686d0cff2bedd6aaccbddf7f94b497168a068ee9aa988adb25c24c1dd48868f13ac72615bd55e2b471953c8ee9c824e66fe",
    [
      "vmTrace"
    ]
  ]
}
```

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x602a600055602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 78997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 78994}, 'pc': 2, 'sub': None}, {'cost': 22100, 'ex': {'mem': None, 'pu

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x602a600055602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 78997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 78994}, 'pc': 2, 'sub': None}, {'cost': 22100, 'ex': {'mem': None, 'pu

</details>

# Raw validation valid all

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. Requested stateDiff records the signed execution state changes. Marker stateDiff records slot zero changing from zero to word 42. Requested vmTrace contains the executing fixture bytecode and its opcode sequence. The valid signed control reports its expected execution success or halt in a root frame.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b0a842da282a9830186a094000000000000000000000000000000000000100201808718e5bb3abd109fa0a2f62f19fe621aee70421dbc7406655686d0cff2bedd6aaccbddf7f94b497168a068ee9aa988adb25c24c1dd48868f13ac72615bd55e2b471953c8ee9c824e66fe",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 2: ex {"mem": null, "push": ["0x00"], "store": null, "used": 78994} (4 in total).
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0xa874'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x0000000000000000000000000000000000001002': {'balance': {'*': {'from': '0x0', 'to': '0x1'}}, 'code': '=', 'nonce': '=', 'storage': {'0x00000000000000000000000000000000000
- Result shape at `vmTrace`: {'code': '0x602a600055602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 78997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 78994}, 'pc': 2, 'sub': None}, {'cost': 22100, 'ex': {'mem': None, 'pu

</details>

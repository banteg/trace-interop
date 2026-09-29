# Raw validation create valid vmtrace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. Requested vmTrace holds the executing fixture bytecode. Requested vmTrace lists every operation that began executing, in order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/raw-validation/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/raw-validation/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/raw-validation/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/raw-validation/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/raw-validation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/raw-validation/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf8600a842da282a9830186a08001893060005260206000f38718e5bb3abd109fa0371d5f6be359abfc8aa07862de5609e2374dea339665f9fcfe54ebfeef4e5d53a00de19f45781c0c3903dca51e8da7bf4ac28cc805e9a63e27c4bf1ef1d00f951a",
    [
      "vmTrace"
    ]
  ]
}
```

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H19](../../decisions/H19.md): Requested vmTrace holds the executing fixture bytecode. Expected 0x3060005260206000f3; got 0x.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: ex {"mem": null, "push": ["0x00de48310d77a4d56aa400248b0b1613508f5b73"], "store": null, "used": 46876} (3 in total).
- Result shape at `vmTrace`: {'code': '0x3060005260206000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x00de48310d77a4d56aa400248b0b1613508f5b73'], 'store': None, 'used': 46876}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 46873}, 'pc': 1, 'sub': None}, {'cost': 6, '

</details>

# Raw validation execution oog valid vmtrace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. Requested vmTrace holds the executing fixture bytecode. Requested vmTrace lists every operation that began executing, in order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 0 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 0 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 0 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-validation/manifest.json) |

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

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (1 in total).
- Result shape at `vmTrace`: {'code': '0x602a600055602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': -3}, 'pc': 0, 'sub': None}]} is not valid under any of the given schemas

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (1 in total).
- Result shape at `vmTrace`: {'code': '0x602a600055602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': -3}, 'pc': 0, 'sub': None}]} is not valid under any of the given schemas

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (1 in total).
- Result shape at `vmTrace`: {'code': '0x602a600055602a60005260206000f3', 'ops': [{'cost': 0, 'ex': None, 'pc': 0, 'sub': None}]} is not valid under any of the given schemas

</details>

# Raw validation create nonce high vmtrace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | RPC error `2` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf8600b842da282a9830186a08001893060005260206000f38718e5bb3abd109fa039e023bf345822f1fa4fc0e026feff8f8d28dfe3dde86558cd11810158c225a8a052a88956c9496272b462ea3bd33db78d8227a41b89ee335d38174bcd53e16d35",
    [
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. creation nonce above selected state

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. creation nonce above selected state

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. creation nonce above selected state

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. creation nonce above selected state

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. creation nonce above selected state

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: ex {"mem": null, "push": ["0x00de48310d77a4d56aa400248b0b1613508f5b73"], "store": null, "used": 46876} (3 in total).
- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. creation nonce above selected state
- Result shape at `vmTrace`: {'code': '0x3060005260206000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x00de48310d77a4d56aa400248b0b1613508f5b73'], 'store': None, 'used': 46876}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 46873}, 'pc': 1, 'sub': None}, {'cost': 6, '

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H13](../../decisions/H13.md): Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Identified nonce_high; code -32000; accepted [-32003, 2].

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H13](../../decisions/H13.md): Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Identified nonce_high; code -32000; accepted [-32003, 2].

</details>

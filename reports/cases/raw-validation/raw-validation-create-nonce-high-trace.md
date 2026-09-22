# Raw validation create nonce high trace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Reject a signed transaction that fails execution validity at the selected state before EVM execution. Proposed transaction-validation error code: -32003 (Transaction rejected).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 1 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 1 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 1 call frames; nonempty output | Differs | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 1 call frames; nonempty output | Differs | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 1 call frames; nonempty output | Differs | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 1 call frames; nonempty output | Differs | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-23/raw-validation-native/observations.json) · [Build/run](../../../evidence/2026-09-23/raw-validation-native/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf8600b842da282a9830186a08001893060005260206000f38718e5bb3abd109fa039e023bf345822f1fa4fc0e026feff8f8d28dfe3dde86558cd11810158c225a8a052a88956c9496272b462ea3bd33db78d8227a41b89ee335d38174bcd53e16d35",
    [
      "trace"
    ]
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. creation nonce above selected state
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'init': '0x3060005260206000f3', 'value': '0x1'}, 'result': {'address': '0xe69a847cd5bc0c9480ada0b339d7f0a8cac2b667', 'code': '0x', 'gasUsed': '0x0'}, 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. creation nonce above selected state
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'init': '0x3060005260206000f3', 'value': '0x1'}, 'result': {'address': '0xe69a847cd5bc0c9480ada0b339d7f0a8cac2b667', 'code': '0x', 'gasUsed': '0x0'}, 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. creation nonce above selected state

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. creation nonce above selected state

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. creation nonce above selected state

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. creation nonce above selected state

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

</details>

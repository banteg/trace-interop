# Raw below basefee trace

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution. Proposed transaction-validation error code: -32003 (Transaction rejected). Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 1 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 1 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/geth-e29edff-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-repeat/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | Incomplete or malformed JSON | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | Incomplete or malformed JSON | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86681850182520894000000000000000000000000000000000000123401808718e5bb3abd10a0a0a6525c23fcea9e006fece50614f7aaf6172e8bcc4cd6226480c174bbc055351c9fc17630ea66fe9c6ebfe8f96bb98c2433c16b43fc260cbd2530add6931d551a",
    [
      "trace"
    ]
  ]
}
```

**Geth draft fork · Draft fork** (`Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000001234', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000001234', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

</details>

# Raw validation funds gas all

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. Reject a signed transaction that fails execution validity at the selected state before EVM execution. Assess this declared topic case. Proposed transaction-validation error code: -32003 (Transaction rejected).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 1 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 1 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 1 call frames; nonempty output | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 1 call frames; nonempty output | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | Incomplete or malformed JSON | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | Incomplete or malformed JSON | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | RPC error `-32003` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | RPC error `-32003` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf8730a842da282a9830186a0940000000000000000000000000000000000001002880de0b6b3a7640000808718e5bb3abd10a0a08d1dbb3889e631f39d0e1b3c5eb58bc2211229b1e8d400981345f2fe4523c3dda0604a32a2b5e1837b5fb05e9bb78186db1760297eacb2b865f4860f9816aae7f9",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. value is affordable but upfront gas plus value is not
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0xde0b6b3a7640000'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. value is affordable but upfront gas plus value is not
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0xde0b6b3a7640000'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. value is affordable but upfront gas plus value is not

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. value is affordable but upfront gas plus value is not

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

</details>

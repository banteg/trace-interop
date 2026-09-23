# Raw validation below basefee all

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. Reject a signed transaction that fails execution validity at the selected state before EVM execution. Proposed transaction-validation error code: -32003 (Transaction rejected). Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b0a842da282a7830186a094000000000000000000000000000000000000100201808718e5bb3abd10a0a07848653cd9629ab7ae07a18eca2d43b09005c23eee0749e60660fe7825f88743a0281eb7c3cab9790d9d7f29b92f7457f58612499c7233f6dae068eb10a47bf837",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. gas price below selected block base fee
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. gas price below selected block base fee
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess the declared property. Cannot inspect this property: malformed_json.

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess the declared property. Cannot inspect this property: malformed_json.

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

</details>

# Root failed

`trace_call` · precompiles · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Retain the root precompile frame, even with zero value. A failed root precompile reports its own execution error. Failed frames have an error string and an explicit object or null result. Stack words use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 1 call frames; nonempty output | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 1 call frames; nonempty output | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 1 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 1 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-geth-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-geth-precompiles/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 1 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 1 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 1 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 1 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x000000000000000000000000000000000000000000000000000000000000002a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x100000",
      "gasPrice": "0x3b9aca00",
      "to": "0x0000000000000000000000000000000000000006"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A failed root precompile reports its own execution error.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A failed root precompile reports its own execution error.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xfabec', 'input': '0x000000000000000000000000000000000000000000000000000000000000002a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xfabec', 'input': '0x000000000000000000000000000000000000000000000000000000000000002a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

</details>

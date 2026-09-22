# State only nonempty output

`trace_call` · repeat · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. The return42 contract still returns word 42.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 1 call frames; nonempty output | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-geth-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-geth-repeat/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 0 call frames; output `null` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 0 call frames; output `null` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "to": "0x0000000000000000000000000000000000001002"
    },
    [
      "stateDiff"
    ],
    "0x30"
  ]
}
```

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H08](../../decisions/H08.md): Unrequested trace is an empty array.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H08](../../decisions/H08.md): The return42 contract still returns word 42.
- Result shape at `output`: None is not of type 'string'

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H08](../../decisions/H08.md): The return42 contract still returns word 42.
- Result shape at `output`: None is not of type 'string'

</details>

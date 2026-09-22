# Call mixed create

`trace_call` · a · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 3 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 3 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 3 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 3 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 3 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-geth-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-geth-a/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 3 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 3 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 3 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 3 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-a/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-a/manifest.json) |

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
      "to": "0x0000000000000000000000000000000000001006"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "0x30"
  ]
}
```

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x601761001b600039601760006000f050607b601760006000f55000600a61000d600039600a6000f3602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x17'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x001b'], 'store': None, 'used

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x601761001b600039601760006000f050607b601760006000f55000600a61000d600039600a6000f3602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x17'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x001b'], 'store': None, 'used

</details>

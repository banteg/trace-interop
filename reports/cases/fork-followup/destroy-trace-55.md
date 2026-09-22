# Destroy trace 55

`trace_call` · fork-followup · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. Delete code/nonce before Cancun; preserve an existing account after EIP-6780.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 2 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 2 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 2 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 2 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 2 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-geth-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-geth-fork-followup/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 2 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 2 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 2 call frames; output `0x` | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 2 call frames; output `0x` | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |

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
      "to": "0x0000000000000000000000000000000000001007"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "0x37"
  ]
}
```

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H26](../../decisions/H26.md): Delete code/nonce before Cancun; preserve an existing account after EIP-6780.
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a8742bfd', 'to': '0xc4f206a5aa5411442'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000001007': {'balance': {'*': {'from': '0x64', 'to': None}}, 'code': {'*': {'from': '0x611008ff

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H26](../../decisions/H26.md): Delete code/nonce before Cancun; preserve an existing account after EIP-6780.
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a8742bfd', 'to': '0xc4f206a5aa5411442'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000001007': {'balance': {'*': {'from': '0x64', 'to': None}}, 'code': {'*': {'from': '0x611008ff

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H26](../../decisions/H26.md): Delete code/nonce before Cancun; preserve an existing account after EIP-6780.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H26](../../decisions/H26.md): Delete code/nonce before Cancun; preserve an existing account after EIP-6780.

</details>

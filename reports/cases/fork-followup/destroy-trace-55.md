# Destroy trace 55

`trace_call` · fork-followup · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Report the exact deleted balance, code, nonce and empty storage before Cancun; preserve an existing account after EIP-6780. A deleted account reports storage {}; its account deletion implies every slot is wiped.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 2 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/fork-followup/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001007",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x"
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

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H26](../../decisions/H26.md): Report the exact deleted balance, code, nonce and empty storage before Cancun; preserve an existing account after EIP-6780.
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a8742bfd', 'to': '0xc4f206a5aa5411442'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000001007': {'balance': {'*': {'from': '0x64', 'to': None}}, 'code': {'*': {'from': '0x611008ff

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H26](../../decisions/H26.md): Report the exact deleted balance, code, nonce and empty storage before Cancun; preserve an existing account after EIP-6780.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H26](../../decisions/H26.md): Report the exact deleted balance, code, nonce and empty storage before Cancun; preserve an existing account after EIP-6780.

</details>

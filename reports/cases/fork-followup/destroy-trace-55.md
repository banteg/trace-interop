# Destroy trace 55

`trace_call` · fork-followup · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Report the exact deleted balance, code and nonce before Cancun; optional slot deletions match the known zero pre-values. Preserve an existing account after EIP-6780. A deleted account reports storage {} or optional old-slot - entries; account deletion implies every slot is wiped.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/fork-followup/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/fork-followup/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/fork-followup/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/fork-followup/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/fork-followup/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/fork-followup/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/fork-followup/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/fork-followup/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/fork-followup/manifest.json) |

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

</details>

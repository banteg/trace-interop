# Destroy trace 56

`trace_call` · fork-followup · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. Report the exact deleted code, nonce and empty storage before Cancun; preserve an existing account after EIP-6780.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/fork-followup/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/fork-followup/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/fork-followup/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/fork-followup/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/fork-followup/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/fork-followup/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../clients/nethermind_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/fork-followup/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/fork-followup/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/fork-followup/manifest.json) |

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
    "0x38"
  ]
}
```

</details>

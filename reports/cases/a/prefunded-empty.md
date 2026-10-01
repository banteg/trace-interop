# Prefunded empty

`trace_call` · a · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. An existing prefunded account does not acquire creation markers for empty code or zero nonce.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x000000000000000000000000000000000000100b",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x",
      "value": "0x1"
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

</details>

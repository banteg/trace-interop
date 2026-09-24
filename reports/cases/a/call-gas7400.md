# Call gas7400

`trace_call` · a · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001009",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x"
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

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x6174e060006101803700', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x74e0'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578994}, 'pc': 3, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0

</details>

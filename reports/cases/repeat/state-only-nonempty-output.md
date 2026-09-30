# State only nonempty output

`trace_call` · repeat · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. The return42 contract still returns word 42.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; output `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001002",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x"
    },
    [
      "stateDiff"
    ],
    "0x30"
  ]
}
```

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H08](../../decisions/H08.md): The return42 contract still returns word 42.
- Result shape at `output`: None is not of type 'string'

</details>

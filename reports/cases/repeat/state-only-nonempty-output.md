# State only nonempty output

`trace_call` · repeat · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. The return42 contract still returns word 42.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; output `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |

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

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H08](../../decisions/H08.md): Unrequested trace is an empty array.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H08](../../decisions/H08.md): The return42 contract still returns word 42.
- Result shape at `output`: None is not of type 'string'

</details>

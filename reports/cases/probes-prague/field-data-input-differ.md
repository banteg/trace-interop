# Field data input differ

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Malformed input returns invalid params (-32602). Disagreeing data and input are invalid params (-32602).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x602a60005260206000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "gasPrice": "0x77359400",
      "input": "0x600160005260206000f3"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Erigon · 3.8.0-dev · 01c118ee** (`3.8.0-dev-01c118ee`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). data and input must agree
- [H14](../../decisions/H14.md): Disagreeing data and input are invalid params (-32602). Observed result with output 0x000000000000000000000000000000000000000000000000000000000000002a

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). data and input must agree
- [H14](../../decisions/H14.md): Disagreeing data and input are invalid params (-32602). Observed result with output 0x000000000000000000000000000000000000000000000000000000000000002a

**Nethermind · 2.1.0-preview · 54b760cd** (`2.1.0-preview+54b760cd`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). data and input must agree
- [H14](../../decisions/H14.md): Disagreeing data and input are invalid params (-32602). Observed result with output 0x0000000000000000000000000000000000000000000000000000000000000001

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). data and input must agree
- [H14](../../decisions/H14.md): Disagreeing data and input are invalid params (-32602). Observed result with output 0x0000000000000000000000000000000000000000000000000000000000000001

</details>

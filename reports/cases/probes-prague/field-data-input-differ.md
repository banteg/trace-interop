# Field data input differ

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended). Disagreeing data and input are rejected (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |

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

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). data and input must agree
- [H14](../../decisions/H14.md): Disagreeing data and input are rejected (-32602 recommended). Observed result with output 0x0000000000000000000000000000000000000000000000000000000000000001

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). data and input must agree
- [H14](../../decisions/H14.md): Disagreeing data and input are rejected (-32602 recommended). Observed result with output 0x0000000000000000000000000000000000000000000000000000000000000001

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). data and input must agree
- [H14](../../decisions/H14.md): Disagreeing data and input are rejected (-32602 recommended). Observed result with output 0x000000000000000000000000000000000000000000000000000000000000002a

**Nethermind · 2.2.0-preview · 287f54f0** (`2.2.0-preview+287f54f0`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). data and input must agree
- [H14](../../decisions/H14.md): Disagreeing data and input are rejected (-32602 recommended). Observed result with output 0x0000000000000000000000000000000000000000000000000000000000000001

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). data and input must agree
- [H14](../../decisions/H14.md): Disagreeing data and input are rejected (-32602 recommended). Observed result with output 0x0000000000000000000000000000000000000000000000000000000000000001

</details>

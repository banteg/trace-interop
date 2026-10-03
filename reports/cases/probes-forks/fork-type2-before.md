# Fork type2 before

`trace_call` · probes-forks · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. An explicit type 2 with no dynamic-fees fields runs at block 35, before London (block 36): type is not a feature.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |

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
      "gas": "0x186a0",
      "to": "0x00000000000000000000000000000000000000ee",
      "type": "0x2"
    },
    [
      "trace"
    ],
    "0x23"
  ]
}
```

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): An explicit type 2 with no dynamic-fees fields runs at block 35, before London (block 36): type is not a feature. Expected a result; observed rpc_error -32003 transaction type not supported

</details>

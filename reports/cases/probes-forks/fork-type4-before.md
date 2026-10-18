# Fork type4 before

`trace_call` · probes-forks · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. An explicit type 4 with no authorization fields runs at block 59, before Prague (block 60): type is not a feature.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/depth-precompile/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/depth-precompile/probes-forks/manifest.json) |

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
      "type": "0x4"
    },
    [
      "trace"
    ],
    "0x3b"
  ]
}
```

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H14](../../decisions/H14.md): An explicit type 4 with no authorization fields runs at block 59, before Prague (block 60): type is not a feature. Expected a result; observed rpc_error -32603 Internal error

</details>

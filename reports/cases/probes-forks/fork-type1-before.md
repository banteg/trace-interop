# Fork type1 before

`trace_call` · probes-forks · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-forks/manifest.json) |

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
      "type": "0x1"
    },
    [
      "trace"
    ],
    "0x1f"
  ]
}
```

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. Expected a result; observed rpc_error -32603 Internal error

</details>

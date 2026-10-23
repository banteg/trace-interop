# Fork blob empty before

`trace_call` · probes-forks · [All reports](../../README.md)

**What this checks:** An empty blobVersionedHashes list at block 55, before Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.1 · e83703cd](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../clients/reth_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../clients/reth_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "blobVersionedHashes": [],
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x186a0",
      "maxFeePerGas": "0x0",
      "maxPriorityFeePerGas": "0x0",
      "to": "0x00000000000000000000000000000000000000ee"
    },
    [
      "trace"
    ],
    "0x37"
  ]
}
```

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 55, before Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. Observed rpc_error -32603: Internal error (-32003 recommended)

</details>

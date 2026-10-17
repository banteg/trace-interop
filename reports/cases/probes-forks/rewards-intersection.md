# Rewards intersection

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** A reward has no from side, so an intersection with a populated fromAddress excludes it.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | 🚧 Blocked | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../clients/besu_development.md) | RPC error `-32602` | 🚧 Blocked | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromAddress": [
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f"
      ],
      "fromBlock": "0x2",
      "mode": "intersection",
      "toAddress": [
        "0x0000000000000000000000000000000000000000"
      ],
      "toBlock": "0x5"
    }
  ]
}
```

**Besu · 26.10-develop · 0776d82f** (`besu/v26.10-develop-0776d82/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A reward has no from side, so an intersection with a populated fromAddress excludes it. Depends on H03: The request names the default mode explicitly, so a server that rejects the mode field fails before matching rewards. Observed rpc_error -32602 Invalid filter params.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A reward has no from side, so an intersection with a populated fromAddress excludes it. Depends on H03: The request names the default mode explicitly, so a server that rejects the mode field fails before matching rewards. Observed rpc_error -32602 Invalid filter params.

</details>

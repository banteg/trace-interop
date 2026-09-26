# Range reversed

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** An explicit fromBlock above toBlock is invalid params (-32602), as eth_getLogs does.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x3",
      "toBlock": "0x2"
    }
  ]
}
```

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H06](../../decisions/H06.md): An explicit fromBlock above toBlock is invalid params (-32602), as eth_getLogs does. Observed rpc_error -32000: invalid parameters: fromBlock cannot be greater than toBlock

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H06](../../decisions/H06.md): An explicit fromBlock above toBlock is invalid params (-32602), as eth_getLogs does. Observed rpc_error -32000: invalid parameters: fromBlock cannot be greater than toBlock

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H06](../../decisions/H06.md): An explicit fromBlock above toBlock is invalid params (-32602), as eth_getLogs does. Observed rpc_error -32000: From block number: 3 is greater than to block number 2

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H06](../../decisions/H06.md): An explicit fromBlock above toBlock is invalid params (-32602), as eth_getLogs does. Observed rpc_error -32000: From block number: 3 is greater than to block number 2

</details>

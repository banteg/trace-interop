# Rewards window

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** A page over matching records crosses a block boundary and reward records in block, transaction, reward order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 5 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 5 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | 🚧 Blocked | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 5 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "after": 3,
      "count": 5,
      "fromAddress": [
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f"
      ],
      "fromBlock": "0x2",
      "mode": "union",
      "toAddress": [
        "0x0000000000000000000000000000000000000000"
      ],
      "toBlock": "0x4"
    }
  ]
}
```

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): A page over matching records crosses a block boundary and reward records in block, transaction, reward order. Expected a result; observed rpc_error -32602 Invalid filter params

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): A page over matching records crosses a block boundary and reward records in block, transaction, reward order. Expected a result; observed rpc_error -32602 Invalid filter params

**Erigon · 3.8.0-dev · 85e1ca92** (`3.8.0-dev-85e1ca92`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `4`: 'transactionHash' is a required property
- Result shape at `4`: 'transactionPosition' is a required property

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `4`: 'transactionHash' is a required property
- Result shape at `4`: 'transactionPosition' is a required property

**Nethermind · 2.2.0-preview · f69690c5** (`2.2.0-preview+f69690c5`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `4`: 'transactionHash' is a required property
- Result shape at `4`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H03](../../decisions/H03.md): A page over matching records crosses a block boundary and reward records in block, transaction, reward order. Depends on H23, which differs for this build in rewards-to, rewards-union. record 0 missing; expected {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0x395e712438dd92dc5d88276418e20a940d2ce71bd6a5c28cc62dab41acdd6436', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}

</details>

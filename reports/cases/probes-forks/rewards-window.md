# Rewards window

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** A page over matching records crosses a block boundary and reward records in block, transaction, reward order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 5 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | 5 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | `[]` | 🚧 Blocked | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | 5 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |

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

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): A page over matching records crosses a block boundary and reward records in block, transaction, reward order. Expected a result; observed rpc_error -32602 Invalid filter params

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): A page over matching records crosses a block boundary and reward records in block, transaction, reward order. Expected a result; observed rpc_error -32602 Invalid filter params

**Erigon · 3.8.0-dev · 6da806cb** (`3.8.0-dev-6da806cb`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `4`: 'transactionHash' is a required property
- Result shape at `4`: 'transactionPosition' is a required property

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `4`: 'transactionHash' is a required property
- Result shape at `4`: 'transactionPosition' is a required property

**Nethermind · 2.2.0-preview · 3370d566** (`2.2.0-preview+3370d566`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `4`: 'transactionHash' is a required property
- Result shape at `4`: 'transactionPosition' is a required property

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H03](../../decisions/H03.md): A page over matching records crosses a block boundary and reward records in block, transaction, reward order. Depends on H23, which differs for this build in rewards-to, rewards-union. record 0 missing; expected {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0x395e712438dd92dc5d88276418e20a940d2ce71bd6a5c28cc62dab41acdd6436', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}

</details>

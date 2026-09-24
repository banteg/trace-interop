# Rewards to

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** A reward matches toAddress by author, after its block's transactions: block reward, then uncle rewards in ommer order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 8 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 8 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 8 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 8 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 8 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toAddress": [
        "0x0000000000000000000000000000000000000000"
      ],
      "toBlock": "0x5"
    }
  ]
}
```

**Besu · 26.9-develop · cf89071f** (`besu/v26.9-develop-cf89071/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A reward matches toAddress by author, after its block's transactions: block reward, then uncle rewards in ommer order. record 0 missing; expected {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0x395e712438dd92dc5d88276418e20a940d2ce71bd6a5c28cc62dab41acdd6436', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A reward matches toAddress by author, after its block's transactions: block reward, then uncle rewards in ommer order. record 0 missing; expected {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0x395e712438dd92dc5d88276418e20a940d2ce71bd6a5c28cc62dab41acdd6436', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}

**Erigon · 3.8.0-dev · 01c118ee** (`3.8.0-dev-01c118ee`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `1`: 'transactionHash' is a required property
- Result shape at `1`: 'transactionPosition' is a required property
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `1`: 'transactionHash' is a required property
- Result shape at `1`: 'transactionPosition' is a required property
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Nethermind · 2.1.0-preview · 54b760cd** (`2.1.0-preview+54b760cd`)

- [H23](../../decisions/H23.md): A reward matches toAddress by author, after its block's transactions: block reward, then uncle rewards in ommer order. record 0 missing; expected {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0x395e712438dd92dc5d88276418e20a940d2ce71bd6a5c28cc62dab41acdd6436', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H23](../../decisions/H23.md): A reward matches toAddress by author, after its block's transactions: block reward, then uncle rewards in ommer order. record 0 missing; expected {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0x395e712438dd92dc5d88276418e20a940d2ce71bd6a5c28cc62dab41acdd6436', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `1`: 'transactionHash' is a required property
- Result shape at `1`: 'transactionPosition' is a required property
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

</details>

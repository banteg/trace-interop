# Genesis range rewards

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** A range from genesis contributes no genesis reward; blocks 1 and 2 contribute their block rewards.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x0",
      "toAddress": [
        "0x0000000000000000000000000000000000000000"
      ],
      "toBlock": "0x2"
    }
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A range from genesis contributes no genesis reward; blocks 1 and 2 contribute their block rewards. record 0 missing; expected {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0xca7c8aea26c81f9bdb4d4a3e9ededebaa234273e58973c278705573b99ca4c97', 'blockNumber': 1, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A range from genesis contributes no genesis reward; blocks 1 and 2 contribute their block rewards. record 0 missing; expected {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0xca7c8aea26c81f9bdb4d4a3e9ededebaa234273e58973c278705573b99ca4c97', 'blockNumber': 1, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}

**Erigon · 3.8.0-dev · f8cfe5a7** (`3.8.0-dev-f8cfe5a7`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `1`: 'transactionHash' is a required property
- Result shape at `1`: 'transactionPosition' is a required property

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `1`: 'transactionHash' is a required property
- Result shape at `1`: 'transactionPosition' is a required property

**Nethermind · 2.1.0-preview · ee1f57da** (`2.1.0-preview+ee1f57da`)

- [H05](../../decisions/H05.md): A range from genesis contributes no genesis reward; blocks 1 and 2 contribute their block rewards. record 0 missing; expected {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0xca7c8aea26c81f9bdb4d4a3e9ededebaa234273e58973c278705573b99ca4c97', 'blockNumber': 1, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H05](../../decisions/H05.md): A range from genesis contributes no genesis reward; blocks 1 and 2 contribute their block rewards. record 0 missing; expected {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0xca7c8aea26c81f9bdb4d4a3e9ededebaa234273e58973c278705573b99ca4c97', 'blockNumber': 1, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H05](../../decisions/H05.md): A range from genesis contributes no genesis reward; blocks 1 and 2 contribute their block rewards. record 0: expected {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0xca7c8aea26c81f9bdb4d4a3e9ededebaa234273e58973c278705573b99ca4c97', 'blockNumber': 1, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}, got {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0xcf99eb0a280bf38e32a54b8cb1d4403fd277ef7b4ff1836b6b2dc3d8d098e409', 'blockNumber': 0, 'result': None, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}
- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `1`: 'transactionHash' is a required property
- Result shape at `1`: 'transactionPosition' is a required property
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

</details>

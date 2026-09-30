# Genesis range rewards

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** A range from genesis contributes no genesis reward; blocks 1 and 2 contribute their block rewards.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-forks/manifest.json) |

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

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A range from genesis contributes no genesis reward; blocks 1 and 2 contribute their block rewards. record 0 missing; expected {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0xca7c8aea26c81f9bdb4d4a3e9ededebaa234273e58973c278705573b99ca4c97', 'blockNumber': 1, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A range from genesis contributes no genesis reward; blocks 1 and 2 contribute their block rewards. record 0 missing; expected {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0xca7c8aea26c81f9bdb4d4a3e9ededebaa234273e58973c278705573b99ca4c97', 'blockNumber': 1, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}

**Erigon · 3.8.0-dev · 85e1ca92** (`3.8.0-dev-85e1ca92`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `1`: 'transactionHash' is a required property
- Result shape at `1`: 'transactionPosition' is a required property

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `1`: 'transactionHash' is a required property
- Result shape at `1`: 'transactionPosition' is a required property

**Nethermind · 2.2.0-preview · f69690c5** (`2.2.0-preview+f69690c5`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `1`: 'transactionHash' is a required property
- Result shape at `1`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H05](../../decisions/H05.md): A range from genesis contributes no genesis reward; blocks 1 and 2 contribute their block rewards. record 0 missing; expected {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0xca7c8aea26c81f9bdb4d4a3e9ededebaa234273e58973c278705573b99ca4c97', 'blockNumber': 1, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}

</details>

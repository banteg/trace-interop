# Filter 35

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. A single-block filter agrees with trace_block at the same fork.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x23",
      "toBlock": "0x23"
    }
  ]
}
```

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress []: error None, result null.
- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `2`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x1c9f78d2893e4000'}, 'blockHash': '0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f', 'blockNumber': 35, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under an
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'uncle', 'value': '0x18493fba64ef0000'}, 'blockHash': '0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f', 'blockNumber': 35, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under an
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress []: error None, result null.
- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `2`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x1c9f78d2893e4000'}, 'blockHash': '0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f', 'blockNumber': 35, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under an
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'uncle', 'value': '0x18493fba64ef0000'}, 'blockHash': '0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f', 'blockNumber': 35, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under an
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

</details>

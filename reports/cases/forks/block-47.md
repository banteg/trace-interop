# Block 47

`trace_block` · forks · [All reports](../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/forks/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/forks/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/forks/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/forks/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/forks/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/forks/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0x2f"
  ]
}
```

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress []: error None, result null.
- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `2`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x1c9f78d2893e4000'}, 'blockHash': '0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826', 'blockNumber': 47, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under an
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'uncle', 'value': '0x18493fba64ef0000'}, 'blockHash': '0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826', 'blockNumber': 47, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under an
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

</details>

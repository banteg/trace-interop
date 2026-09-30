# Block 51

`trace_block` · forks · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. A PoS block has no synthetic PoW reward records. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 12 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 12 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 11 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 11 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 11 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 12 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 11 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 11 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 11 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0x33"
  ]
}
```

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x0', 'input': '0x', 'to': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'value': '0x1'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'result': {'g

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x0', 'input': '0x', 'to': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'value': '0x1'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'result': {'g

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x0', 'input': '0x', 'to': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'value': '0x1'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'result': {'g

</details>

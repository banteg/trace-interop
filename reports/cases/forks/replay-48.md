# Replay 48

`trace_replayBlockTransactions` · forks · [All reports](../../README.md)

**What this checks:** Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Block replay has exactly one envelope per frozen transaction, with hashes in transaction order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x30",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a8636459', 'to': '0xc4f200cb8a8642ef5'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b3487fa7

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a8636459', 'to': '0xc4f200cb8a8642ef5'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b3487fa7

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a8636459', 'to': '0xc4f200cb8a8642ef5'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b3487fa7

</details>

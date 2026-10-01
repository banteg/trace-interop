# Replay 60

`trace_replayBlockTransactions` · forks · [All reports](../../README.md)

**What this checks:** Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Block replay has exactly one envelope per frozen transaction, with hashes in transaction order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x3c",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x36156009575f355f555b305f525f5460205260405ff3', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a87c8295', 'to': '0xc4f200cb8a87d6506'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balanc

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x36156009575f355f555b305f525f5460205260405ff3', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a87c8295', 'to': '0xc4f200cb8a87d6506'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balanc

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x36156009575f355f555b305f525f5460205260405ff3', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a87c8295', 'to': '0xc4f200cb8a87d6506'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balanc

</details>

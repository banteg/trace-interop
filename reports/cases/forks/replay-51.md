# Replay 51

`trace_replayBlockTransactions` · forks · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. An account created and destroyed within the transaction is absent at both endpoints and has no account diff.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x33",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a86a25b7', 'to': '0xc4f200cb8a86a77bf'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b34838c6

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a86a25b7', 'to': '0xc4f200cb8a86a77bf'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b34838c6

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a86a25b7', 'to': '0xc4f200cb8a86a77bf'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b34838c6

</details>

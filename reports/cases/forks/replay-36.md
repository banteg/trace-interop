# Replay 36

`trace_replayBlockTransactions` · forks · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. An account created and destroyed within the transaction is absent at both endpoints and has no account diff.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/forks/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x24",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x', 'revertReason': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xa9d71bf4a79560

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x', 'revertReason': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xa9d71bf4a79560

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xa9d71bf4a79560ea9', 'to': '0xa9d71bf

</details>

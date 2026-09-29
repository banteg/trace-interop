# Replay 36

`trace_replayBlockTransactions` · forks · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. An account created and destroyed within the transaction is absent at both endpoints and has no account diff.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/forks/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/forks/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/forks/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/forks/manifest.json) |

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

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x', 'revertReason': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xa9d71bf4a79560

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x', 'revertReason': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xa9d71bf4a79560

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xa9d71bf4a79560ea9', 'to': '0xa9d71bf

</details>

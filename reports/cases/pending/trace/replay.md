# Trace/replay

`trace_replayBlockTransactions` · pending · [All reports](../../../README.md)

**What this checks:** Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../../clients/besu_release.md) | 3 records | ⚠️ Differs | [Response](../../../../evidence/2026-10-18/eval-pending/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval-pending/pending/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../../clients/besu_development.md) | 3 records | ⚠️ Differs | [Response](../../../../evidence/2026-10-18/eval-pending/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval-pending/pending/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval-pending/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval-pending/pending/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval-pending/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval-pending/pending/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval-pending/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval-pending/pending/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval-pending/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval-pending/pending/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval-pending/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval-pending/pending/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval-pending/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval-pending/pending/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval-pending/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval-pending/pending/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "pending",
    [
      "trace"
    ]
  ]
}
```

**Besu · 26.10-develop · 0776d82f** (`besu/v26.10-develop-0776d82/linux-x86_64/openjdk-java-25`)

- [H32](../../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. 3 envelopes, 3 of them canonical transactions. The pooled transaction 0xa5ecd8bea38daf73327710f814278a9dd16292def35e16dc5e1aa6165face4a4 is missing.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H32](../../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. 3 envelopes, 3 of them canonical transactions. The pooled transaction 0xa5ecd8bea38daf73327710f814278a9dd16292def35e16dc5e1aa6165face4a4 is missing.

</details>

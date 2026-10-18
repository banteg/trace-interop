# Trace/block

`trace_block` · pending · [All reports](../../../README.md)

**What this checks:** Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../../clients/besu_release.md) | 4 records | ⚠️ Differs | [Response](../../../../evidence/2026-10-18/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/pending/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../../clients/besu_development.md) | 4 records | ⚠️ Differs | [Response](../../../../evidence/2026-10-18/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/pending/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/pending/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/pending/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/pending/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/pending/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/pending/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/pending/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/pending/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "pending"
  ]
}
```

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H32](../../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. Records from blocks [48]; the head is 48. The pooled transaction 0xa5ecd8bea38daf73327710f814278a9dd16292def35e16dc5e1aa6165face4a4 is missing.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H32](../../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. Records from blocks [48]; the head is 48. The pooled transaction 0xa5ecd8bea38daf73327710f814278a9dd16292def35e16dc5e1aa6165face4a4 is missing.

</details>

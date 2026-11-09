# Trace/block

`trace_block` · pending · [All reports](../../../README.md)

**What this checks:** Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.0 · 0e595f9e](../../../clients/besu_release.md) | 4 records | ⚠️ Differs | [Response](../../../../evidence/2026-11-09/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/pending/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/pending/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/pending/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/pending/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/pending/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/pending/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/pending/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/pending/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/pending/manifest.json) |

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

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H32](../../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. Records from blocks [48] with hashes ['0xf0b1510b2a9c8d4c4bd1ff2c578ddbffc04741aa06b3cc8680a343741ef15e84']; the head is 48. 0xf0b1510b2a9c8d4c4bd1ff2c578ddbffc04741aa06b3cc8680a343741ef15e84 is a canonical block hash. The pooled transaction 0xa5ecd8bea38daf73327710f814278a9dd16292def35e16dc5e1aa6165face4a4 is missing.

</details>

# Trace/block

`trace_block` · pending · [All reports](../../../README.md)

**What this checks:** Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.1 · e83703cd](../../../clients/besu_release.md) | 4 records | ⚠️ Differs | [Response](../../../../evidence/2026-10-23/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/pending/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../../clients/besu_development.md) | 4 records | ⚠️ Differs | [Response](../../../../evidence/2026-10-23/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/pending/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/pending/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/pending/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/pending/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/pending/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/pending/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/pending/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/pending/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/pending/manifest.json) |

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

**Besu · 26.10-develop · 781a7e1d** (`besu/v26.10-develop-781a7e1/linux-x86_64/openjdk-java-25`)

- [H32](../../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. Records from blocks [48]; the head is 48. The pooled transaction 0xa5ecd8bea38daf73327710f814278a9dd16292def35e16dc5e1aa6165face4a4 is missing.

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- [H32](../../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. Records from blocks [48]; the head is 48. The pooled transaction 0xa5ecd8bea38daf73327710f814278a9dd16292def35e16dc5e1aa6165face4a4 is missing.

</details>

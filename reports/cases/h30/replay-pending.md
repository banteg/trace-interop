# Replay pending

`trace_replayBlockTransactions` · h30 · [All reports](../../README.md)

**What this checks:** Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | `[]` | 🚧 Blocked | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `[]` | 🚧 Blocked | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | `[]` | 🚧 Blocked | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayBlockTransactions",
  "params": [
    "pending",
    [
      "trace"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · df92604b** (`anvil Version: 1.8.4-nightly+df92604b`)

- [H32](../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. 3 envelopes, 3 of them canonical transactions.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H32](../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. 3 envelopes, 3 of them canonical transactions.

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. 3 envelopes, 3 of them canonical transactions.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. 3 envelopes, 3 of them canonical transactions.

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H32](../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. An empty result names no block, so it cannot show a pending environment.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H32](../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. 3 envelopes, 3 of them canonical transactions.

**Reth · 2.7.0 · 5b686303** (`Reth Version: 2.7.0+5b686303`)

- [H32](../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. An empty result names no block, so it cannot show a pending environment.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H32](../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. An empty result names no block, so it cannot show a pending environment.

</details>

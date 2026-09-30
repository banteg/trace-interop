# Restored/filter hash a

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Once branch A is restored, the hash of its block 0x2d selects A’s records again. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | 4 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../../clients/besu_development.md) | 4 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../clients/erigon_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../../clients/go-ethereum_trace.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../../clients/nethermind_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-09-30/refresh/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-30/refresh/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xe6d9078b4964bc1b329fb12242254e21cf88ffa9a88058e515d6e79f7d8fce0d"
    }
  ]
}
```

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Once branch A is restored, the hash of its block 0x2d selects A’s records again. Answered another block: 4 records from block 0x30 (the head), where the numeric equivalent restored/filter-tail has 3 records from block 0x2d.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Once branch A is restored, the hash of its block 0x2d selects A’s records again. Answered another block: 4 records from block 0x30 (the head), where the numeric equivalent restored/filter-tail has 3 records from block 0x2d.

**Erigon · 3.8.0-dev · 85e1ca92** (`3.8.0-dev-85e1ca92`)

- [H33](../../../decisions/H33.md): Assess this declared topic case. Scenario setup stopped: Invalid forkchoice state

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H33](../../../decisions/H33.md): Assess this declared topic case. Scenario setup stopped: Invalid forkchoice state

**Geth draft fork · 1.17.7-unstable · e26833e3** (`Geth/v1.17.7-unstable-e26833e3-2026-09-26/linux-amd64/go1.26.1`)

- [H33](../../../decisions/H33.md): Once branch A is restored, the hash of its block 0x2d selects A’s records again. Rejected (-32602: invalid argument 0: json: unknown field "blockHash"), where the numeric equivalent restored/filter-tail has 2 records from block 0x2d.

**Nethermind · 2.2.0-preview · f69690c5** (`2.2.0-preview+f69690c5`)

- [H33](../../../decisions/H33.md): Once branch A is restored, the hash of its block 0x2d selects A’s records again. Rejected (-32602: Invalid params), where the numeric equivalent restored/filter-tail has 2 records from block 0x2d.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H33](../../../decisions/H33.md): Once branch A is restored, the hash of its block 0x2d selects A’s records again. Answered another block: 4 records from block 0x30 (the head), where the numeric equivalent restored/filter-tail has 3 records from block 0x2d.
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H33](../../../decisions/H33.md): Once branch A is restored, the hash of its block 0x2d selects A’s records again. Rejected (-32602: Invalid params), where the numeric equivalent restored/filter-tail has 2 records from block 0x2d.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../../decisions/H33.md): Once branch A is restored, the hash of its block 0x2d selects A’s records again. Rejected (-32602: Invalid params), where the numeric equivalent restored/filter-tail has 2 records from block 0x2d.

</details>

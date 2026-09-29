# Restored/filter hash b

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001 recommended), never A’s records. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../../clients/besu_release.md) | 4 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../../clients/besu_development.md) | 4 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../clients/erigon_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../../clients/nethermind_development.md) | 3 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-09-29/h33-blockhash/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xb75975dcf8dc29c9d8f63272511a20eb5c16c8466634e83f6b840d3baaa54110"
    }
  ]
}
```

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001 recommended), never A’s records. Accepted: answered another block, 4 records from block 0x30 (the head).

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001 recommended), never A’s records. Accepted: answered another block, 4 records from block 0x30 (the head).

**Erigon · 3.8.0-dev · a2a19253** (`3.8.0-dev-a2a19253`)

- [H33](../../../decisions/H33.md): Assess this declared topic case. Scenario setup stopped: Invalid forkchoice state

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H33](../../../decisions/H33.md): Assess this declared topic case. Scenario setup stopped: Invalid forkchoice state

**Nethermind · 2.2.0-preview · 287f54f0** (`2.2.0-preview+287f54f0`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001 recommended), never A’s records. Accepted: answered another block, 3 records from block 0x30 (the head).

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001 recommended), never A’s records. Accepted: answered another block, 4 records from block 0x30 (the head).
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

</details>

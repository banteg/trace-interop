# Transaction selfdestruct self

`trace_transaction` · mined-probes · [All reports](../../README.md)

**What this checks:** SELFDESTRUCT emits one suicide frame under the call. The suicide frame records the contract’s whole balance transferred to itself. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_transaction",
  "params": [
    "0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2"
  ]
}
```

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

</details>

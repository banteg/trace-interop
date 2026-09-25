# Transaction refund capped

`trace_transaction` · mined-probes · [All reports](../../README.md)

**What this checks:** The storage program is one call frame. Root gasUsed is execution gas before the refund (10009, refund 9600, receipt 24808). Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_transaction",
  "params": [
    "0xaab516a3fb838f33cf12da5aaa74a59d6a192d6f74524e0717bcc5a3b2e3b13e"
  ]
}
```

</details>

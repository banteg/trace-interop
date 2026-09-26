# Transaction refund clear

`trace_transaction` · mined-probes · [All reports](../../README.md)

**What this checks:** The storage program is one call frame. Root gasUsed is execution gas before the refund (5004, refund 4800, receipt 21204). Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · b4211ad9](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_transaction",
  "params": [
    "0x6c9c863f8bedabd9d2b96c9f1582c133b0eeaa83343a29c6ad72d77ba46b297a"
  ]
}
```

</details>

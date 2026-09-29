# Transaction refund capped

`trace_transaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. The storage program is one call frame. Root gasUsed is execution gas before the refund (10009, refund 9600, receipt 24808). Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |

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

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H09](../../decisions/H09.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H09](../../decisions/H09.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

</details>

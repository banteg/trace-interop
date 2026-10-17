# Block 5

`trace_block` · mined-probes · [All reports](../../README.md)

**What this checks:** The storage program is one call frame. Root gasUsed is execution gas before the refund (5004, refund 4800, receipt 21204). Root gasUsed is execution gas before the refund (10009, refund 9600, receipt 24808). Trace roots preserve the frozen transaction inventory and recovered senders in canonical order. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-17/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.6-nightly · de005f70](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/mined-probes/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "0x5"
  ]
}
```

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H09](../../decisions/H09.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

</details>

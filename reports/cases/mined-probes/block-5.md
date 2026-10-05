# Block 5

`trace_block` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. The storage program is one call frame. Root gasUsed is execution gas before the refund (5004, refund 4800, receipt 21204). Root gasUsed is execution gas before the refund (10009, refund 9600, receipt 24808). Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |

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

**Anvil · 1.8.4-nightly · e15c2f1c** (`anvil Version: 1.8.4-nightly+e15c2f1c`)

- [H09](../../decisions/H09.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H09](../../decisions/H09.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x2bb38', 'input': '0x', 'to': '0x0000000000000000000000000000000000005501', 'value': '0x0'}, 'blockHash': '0xda78f13c0d843c94e59269523b68de3a32b6b9970c97e4bcf6f90c4b3265097f', 'blockNumber': 5, 'result':

</details>

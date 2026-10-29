# Transaction selfdestruct self

`trace_transaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. SELFDESTRUCT emits one suicide frame under the call. The suicide frame records the contract’s whole balance transferred to itself. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |

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

**Anvil · 1.8.7-nightly · 716e795c** (`anvil Version: 1.8.7-nightly+716e795c`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H26](../../decisions/H26.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [0]: error None, result null.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x2bb38', 'input': '0x', 'to': '0x000000000000000000000000000000000000de57', 'value': '0x0'}, 'blockHash': '0xc8c95be3c7677411d196b7ef4b16b998aa6e584f82bd0d360eb5aaf21b40ded4', 'blockNumber': 4, 'result':

</details>

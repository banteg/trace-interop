# Transaction selfdestruct self

`trace_transaction` · mined-probes · [All reports](../../README.md)

**What this checks:** SELFDESTRUCT emits one suicide frame under the call. The suicide frame records the contract’s whole balance transferred to itself. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |

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

**Anvil · 1.8.6-nightly · 6c21ffe2** (`anvil Version: 1.8.6-nightly+6c21ffe2`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H26](../../decisions/H26.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

</details>

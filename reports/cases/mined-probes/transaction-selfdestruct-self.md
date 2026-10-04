# Transaction selfdestruct self

`trace_transaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. SELFDESTRUCT emits one suicide frame under the call. The suicide frame records the contract’s whole balance transferred to itself. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |

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

**Anvil · 1.8.4-nightly · 60255eee** (`anvil Version: 1.8.4-nightly+60255eee`)

- [H26](../../decisions/H26.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H26](../../decisions/H26.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Reth · 2.7.0 · 10bcf461** (`Reth Version: 2.7.0+10bcf461`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

</details>

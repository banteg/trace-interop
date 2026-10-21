# Replay block 5

`trace_replayBlockTransactions` · mined-probes · [All reports](../../README.md)

**What this checks:** The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. The storage program is one call frame. Root gasUsed is execution gas before the refund (5004, refund 4800, receipt 21204). Cleared slots change from their genesis values to zero. Root gasUsed is execution gas before the refund (10009, refund 9600, receipt 24808). Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x5",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H09](../../decisions/H09.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

</details>

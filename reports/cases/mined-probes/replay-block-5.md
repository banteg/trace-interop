# Replay block 5

`trace_replayBlockTransactions` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. The storage program is one call frame. Root gasUsed is execution gas before the refund (5004, refund 4800, receipt 21204). Cleared slots change from their genesis values to zero. Root gasUsed is execution gas before the refund (10009, refund 9600, receipt 24808). Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |

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

**Anvil · 1.8.4-nightly · e3429853** (`anvil Version: 1.8.4-nightly+e3429853`)

- [H09](../../decisions/H09.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H09](../../decisions/H09.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

</details>

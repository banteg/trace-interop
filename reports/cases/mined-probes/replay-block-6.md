# Replay block 6

`trace_replayBlockTransactions` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. Tuples fold per authority in order: two valid tuples replace A with B, the stale-nonce tuple is skipped, and the nonce advances once per applied tuple. An absent authority is born with creation markers for zero balance, nonce one and its delegation. Tuples that end at the original delegation report no code change, but the nonce advances twice. Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x6",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · 60255eee** (`anvil Version: 1.8.4-nightly+60255eee`)

- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H17](../../decisions/H17.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H18](../../decisions/H18.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H17](../../decisions/H17.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H18](../../decisions/H18.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

</details>

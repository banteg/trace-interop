# Replay block 6

`trace_replayBlockTransactions` · mined-probes · [All reports](../../README.md)

**What this checks:** Tuples fold per authority in order: two valid tuples replace A with B, the stale-nonce tuple is skipped, and the nonce advances once per applied tuple. An absent authority is born with creation markers for zero balance, nonce one and its delegation. Tuples that end at the original delegation report no code change, but the nonce advances twice. Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |

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

</details>

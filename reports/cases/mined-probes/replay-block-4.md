# Replay block 4

`trace_replayBlockTransactions` · mined-probes · [All reports](../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. A deleted account reports storage {} or optional old-slot - entries; account deletion implies every slot is wiped. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. SELFDESTRUCT emits one suicide frame under the call. The suicide frame records the contract’s whole balance transferred to itself. A pre-existing contract survives SELFDESTRUCT after Cancun with its balance, code and storage, so it has no account diff. The creation and its SELFDESTRUCT both appear. The factory call returns the created address word. The creation succeeds with empty code before destroying itself. The suicide frame transfers the new contract’s whole balance, including any prefunded wei, to itself. An account created and destroyed in one transaction is absent at both endpoints and has no account diff. The factory forwards the value it received, so only its nonce changes. A prefunded address destroyed in its creating transaction is a deletion: - markers for its pre-state and storage {}. Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x4",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

</details>

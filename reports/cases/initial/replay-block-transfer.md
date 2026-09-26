# Replay block transfer

`trace_replayBlockTransactions` · initial · [All reports](../../README.md)

**What this checks:** Block replay has exactly one envelope per frozen transaction, with hashes in transaction order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x5",
    [
      "trace"
    ]
  ]
}
```

</details>

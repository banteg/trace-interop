# Replay block transfer

`trace_replayBlockTransactions` · initial · [All reports](../../README.md)

**What this checks:** Block replay has exactly one envelope per frozen transaction, with hashes in transaction order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 07915e32](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/initial/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 3904de43](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · 5ece5fba](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/initial/manifest.json) |
| [Reth · 2.5.2 · 863f7055](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/initial/manifest.json) |

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

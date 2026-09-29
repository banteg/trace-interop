# Replay block transfer

`trace_replayBlockTransactions` · initial · [All reports](../../README.md)

**What this checks:** Block replay has exactly one envelope per frozen transaction, with hashes in transaction order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |

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

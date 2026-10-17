# Transaction transfer

`trace_transaction` · initial · [All reports](../../README.md)

**What this checks:** Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Anvil · 1.8.6-nightly · de005f70](../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_transaction",
  "params": [
    "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe"
  ]
}
```

</details>

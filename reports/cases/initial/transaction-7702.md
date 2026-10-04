# Transaction 7702

`trace_transaction` · initial · [All reports](../../README.md)

**What this checks:** Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_transaction",
  "params": [
    "0xb54bc1221b206db9ee0449a716ddde73c1e2d0f72d2e789fcb51230fe851cc8a"
  ]
}
```

</details>

# Filter page

`trace_filter` · initial · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toBlock": "0x2",
      "after": 1,
      "count": 2
    }
  ]
}
```

</details>

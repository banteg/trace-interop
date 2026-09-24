# Filter page

`trace_filter` · initial · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "after": 1,
      "count": 2,
      "fromBlock": "0x2",
      "toBlock": "0x2"
    }
  ]
}
```

</details>

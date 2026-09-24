# Filter past end page

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "after": 10000,
      "count": 1,
      "fromBlock": "0x2",
      "toBlock": "0x2"
    }
  ]
}
```

</details>

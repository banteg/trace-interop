# System beacon 55 8751

`eth_getStorageAt` · forks · [All reports](../../README.md)

**What this checks:** Historical beacon-root storage excludes the following block system update.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | `0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000000000000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getStorageAt",
  "params": [
    "0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02",
    "0x222f",
    "0x37"
  ]
}
```

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H28](../../decisions/H28.md): Historical beacon-root storage excludes the following block system update.

</details>

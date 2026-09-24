# After/filter tail

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Every phase range has exactly the frozen canonical roots and block hashes; restoration returns the original inventory.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../clients/besu_release.md) | 9 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../../clients/besu_development.md) | 9 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../../clients/erigon_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | 9 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../../clients/nethermind_development.md) | 9 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../clients/reth_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x28",
      "toBlock": "0x30"
    }
  ]
}
```

**Nethermind · 2.1.0-unstable · 641592d2** (`2.1.0-unstable+641592d2`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `1`: 'transactionHash' is a required property
- Result shape at `1`: 'transactionPosition' is a required property
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `1`: 'transactionHash' is a required property
- Result shape at `1`: 'transactionPosition' is a required property
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

</details>

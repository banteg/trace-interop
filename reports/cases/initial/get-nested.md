# Get nested

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Return the transaction-tree record at [0, 0], or null if absent. The nested path returns its independently anchored frame or null when absent.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../clients/nethermind_development.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "0x0",
      "0x0"
    ]
  ]
}
```

**Nethermind · 2.1.0-unstable · 2a3b2531** (`2.1.0-unstable+2a3b2531`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [0, 0], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.
- [H06](../../decisions/H06.md): The nested path returns its independently anchored frame or null when absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xf35c', 'input': '0xff01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1', 'value': '0x1'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'result

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [0, 0], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.
- [H06](../../decisions/H06.md): The nested path returns its independently anchored frame or null when absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xf35c', 'input': '0xff01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1', 'value': '0x1'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'result

</details>

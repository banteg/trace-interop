# Get zero

`trace_get` · initial · [All reports](../../README.md)

**What this checks:** Return the transaction-tree record at [0], or null if absent.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | One frame, path `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | One frame, path `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | One frame, path `[0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | One frame, path `[0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | One frame, path `[0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | One frame, path `[0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | One frame, path `[0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | One frame, path `[0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | One frame, path `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | One frame, path `[0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "0x0"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [0], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [0], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [0], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xf35c', 'input': '0xff01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1', 'value': '0x1'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'result

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [0], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.

</details>

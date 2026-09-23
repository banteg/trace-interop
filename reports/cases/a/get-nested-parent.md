# Get nested parent

`trace_get` · a · [All reports](../../README.md)

**What this checks:** Return the transaction-tree record at [6], or null if absent.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | One frame, path `[6]` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | One frame, path `[6]` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | One frame, path `[6]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | One frame, path `[6]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | One frame, path `[6]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | One frame, path `[5]` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | One frame, path `[5]` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "0x6"
    ]
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- Result shape at `/`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- Result shape at `/`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [6], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.
- Result shape at `/`: [{'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [6], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.
- Result shape at `/`: [{'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [6], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H02](../../decisions/H02.md): Return the transaction-tree record at [6], or null if absent. Compared with the same client and transaction; precompile inclusion can shift sibling indexes.

</details>

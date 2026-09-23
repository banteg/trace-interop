# Block 55

`trace_block` · forks · [All reports](../../README.md)

**What this checks:** A PoS block has no synthetic PoW reward records. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "0x37"
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

</details>

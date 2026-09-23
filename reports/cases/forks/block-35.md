# Block 35

`trace_block` · forks · [All reports](../../README.md)

**What this checks:** Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 4 records | ⚪ Not assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 4 records | ⚪ Not assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 4 records | ⚪ Not assessed; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 4 records | ⚪ Not assessed; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 4 records | ⚪ Not assessed | [Response](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-forks/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 4 records | ⚪ Not assessed; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 4 records | ⚪ Not assessed; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 4 records | ⚪ Not assessed; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 4 records | ⚪ Not assessed; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "0x23"
  ]
}
```

**Geth draft fork · 🧪 Draft fork** (`Geth/v1.17.6-unstable-c36ee43e-2026-09-23/linux-amd64/go1.26.1`)

- [H27](../../decisions/H27.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H27](../../decisions/H27.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H27](../../decisions/H27.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H27](../../decisions/H27.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H27](../../decisions/H27.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H27](../../decisions/H27.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H27](../../decisions/H27.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

</details>

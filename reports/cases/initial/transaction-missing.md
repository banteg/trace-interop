# Transaction missing

`trace_transaction` · initial · [All reports](../../README.md)

**What this checks:** Unknown transaction returns null, not an empty collection or RPC error. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-initial/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | `null` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_transaction",
  "params": [
    "0xfefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefe"
  ]
}
```

**Geth draft fork · 🧪 Draft fork** (`Geth/v1.17.6-unstable-c36ee43e-2026-09-23/linux-amd64/go1.26.1`)

- [H02](../../decisions/H02.md): Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H02](../../decisions/H02.md): Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H02](../../decisions/H02.md): Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H02](../../decisions/H02.md): Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H02](../../decisions/H02.md): Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

</details>

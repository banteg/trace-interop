# Withdrawal balance 51

`eth_getBalance` · fork-followup · [All reports](../../README.md)

**What this checks:** Retain independent reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | `0xc097ce7bc90715b34b9f1000000006` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | `0xc097ce7bc90715b34b9f1000000006` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | `0xc097ce7bc90715b34b9f1000000006` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | `0xc097ce7bc90715b34b9f1000000006` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | `0xc097ce7bc90715b34b9f1000000006` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-fork-followup/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | `0xc097ce7bc90715b34b9f1000000006` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | `0xc097ce7bc90715b34b9f1000000006` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | `0xc097ce7bc90715b34b9f1000000006` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | `0xc097ce7bc90715b34b9f1000000006` | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-fork-followup/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getBalance",
  "params": [
    "0x717f8aa2b982bee0e29f573d31df288663e1ce16",
    "0x33"
  ]
}
```

**Geth draft fork · 🧪 Draft fork** (`Geth/v1.17.6-unstable-c36ee43e-2026-09-23/linux-amd64/go1.26.1`)

- [H05](../../decisions/H05.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H05](../../decisions/H05.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H05](../../decisions/H05.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H05](../../decisions/H05.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H05](../../decisions/H05.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H05](../../decisions/H05.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H05](../../decisions/H05.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

</details>

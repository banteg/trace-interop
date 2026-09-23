# Debug siblings revert ok

`debug_traceCall` · repeat · [All reports](../../README.md)

**What this checks:** Retain independent reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-repeat/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "debug_traceCall",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "to": "0x0000000000000000000000000000000000001005"
    },
    "0x30",
    {
      "tracer": "callTracer"
    }
  ]
}
```

**Geth draft fork · 🧪 Draft fork** (`Geth/v1.17.6-unstable-c36ee43e-2026-09-23/linux-amd64/go1.26.1`)

- [H24](../../decisions/H24.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H24](../../decisions/H24.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H24](../../decisions/H24.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H24](../../decisions/H24.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H24](../../decisions/H24.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H24](../../decisions/H24.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H24](../../decisions/H24.md): Retain independent reference evidence. Non-trace state/header/receipt or diagnostic control; not a trace conformance assertion.

</details>

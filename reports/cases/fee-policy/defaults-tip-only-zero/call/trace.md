# Defaults tip only zero/call/trace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Observe unresolved fee defaults. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../../../clients/besu_release.md) | RPC error `-32603` | ⚪ Not assessed | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Besu · 🛠️ Development](../../../../clients/besu_development.md) | RPC error `-32603` | ⚪ Not assessed | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Erigon · 📦 Release](../../../../clients/erigon_release.md) | 1 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Erigon · 🛠️ Development](../../../../clients/erigon_development.md) | 1 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Nethermind · 📦 Release](../../../../clients/nethermind_release.md) | 1 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Nethermind · 🛠️ Development](../../../../clients/nethermind_development.md) | 1 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Reth · 📦 Release](../../../../clients/reth_release.md) | 1 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Reth · 🛠️ Development](../../../../clients/reth_development.md) | 1 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x30d40",
      "maxPriorityFeePerGas": "0x0",
      "value": "0x7"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Geth draft fork · 🧪 Draft fork** (`Geth/v1.17.6-unstable-c36ee43e-2026-09-23/linux-amd64/go1.26.1`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

</details>

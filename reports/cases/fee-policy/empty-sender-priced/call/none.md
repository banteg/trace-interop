# Empty sender priced/call/none

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. Identify a fee/funding validation rejection. Unrequested trace is an empty array. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Reject this independently invalid fee/funding request before execution.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../../../clients/besu_development.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../../../clients/erigon_development.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../../../clients/go-ethereum_trace.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../../../clients/reth_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
      "from": "0x0000000000000000000000000000000000004444",
      "gas": "0x30d40",
      "gasPrice": "0x2da282a9",
      "value": "0x0"
    },
    [],
    "latest"
  ]
}
```

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. An unfunded sender cannot afford positive gas fees.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. An unfunded sender cannot afford positive gas fees.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. An unfunded sender cannot afford positive gas fees.

</details>

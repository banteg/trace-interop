# Typed tip over cap/call/vmtrace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. Identify a fee/funding validation rejection.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../../../clients/besu_development.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../../../clients/reth_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/refresh/fee-policy/manifest.json) |

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
      "maxFeePerGas": "0x2da282a8",
      "maxPriorityFeePerGas": "0x2da282a9",
      "value": "0x7"
    },
    [
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

</details>

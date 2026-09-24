# Typed zero cap positive tip/trace/trace statediff vmtrace

`trace_call` · fee-compat · [All reports](../../../../README.md)

**What this checks:** The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. Identify a fee/funding validation rejection. Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../../clients/besu_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../../../clients/besu_development.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../../clients/reth_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |

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
      "maxFeePerGas": "0x0",
      "maxPriorityFeePerGas": "0x1",
      "value": "0x7"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Besu · 26.9-develop · cf89071f** (`besu/v26.9-develop-cf89071/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: base_fee rejection; trace_call: unclassified RPC error: internal error.
- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: base_fee rejection; trace_call: unclassified RPC error: internal error.
- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Erigon · 3.8.0-dev · 01c118ee** (`3.8.0-dev-01c118ee`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code. Expected call 0: base_fee or priority; observed priority with code -32000, which requires -32602. Positive cap/price below BASEFEE or priority cap above total cap.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code. Expected call 0: base_fee or priority; observed priority with code -32000, which requires -32602. Positive cap/price below BASEFEE or priority cap above total cap.

**Nethermind · 2.1.0-preview · 54b760cd** (`2.1.0-preview+54b760cd`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code. Expected call 0: base_fee or priority; observed priority with code -32000, which requires -32602. Positive cap/price below BASEFEE or priority cap above total cap.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code. Expected call 0: base_fee or priority; observed priority with code -32000, which requires -32602. Positive cap/price below BASEFEE or priority cap above total cap.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code. Expected call 0: base_fee or priority; observed base_fee with code -32000, which requires -38012. Positive cap/price below BASEFEE or priority cap above total cap.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code. Expected call 0: base_fee or priority; observed base_fee with code -32000, which requires -38012. Positive cap/price below BASEFEE or priority cap above total cap.

</details>

# Typed one/call/statediff vmtrace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Unrequested trace is an empty array. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Reject this independently invalid fee/funding request before execution. Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. Identify a fee/funding validation rejection. Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../../../clients/anvil_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../../../clients/anvil_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../../../clients/besu_development.md) | RPC error `-32009` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../../../clients/erigon_development.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../../../clients/go-ethereum_trace.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../../../clients/nethermind_development.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-05/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-05/eval/fee-policy/manifest.json) |

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
      "maxFeePerGas": "0x1",
      "maxPriorityFeePerGas": "0x0",
      "value": "0x7"
    },
    [
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · e15c2f1c** (`anvil Version: 1.8.4-nightly+e15c2f1c`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../../../decisions/H15.md): Assess the declared property. Cannot inspect this property: malformed_json.

</details>

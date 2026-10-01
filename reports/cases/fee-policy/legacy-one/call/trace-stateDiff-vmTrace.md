# Legacy one/call/trace statediff vmtrace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth. Reject this independently invalid fee/funding request before execution. Identify a fee/funding validation rejection. Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../../../clients/anvil_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../../../clients/anvil_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../../../clients/besu_development.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../../../clients/erigon_development.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../../../clients/go-ethereum_trace.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../../../clients/reth_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-01/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-01/eval/fee-policy/manifest.json) |

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
      "gasPrice": "0x1",
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

**Anvil · 1.8.4-nightly · df92604b** (`anvil Version: 1.8.4-nightly+df92604b`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../../../decisions/H15.md): Assess the declared property. Cannot inspect this property: malformed_json.

**Reth · 2.7.0 · 5b686303** (`Reth Version: 2.7.0+5b686303`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.

</details>

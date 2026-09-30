# Legacy below base/trace/trace vmtrace

`trace_call` · fee-compat · [All reports](../../../../README.md)

**What this checks:** Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth. The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. Reject this independently invalid fee/funding request before execution. Identify a fee/funding validation rejection. Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. Return one complete JSON-RPC response; never wrap an error envelope as a successful result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../../../clients/anvil_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-30/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-compat/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../../../clients/anvil_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-30/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-compat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-30/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-compat/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../../../clients/besu_development.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-30/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-compat/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-compat/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../../../clients/erigon_development.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../../../clients/go-ethereum_trace.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-compat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../../../evidence/2026-09-30/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-compat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-30/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-compat/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../../../clients/reth_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-30/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-compat/manifest.json) |

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
      "gasPrice": "0x2da282a7",
      "value": "0x7"
    },
    [
      "trace",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · e3429853** (`anvil Version: 1.8.4-nightly+e3429853`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. eth_call: base_fee rejection; trace_call: unclassified RPC error: internal error.
- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. eth_call: base_fee rejection; trace_call: unclassified RPC error: internal error.
- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. eth_call: base_fee rejection; trace_call: malformed_json.

**Reth · 2.7.0 · 43a93dbc** (`Reth Version: 2.7.0+43a93dbc`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.

</details>

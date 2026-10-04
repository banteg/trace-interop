# Funding typed effective only/trace/trace statediff

`trace_call` · fee-compat · [All reports](../../../../README.md)

**What this checks:** The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. Identify a fee/funding validation rejection. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Reject this independently invalid fee/funding request before execution. Return one complete JSON-RPC response; never wrap an error envelope as a successful result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-compat/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-compat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-10-04/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-compat/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../../../clients/besu_development.md) | RPC error `-32004` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-compat/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-04/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-compat/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../../../clients/erigon_development.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../../../clients/go-ethereum_trace.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-compat/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../../../evidence/2026-10-04/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../../../clients/nethermind_development.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-04/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-compat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-04/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-compat/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../../../clients/reth_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-04/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-04/eval/fee-compat/manifest.json) |

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
      "maxFeePerGas": "0x5b450550",
      "maxPriorityFeePerGas": "0x1",
      "value": "0xde02b6f7625c0c0"
    },
    [
      "trace",
      "stateDiff"
    ],
    "latest"
  ]
}
```

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. eth_call: funds rejection; trace_call: unclassified RPC error: internal error.
- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. eth_call: funds rejection; trace_call: execution output (224 bytes).
- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Affordable at effective price, but not at the EIP-1559 fee cap.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. eth_call: funds rejection; trace_call: malformed_json.

**Reth · 2.7.0 · 10bcf461** (`Reth Version: 2.7.0+10bcf461`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Affordable at effective price, but not at the EIP-1559 fee cap.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Affordable at effective price, but not at the EIP-1559 fee cap.

</details>

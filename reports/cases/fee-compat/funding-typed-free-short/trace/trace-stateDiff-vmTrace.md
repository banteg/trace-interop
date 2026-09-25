# Funding typed free short/trace/trace statediff vmtrace

`trace_call` · fee-compat · [All reports](../../../../README.md)

**What this checks:** The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. Identify a fee/funding validation rejection. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth. Reject this independently invalid fee/funding request before execution. Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code. Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Failed frames have an error string; an exceptional halt omits result or sets it to null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../../clients/besu_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-25/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-compat/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../../../clients/besu_development.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-25/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-compat/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-compat/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../../../clients/erigon_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../../../clients/go-ethereum_trace.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-compat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-compat/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../../../clients/nethermind_development.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-compat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-compat/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../../../clients/reth_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-compat/manifest.json) |

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
      "maxPriorityFeePerGas": "0x0",
      "value": "0xde0b6b3a7640001"
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

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: funds rejection; trace_call: unclassified RPC error: internal error.
- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: funds rejection; trace_call: unclassified RPC error: internal error.
- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Erigon · 3.8.0-dev · f8cfe5a7** (`3.8.0-dev-f8cfe5a7`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: funds rejection; trace_call: execution output (224 bytes).
- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: funds rejection; trace_call: execution output (224 bytes).
- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Nethermind · 2.1.0-preview · ee1f57da** (`2.1.0-preview+ee1f57da`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: funds rejection; trace_call: malformed_json.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: funds rejection; trace_call: malformed_json.

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: unclassified RPC error: evm error: outoffunds; trace_call: execution output (0 bytes).
- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: unclassified RPC error: evm error: outoffunds; trace_call: execution output (0 bytes).
- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

</details>

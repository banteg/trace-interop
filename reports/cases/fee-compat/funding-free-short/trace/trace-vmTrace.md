# Funding free short/trace/trace vmtrace

`trace_call` · fee-compat · [All reports](../../../../README.md)

**What this checks:** The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Identify a fee/funding validation rejection. Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt omits result or sets it to null. Reject this independently invalid fee/funding request before execution.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../../../clients/anvil_release.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-29/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/refresh/fee-compat/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../../../clients/anvil_development.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-29/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/refresh/fee-compat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-29/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/refresh/fee-compat/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../../../clients/besu_development.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-29/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/refresh/fee-compat/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-29/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/refresh/fee-compat/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../../../clients/erigon_development.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-29/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/refresh/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../../../clients/go-ethereum_trace.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-29/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/refresh/fee-compat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../../../evidence/2026-09-29/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/refresh/fee-compat/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-29/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/refresh/fee-compat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-29/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/refresh/fee-compat/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../../../clients/reth_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-29/refresh/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/refresh/fee-compat/manifest.json) |

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
      "gasPrice": "0x0",
      "value": "0xde0b6b3a7640001"
    },
    [
      "trace",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Expected call 0: funds; observed funds with code -32003, which requires -38014. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Expected call 0: funds; observed funds with code -32003, which requires -38014. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: funds rejection; trace_call: unclassified RPC error: internal error.
- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: funds rejection; trace_call: unclassified RPC error: internal error.
- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: funds rejection; trace_call: base_fee rejection.
- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Expected call 0: funds; observed base_fee with code -32000, which requires -38012. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Nethermind · 2.2.0-preview · 287f54f0** (`2.2.0-preview+287f54f0`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Expected call 0: funds; observed funds with code -32000, which requires -38014. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: funds rejection; trace_call: malformed_json.

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: unclassified RPC error: evm error: outoffunds; trace_call: execution output (0 bytes).
- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: unclassified RPC error: evm error: outoffunds; trace_call: execution output (0 bytes).
- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

</details>

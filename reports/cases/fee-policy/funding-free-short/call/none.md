# Funding free short/call/none

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Identify a fee/funding validation rejection. Unrequested trace is an empty array. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Reject this independently invalid fee/funding request before execution.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../../../clients/anvil_release.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../../../clients/anvil_development.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../../../clients/besu_development.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · a1ce80fb](../../../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../../../clients/go-ethereum_trace.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-preview · 45912ba3](../../../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../../../clients/reth_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |

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
    [],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · dd372126** (`anvil Version: 1.8.4-nightly+dd372126`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Expected call 0: funds; observed funds with code -32003, which requires -38014. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Expected call 0: funds; observed funds with code -32003, which requires -38014. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Erigon · 3.8.0-dev · a1ce80fb** (`3.8.0-dev-a1ce80fb`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Expected call 0: funds; observed funds with code -32000, which requires -38014. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Expected call 0: funds; observed base_fee with code -32000, which requires -38012. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Nethermind · 2.1.0-preview · 45912ba3** (`2.1.0-preview+45912ba3`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Expected call 0: funds; observed funds with code -32000, which requires -38014. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Reth · 2.5.2 · 5723a3fe** (`Reth Version: 2.5.2+5723a3fe`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

</details>

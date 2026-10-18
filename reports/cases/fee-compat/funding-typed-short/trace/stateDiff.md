# Funding typed short/trace/statediff

`trace_call` · fee-compat · [All reports](../../../../README.md)

**What this checks:** The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Reject this independently invalid fee/funding request before execution.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../../../clients/besu_release.md) | RPC error `-32004` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../../../clients/besu_development.md) | RPC error `-32004` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../../clients/erigon_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../../../clients/erigon_development.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../../../clients/go-ethereum_trace.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../../clients/nethermind_release.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../../../clients/nethermind_development.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../../../clients/reth_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |

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
      "value": "0xddfa02b44ed9c01"
    },
    [
      "stateDiff"
    ],
    "latest"
  ]
}
```

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. eth_call: funds rejection; trace_call: execution output (224 bytes).
- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Value plus the applicable maximum upfront gas commitment exceeds sender balance.

</details>

# Typed below base/call/statediff

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Reject this independently invalid fee/funding request before execution.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../../../clients/anvil_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../../../clients/besu_release.md) | RPC error `-32009` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../../../clients/besu_development.md) | RPC error `-32009` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../../../clients/erigon_release.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../../../clients/erigon_development.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../../../clients/go-ethereum_trace.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../../clients/nethermind_release.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../../../clients/nethermind_development.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |

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
      "maxFeePerGas": "0x2da282a7",
      "maxPriorityFeePerGas": "0x0",
      "value": "0x7"
    },
    [
      "stateDiff"
    ],
    "latest"
  ]
}
```

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.

</details>

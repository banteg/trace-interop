# Typed zero cap positive tip/call/statediff vmtrace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../../../clients/besu_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../../../clients/besu_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../../../clients/reth_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../../../clients/reth_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-10-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-29/eval/fee-policy/manifest.json) |

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
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. Expected call 0: priority; observed base_fee with code -32000 (-38012 recommended). base_fee is violated too, but priority takes precedence. Positive cap/price below BASEFEE or priority cap above total cap.

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. Expected call 0: priority; observed base_fee with code -32000 (-38012 recommended). base_fee is violated too, but priority takes precedence. Positive cap/price below BASEFEE or priority cap above total cap.

</details>

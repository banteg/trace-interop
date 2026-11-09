# Typed zero cap positive tip/trace/none

`trace_call` · fee-compat · [All reports](../../../../README.md)

**What this checks:** The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-compat/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-compat/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../../../clients/besu_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-compat/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../../../clients/besu_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-compat/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-compat/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-compat/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-compat/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../../../clients/reth_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-11-09/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-compat/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../../../clients/reth_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-11-09/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-compat/manifest.json) |

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
    [],
    "latest"
  ]
}
```

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. Expected call 0: priority; observed base_fee with code -32000 (-38012 recommended). base_fee is violated too, but priority takes precedence. Positive cap/price below BASEFEE or priority cap above total cap.

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. Expected call 0: priority; observed base_fee with code -32000 (-38012 recommended). base_fee is violated too, but priority takes precedence. Positive cap/price below BASEFEE or priority cap above total cap.

</details>

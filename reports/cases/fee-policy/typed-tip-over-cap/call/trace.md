# Typed tip over cap/call/trace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-17/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-17/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.6-nightly · de005f70](../../../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-17/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-17/eval/fee-policy/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../../../clients/besu_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-17/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-17/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../../../clients/besu_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-17/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-17/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-17/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-17/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-17/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-17/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-17/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-17/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-17/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-17/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-17/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-17/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-17/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-17/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../../../clients/reth_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-17/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-17/eval/fee-policy/manifest.json) |

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
      "maxFeePerGas": "0x2da282a8",
      "maxPriorityFeePerGas": "0x2da282a9",
      "value": "0x7"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

</details>

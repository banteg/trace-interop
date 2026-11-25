# Typed below base positive tip/many/trace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. A supplied error.data.index must identify the failing decoded item; the field is recommended.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../../../clients/besu_release.md) | RPC error `-32009` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../../../clients/besu_development.md) | RPC error `-32009` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../../../clients/erigon_release.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../../../clients/erigon_development.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../../../clients/go-ethereum_trace.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../../clients/nethermind_release.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../../../clients/nethermind_development.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_callMany",
  "params": [
    [
      [
        {
          "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "maxFeePerGas": "0x2da282a7",
          "maxPriorityFeePerGas": "0x1",
          "value": "0x7"
        },
        [
          "trace"
        ]
      ]
    ],
    "latest"
  ]
}
```

</details>

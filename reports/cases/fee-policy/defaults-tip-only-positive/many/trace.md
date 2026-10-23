# Defaults tip only positive/many/trace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. A supplied error.data.index must identify the failing decoded item; the field is recommended. Return one execution envelope per input call, in order. Reject this independently invalid fee/funding request before execution.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.7-nightly · 4e8874b2](../../../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Besu · 26.10.1 · e83703cd](../../../../clients/besu_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../../../clients/besu_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../../../clients/reth_release.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../../../clients/reth_development.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |

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

**Reth · 2.8.0 · 53bf066f** (`Reth Version: 2.8.0+53bf066f`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. The omitted fee cap defaults to zero, below the supplied priority fee.

**Reth · 2.8.1 · d763342f** (`Reth Version: 2.8.1+d763342f`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. The omitted fee cap defaults to zero, below the supplied priority fee.

</details>

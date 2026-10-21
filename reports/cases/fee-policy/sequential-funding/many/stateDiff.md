# Sequential funding/many/statediff

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. A supplied error.data.index must identify the failing decoded item; the field is recommended. Return one execution envelope per input call, in order. Reject this independently invalid fee/funding request before execution.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../../../clients/besu_release.md) | RPC error `-32004` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../../../clients/besu_development.md) | RPC error `-32004` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../../../clients/erigon_release.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../../../clients/erigon_development.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../../../clients/go-ethereum_trace.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../../clients/nethermind_release.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../../../clients/nethermind_development.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-10-21/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-21/eval/fee-policy/manifest.json) |

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
          "data": "0x",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "gasPrice": "0x2da282a9",
          "to": "0x0000000000000000000000000000000000004444",
          "value": "0x0"
        },
        [
          "stateDiff"
        ]
      ],
      [
        {
          "data": "0x",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "gasPrice": "0x2da282a9",
          "to": "0x0000000000000000000000000000000000004444",
          "value": "0xde02b6f7625c0c0"
        },
        [
          "stateDiff"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Second call funding must use the post-fee balance of the first call.

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Second call funding must use the post-fee balance of the first call.

</details>

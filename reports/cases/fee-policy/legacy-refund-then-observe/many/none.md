# Legacy refund then observe/many/none

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../../../clients/erigon_development.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/refresh/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/refresh/fee-policy/manifest.json) |

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
          "data": "0x6001600055600060005560006000f3",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "gasPrice": "0x2da282a9",
          "value": "0x7"
        },
        []
      ],
      [
        {
          "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "gasPrice": "0x2da282a9",
          "value": "0x7"
        },
        []
      ]
    ],
    "latest"
  ]
}
```

**Erigon · 3.8.0-dev · f8cfe5a7** (`3.8.0-dev-f8cfe5a7`)

- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0016ec2a2f412000000000000000000000000000000000000000000000000000000000000eba0; independently charged gas 98623.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0016ec2a2f412000000000000000000000000000000000000000000000000000000000000eba0; independently charged gas 98623.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H15](../../../../decisions/H15.md): Execute each valid simulation and return one envelope per call.

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0016ec2a2f412000000000000000000000000000000000000000000000000000000000000eba0; independently charged gas 98623.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Call 1: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0016ec2a2f412000000000000000000000000000000000000000000000000000000000000eba0; independently charged gas 98623.

</details>

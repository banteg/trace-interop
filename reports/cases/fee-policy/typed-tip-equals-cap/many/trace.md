# Typed tip equals cap/many/trace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../../clients/erigon_release.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../../../clients/erigon_development.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../../clients/reth_development.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/adopted-stances/fee-policy/manifest.json) |

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
          "maxFeePerGas": "0x2da282a8",
          "maxPriorityFeePerGas": "0x2da282a8",
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

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23c1c', 'init': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'value': '0x7'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x000000000000000000000000000000000000

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23c1c', 'init': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'value': '0x7'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x000000000000000000000000000000000000

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

</details>

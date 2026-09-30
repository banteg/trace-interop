# Defaults cap only positive/call/none

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../../../clients/anvil_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-30/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../../../clients/anvil_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-30/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-policy/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-30/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-30/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-30/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-30/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../../../clients/reth_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-30/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-30/eval/fee-policy/manifest.json) |

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
      "value": "0x7"
    },
    [],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · e3429853** (`anvil Version: 1.8.4-nightly+e3429853`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H08](../../../../decisions/H08.md): Unrequested trace is an empty array.
- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H15](../../../../decisions/H15.md): Execute each valid simulation and return one envelope per call.

**Reth · 2.7.0 · 43a93dbc** (`Reth Version: 2.7.0+43a93dbc`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

</details>

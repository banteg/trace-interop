# Defaults cap only positive/trace/none

`trace_call` · fee-compat · [All reports](../../../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../../../clients/anvil_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-compat/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../../../clients/anvil_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-compat/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-compat/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-compat/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-compat/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../../clients/nethermind_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-compat/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-compat/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../../../clients/reth_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-11-25/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-compat/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../../../clients/reth_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-11-25/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-compat/manifest.json) |

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

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

</details>

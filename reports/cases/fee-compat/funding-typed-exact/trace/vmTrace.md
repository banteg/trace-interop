# Funding typed exact/trace/vmtrace

`trace_call` · fee-compat · [All reports](../../../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../../../clients/erigon_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../../clients/reth_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-compat/manifest.json) |

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
      "maxPriorityFeePerGas": "0x1",
      "value": "0xddfa02b44ed9c00"
    },
    [
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Erigon · 3.8.0-dev · 01c118ee** (`3.8.0-dev-01c118ee`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: execution output (224 bytes); trace_call: execution output (224 bytes). Differing words: GASLIMIT: eth_call 100000000, trace_call 115792089237316195423570985008687907853269984665640564039457584007913129639935; sender BALANCE: eth_call 153124999800000, trace_call 306250000000000.
- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e10000000000000000000000000000000000000000000000000000008b44313824c00000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H08](../../../../decisions/H08.md): Unrequested trace is an empty array.
- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: execution output (224 bytes); trace_call: execution output (224 bytes). Differing words: GASLIMIT: eth_call 100000000, trace_call 115792089237316195423570985008687907853269984665640564039457584007913129639935; sender BALANCE: eth_call 153124999800000, trace_call 306250000000000.
- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e10000000000000000000000000000000000000000000000000000008b44313824c00000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x000000000000000000000000000000000000000000000000000000002da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push':

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e10000000000000000000000000000000000000000000000000000008b44313824c00000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e10000000000000000000000000000000000000000000000000000008b44313824c00000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

</details>

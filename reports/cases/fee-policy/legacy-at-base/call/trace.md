# Legacy at base/call/trace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Execute each valid simulation and return one envelope per call. Call 0: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Besu · 🛠️ Development](../../../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Erigon · 📦 Release](../../../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Erigon · 🛠️ Development](../../../../clients/erigon_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Nethermind · 📦 Release](../../../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Nethermind · 🛠️ Development](../../../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Reth · 📦 Release](../../../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |
| [Reth · 🛠️ Development](../../../../clients/reth_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) |

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
      "gasPrice": "0x2da282a8",
      "value": "0x7"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H15](../../../../decisions/H15.md): Call 0: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H15](../../../../decisions/H15.md): Call 0: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H15](../../../../decisions/H15.md): Call 0: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Call 0: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de02b6f7628cdf90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

</details>

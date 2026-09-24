# Legacy revert/call/statediff

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Execute each valid simulation and return one envelope per call. Call 0: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Failed frames have an error string and an explicit object or null result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../../../clients/erigon_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | 0 call frames; output `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-unstable · 9d6e8b8d](../../../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../../clients/reth_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x602a60005260206000fd",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x30d40",
      "gasPrice": "0x2da282a9",
      "value": "0x7"
    },
    [
      "stateDiff"
    ],
    "latest"
  ]
}
```

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999959302437446844; miner 0->53156; burn 40697562500000.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H08](../../../../decisions/H08.md): Unrequested trace is an empty array.
- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999959302437446844; miner 0->53156; burn 40697562500000.
- Result shape at `trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dae', 'init': '0x602a60005260206000fd', 'value': '0x7'}, 'error': 'Reverted', 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H08](../../../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H15](../../../../decisions/H15.md): Call 0: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000000000002a; independently charged gas 53156.
- Result shape at `output`: None is not of type 'string'

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999959302437446844; miner 0->53156; burn 40697562500000.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999959302437446844; miner 0->53156; burn 40697562500000.

</details>

# Legacy out of gas/call/trace statediff

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Unrequested vmTrace is null. Output remains a byte string under every trace selection. Failed frames have an error string; an exceptional halt omits result or sets it to null. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../../../clients/erigon_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../../../clients/reth_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x63ffffffff51",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x30d40",
      "gasPrice": "0x2da282a9",
      "value": "0x7"
    },
    [
      "trace",
      "stateDiff"
    ],
    "latest"
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0x30d40'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0xde0b6b3a7640000', 'to': '0xde02b6f7625c0c0'}}, 'code': '=', 'nonce': {'*': {'from': '0xa', 'to'

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.

</details>

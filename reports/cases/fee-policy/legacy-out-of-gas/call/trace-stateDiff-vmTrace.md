# Legacy out of gas/call/trace statediff vmtrace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. Failed frames have an error string and an explicit object or null result. Execute each valid simulation and return one envelope per call. Call 0: preserve the block environment and effective price; expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../../../clients/erigon_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-unstable · 9d6e8b8d](../../../../clients/nethermind_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../../clients/reth_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h17-retest/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h17-retest/fee-policy/manifest.json) |

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
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H09](../../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.

**Nethermind · 2.1.0-unstable · 9d6e8b8d** (`2.1.0-unstable+9d6e8b8d`)

- [H09](../../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999846874999800000; miner 0->200000; burn 153125000000000.

</details>

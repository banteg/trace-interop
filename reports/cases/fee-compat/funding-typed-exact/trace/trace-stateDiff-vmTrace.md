# Funding typed exact/trace/trace statediff vmtrace

`trace_call` · fee-compat · [All reports](../../../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../../../clients/besu_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../../../clients/besu_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../../../clients/erigon_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../../../clients/reth_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-10-18/eval/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-compat/manifest.json) |

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
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H10](../../../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (26 in total).
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23c1c', 'init': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'value': '0xddfa02b44ed9c00'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000
- Result shape at `vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x2da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub':

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H10](../../../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (26 in total).
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23c1c', 'init': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'value': '0xddfa02b44ed9c00'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000
- Result shape at `vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x2da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub':

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (26 in total).
- Result shape at `vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x2da282a9'], 'store': None, 'used': 146458}, 'idx': '0', 'op': 'GASPRICE', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'u

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (26 in total).
- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output, identifiable execution halt or fee/funding rejection class. eth_call: execution output (224 bytes); trace_call: execution output (224 bytes). Differing words: GASLIMIT: eth_call 100000000, trace_call 115792089237316195423570985008687907853269984665640564039457584007913129639935; sender BALANCE: eth_call 153124999800000, trace_call 306250000000000.
- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e10000000000000000000000000000000000000000000000000000008b44313824c00000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->230741765526377; miner 0->98623; burn 75508234375000.
- Result shape at `vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x2da282a9'], 'store': None, 'used': 146458}, 'idx': '0', 'op': 'GASPRICE', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'u

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (26 in total).
- Result shape at `vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x2da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub':

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (26 in total).
- Result shape at `vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x2da282a9'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146455}, 'pc': 1, 'sub':

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e10000000000000000000000000000000000000000000000000000008b44313824c00000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->230741765526377; miner 0->98623; burn 75508234375000.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x000000000000000000000000000000000000000000000000000000002da282a9000000000000000000000000000000000000000000000000000000002da282a8000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e10000000000000000000000000000000000000000000000000000008b44313824c00000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.
- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->230741765526377; miner 0->98623; burn 75508234375000.

</details>

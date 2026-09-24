# Model environment

`trace_call` · coverage · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth. Unsigned execution accepts the supplied nonzero fee and returns one envelope per call; exact environment values are checked by coverage/model-environment. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes. GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved. A new contract has creation markers for nonce one, returned runtime and balance, including empty values.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x3a6000524860205243604052426060524560805260a06000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "gasPrice": "0x77359400"
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

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 12 pushed stack values disagree with the model; step 14 (MSTORE) mem: expected {'off': 128, 'data': '0x0000000000000000000000000000000000000000000000000000000005f5e100'}, got {'data': '0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'off': 128}
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 12 pushed stack values disagree with the model; step 14 (MSTORE) mem: expected {'off': 128, 'data': '0x0000000000000000000000000000000000000000000000000000000005f5e100'}, got {'data': '0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'off': 128}
- [H08](../../decisions/H08.md): Modelled execution returns exactly the independently computed bytes.
- [H15](../../decisions/H15.md): GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 12 pushed stack values disagree with the model; step 14 (MSTORE) mem: expected {'off': 128, 'data': '0x0000000000000000000000000000000000000000000000000000000005f5e100'}, got {'data': '0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'off': 128}
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 12 pushed stack values disagree with the model; step 14 (MSTORE) mem: expected {'off': 128, 'data': '0x0000000000000000000000000000000000000000000000000000000005f5e100'}, got {'data': '0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'off': 128}
- [H08](../../decisions/H08.md): Modelled execution returns exactly the independently computed bytes.
- [H15](../../decisions/H15.md): GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth.
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000000000: new account lacks creation markers for all fields
- Result shape at `vmTrace`: {'code': '0x3a6000524860205243604052426060524560805260a06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0000000000000000000000000000000000000000000000000000000077359400'], 'store': None, 'used': 246620}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': N

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x3a6000524860205243604052426060524560805260a06000f3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. operation 0 mnemonic disagrees with bytecode; operation 1 mnemonic disagrees with bytecode; operation 1 post-step gas does not deduct this operation cost; operation 2 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x3a6000524860205243604052426060524560805260a06000f3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. operation 0 mnemonic disagrees with bytecode; operation 1 mnemonic disagrees with bytecode; operation 1 post-step gas does not deduct this operation cost; operation 2 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

</details>

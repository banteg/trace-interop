# Model environment free

`trace_call` · coverage · [All reports](../../README.md)

**What this checks:** Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately. Assess the declared property. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes. GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved. A new contract has creation markers for nonce one, returned runtime and balance, including empty values.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/coverage/manifest.json) |
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
      "gasPrice": "0x0"
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

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H08](../../decisions/H08.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H17](../../decisions/H17.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H19](../../decisions/H19.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H20](../../decisions/H20.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H21](../../decisions/H21.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H08](../../decisions/H08.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H17](../../decisions/H17.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H19](../../decisions/H19.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H20](../../decisions/H20.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H21](../../decisions/H21.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H08](../../decisions/H08.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H17](../../decisions/H17.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H19](../../decisions/H19.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H20](../../decisions/H20.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H21](../../decisions/H21.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H08](../../decisions/H08.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H17](../../decisions/H17.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H19](../../decisions/H19.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H20](../../decisions/H20.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H21](../../decisions/H21.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Geth draft fork · 1.17.7-unstable · fa8ecb92** (`Geth/v1.17.7-unstable-fa8ecb92-2026-09-24/linux-amd64/go1.26.1`)

- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 3 pushed stack values disagree with the model; step 5 (MSTORE) mem: expected {'off': 32, 'data': '0x0000000000000000000000000000000000000000000000000000000000000000'}, got {'data': '0x000000000000000000000000000000000000000000000000000000002da282a8', 'off': 32}
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 3 pushed stack values disagree with the model; step 5 (MSTORE) mem: expected {'off': 32, 'data': '0x0000000000000000000000000000000000000000000000000000000000000000'}, got {'data': '0x000000000000000000000000000000000000000000000000000000002da282a8', 'off': 32}
- [H08](../../decisions/H08.md): Modelled execution returns exactly the independently computed bytes.
- [H15](../../decisions/H15.md): GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved.

**Nethermind · 2.1.0-unstable · 641592d2** (`2.1.0-unstable+641592d2`)

- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 3 pushed stack values disagree with the model; step 5 (MSTORE) mem: expected {'off': 32, 'data': '0x0000000000000000000000000000000000000000000000000000000000000000'}, got {'data': '0x000000000000000000000000000000000000000000000000000000002da282a8', 'off': 32}
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 3 pushed stack values disagree with the model; step 5 (MSTORE) mem: expected {'off': 32, 'data': '0x0000000000000000000000000000000000000000000000000000000000000000'}, got {'data': '0x000000000000000000000000000000000000000000000000000000002da282a8', 'off': 32}
- [H08](../../decisions/H08.md): Modelled execution returns exactly the independently computed bytes.
- [H15](../../decisions/H15.md): GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 3 pushed stack values disagree with the model; step 5 (MSTORE) mem: expected {'off': 32, 'data': '0x0000000000000000000000000000000000000000000000000000000000000000'}, got {'data': '0x000000000000000000000000000000000000000000000000000000002da282a8', 'off': 32}
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 3 pushed stack values disagree with the model; step 5 (MSTORE) mem: expected {'off': 32, 'data': '0x0000000000000000000000000000000000000000000000000000000000000000'}, got {'data': '0x000000000000000000000000000000000000000000000000000000002da282a8', 'off': 32}
- [H08](../../decisions/H08.md): Modelled execution returns exactly the independently computed bytes.
- [H15](../../decisions/H15.md): GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved.
- Result shape at `vmTrace`: {'code': '0x3a6000524860205243604052426060524560805260a06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0000000000000000000000000000000000000000000000000000000000000000'], 'store': None, 'used': 246620}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': N

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x3a6000524860205243604052426060524560805260a06000f3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x3a6000524860205243604052426060524560805260a06000f3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

</details>

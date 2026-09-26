# Model environment free

`trace_call` · coverage · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth. Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes. GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved. A new contract has creation markers for nonce one, returned runtime and balance, including empty values. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/coverage/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/coverage/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/coverage/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/coverage/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/coverage/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/coverage/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/coverage/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/coverage/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/coverage/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/coverage/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/coverage/manifest.json) |

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

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x3a6000524860205243604052426060524560805260a06000f3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H08](../../decisions/H08.md): Modelled execution returns exactly the independently computed bytes.
- [H15](../../decisions/H15.md): GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x3a6000524860205243604052426060524560805260a06000f3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H08](../../decisions/H08.md): Modelled execution returns exactly the independently computed bytes.
- [H15](../../decisions/H15.md): GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved.

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H08](../../decisions/H08.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H17](../../decisions/H17.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H19](../../decisions/H19.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H20](../../decisions/H20.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H21](../../decisions/H21.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H08](../../decisions/H08.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H17](../../decisions/H17.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H19](../../decisions/H19.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H20](../../decisions/H20.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H21](../../decisions/H21.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H08](../../decisions/H08.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H17](../../decisions/H17.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H19](../../decisions/H19.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H20](../../decisions/H20.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H21](../../decisions/H21.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H08](../../decisions/H08.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H17](../../decisions/H17.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H19](../../decisions/H19.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H20](../../decisions/H20.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H21](../../decisions/H21.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 3 pushed stack values disagree with the model; step 5 (MSTORE) mem: expected {'off': 32, 'data': '0x0000000000000000000000000000000000000000000000000000000000000000'}, got {'data': '0x000000000000000000000000000000000000000000000000000000002da282a8', 'off': 32}
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 3 pushed stack values disagree with the model; step 5 (MSTORE) mem: expected {'off': 32, 'data': '0x0000000000000000000000000000000000000000000000000000000000000000'}, got {'data': '0x000000000000000000000000000000000000000000000000000000002da282a8', 'off': 32}
- [H08](../../decisions/H08.md): Modelled execution returns exactly the independently computed bytes.
- [H15](../../decisions/H15.md): GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: ex {"mem": null, "push": ["0x0000000000000000000000000000000000000000000000000000000000000000"], "store": null, "used": 246620} (7 in total).
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 3 pushed stack values disagree with the model; step 5 (MSTORE) mem: expected {'off': 32, 'data': '0x0000000000000000000000000000000000000000000000000000000000000000'}, got {'data': '0x000000000000000000000000000000000000000000000000000000002da282a8', 'off': 32}
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 3 pushed stack values disagree with the model; step 5 (MSTORE) mem: expected {'off': 32, 'data': '0x0000000000000000000000000000000000000000000000000000000000000000'}, got {'data': '0x000000000000000000000000000000000000000000000000000000002da282a8', 'off': 32}
- [H08](../../decisions/H08.md): Modelled execution returns exactly the independently computed bytes.
- [H15](../../decisions/H15.md): GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved.
- Result shape at `vmTrace`: {'code': '0x3a6000524860205243604052426060524560805260a06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0000000000000000000000000000000000000000000000000000000000000000'], 'store': None, 'used': 246620}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': N

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x3a6000524860205243604052426060524560805260a06000f3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

</details>

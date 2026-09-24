# Model mload existing

`trace_call` · coverage · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes. A new contract has creation markers for nonce one, returned runtime and balance, including empty values.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x602a6000526000515060006000f3",
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

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c426', 'init': '0x602a6000526000515060006000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x', 'gasUsed': '0x1a'}, 'subtraces': 0, 'traceAddress': [], 'type': 'create'} i

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c426', 'init': '0x602a6000526000515060006000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x', 'gasUsed': '0x1a'}, 'subtraces': 0, 'traceAddress': [], 'type': 'create'} i

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth.
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000000000: new account lacks creation markers for all fields; 0x00de48310d77a4d56aa400248b0b1613508f5b73: new account lacks creation markers for all fields
- [H17](../../decisions/H17.md): A new contract has creation markers for nonce one, returned runtime and balance, including empty values.
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0x3bbad8d084e0'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x00de48310d77a4d56aa400248b0b1613508f5b73': {'balance': {'+': '0x0'}, 'code': '=', 'nonce': {'+': '0x1'}, 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395
- Result shape at `vmTrace`: {'code': '0x602a6000526000515060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 246819}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 246816}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x0

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x602a6000526000515060006000f3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 246819, got 246822; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246816, got 246819; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 246819, got 246822; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246816, got 246819; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x602a6000526000515060006000f3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 246819, got 246822; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246816, got 246819; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 246819, got 246822; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246816, got 246819; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

</details>

# Model revert

`trace_call` · coverage · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes. The modelled REVERT root retains its exact return bytes and independently calculated execution gas.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/coverage/manifest.json) |

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

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- [H09](../../decisions/H09.md): The modelled REVERT root retains its exact return bytes and independently calculated execution gas.
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c44e', 'init': '0x602a60005260206000fd', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x000000000000000000000000000000000000000000000000000000000000002a', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is n

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- [H09](../../decisions/H09.md): The modelled REVERT root retains its exact return bytes and independently calculated execution gas.
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c44e', 'init': '0x602a60005260206000fd', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x000000000000000000000000000000000000000000000000000000000000002a', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is n

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- [H09](../../decisions/H09.md): The modelled REVERT root retains its exact return bytes and independently calculated execution gas.
- Result shape at `trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c44e', 'init': '0x602a60005260206000fd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- [H09](../../decisions/H09.md): The modelled REVERT root retains its exact return bytes and independently calculated execution gas.
- Result shape at `trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c44e', 'init': '0x602a60005260206000fd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000

**Nethermind · 2.1.0-preview · ce501a97** (`2.1.0-preview+ce501a97`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- [H09](../../decisions/H09.md): The modelled REVERT root retains its exact return bytes and independently calculated execution gas.
- Result shape at `trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c44e', 'init': '0x602a60005260206000fd', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- [H09](../../decisions/H09.md): The modelled REVERT root retains its exact return bytes and independently calculated execution gas.
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0x3bad0d3d4460'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0xde0b6b3a7640000', 'to': '0xde05602f6653000'}}, 'code': '=', 'nonce': {'*': {'from': '0xa
- Result shape at `trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c44e', 'init': '0x602a60005260206000fd', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `vmTrace`: {'code': '0x602a60005260206000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 246859}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 246856}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x000000000

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x602a60005260206000fd.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 246859, got 246862; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246856, got 246859; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 246859, got 246862; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246856, got 246859; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H09](../../decisions/H09.md): The modelled REVERT root retains its exact return bytes and independently calculated execution gas.
- Result shape at `trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c44e', 'init': '0x602a60005260206000fd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x602a60005260206000fd.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 246859, got 246862; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246856, got 246859; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 246859, got 246862; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246856, got 246859; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H09](../../decisions/H09.md): The modelled REVERT root retains its exact return bytes and independently calculated execution gas.
- Result shape at `trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c44e', 'init': '0x602a60005260206000fd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000

</details>

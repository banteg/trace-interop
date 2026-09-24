# Precheck create value

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth. A CALL or CREATE that fails its balance precheck emits no frame; the next sibling keeps traceAddress [0] and the parent counts only emitted frames. The caller continues: the failed CREATE pushes 0 and the next CREATE uses the unchanged creator nonce. The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Failed frames have an error string; an exceptional halt omits result or sets it to null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 3 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | 3 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "gasPrice": "0x77359400"
    },
    [
      "trace",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Besu · 26.9-develop · cf89071f** (`besu/v26.9-develop-cf89071/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits no frame; the next sibling keeps traceAddress [0] and the parent counts only emitted frames. record 1: expected {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'init': '0x60006000f3', 'value': '0x0'}, 'error': None, 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0x'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}, got {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338b6', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a121e69656643935d9773b079316e0bf2bcfead3', 'gasUsed': '0xa212'}, 'subtraces': 1, 'traceAddress': [0], 'type': 'create'}
- [H20](../../decisions/H20.md): The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [15].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. subtrace 6: nonempty executing bytecode has no operations
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000
- Result shape at `trace/1`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338b6', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000
- Result shape at `trace/2`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x2bd97', 'init': '0x60006000f3', 'value': '0x0'}, 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0x', 'gasUsed': '0x6'}, 'subtraces': 0, 'traceAddress': [0, 0], 'type': 'create'} is not valid und

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits no frame; the next sibling keeps traceAddress [0] and the parent counts only emitted frames. record 1: expected {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'init': '0x60006000f3', 'value': '0x0'}, 'error': None, 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0x'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}, got {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338b6', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a121e69656643935d9773b079316e0bf2bcfead3', 'gasUsed': '0xa212'}, 'subtraces': 1, 'traceAddress': [0], 'type': 'create'}
- [H20](../../decisions/H20.md): The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [15].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. subtrace 6: nonempty executing bytecode has no operations
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000
- Result shape at `trace/1`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338b6', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000
- Result shape at `trace/2`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x2bd97', 'init': '0x60006000f3', 'value': '0x0'}, 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0x', 'gasUsed': '0x6'}, 'subtraces': 0, 'traceAddress': [0, 0], 'type': 'create'} is not valid und

**Erigon · 3.8.0-dev · 01c118ee** (`3.8.0-dev-01c118ee`)

- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits no frame; the next sibling keeps traceAddress [0] and the parent counts only emitted frames. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a121e69656643935d9773b079316e0bf2bcfead3', 'gasUsed': '0x12c40'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}
- [H20](../../decisions/H20.md): The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [15].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. subtrace 6: nonempty executing bytecode has no operations

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits no frame; the next sibling keeps traceAddress [0] and the parent counts only emitted frames. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a121e69656643935d9773b079316e0bf2bcfead3', 'gasUsed': '0x12c40'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}
- [H20](../../decisions/H20.md): The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [15].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. subtrace 6: nonempty executing bytecode has no operations

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 6: ex {"mem": null, "push": ["0x00"], "store": null, "used": 246494} (8 in total).
- Result shape at `vmTrace`: {'code': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x60006000f3'], 'store': None, 'used': 246497}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 246494}, 'pc': 6, 'sub'

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits no frame; the next sibling keeps traceAddress [0] and the parent counts only emitted frames. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a121e69656643935d9773b079316e0bf2bcfead3', 'gasUsed': '0x12c40'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}
- [H20](../../decisions/H20.md): The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [15].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits no frame; the next sibling keeps traceAddress [0] and the parent counts only emitted frames. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a121e69656643935d9773b079316e0bf2bcfead3', 'gasUsed': '0x12c40'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}
- [H20](../../decisions/H20.md): The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [15].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.

</details>

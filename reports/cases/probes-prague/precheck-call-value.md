# Precheck call value

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth. A CALL or CREATE that fails its balance precheck emits no frame; the next sibling keeps traceAddress [0] and the parent counts only emitted frames. The caller continues: the failed CALL pushes 0 and the next CALL succeeds. The CALL whose precheck failed has sub null; the sibling that entered a frame has a sub. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Failed frames have an error string; an exceptional halt omits result or sets it to null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-prague/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-prague/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-prague/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x600060006000600060016110025af1600052600060006000600060006110025af160205260406000f3",
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

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H20](../../decisions/H20.md): The CALL whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [14].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 7 call mem is not the full output window; subtrace 7: nonempty executing bytecode has no operations; operation 17 call mem is not the full output window
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2c8', 'init': '0x600060006000600060016110025af1600052600060006000600060006110025af160205260406000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x000000000000000000000000

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H20](../../decisions/H20.md): The CALL whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [14].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 7 call mem is not the full output window; subtrace 7: nonempty executing bytecode has no operations; operation 17 call mem is not the full output window
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2c8', 'init': '0x600060006000600060016110025af1600052600060006000600060006110025af160205260406000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x000000000000000000000000

**Erigon · 3.8.0-dev · f8cfe5a7** (`3.8.0-dev-f8cfe5a7`)

- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits no frame; the next sibling keeps traceAddress [0] and the parent counts only emitted frames. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2c8', 'init': '0x600060006000600060016110025af1600052600060006000600060006110025af160205260406000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0xad64'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}
- [H20](../../decisions/H20.md): The CALL whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [14].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. subtrace 7: nonempty executing bytecode has no operations

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits no frame; the next sibling keeps traceAddress [0] and the parent counts only emitted frames. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2c8', 'init': '0x600060006000600060016110025af1600052600060006000600060006110025af160205260406000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0xad64'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}
- [H20](../../decisions/H20.md): The CALL whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [14].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. subtrace 7: nonempty executing bytecode has no operations

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: ex {"mem": null, "push": ["0x00"], "store": null, "used": 246469} (19 in total).
- Result shape at `vmTrace`: {'code': '0x600060006000600060016110025af1600052600060006000600060006110025af160205260406000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 246469}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 246466}, 'pc': 2,

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits no frame; the next sibling keeps traceAddress [0] and the parent counts only emitted frames. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2c8', 'init': '0x600060006000600060016110025af1600052600060006000600060006110025af160205260406000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0xad64'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}
- [H20](../../decisions/H20.md): The CALL whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [14].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits no frame; the next sibling keeps traceAddress [0] and the parent counts only emitted frames. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2c8', 'init': '0x600060006000600060016110025af1600052600060006000600060006110025af160205260406000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0xad64'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}
- [H20](../../decisions/H20.md): The CALL whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [14].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.

</details>

# Precheck create value

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt carries result null. A CALL or CREATE that fails its balance precheck emits a failed frame with no result and no subtraces; the next sibling follows at [1] and the parent counts both. A CREATE that fails its balance precheck has error "Insufficient balance for transfer". The caller continues: the failed CREATE pushes 0 and the next CREATE uses the unchanged creator nonce. The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 3 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 3 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 3 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 3 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |

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

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress [0]: creationMethod null
- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress [0, 0]: creationMethod null
- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (21 in total).
- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits a failed frame with no result and no subtraces; the next sibling follows at [1] and the parent counts both. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}, got {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a121e69656643935d9773b079316e0bf2bcfead3', 'gasUsed': '0x0'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}
- [H09](../../decisions/H09.md): A CREATE that fails its balance precheck has error "Insufficient balance for transfer". No frame matches {'action': {'value': '0x1'}, 'traceAddress': [0], 'type': 'create'}.
- [H20](../../decisions/H20.md): The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [15].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 6 entered no child frame, but its cost does not include the gas it forwarded; subtrace 6: nonempty executing bytecode has no operations
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000
- Result shape at `trace/1`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338b6', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000
- Result shape at `trace/2`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x2bd97', 'init': '0x60006000f3', 'value': '0x0'}, 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0x', 'gasUsed': '0x6'}, 'subtraces': 0, 'traceAddress': [0, 0], 'type': 'create'} is not valid und
- Result shape at `vmTrace`: {'code': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x60006000f3'], 'store': None, 'used': 246497}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 246494}, 'pc': 6, 'sub':

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress [0]: creationMethod null
- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress [0, 0]: creationMethod null
- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (21 in total).
- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits a failed frame with no result and no subtraces; the next sibling follows at [1] and the parent counts both. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}, got {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a121e69656643935d9773b079316e0bf2bcfead3', 'gasUsed': '0x0'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}
- [H09](../../decisions/H09.md): A CREATE that fails its balance precheck has error "Insufficient balance for transfer". No frame matches {'action': {'value': '0x1'}, 'traceAddress': [0], 'type': 'create'}.
- [H20](../../decisions/H20.md): The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [15].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 6 entered no child frame, but its cost does not include the gas it forwarded; subtrace 6: nonempty executing bytecode has no operations
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000
- Result shape at `trace/1`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338b6', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000
- Result shape at `trace/2`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x2bd97', 'init': '0x60006000f3', 'value': '0x0'}, 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0x', 'gasUsed': '0x6'}, 'subtraces': 0, 'traceAddress': [0, 0], 'type': 'create'} is not valid und
- Result shape at `vmTrace`: {'code': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x60006000f3'], 'store': None, 'used': 246497}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 246494}, 'pc': 6, 'sub':

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (21 in total).
- Result shape at `vmTrace`: {'code': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x60006000f3'], 'store': None, 'used': 246497}, 'idx': '0', 'op': 'PUSH5', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (21 in total).
- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [0]: error 'Insufficient balance for transfer', result null.
- Result shape at `trace/1`: {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338b6', 'init': '0x60006000f3', 'value': '0x1'}, 'error': 'Insufficient balance for transfer', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `vmTrace`: {'code': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x60006000f3'], 'store': None, 'used': 246497}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 246494}, 'pc': 6, 'sub':

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 6 entered no child frame, but its cost does not include the gas it forwarded

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 6 entered no child frame, but its cost does not include the gas it forwarded

</details>

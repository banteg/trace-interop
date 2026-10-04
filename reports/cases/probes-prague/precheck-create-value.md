# Precheck create value

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt omits result or sets it to null. A CALL or CREATE that fails its balance precheck emits a failed frame with no result and no subtraces; the next sibling follows at [1] and the parent counts both. A CREATE that fails its balance precheck has error "Insufficient balance for transfer". The caller continues: the failed CREATE pushes 0 and the next CREATE uses the unchanged creator nonce. The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 3 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 2 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |

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

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits a failed frame with no result and no subtraces; the next sibling follows at [1] and the parent counts both. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}, got {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a121e69656643935d9773b079316e0bf2bcfead3', 'gasUsed': '0x0'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}
- [H09](../../decisions/H09.md): A CREATE that fails its balance precheck has error "Insufficient balance for transfer". No frame matches {'action': {'value': '0x1'}, 'traceAddress': [0], 'type': 'create'}.
- [H20](../../decisions/H20.md): The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [15].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 6 entered no child frame, but its cost does not include the gas it forwarded; subtrace 6: nonempty executing bytecode has no operations
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000
- Result shape at `trace/1`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338b6', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000
- Result shape at `trace/2`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x2bd97', 'init': '0x60006000f3', 'value': '0x0'}, 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0x', 'gasUsed': '0x6'}, 'subtraces': 0, 'traceAddress': [0, 0], 'type': 'create'} is not valid und

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits a failed frame with no result and no subtraces; the next sibling follows at [1] and the parent counts both. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}, got {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a121e69656643935d9773b079316e0bf2bcfead3', 'gasUsed': '0x0'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}
- [H09](../../decisions/H09.md): A CREATE that fails its balance precheck has error "Insufficient balance for transfer". No frame matches {'action': {'value': '0x1'}, 'traceAddress': [0], 'type': 'create'}.
- [H20](../../decisions/H20.md): The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [15].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 6 entered no child frame, but its cost does not include the gas it forwarded; subtrace 6: nonempty executing bytecode has no operations
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000
- Result shape at `trace/1`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338b6', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000
- Result shape at `trace/2`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x2bd97', 'init': '0x60006000f3', 'value': '0x0'}, 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0x', 'gasUsed': '0x6'}, 'subtraces': 0, 'traceAddress': [0, 0], 'type': 'create'} is not valid und

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H09](../../decisions/H09.md): A CREATE that fails its balance precheck has error "Insufficient balance for transfer". Expected {'error': 'Insufficient balance for transfer'}; got {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338b6', 'init': '0x60006000f3', 'value': '0x1'}, 'error': 'insufficient balance for transfer', 'result': None, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- [H20](../../decisions/H20.md): The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [15].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. subtrace 6: nonempty executing bytecode has no operations

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits a failed frame with no result and no subtraces; the next sibling follows at [1] and the parent counts both. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2e4', 'init': '0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a121e69656643935d9773b079316e0bf2bcfead3', 'gasUsed': '0x12c40'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}
- [H09](../../decisions/H09.md): A CREATE that fails its balance precheck has error "Insufficient balance for transfer". No frame matches {'action': {'value': '0x1'}, 'traceAddress': [0], 'type': 'create'}.
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 6 entered no child frame, but its cost does not include the gas it forwarded

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H20](../../decisions/H20.md): The CREATE whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [15].

</details>

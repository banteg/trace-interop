# Precheck call value

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt carries result null. A CALL or CREATE that fails its balance precheck emits a failed frame with no result and no subtraces; the next sibling follows at [1] and the parent counts both. A CALL that fails its balance precheck has error "Insufficient balance for transfer". The caller continues: the failed CALL pushes 0 and the next CALL succeeds. The CALL whose precheck failed has sub null; the sibling that entered a frame has a sub. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 3 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |

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

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (32 in total).
- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits a failed frame with no result and no subtraces; the next sibling follows at [1] and the parent counts both. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2c8', 'init': '0x600060006000600060016110025af1600052600060006000600060006110025af160205260406000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0xad64'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}
- [H09](../../decisions/H09.md): A CALL that fails its balance precheck has error "Insufficient balance for transfer". No frame matches {'action': {'value': '0x1'}, 'traceAddress': [0], 'type': 'call'}.
- [H20](../../decisions/H20.md): The CALL whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [14].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 7 entered no child frame, but its cost does not include the gas it forwarded; operation 7 call mem is neither the output window nor the copied return data; subtrace 7: nonempty executing bytecode has no operations; operation 17 call mem is neither the output window nor the copied return data
- Result shape at `vmTrace`: {'code': '0x600060006000600060016110025af1600052600060006000600060006110025af160205260406000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 246469}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 246466}, 'pc': 2, '

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (32 in total).
- [H29](../../decisions/H29.md): A CALL or CREATE that fails its balance precheck emits a failed frame with no result and no subtraces; the next sibling follows at [1] and the parent counts both. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2c8', 'init': '0x600060006000600060016110025af1600052600060006000600060006110025af160205260406000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0xad64'}, 'subtraces': 1, 'traceAddress': [], 'type': 'create'}
- [H09](../../decisions/H09.md): A CALL that fails its balance precheck has error "Insufficient balance for transfer". No frame matches {'action': {'value': '0x1'}, 'traceAddress': [0], 'type': 'call'}.
- [H20](../../decisions/H20.md): The CALL whose precheck failed has sub null; the sibling that entered a frame has a sub. Operations missing at pc []; wrong sub at pc [14].
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 7 entered no child frame, but its cost does not include the gas it forwarded; operation 7 call mem is neither the output window nor the copied return data; subtrace 7: nonempty executing bytecode has no operations; operation 17 call mem is neither the output window nor the copied return data
- Result shape at `vmTrace`: {'code': '0x600060006000600060016110025af1600052600060006000600060006110025af160205260406000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 246469}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 246466}, 'pc': 2, '

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (32 in total).
- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [0]: error 'Insufficient balance for transfer', result null.
- Result shape at `trace/1`: {'action': {'callType': 'call', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x3900b', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x1'}, 'error': 'Insufficient balance for transfer', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid
- Result shape at `vmTrace`: {'code': '0x600060006000600060016110025af1600052600060006000600060006110025af160205260406000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 246469}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 246466}, 'pc': 2, '

</details>

# Constructor

`trace_call` · repeat · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Creation vmTrace.code is executing initcode. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "data": "0x60016000526001601ff3",
      "gas": "0x927c0",
      "gasPrice": "0x77359400"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "0x30"
  ]
}
```

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H19](../../decisions/H19.md): Creation vmTrace.code is executing initcode.
- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x60016000526001601ff3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 546847, got 546850; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 546844, got 546847; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 546847, got 546850; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 546844, got 546847; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x85822', 'init': '0x60016000526001601ff3', 'value': '0x0'}, 'result': {'address': '0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41', 'code': '0x01', 'gasUsed': '0xda'}, 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x85822', 'init': '0x60016000526001601ff3', 'value': '0x0'}, 'result': {'address': '0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41', 'code': '0x01', 'gasUsed': '0xda'}, 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: ex {"mem": null, "push": ["0x01"], "store": null, "used": 546847} (3 in total).
- Result shape at `vmTrace`: {'code': '0x60016000526001601ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x01'], 'store': None, 'used': 546847}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 546844}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x000000000

</details>

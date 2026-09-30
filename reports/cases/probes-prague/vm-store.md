# Vm store

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth. store is set by each completed SSTORE with its key and value, including an unchanged warm write; SLOAD, TSTORE and TLOAD never set it. Its presence does not depend on selecting stateDiff. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes. A new contract has creation markers for nonce one, returned runtime and balance, including empty values.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x602a600155602a600155600254600760035d60035c600080f3",
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

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H17](../../decisions/H17.md): A new contract has creation markers for nonce one, returned runtime and balance, including empty values.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H20](../../decisions/H20.md): store is set by each completed SSTORE with its key and value, including an unchanged warm write; SLOAD, TSTORE and TLOAD never set it. Its presence does not depend on selecting stateDiff. SSTORE at pc 4: expected {'key': '0x1', 'val': '0x2a'}, got None; SSTORE at pc 9: expected {'key': '0x1', 'val': '0x2a'}, got None
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 246607, got 246610; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246604, got 246607; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c352', 'init': '0x602a600155602a600155600254600760035d60035c600080f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x', 'gasUsed': '0x5fd2'}, 'subtraces': 0, 'traceAddress':

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c352', 'init': '0x602a600155602a600155600254600760035d60035c600080f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x', 'gasUsed': '0x5fd2'}, 'subtraces': 0, 'traceAddress':

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 2: ex {"mem": null, "push": ["0x01"], "store": null, "used": 246604} (12 in total).
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 14 DUP1 push is not the top 2 words after execution, deepest first
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 14 pushed stack values disagree with the model
- [H17](../../decisions/H17.md): A new contract has creation markers for nonce one, returned runtime and balance, including empty values.
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0x577a3bbf0100'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x00de48310d77a4d56aa400248b0b1613508f5b73': {'balance': {'+': '0x0'}, 'code': '=', 'nonce': {'+': '0x1'}, 'storage': {'0x00000000000000000000000000000000000000000
- Result shape at `vmTrace`: {'code': '0x602a600155602a600155600254600760035d60035c600080f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 246607}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x01'], 'store': None, 'used': 246604}, 'pc': 2, 'sub': None}, {'cost': 22100, '

</details>

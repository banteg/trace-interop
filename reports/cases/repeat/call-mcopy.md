# Call mcopy

`trace_call` · repeat · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. MCOPY reports its same-step write of word 42 at offset 32. Stack words and storage operands use minimal hex quantities at every depth. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x000000000000000000000000000000000000100a",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x"
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

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 578997, got 579000; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 578994, got 578997; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 2 post-step gas does not deduct this operation cost; operation 3 post-step gas does not deduct this operation cost; operation 6 post-step gas does not deduct this operation cost; operation 7 post-step gas does not deduct this operation cost
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 578997, got 579000; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 578994, got 578997; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 578997, got 579000; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 578994, got 578997; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 2 post-step gas does not deduct this operation cost; operation 3 post-step gas does not deduct this operation cost; operation 6 post-step gas does not deduct this operation cost; operation 7 post-step gas does not deduct this operation cost
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 578997, got 579000; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 578994, got 578997; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H20](../../decisions/H20.md): MCOPY reports its same-step write of word 42 at offset 32.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 6 (MCOPY) mem: expected {'off': 32, 'data': '0x000000000000000000000000000000000000000000000000000000000000002a'}, got None
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 6 (MCOPY) mem: expected {'off': 32, 'data': '0x000000000000000000000000000000000000000000000000000000000000002a'}, got None

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H20](../../decisions/H20.md): MCOPY reports its same-step write of word 42 at offset 32.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 6 (MCOPY) mem: expected {'off': 32, 'data': '0x000000000000000000000000000000000000000000000000000000000000002a'}, got None
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 6 (MCOPY) mem: expected {'off': 32, 'data': '0x000000000000000000000000000000000000000000000000000000000000002a'}, got None

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 2: ex {"mem": null, "push": ["0x00"], "store": null, "used": 578994} (2 in total).
- Result shape at `vmTrace`: {'code': '0x602a6000526020600060205e00', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578994}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x000

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 578997, got 579000; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 578994, got 578997; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 2 post-step gas does not deduct this operation cost; operation 3 post-step gas does not deduct this operation cost; operation 6 post-step gas does not deduct this operation cost; operation 7 post-step gas does not deduct this operation cost
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 578997, got 579000; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 578994, got 578997; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

</details>

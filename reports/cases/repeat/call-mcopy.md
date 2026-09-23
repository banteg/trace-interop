# Call mcopy

`trace_call` · repeat · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. MCOPY reports its same-step write of word 42 at offset 32. Stack words use minimal hex quantities at every depth. At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-repeat/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "to": "0x000000000000000000000000000000000000100a"
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

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H20](../../decisions/H20.md): MCOPY reports its same-step write of word 42 at offset 32.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 6 (MCOPY) ex: expected {'used': 578970, 'push': [], 'mem': {'off': 32, 'data': '0x000000000000000000000000000000000000000000000000000000000000002a'}, 'store': None}, got {'mem': None, 'push': [], 'store': None, 'used': 578970}

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H20](../../decisions/H20.md): MCOPY reports its same-step write of word 42 at offset 32.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 6 (MCOPY) ex: expected {'used': 578970, 'push': [], 'mem': {'off': 32, 'data': '0x000000000000000000000000000000000000000000000000000000000000002a'}, 'store': None}, got {'mem': None, 'push': [], 'store': None, 'used': 578970}

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H20](../../decisions/H20.md): MCOPY reports its same-step write of word 42 at offset 32.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 6 (MCOPY) ex: expected {'used': 578970, 'push': [], 'mem': {'off': 32, 'data': '0x000000000000000000000000000000000000000000000000000000000000002a'}, 'store': None}, got {'mem': None, 'push': [], 'store': None, 'used': 578970}

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 1 (PUSH1) ex: expected {'used': 578994, 'push': ['0x0'], 'mem': None, 'store': None}, got {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578994}; step 4 (PUSH1) ex: expected {'used': 578982, 'push': ['0x0'], 'mem': None, 'store': None}, got {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578982}
- Result shape at `vmTrace`: {'code': '0x602a6000526020600060205e00', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578994}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x000

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 1 (PUSH1) ex: expected {'used': 578994, 'push': ['0x0'], 'mem': None, 'store': None}, got {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578994}; step 4 (PUSH1) ex: expected {'used': 578982, 'push': ['0x0'], 'mem': None, 'store': None}, got {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578982}
- Result shape at `vmTrace`: {'code': '0x602a6000526020600060205e00', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578994}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x000

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. operation 2 post-step gas does not deduct this operation cost; operation 3 post-step gas does not deduct this operation cost; operation 6 post-step gas does not deduct this operation cost; operation 7 post-step gas does not deduct this operation cost
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) ex: expected {'used': 578997, 'push': ['0x2a'], 'mem': None, 'store': None}, got {'mem': {'data': '0x', 'off': 0}, 'push': ['0x2a'], 'store': None, 'used': 579000}; step 1 (PUSH1) ex: expected {'used': 578994, 'push': ['0x0'], 'mem': None, 'store': None}, got {'mem': {'data': '0x', 'off': 0}, 'push': ['0x0'], 'store': None, 'used': 578997}; step 2 (MSTORE) ex: expected {'used': 578988, 'push': [], 'mem': {'off': 0, 'data': '0x000000000000000000000000000000000000000000000000000000000000002a'}, 'store': None}, got {'mem': {'data': '0x', 'off': 0}, 'push': [], 'store': None, 'used': 578994}; step 3 (PUSH1) ex: expected {'used': 578985, 'push': ['0x20'], 'mem': None, 'store': None}, got {'mem': {'data': '0x000000000000000000000000000000000000000000000000000000000000002a', 'off': 32}, 'push': ['0x20'], 'store': None, 'used': 578988}

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. operation 2 post-step gas does not deduct this operation cost; operation 3 post-step gas does not deduct this operation cost; operation 6 post-step gas does not deduct this operation cost; operation 7 post-step gas does not deduct this operation cost
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) ex: expected {'used': 578997, 'push': ['0x2a'], 'mem': None, 'store': None}, got {'mem': {'data': '0x', 'off': 0}, 'push': ['0x2a'], 'store': None, 'used': 579000}; step 1 (PUSH1) ex: expected {'used': 578994, 'push': ['0x0'], 'mem': None, 'store': None}, got {'mem': {'data': '0x', 'off': 0}, 'push': ['0x0'], 'store': None, 'used': 578997}; step 2 (MSTORE) ex: expected {'used': 578988, 'push': [], 'mem': {'off': 0, 'data': '0x000000000000000000000000000000000000000000000000000000000000002a'}, 'store': None}, got {'mem': {'data': '0x', 'off': 0}, 'push': [], 'store': None, 'used': 578994}; step 3 (PUSH1) ex: expected {'used': 578985, 'push': ['0x20'], 'mem': None, 'store': None}, got {'mem': {'data': '0x000000000000000000000000000000000000000000000000000000000000002a', 'off': 32}, 'push': ['0x20'], 'store': None, 'used': 578988}

</details>

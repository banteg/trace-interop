# Model mcopy zero

`trace_call` · coverage · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words use minimal hex quantities at every depth. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes. A new contract has creation markers for nonce one, deployed code and balance, including empty values.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x600060ff60ff5e60006000f3",
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

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000000000: new account lacks creation markers for all fields; 0x00de48310d77a4d56aa400248b0b1613508f5b73: new account lacks creation markers for all fields
- [H17](../../decisions/H17.md): A new contract has creation markers for nonce one, deployed code and balance, including empty values.
- Result shape at `vmTrace`: {'code': '0x600060ff60ff5e60006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 246839}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0xff'], 'store': None, 'used': 246836}, 'pc': 2, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000000000: new account lacks creation markers for all fields; 0x00de48310d77a4d56aa400248b0b1613508f5b73: new account lacks creation markers for all fields
- [H17](../../decisions/H17.md): A new contract has creation markers for nonce one, deployed code and balance, including empty values.
- Result shape at `vmTrace`: {'code': '0x600060ff60ff5e60006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 246839}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0xff'], 'store': None, 'used': 246836}, 'pc': 2, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H19](../../decisions/H19.md): The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. Expected source 0x600060ff60ff5e60006000f3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 246839, got 246842; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246836, got 246839; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. operation 0 mnemonic disagrees with bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 246839, got 246842; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246836, got 246839; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H19](../../decisions/H19.md): The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. Expected source 0x600060ff60ff5e60006000f3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 246839, got 246842; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246836, got 246839; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. operation 0 mnemonic disagrees with bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 246839, got 246842; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246836, got 246839; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

</details>

# Call constructor priced

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Creation vmTrace.code is executing initcode. Successful creation uses address, code and gasUsed. Stack words use minimal hex quantities at every depth. Unsigned execution accepts the supplied nonzero fee and returns one envelope per call; exact environment values are checked by coverage/model-environment. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x60016000526001601ff3",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x186a0",
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

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x60016000526001601ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x01'], 'store': None, 'used': 46847}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 46844}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x00000000000

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x60016000526001601ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x01'], 'store': None, 'used': 46847}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 46844}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x00000000000

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H19](../../decisions/H19.md): Creation vmTrace.code is executing initcode.
- [H19](../../decisions/H19.md): The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. Expected source 0x60016000526001601ff3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 46847, got 46850; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 46844, got 46847; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. operation 0 mnemonic disagrees with bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 46847, got 46850; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 46844, got 46847; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H19](../../decisions/H19.md): Creation vmTrace.code is executing initcode.
- [H19](../../decisions/H19.md): The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. Expected source 0x60016000526001601ff3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 46847, got 46850; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 46844, got 46847; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. operation 0 mnemonic disagrees with bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 46847, got 46850; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 46844, got 46847; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

</details>

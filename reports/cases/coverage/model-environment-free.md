# Model environment free

`trace_call` · coverage · [All reports](../../README.md)

**What this checks:** Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks. Assess the declared property. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words use minimal hex quantities at every depth. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes. GASPRICE, BASEFEE, NUMBER, TIMESTAMP and GASLIMIT preserve the selected block and supplied fee. A new contract has creation markers for nonce one, deployed code and balance, including empty values.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x3a6000524860205243604052426060524560805260a06000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "gasPrice": "0x0"
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

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
- [H08](../../decisions/H08.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H17](../../decisions/H17.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H19](../../decisions/H19.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H20](../../decisions/H20.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H21](../../decisions/H21.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
- [H08](../../decisions/H08.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H17](../../decisions/H17.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H19](../../decisions/H19.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H20](../../decisions/H20.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H21](../../decisions/H21.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
- [H08](../../decisions/H08.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H17](../../decisions/H17.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H19](../../decisions/H19.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H20](../../decisions/H20.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H21](../../decisions/H21.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
- [H08](../../decisions/H08.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H17](../../decisions/H17.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H19](../../decisions/H19.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H20](../../decisions/H20.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H21](../../decisions/H21.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x3a6000524860205243604052426060524560805260a06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0000000000000000000000000000000000000000000000000000000000000000'], 'store': None, 'used': 246620}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': N

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x3a6000524860205243604052426060524560805260a06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0000000000000000000000000000000000000000000000000000000000000000'], 'store': None, 'used': 246620}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': N

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H19](../../decisions/H19.md): The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. Expected source 0x3a6000524860205243604052426060524560805260a06000f3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. operation 0 mnemonic disagrees with bytecode; operation 1 mnemonic disagrees with bytecode; operation 1 post-step gas does not deduct this operation cost; operation 2 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H08](../../decisions/H08.md): Modelled execution returns exactly the independently computed bytes.
- [H15](../../decisions/H15.md): GASPRICE, BASEFEE, NUMBER, TIMESTAMP and GASLIMIT preserve the selected block and supplied fee.
- [H17](../../decisions/H17.md): A new contract has creation markers for nonce one, deployed code and balance, including empty values.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H19](../../decisions/H19.md): The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. Expected source 0x3a6000524860205243604052426060524560805260a06000f3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. operation 0 mnemonic disagrees with bytecode; operation 1 mnemonic disagrees with bytecode; operation 1 post-step gas does not deduct this operation cost; operation 2 pc outside executing bytecode
- [H19](../../decisions/H19.md): Root VM bytecode equals the independently frozen execution source.
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (GASPRICE) used: expected 246620, got 246622; step 0 (GASPRICE) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 246617, got 246620; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H08](../../decisions/H08.md): Modelled execution returns exactly the independently computed bytes.
- [H15](../../decisions/H15.md): GASPRICE, BASEFEE, NUMBER, TIMESTAMP and GASLIMIT preserve the selected block and supplied fee.
- [H17](../../decisions/H17.md): A new contract has creation markers for nonce one, deployed code and balance, including empty values.

</details>

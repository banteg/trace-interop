# Model mcopy zero

`trace_call` · coverage · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes. A new contract has creation markers for nonce one, returned runtime and balance, including empty values.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |

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

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (7 in total).
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c43a', 'init': '0x600060ff60ff5e60006000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x', 'gasUsed': '0x12'}, 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is no
- Result shape at `vmTrace`: {'code': '0x600060ff60ff5e60006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 246839}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0xff'], 'store': None, 'used': 246836}, 'pc': 2, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (7 in total).
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c43a', 'init': '0x600060ff60ff5e60006000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x', 'gasUsed': '0x12'}, 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is no
- Result shape at `vmTrace`: {'code': '0x600060ff60ff5e60006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 246839}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0xff'], 'store': None, 'used': 246836}, 'pc': 2, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (7 in total).
- Result shape at `vmTrace`: {'code': '0x600060ff60ff5e60006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 246839}, 'idx': '0', 'op': 'PUSH1', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0xff'], 'store': None, 'used': 246836}, 'idx': '1', 'op': 'PUSH1', 'pc': 2, 'sub

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (7 in total).
- Result shape at `vmTrace`: {'code': '0x600060ff60ff5e60006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 246839}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0xff'], 'store': None, 'used': 246836}, 'pc': 2, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x

</details>

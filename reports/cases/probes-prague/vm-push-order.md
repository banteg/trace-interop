# Vm push order

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. DUPn and SWAPn push the top n+1 stack words after execution, deepest first. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes. A new contract has creation markers for nonce one, returned runtime and balance, including empty values.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x600160026003829190805050505050600080f3",
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

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (15 in total).
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c3b2', 'init': '0x600160026003829190805050505050600080f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x', 'gasUsed': '0x25'}, 'subtraces': 0, 'traceAddress': [], 'type': '
- Result shape at `vmTrace`: {'code': '0x600160026003829190805050505050600080f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1'], 'store': None, 'used': 246703}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x2'], 'store': None, 'used': 246700}, 'pc': 2, 'sub': None}, {'cost': 3, 'ex': {'mem': None,

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (15 in total).
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c3b2', 'init': '0x600160026003829190805050505050600080f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x', 'gasUsed': '0x25'}, 'subtraces': 0, 'traceAddress': [], 'type': '
- Result shape at `vmTrace`: {'code': '0x600160026003829190805050505050600080f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1'], 'store': None, 'used': 246703}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x2'], 'store': None, 'used': 246700}, 'pc': 2, 'sub': None}, {'cost': 3, 'ex': {'mem': None,

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (15 in total).
- Result shape at `vmTrace`: {'code': '0x600160026003829190805050505050600080f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1'], 'store': None, 'used': 246703}, 'idx': '0', 'op': 'PUSH1', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x2'], 'store': None, 'used': 246700}, 'idx': '1', 'op': 'PUSH1',

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (15 in total).
- Result shape at `vmTrace`: {'code': '0x600160026003829190805050505050600080f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1'], 'store': None, 'used': 246703}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x2'], 'store': None, 'used': 246700}, 'pc': 2, 'sub': None}, {'cost': 3, 'ex': {'mem': None,

</details>

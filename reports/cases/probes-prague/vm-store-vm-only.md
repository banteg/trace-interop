# Vm store vm only

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. store is set by each completed SSTORE with its key and value, including an unchanged warm write; SLOAD, TSTORE and TLOAD never set it. Its presence does not depend on selecting stateDiff. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 0 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 0 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 0 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 0 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |

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
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (16 in total).
- Result shape at `vmTrace`: {'code': '0x602a600155602a600155600254600760035d60035c600080f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 246607}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x1'], 'store': None, 'used': 246604}, 'pc': 2, 'sub': None}, {'cost': 22100, 'e

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (16 in total).
- Result shape at `vmTrace`: {'code': '0x602a600155602a600155600254600760035d60035c600080f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 246607}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x1'], 'store': None, 'used': 246604}, 'pc': 2, 'sub': None}, {'cost': 22100, 'e

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (16 in total).
- Result shape at `vmTrace`: {'code': '0x602a600155602a600155600254600760035d60035c600080f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 246607}, 'idx': '0', 'op': 'PUSH1', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x1'], 'store': None, 'used': 246604}, 'idx': '1', 'o

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (16 in total).
- Result shape at `vmTrace`: {'code': '0x602a600155602a600155600254600760035d60035c600080f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 246607}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x1'], 'store': None, 'used': 246604}, 'pc': 2, 'sub': None}, {'cost': 22100, 'e

</details>

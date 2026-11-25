# Constructor

`trace_call` · repeat · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Creation vmTrace.code is executing initcode. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |

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

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (6 in total).
- Result shape at `vmTrace`: {'code': '0x60016000526001601ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1'], 'store': None, 'used': 546847}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 546844}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x00000000000

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (6 in total).
- Result shape at `vmTrace`: {'code': '0x60016000526001601ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1'], 'store': None, 'used': 546847}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 546844}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x00000000000

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (6 in total).
- Result shape at `vmTrace`: {'code': '0x60016000526001601ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1'], 'store': None, 'used': 546847}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 546844}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x00000000000

</details>

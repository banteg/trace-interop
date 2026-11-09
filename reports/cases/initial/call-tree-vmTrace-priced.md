# Call tree vmtrace priced

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Unsigned execution accepts the supplied nonzero fee and returns one envelope per call; exact environment values are checked by coverage/model-environment. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x"
    },
    [
      "vmTrace"
    ],
    "0x30"
  ]
}
```

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (237 in total).
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 10 post-step gas does not deduct its cost and return the child leftover; operation 22 call mem is neither the output window nor the copied return data; subtrace 38: operation 11 SSTORE store is not its key and value operands; operation 49 call mem is neither the output window nor the copied return data
- Result shape at `vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (237 in total).
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 10 post-step gas does not deduct its cost and return the child leftover; operation 22 call mem is neither the output window nor the copied return data; subtrace 38: operation 11 SSTORE store is not its key and value operands; operation 49 call mem is neither the output window nor the copied return data
- Result shape at `vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (237 in total).
- Result shape at `vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (237 in total).
- Result shape at `vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 81 post-step gas does not deduct its cost and return the child leftover

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 10 post-step gas does not deduct its cost and return the child leftover; operation 22 post-step gas does not deduct its cost and return the child leftover; operation 30 post-step gas does not deduct its cost and return the child leftover; operation 49 post-step gas does not deduct its cost and return the child leftover

</details>

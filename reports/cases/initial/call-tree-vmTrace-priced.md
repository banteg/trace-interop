# Call tree vmtrace priced

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Unsigned execution accepts the supplied nonzero fee and returns one envelope per call; exact environment values are checked by coverage/model-environment. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../clients/anvil_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 558586f0](../../clients/erigon_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · 82516987](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |

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

**Anvil · 1.8.4-nightly · dd372126** (`anvil Version: 1.8.4-nightly+dd372126`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. subtrace 49: operation 23 pc outside executing bytecode

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 2 post-step gas does not deduct this operation cost; operation 3 post-step gas does not deduct this operation cost; operation 10 post-step gas does not deduct its cost and return the child leftover; operation 10 call mem is neither the output window nor the copied return data

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 10 post-step gas does not deduct its cost and return the child leftover; operation 22 call mem is neither the output window nor the copied return data; operation 49 call mem is neither the output window nor the copied return data; operation 70 call mem is neither the output window nor the copied return data

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 10 post-step gas does not deduct its cost and return the child leftover; operation 22 call mem is neither the output window nor the copied return data; operation 49 call mem is neither the output window nor the copied return data; operation 70 call mem is neither the output window nor the copied return data

**Erigon · 3.8.0-dev · 558586f0** (`3.8.0-dev-558586f0`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. subtrace 49: operation 23 pc outside executing bytecode

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. subtrace 49: operation 23 pc outside executing bytecode; subtrace 81: operation 6 has a subtrace but entered no child frame

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 33: ex {"mem": null, "push": ["0x00"], "store": null, "used": 578994} (124 in total).
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. subtrace 30: operation 2 DUP2 push is not the top 3 words after execution, deepest first; subtrace 30: operation 7 DUP2 push is not the top 3 words after execution, deepest first; subtrace 30: operation 12 DUP2 push is not the top 3 words after execution, deepest first; subtrace 30: operation 17 DUP2 push is not the top 3 words after execution, deepest first
- Result shape at `vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261

**Reth · 2.5.2 · 5723a3fe** (`Reth Version: 2.5.2+5723a3fe`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. subtrace 49: operation 23 pc outside executing bytecode

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. subtrace 49: operation 23 pc outside executing bytecode

</details>

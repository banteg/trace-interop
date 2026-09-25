# Replay tree vmtrace

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** trace_replayTransaction Assess the declared property. Individual replay includes its transactionHash. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. The method responds without Method not found (-32601). The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayTransaction",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H19](../../decisions/H19.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H20](../../decisions/H20.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H21](../../decisions/H21.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H19](../../decisions/H19.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H20](../../decisions/H20.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H21](../../decisions/H21.md): Assess the declared property. Cannot inspect this property: unsupported.

**Erigon · 3.8.0-dev · f8cfe5a7** (`3.8.0-dev-f8cfe5a7`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. subtrace 49: operation 23 pc outside executing bytecode; subtrace 81: operation 6 has a subtrace but entered no child frame

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. subtrace 49: operation 23 pc outside executing bytecode; subtrace 81: operation 6 has a subtrace but entered no child frame

**Nethermind · 2.1.0-preview · ee1f57da** (`2.1.0-preview+ee1f57da`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 10 call mem is not the full output window

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 33: ex {"mem": null, "push": ["0x00"], "store": null, "used": 578994} (125 in total).
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 10 call mem is not the full output window; subtrace 30: operation 2 DUP2 push is not the top 3 words after execution, deepest first; subtrace 30: operation 7 DUP2 push is not the top 3 words after execution, deepest first; subtrace 30: operation 12 DUP2 push is not the top 3 words after execution, deepest first
- Result shape at `/`: {'output': '0xffee', 'stateDiff': None, 'trace': [], 'transactionHash': '0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738', 'vmTrace': {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 2 post-step gas does not deduct this operation cost; operation 3 post-step gas does not deduct this operation cost; operation 10 post-step gas does not deduct its cost and return the child leftover; operation 10 call mem is not the full output window

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738.
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 2 post-step gas does not deduct this operation cost; operation 3 post-step gas does not deduct this operation cost; operation 10 post-step gas does not deduct its cost and return the child leftover; operation 10 call mem is not the full output window
- Result shape at `/`: {'output': '0xffee', 'stateDiff': None, 'trace': [], 'vmTrace': {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60

</details>

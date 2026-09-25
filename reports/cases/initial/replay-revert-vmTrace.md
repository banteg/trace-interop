# Replay revert vmtrace

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** trace_replayTransaction Assess the declared property. Individual replay includes its transactionHash. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. The method responds without Method not found (-32601). The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayTransaction",
  "params": [
    "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
    [
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H20](../../decisions/H20.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H21](../../decisions/H21.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H20](../../decisions/H20.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H21](../../decisions/H21.md): Assess the declared property. Cannot inspect this property: unsupported.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: ex {"mem": null, "push": ["0x00"], "store": null, "used": 78981} (8 in total).
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 5 pushed stack values disagree with the model; step 6 pushed stack values disagree with the model
- Result shape at `/`: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [], 'transactionHash': '0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae', 'vmTra

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 78981, got 78984; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (CALLDATALOAD) used: expected 78978, got 78981; step 1 (CALLDATALOAD) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 3 post-step gas does not deduct this operation cost; operation 4 post-step gas does not deduct this operation cost; operation 5 post-step gas does not deduct this operation cost; operation 8 post-step gas does not deduct this operation cost

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 78981, got 78984; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (CALLDATALOAD) used: expected 78978, got 78981; step 1 (CALLDATALOAD) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 3 post-step gas does not deduct this operation cost; operation 4 post-step gas does not deduct this operation cost; operation 5 post-step gas does not deduct this operation cost; operation 8 post-step gas does not deduct this operation cost
- Result shape at `/`: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [], 'vmTrace': {'code': '0x6000356142ff54501515603b577f4e487b71000000000000000000000000000000000000

</details>

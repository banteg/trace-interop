# Replay block tree

`trace_replayBlockTransactions` · initial · [All reports](../../README.md)

**What this checks:** Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The method responds without Method not found (-32601). Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. The creation fixture contains its CREATE frame and successful creations include address, code and gasUsed. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Replay VM numeric fields use nonnegative integers; stack words and storage operands use minimal quantities at every depth. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 5 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 5 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 5 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 5 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x2",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.9-develop · cf89071f** (`besu/v26.9-develop-cf89071/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H10](../../decisions/H10.md): The creation fixture contains its CREATE frame and successful creations include address, code and gasUsed.
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 10 post-step gas does not deduct its cost and return the child leftover; operation 10 call mem is not the full output window; operation 22 call mem is not the full output window; operation 49 call mem is not the full output window
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000
- Result shape at `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `1/trace/7`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceA

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H10](../../decisions/H10.md): The creation fixture contains its CREATE frame and successful creations include address, code and gasUsed.
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 10 post-step gas does not deduct its cost and return the child leftover; operation 10 call mem is not the full output window; operation 22 call mem is not the full output window; operation 49 call mem is not the full output window
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000
- Result shape at `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `1/trace/7`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceA

**Erigon · 3.8.0-dev · 01c118ee** (`3.8.0-dev-01c118ee`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. subtrace 49: operation 23 pc outside executing bytecode; subtrace 81: operation 6 has a subtrace but entered no child frame

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. subtrace 49: operation 23 pc outside executing bytecode; subtrace 81: operation 6 has a subtrace but entered no child frame

**Nethermind · 2.1.0-preview · 54b760cd** (`2.1.0-preview+54b760cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H21](../../decisions/H21.md): Replay VM numeric fields use nonnegative integers; stack words and storage operands use minimal quantities at every depth.
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 10 call mem is not the full output window
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given s
- Result shape at `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `1/vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261
- Result shape at `4/vmTrace`: {'code': '0x36156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x7'], 'store': None, 'used': 48886}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 48883}, 'pc': 1, 'sub': None}, {'cost': 3, 'ex': {'mem': N

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 5 pushed stack values disagree with the model; step 6 pushed stack values disagree with the model
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 3 pushed stack values disagree with the model
- [H21](../../decisions/H21.md): Replay VM numeric fields use nonnegative integers; stack words and storage operands use minimal quantities at every depth.
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 10 call mem is not the full output window; subtrace 30: operation 2 DUP2 push is not the top 3 words after execution, deepest first; subtrace 30: operation 7 DUP2 push is not the top 3 words after execution, deepest first; subtrace 30: operation 12 DUP2 push is not the top 3 words after execution, deepest first
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given s
- Result shape at `0/vmTrace`: {'code': '0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7f08c379a0000000000000000000000000000000000000000000000000000000006000526020600452600a6024527f75736572206572726f7200000000000000000000000000000000000000000000604452604e
- Result shape at `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `1/vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261
- Result shape at `2/vmTrace`: {'code': '0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0d'], 'store': None, 'used': 19211}, 'pc': 0, 'sub': None}, {'cost': 2, 'ex': {'mem': None, 'push': ['0x00000023'], 'store': None, 'used': 19209}, 'pc': 2, 'sub':
- Result shape at `4/vmTrace`: {'code': '0x36156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x00000007'], 'store': None, 'used': 48886}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 48883}, 'pc': 1, 'sub': None}, {'cost': 3, 'ex': {'mem':

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 78981, got 78984; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (CALLDATALOAD) used: expected 78978, got 78981; step 1 (CALLDATALOAD) mem: expected None, got {'data': '0x', 'off': 0}
- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739d.
- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 19211, got 19214; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (CODESIZE) used: expected 19209, got 19211; step 1 (CODESIZE) mem: expected None, got {'data': '0x', 'off': 0}
- [H18](../../decisions/H18.md): Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Authority 0xeda8645ba6948855e3b3cd596bbb07596d59c603; 1 of 1 tuples valid; expected {'code': {'*': {'from': '0x', 'to': '0xef01004055cae5c7d838cda10d40f9d07106c7f5f3be1c'}}, 'nonce': {'*': {'from': '0x0', 'to': '0x1'}}}.
- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x36156009575f355f555b305f525f5460205260405ff3.
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 78981, got 78984; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (CALLDATALOAD) used: expected 78978, got 78981; step 1 (CALLDATALOAD) mem: expected None, got {'data': '0x', 'off': 0}
- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739d.
- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 19211, got 19214; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (CODESIZE) used: expected 19209, got 19211; step 1 (CODESIZE) mem: expected None, got {'data': '0x', 'off': 0}
- [H18](../../decisions/H18.md): Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Authority 0xeda8645ba6948855e3b3cd596bbb07596d59c603; 1 of 1 tuples valid; expected {'code': {'*': {'from': '0x', 'to': '0xef01004055cae5c7d838cda10d40f9d07106c7f5f3be1c'}}, 'nonce': {'*': {'from': '0x0', 'to': '0x1'}}}.
- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x36156009575f355f555b305f525f5460205260405ff3.
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 0 pc outside executing bytecode; operation 1 pc outside executing bytecode; operation 2 pc outside executing bytecode; operation 3 pc outside executing bytecode

</details>

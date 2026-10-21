# Replay block tree

`trace_replayBlockTransactions` · initial · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Reward and SELFDESTRUCT records carry result null. The method responds without Method not found (-32601). Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. The creation fixture contains its CREATE frame; every creation names its creationMethod and successful creations include address, code and gasUsed. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. An account created and destroyed within the transaction is absent at both endpoints and has no account diff. Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Replay VM numeric fields use nonnegative integers; stack words and storage operands use minimal quantities at every depth. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 5 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |

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

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H10](../../decisions/H10.md): The creation fixture contains its CREATE frame; every creation names its creationMethod and successful creations include address, code and gasUsed. traceAddress [6]: result.code null
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 10 post-step gas does not deduct its cost and return the child leftover; operation 22 call mem is neither the output window nor the copied return data; subtrace 38: operation 11 SSTORE store is not its key and value operands; operation 49 call mem is neither the output window nor the copied return data
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000
- Result shape at `0/vmTrace`: {'code': '0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7f08c379a0000000000000000000000000000000000000000000000000000000006000526020600452600a6024527f75736572206572726f7200000000000000000000000000000000000000000000604452604e
- Result shape at `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under an
- Result shape at `1/trace/7`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceA
- Result shape at `1/vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261
- Result shape at `2/vmTrace`: {'code': '0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xd'], 'store': None, 'used': 19211}, 'pc': 0, 'sub': None}, {'cost': 2, 'ex': {'mem': None, 'push': ['0x23'], 'store': None, 'used': 19209}, 'pc': 2, 'sub': None},
- Result shape at `4/vmTrace`: {'code': '0x36156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x7'], 'store': None, 'used': 48886}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 48883}, 'pc': 1, 'sub': None}, {'cost': 3, 'ex': {'mem': N

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H10](../../decisions/H10.md): The creation fixture contains its CREATE frame; every creation names its creationMethod and successful creations include address, code and gasUsed. traceAddress [6]: result.code null
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 10 post-step gas does not deduct its cost and return the child leftover; operation 22 call mem is neither the output window nor the copied return data; subtrace 38: operation 11 SSTORE store is not its key and value operands; operation 49 call mem is neither the output window nor the copied return data
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000
- Result shape at `0/vmTrace`: {'code': '0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7f08c379a0000000000000000000000000000000000000000000000000000000006000526020600452600a6024527f75736572206572726f7200000000000000000000000000000000000000000000604452604e
- Result shape at `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under an
- Result shape at `1/trace/7`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceA
- Result shape at `1/vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261
- Result shape at `2/vmTrace`: {'code': '0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xd'], 'store': None, 'used': 19211}, 'pc': 0, 'sub': None}, {'cost': 2, 'ex': {'mem': None, 'push': ['0x23'], 'store': None, 'used': 19209}, 'pc': 2, 'sub': None},
- Result shape at `4/vmTrace`: {'code': '0x36156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x7'], 'store': None, 'used': 48886}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 48883}, 'pc': 1, 'sub': None}, {'cost': 3, 'ex': {'mem': N

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- Result shape at `0/vmTrace`: {'code': '0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7f08c379a0000000000000000000000000000000000000000000000000000000006000526020600452600a6024527f75736572206572726f7200000000000000000000000000000000000000000000604452604e
- Result shape at `1/vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261
- Result shape at `2/vmTrace`: {'code': '0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xd'], 'store': None, 'used': 19211}, 'idx': '2-0', 'op': 'PUSH1', 'pc': 0, 'sub': None}, {'cost': 2, 'ex': {'mem': None, 'push': ['0x23'], 'store': None, 'used': 19
- Result shape at `4/vmTrace`: {'code': '0x36156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x7'], 'store': None, 'used': 48886}, 'idx': '4-0', 'op': 'CALLDATASIZE', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 48883}, 'idx': '4-1',

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [3]: error 'Mutable Call In Static Context', result null.
- Result shape at `0/vmTrace`: {'code': '0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7f08c379a0000000000000000000000000000000000000000000000000000000006000526020600452600a6024527f75736572206572726f7200000000000000000000000000000000000000000000604452604e
- Result shape at `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Mutable Call In Static Context', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not vali
- Result shape at `1/vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261
- Result shape at `2/vmTrace`: {'code': '0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xd'], 'store': None, 'used': 19211}, 'pc': 0, 'sub': None}, {'cost': 2, 'ex': {'mem': None, 'push': ['0x23'], 'store': None, 'used': 19209}, 'pc': 2, 'sub': None},
- Result shape at `4/vmTrace`: {'code': '0x36156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x7'], 'store': None, 'used': 48886}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 48883}, 'pc': 1, 'sub': None}, {'cost': 3, 'ex': {'mem': N

</details>

# Replay block tree

`trace_replayBlockTransactions` · initial · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The method responds without Method not found (-32601). Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. The creation fixture contains its CREATE frame; every creation names its creationMethod and successful creations include address, code and gasUsed. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. An account created and destroyed within the transaction is absent at both endpoints and has no account diff. Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Replay VM numeric fields use nonnegative integers; stack words and storage operands use minimal quantities at every depth. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 5 records | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 5 records | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |

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

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H10](../../decisions/H10.md): The creation fixture contains its CREATE frame; every creation names its creationMethod and successful creations include address, code and gasUsed. traceAddress [6]: result.code null
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 10 post-step gas does not deduct its cost and return the child leftover; operation 22 call mem is neither the output window nor the copied return data; subtrace 38: operation 11 SSTORE store is not its key and value operands; operation 49 call mem is neither the output window nor the copied return data
- Result shape at `/`: [{'output': '0x', 'revertReason': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x35561', 'to':

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H10](../../decisions/H10.md): The creation fixture contains its CREATE frame; every creation names its creationMethod and successful creations include address, code and gasUsed. traceAddress [6]: result.code null
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. operation 10 post-step gas does not deduct its cost and return the child leftover; operation 22 call mem is neither the output window nor the copied return data; subtrace 38: operation 11 SSTORE store is not its key and value operands; operation 49 call mem is neither the output window nor the copied return data
- Result shape at `/`: [{'output': '0x', 'revertReason': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x35561', 'to':

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. subtrace 49: operation 23 pc outside executing bytecode; subtrace 81: operation 6 has a subtrace but entered no child frame

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. subtrace 49: operation 23 pc outside executing bytecode

</details>

# Call siblings revert ok

`trace_call` · a · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. The successful second sibling retains its output and has no error. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001005",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x"
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

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): The successful second sibling retains its output and has no error.
- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (28 in total).
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- Result shape at `trace/1`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid under any of the given sch
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [1], 'type': 'call'} is not valid under any of the given sch
- Result shape at `vmTrace`: {'code': '0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x20'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 578994}, 'pc': 2, 'sub': N

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): The successful second sibling retains its output and has no error.
- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (28 in total).
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- Result shape at `trace/1`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid under any of the given sch
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [1], 'type': 'call'} is not valid under any of the given sch
- Result shape at `vmTrace`: {'code': '0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x20'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 578994}, 'pc': 2, 'sub': N

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (28 in total).
- Result shape at `vmTrace`: {'code': '0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x20'], 'store': None, 'used': 578997}, 'idx': '0', 'op': 'PUSH1', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used':

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (28 in total).
- Result shape at `vmTrace`: {'code': '0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x20'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 578994}, 'pc': 2, 'sub': N

</details>

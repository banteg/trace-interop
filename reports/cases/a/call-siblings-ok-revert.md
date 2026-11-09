# Call siblings ok revert

`trace_call` · a · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001004",
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

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (28 in total).
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001004', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [1], 'type': 'call'} is not valid under any of the given sch
- Result shape at `vmTrace`: {'code': '0x6020600060006000600061100261ea60f1506020600060006000600061100361ea60f15000', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x20'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 578994}, 'pc': 2, 'sub': N

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (28 in total).
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001004', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [1], 'type': 'call'} is not valid under any of the given sch
- Result shape at `vmTrace`: {'code': '0x6020600060006000600061100261ea60f1506020600060006000600061100361ea60f15000', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x20'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 578994}, 'pc': 2, 'sub': N

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (28 in total).
- Result shape at `vmTrace`: {'code': '0x6020600060006000600061100261ea60f1506020600060006000600061100361ea60f15000', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x20'], 'store': None, 'used': 578997}, 'idx': '0', 'op': 'PUSH1', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used':

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (28 in total).
- Result shape at `vmTrace`: {'code': '0x6020600060006000600061100261ea60f1506020600060006000600061100361ea60f15000', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x20'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 578994}, 'pc': 2, 'sub': N

</details>

# Nested delegatecall value1 success

`trace_call` · precompiles · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree. The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome. A handled precompile failure must not mark the successful parent as failed. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/precompiles/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/precompiles/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/precompiles/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/precompiles/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/precompiles/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/precompiles/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/precompiles/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/precompiles/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/precompiles/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/precompiles/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/precompiles/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x100000",
      "gasPrice": "0x3b9aca00",
      "value": "0x1",
      "data": "0x600060005260406000608060006006620186a0f45060006000f3"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- [H29](../../decisions/H29.md): The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.
- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (14 in total).
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f9e', 'init': '0x600060005260406000608060006006620186a0f45060006000f3', 'value': '0x1'}, 'result': {'address': '0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41', 'code': '0x', 'gasUsed': '0x129'}, 'subtraces': 0, 'traceAddress'
- Result shape at `vmTrace`: {'code': '0x600060005260406000608060006006620186a0f45060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995227}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995224}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex':

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- [H29](../../decisions/H29.md): The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.
- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (14 in total).
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f9e', 'init': '0x600060005260406000608060006006620186a0f45060006000f3', 'value': '0x1'}, 'result': {'address': '0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41', 'code': '0x', 'gasUsed': '0x129'}, 'subtraces': 0, 'traceAddress'
- Result shape at `vmTrace`: {'code': '0x600060005260406000608060006006620186a0f45060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995227}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995224}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex':

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (14 in total).
- Result shape at `vmTrace`: {'code': '0x600060005260406000608060006006620186a0f45060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995227}, 'idx': '0', 'op': 'PUSH1', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995224}, 'idx': '1', '

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (14 in total).
- Result shape at `vmTrace`: {'code': '0x600060005260406000608060006006620186a0f45060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995227}, 'idx': '0', 'op': 'PUSH1', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995224}, 'idx': '1', '

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (14 in total).
- Result shape at `vmTrace`: {'code': '0x600060005260406000608060006006620186a0f45060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995227}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995224}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex':

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (14 in total).
- Result shape at `vmTrace`: {'code': '0x600060005260406000608060006006620186a0f45060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995227}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 995224}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex':

</details>

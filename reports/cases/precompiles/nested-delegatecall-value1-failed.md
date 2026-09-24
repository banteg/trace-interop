# Nested delegatecall value1 failed

`trace_call` · precompiles · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree. The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome. A handled precompile failure must not mark the successful parent as failed. Stack words use minimal hex quantities at every depth. Failed frames have an error string and an explicit object or null result. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompiles/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompiles/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompiles/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompiles/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompiles/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompiles/manifest.json) |
| [Nethermind · 2.1.0-unstable · 9d6e8b8d](../../clients/nethermind_development.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompiles/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompiles/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompiles/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x602a60005260406000608060006006620186a0f45060006000f3",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x100000",
      "gasPrice": "0x3b9aca00",
      "value": "0x1"
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

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- [H29](../../decisions/H29.md): The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.
- [H24](../../decisions/H24.md): A handled precompile failure must not mark the successful parent as failed.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f92', 'init': '0x602a60005260406000608060006006620186a0f45060006000f3', 'value': '0x1'}, 'error': 'Precompile error', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- [H29](../../decisions/H29.md): The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.
- [H24](../../decisions/H24.md): A handled precompile failure must not mark the successful parent as failed.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f92', 'init': '0x602a60005260406000608060006006620186a0f45060006000f3', 'value': '0x1'}, 'error': 'Precompile error', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

**Nethermind · 2.1.0-unstable · 9d6e8b8d** (`2.1.0-unstable+9d6e8b8d`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/1`: {'action': {'callType': 'delegatecall', 'from': '0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41', 'gas': '0x186a0', 'input': '0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/1`: {'action': {'callType': 'delegatecall', 'from': '0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41', 'gas': '0x186a0', 'input': '0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
- Result shape at `vmTrace`: {'code': '0x602a60005260406000608060006006620186a0f45060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 995215}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995212}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex

</details>

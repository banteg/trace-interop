# Nested staticcall value0 failed

`trace_call` · precompiles · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree. A handled precompile failure must not mark the successful parent as failed. Successful creation uses address, code and gasUsed. Stack words use minimal hex quantities at every depth. Failed frames have an error string and an explicit object or null result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 1 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 1 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 1 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 1 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-geth-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-geth-precompiles/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 1 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 1 call frames; output `0x` | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 1 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 1 call frames; output `0x` | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-precompiles/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-precompiles/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x602a60005260406000608060006006620186a0fa5060006000f3",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x100000",
      "gasPrice": "0x3b9aca00",
      "value": "0x0"
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

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): A handled precompile failure must not mark the successful parent as failed.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f92', 'init': '0x602a60005260406000608060006006620186a0fa5060006000f3', 'value': '0x0'}, 'error': 'Precompile error', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): A handled precompile failure must not mark the successful parent as failed.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f92', 'init': '0x602a60005260406000608060006006620186a0fa5060006000f3', 'value': '0x0'}, 'error': 'Precompile error', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x602a60005260406000608060006006620186a0fa5060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 995215}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995212}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x602a60005260406000608060006006620186a0fa5060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 995215}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995212}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex

</details>

# Call siblings revert ok

`trace_call` · repeat · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. The successful second sibling retains its output and has no error. Stack words use minimal hex quantities at every depth. Failed frames have an error string and an explicit object or null result. The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 3 call frames; output `0x` | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 3 call frames; output `0x` | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 3 call frames; output `0x` | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-geth-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-geth-repeat/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 3 call frames; output `0x` | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 3 call frames; output `0x` | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "to": "0x0000000000000000000000000000000000001005"
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

**Geth draft fork · 🧪 Draft fork** (`Geth/v1.17.6-unstable-40eecf36-2026-09-23/linux-amd64/go1.26.1`)

- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): The successful second sibling retains its output and has no error.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `trace/1`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid under any of the given sch
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [1], 'type': 'call'} is not valid under any of the given sch

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): The successful second sibling retains its output and has no error.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `trace/1`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid under any of the given sch
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [1], 'type': 'call'} is not valid under any of the given sch

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `trace/1`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid under any of the given sch
- Result shape at `vmTrace`: {'code': '0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x20'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578994}, 'pc': 2, 'sub':

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `trace/1`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid under any of the given sch
- Result shape at `vmTrace`: {'code': '0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x20'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578994}, 'pc': 2, 'sub':

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

</details>

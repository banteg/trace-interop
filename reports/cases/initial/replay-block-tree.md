# Replay block tree

`trace_replayBlockTransactions` · initial · [All reports](../../README.md)

**What this checks:** Failed frames have an error string and an explicit object or null result. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 5 records | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 5 records | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 5 records | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-initial/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 5 records | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 5 records | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
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

**Geth draft fork · 🧪 Draft fork** (`Geth/v1.17.6-unstable-c36ee43e-2026-09-23/linux-amd64/go1.26.1`)

- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H07](../../decisions/H07.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H10](../../decisions/H10.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H18](../../decisions/H18.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H21](../../decisions/H21.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H07](../../decisions/H07.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H10](../../decisions/H10.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H18](../../decisions/H18.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H21](../../decisions/H21.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000
- Result shape at `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under an
- Result shape at `1/trace/7`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceA

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H07](../../decisions/H07.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H10](../../decisions/H10.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H18](../../decisions/H18.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H21](../../decisions/H21.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000
- Result shape at `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under an
- Result shape at `1/trace/7`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceA

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H07](../../decisions/H07.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H10](../../decisions/H10.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H18](../../decisions/H18.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H21](../../decisions/H21.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H07](../../decisions/H07.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H10](../../decisions/H10.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H18](../../decisions/H18.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H21](../../decisions/H21.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H07](../../decisions/H07.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H10](../../decisions/H10.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H18](../../decisions/H18.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H21](../../decisions/H21.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given s
- Result shape at `0/vmTrace`: {'code': '0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7f08c379a0000000000000000000000000000000000000000000000000000000006000526020600452600a6024527f75736572206572726f7200000000000000000000000000000000000000000000604452604e
- Result shape at `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a
- Result shape at `1/vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261
- Result shape at `2/vmTrace`: {'code': '0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0d'], 'store': None, 'used': 19211}, 'pc': 0, 'sub': None}, {'cost': 2, 'ex': {'mem': None, 'push': ['0x00000023'], 'store': None, 'used': 19209}, 'pc': 2, 'sub':
- Result shape at `4/vmTrace`: {'code': '0x36156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x00000007'], 'store': None, 'used': 48886}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0000000000000000000000000000000000000000000000000000000000000000'], 'store': No

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H07](../../decisions/H07.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H10](../../decisions/H10.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H18](../../decisions/H18.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H21](../../decisions/H21.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given s
- Result shape at `0/vmTrace`: {'code': '0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7f08c379a0000000000000000000000000000000000000000000000000000000006000526020600452600a6024527f75736572206572726f7200000000000000000000000000000000000000000000604452604e
- Result shape at `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- Result shape at `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a
- Result shape at `1/vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261
- Result shape at `2/vmTrace`: {'code': '0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0d'], 'store': None, 'used': 19211}, 'pc': 0, 'sub': None}, {'cost': 2, 'ex': {'mem': None, 'push': ['0x00000023'], 'store': None, 'used': 19209}, 'pc': 2, 'sub':
- Result shape at `4/vmTrace`: {'code': '0x36156009575f355f555b305f525f5460205260405ff3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x00000007'], 'store': None, 'used': 48886}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 48883}, 'pc': 1, 'sub': None}, {'cost': 3, 'ex': {'mem':

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H07](../../decisions/H07.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H10](../../decisions/H10.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H18](../../decisions/H18.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H21](../../decisions/H21.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H07](../../decisions/H07.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H10](../../decisions/H10.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H18](../../decisions/H18.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H21](../../decisions/H21.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

</details>
